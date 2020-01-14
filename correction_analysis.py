from threading import Thread, Event
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import time
import logging
logger = logging.getLogger(__name__)


class CorrectionAnalysis(Thread):
    def __init__(self):
        super(CorrectionAnalysis, self).__init__()
        self.orbit_1 = {}
        self.orbit_2 = {}
        self.kicks = {}
        self.bpm_names = None
        self.cor_names = None
        self.df = None

    def initialization(self, mi_orbit, orbit):
        self.orbit = orbit
        self.rm = self.orbit.response_matrix
        if self.df is None:
            self.mi_orbit = mi_orbit
            self.cor_names = np.append([cor.id for cor in self.orbit.hcors], [cor.id for cor in self.orbit.vcors])
            self.bpm_names = np.append([self.rm.bpm2x_name(bpm.id) for bpm in self.orbit.bpms], [self.rm.bpm2y_name(bpm.id) for bpm in self.orbit.bpms])
            columns = np.append(self.cor_names, self.bpm_names)
            self.df = pd.DataFrame(columns=columns)

    def retrieve_from_scan(self, df_scan):
        from sklearn.linear_model import LinearRegression
        bpm_names = [bpm.id for bpm in self.orbit.bpms]
        df_slice = self.rm.extract_df_slice(self.cor_names, bpm_names)
        ax = sns.heatmap(df_slice, annot=True)
        ax.set_title("Orbit response matrix")
        plt.show()
        print("ref shape = ", self.rm.extract(self.cor_names, bpm_names).shape)
        print(f"cor num = {len(self.cor_names)}, bpm num = {len(self.bpm_names)}")
        x = df_scan.loc[:, self.cor_names].values
        y = df_scan.loc[:, self.bpm_names].values
        print("x = ",  x.shape)
        print("y = ", y.shape)

        reg = LinearRegression().fit(x, y)
        #x_test = np.eye(np.shape(x)[1])
        rm = reg.coef_
        print("rm = ", rm.shape)
        #df_rm = pd.DataFrame(rm.T, columns=self.cor_names, index=bpm_x+bpm_y)
        self.df = self.rm.data2df(matrix=rm, bpm_names=bpm_names, cor_names=self.cor_names)
        return self.df

    def calculate_orm(self):
        self.df.fillna(0)
        df = self.retrieve_from_scan(self.df)
        print("RM = ", df)

        ax = sns.heatmap(df, annot=True)
        ax.set_title("Orbit response matrix")
        plt.show()


    def get_snapshot(self):
        shapshot = {}
        x = 0.
        y = 0.
        # BPM pos
        for bpm in self.orbit.bpms:
            x += bpm.x**2
            y += bpm.y**2
            self.orbit_1[bpm.id] = [bpm.x, bpm.y]
            x_name = self.rm.bpm2x_name(bpm.id)
            y_name = self.rm.bpm2y_name(bpm.id)
            shapshot[x_name] = bpm.x
            shapshot[y_name] = bpm.y

        self.xi2_x1, self.xi2_y1 = np.sqrt(x), np.sqrt(y)

        # corrector strength
        for cor in np.append(self.orbit.hcors, self.orbit.vcors):
           kick_mrad = cor.ui.get_value()
           angle = cor.mi.hw2phys(kick_mrad)
           shapshot[cor.id] = angle

        sr_row = pd.Series(shapshot)
        self.df = self.df.append(sr_row, ignore_index=True)
        self.df.fillna(0)
        print(self.df)

    def read_orbit(self):
        orbit = {}
        if self.mi_orbit.mi.allow_star_operation is True:

            bpm_names, mean_x, mean_y, mean_charge = self.mi_orbit.read_and_average(nreadings=1, take_last_n=1)
            for bpm_id, x, y in zip(bpm_names, mean_x, mean_y):
                orbit[bpm_id] = [x / 1000., y / 1000.]  # mm -> m
        else:
            for elem in self.orbit.bpms:
                try:
                    x_mm, y_mm = elem.mi.get_pos()
                    orbit[elem.id] = [x_mm / 1000., y_mm / 1000.]  # mm -> m
                    if np.isnan(x_mm) or np.isnan(y_mm):
                        logger.warning("read bpm: " + elem.id + "NaN -> was unchecked")
                except Exception as exc:
                    logger.error("read bpm: " + elem.id + " was unchecked.  Error: " + str(exc))
            return orbit


    def tmp(self):

        cor_names = np.append([cor.id for cor in self.orbit.hcors], [cor.id for cor in self.orbit.vcors])
        bpm_names = np.append([self.rm.bpm2x_name(bpm.id) for bpm in self.orbit.bpms], [self.rm.bpm2y_name(bpm.id) for bpm in self.orbit.bpms])
        columns = np.append(cor_names, bpm_names)
        df = pd.DataFrame(np.zeros((len(data), len(columns))), columns=columns)

        for i, row in enumerate(data):
            df.iloc[i] = pd.Series(row)

        df = df.fillna(0)
        df.to_pickle("rm_meas2.p")

    def save_old_orbit(self):
        x = 0.
        y = 0.
        for bpm in self.orbit.bpms:
            x += bpm.x**2
            y += bpm.y**2
            self.orbit_1[bpm.id] = [bpm.x, bpm.y]
        return np.sqrt(x), np.sqrt(y)

    def save_new_orbit(self):
        orbit = self.read_orbit()
        x = 0
        y = 0
        for bpm in self.orbit.bpms:
            if bpm.id in orbit.keys():
                bpm_x, bpm_y = orbit[bpm.id]
                self.orbit_2[bpm.id] = [bpm_x, bpm_y]
                x += bpm_x ** 2
                y += bpm_y ** 2
            else:
                logger.critical(" CorrectionAnalysis: BPM: " + bpm.id + "is not available in the DOOCS")
        return np.sqrt(x), np.sqrt(y)

    def used_correctors(self, correctors):
        #for cor in correctors:
        #    kick_mrad = cor.ui.get_value()
        #    angle = cor.mi.hw2phys(kick_mrad)
        #    kick_mrad = cor.ui.get_init_value()
        pass


    def delta_orbit(self):
        row = {}
        if len(self.orbit_1) != len(self.orbit_2):
            print("New and old orbits are not the same length")

        for bpm in self.orbit.bpms:
            if bpm.id in self.orbit_2.keys() and bpm.id in self.orbit_1.keys():
                x_old, y_old = self.orbit_1[bpm.id]
                x_new, y_new = self.orbit_2[bpm.id]
                x_name = self.rm.bpm2x_name(bpm.id)
                y_name = self.rm.bpm2y_name(bpm.id)
                row[x_name] = x_new - x_old
                row[y_name] = y_new - y_old

            else:
                logger.critical(" CorrectionAnalysis: BPM: " + bpm.id + "is not available in the DOOCS")
        return row

    def save_kicks(self, kicks):
        self.kicks = kicks

    def run(self):
        #xi2_x1, xi2_y1 = self.save_old_orbit(self.bpms)
        time.sleep(1)
        xi2_x2, xi2_y2 = self.save_new_orbit()
        row = self.delta_orbit()
        row.update(self.kicks )
        #print(row)
        sr_row = pd.Series(row)
        self.df = self.df.append(sr_row, ignore_index=True)
        print(self.df)
        # logger.info(" correction analysis: from " + self.bpms[0].id + " to " + self.bpms[-1].id +
        # ": X_chi2 = " +str(np.round(self.xi2_x1*1e6, 1))+"/" +str(np.round(xi2_x2*1e6, 1)) +
        # " um; Y_chi2 = "+str(np.round(self.xi2_y1*1e6, 1)) +"/" +str(np.round(xi2_y2*1e6, 1)) + " um")
        # print(" correction analysis: from " + self.bpms[0].id + " to " + self.bpms[-1].id +
        # ": X_chi2 = " +str(np.round(self.xi2_x1*1e6, 1))+"/" +str(np.round(xi2_x2*1e6, 1)) +
        # " um; Y_chi2 = "+str(np.round(self.xi2_y1*1e6, 1)) +"/" +str(np.round(xi2_y2*1e6, 1)) + " um")
