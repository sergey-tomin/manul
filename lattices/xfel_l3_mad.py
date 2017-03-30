from ocelot import * 
tws_l3 = Twiss()
tws_l3.beta_x  = 15.6915174102
tws_l3.beta_y  = 5.0626084624
tws_l3.alpha_x = 1.05234548452
tws_l3.alpha_y = -1.42121287541
tws_l3.E       = 2.39999998888
# drifts 
d_1 = Drift(l=3.50665, eid='D_1')
d_2 = Drift(l=0.13165, eid='D_2')
d_3 = Drift(l=1.06828, eid='D_3')
d_4 = Drift(l=0.1481, eid='D_4')
d_5 = Drift(l=0.1543, eid='D_5')
d_6 = Drift(l=0.16597, eid='D_6')
d_7 = Drift(l=1.54665, eid='D_7')
d_8 = Drift(l=3.35, eid='D_8')
d_9 = Drift(l=0.2216, eid='D_9')
d_10 = Drift(l=0.3459, eid='D_10')
d_17 = Drift(l=0.2475, eid='D_17')
d_18 = Drift(l=0.0432, eid='D_18')
d_19 = Drift(l=0.085, eid='D_19')
d_20 = Drift(l=0.4579, eid='D_20')
d_153 = Drift(l=2.9978, eid='D_153')
d_658 = Drift(l=0.1282, eid='D_658')
d_974 = Drift(l=3.25, eid='D_974')
d_975 = Drift(l=1.5458, eid='D_975')
d_976 = Drift(l=16.2017, eid='D_976')
d_977 = Drift(l=0.23555, eid='D_977')
d_978 = Drift(l=0.33555, eid='D_978')
d_979 = Drift(l=22.7834, eid='D_979')
d_982 = Drift(l=23.008175, eid='D_982')
d_983 = Drift(l=18.037275, eid='D_983')
d_984 = Drift(l=0.205, eid='D_984')
d_985 = Drift(l=0.14, eid='D_985')
d_986 = Drift(l=36.03955, eid='D_986')
d_989 = Drift(l=18.002275, eid='D_989')
d_993 = Drift(l=12.90325, eid='D_993')
d_996 = Drift(l=5.81, eid='D_996')
d_997 = Drift(l=5.845, eid='D_997')
d_998 = Drift(l=0.20895, eid='D_998')
d_999 = Drift(l=0.15395, eid='D_999')
d_1000 = Drift(l=8.355, eid='D_1000')
d_1003 = Drift(l=1.1663, eid='D_1003')
d_1004 = Drift(l=6.3887, eid='D_1004')
d_1005 = Drift(l=0.1, eid='D_1005')
d_1006 = Drift(l=0.7, eid='D_1006')
d_1009 = Drift(l=6.21, eid='D_1009')
d_1010 = Drift(l=0.15545, eid='D_1010')
d_1011 = Drift(l=0.2209, eid='D_1011')
d_1012 = Drift(l=0.21045, eid='D_1012')
d_1013 = Drift(l=0.36045, eid='D_1013')
d_1016 = Drift(l=0.74395, eid='D_1016')
d_1018 = Drift(l=0.1718, eid='D_1018')
d_1019 = Drift(l=0.4418, eid='D_1019')
d_1020 = Drift(l=0.096, eid='D_1020')
d_1021 = Drift(l=1.954002, eid='D_1021')
d_1022 = Drift(l=2.733952, eid='D_1022')
d_1026 = Drift(l=4.2, eid='D_1026')
d_1027 = Drift(l=0.0, eid='D_1027')
d_1028 = Drift(l=0.45, eid='D_1028')
d_1029 = Drift(l=1.6918, eid='D_1029')
d_1030 = Drift(l=0.42575, eid='D_1030')
d_1035 = Drift(l=1.604, eid='D_1035')
d_1037 = Drift(l=4.6418, eid='D_1037')
d_1040 = Drift(l=0.93, eid='D_1040')
d_1041 = Drift(l=1.550002, eid='D_1041')
d_1042 = Drift(l=2.491802, eid='D_1042')
d_1047 = Drift(l=2.050002, eid='D_1047')
d_1071 = Drift(l=0.38, eid='D_1071')
d_1072 = Drift(l=0.675, eid='D_1072')
d_1079 = Drift(l=1.31895, eid='D_1079')
d_1082 = Drift(l=3.28395, eid='D_1082')
d_1085 = Drift(l=2.28395, eid='D_1085')
d_1088 = Drift(l=0.4343, eid='D_1088')
d_1089 = Drift(l=1.849647, eid='D_1089')
d_1095 = Drift(l=0.685, eid='D_1095')
d_1102 = Drift(l=1.30895, eid='D_1102')
d_1119 = Drift(l=1.7, eid='D_1119')
d_1153 = Drift(l=0.2168, eid='D_1153')
d_1156 = Drift(l=0.69, eid='D_1156')
d_1159 = Drift(l=0.5709, eid='D_1159')
d_1161 = Drift(l=0.41295, eid='D_1161')
d_1163 = Drift(l=0.3015, eid='D_1163')
d_1164 = Drift(l=2.0865, eid='D_1164')
d_1166 = Drift(l=0.33645, eid='D_1166')
d_1170 = Drift(l=2.325, eid='D_1170')
d_1173 = Drift(l=3.855, eid='D_1173')
d_1176 = Drift(l=4.8525, eid='D_1176')
d_1178 = Drift(l=2.61545, eid='D_1178')
d_1179 = Drift(l=2.50395, eid='D_1179')
d_1180 = Drift(l=4.3525, eid='D_1180')
d_1183 = Drift(l=2.53395, eid='D_1183')
d_1184 = Drift(l=4.1, eid='D_1184')
d_1185 = Drift(l=7.73395, eid='D_1185')
d_1186 = Drift(l=2.71145, eid='D_1186')
d_1189 = Drift(l=3.525, eid='D_1189')
d_1195 = Drift(l=1.2775, eid='D_1195')
d_1197 = Drift(l=1.0715, eid='D_1197')
d_1198 = Drift(l=0.3, eid='D_1198')
d_1199 = Drift(l=2.6775, eid='D_1199')
d_1200 = Drift(l=2.31145, eid='D_1200')
d_1202 = Drift(l=1.5025, eid='D_1202')
d_1204 = Drift(l=0.4815, eid='D_1204')
d_1205 = Drift(l=0.27, eid='D_1205')
d_1206 = Drift(l=11.663951, eid='D_1206')
d_1207 = Drift(l=11.933951, eid='D_1207')
d_1208 = Drift(l=0.64, eid='D_1208')
d_1209 = Drift(l=1.285, eid='D_1209')
d_1210 = Drift(l=0.208951, eid='D_1210')
d_1211 = Drift(l=0.153951, eid='D_1211')
d_1212 = Drift(l=0.2, eid='D_1212')
d_1213 = Drift(l=9.0692, eid='D_1213')
d_1215 = Drift(l=0.15, eid='D_1215')
d_1217 = Drift(l=1.86074, eid='D_1217')

# quadrupoles 
qd_470_b2 = Quadrupole(l=0.2367, k1=-1.289057389, tilt=0.0, eid='QD.470.B2')
qd_472_b2 = Quadrupole(l=0.2367, k1=0.8838899148, tilt=0.0, eid='QD.472.B2')
q_488_l3 = Quadrupole(l=0.2136, k1=-0.3339147164, tilt=0.0, eid='Q.488.L3')
q_500_l3 = Quadrupole(l=0.2136, k1=0.4269256757, tilt=0.0, eid='Q.500.L3')
q_512_l3 = Quadrupole(l=0.2136, k1=-0.2701007323, tilt=0.0, eid='Q.512.L3')
q_524_l3 = Quadrupole(l=0.2136, k1=-0.0803619504, tilt=0.0, eid='Q.524.L3')
q_536_l3 = Quadrupole(l=0.2136, k1=0.3005952661, tilt=0.0, eid='Q.536.L3')
q_548_l3 = Quadrupole(l=0.2136, k1=-0.3005952661, tilt=0.0, eid='Q.548.L3')
q_560_l3 = Quadrupole(l=0.2136, k1=0.3005952661, tilt=0.0, eid='Q.560.L3')
q_572_l3 = Quadrupole(l=0.2136, k1=-0.3005952661, tilt=0.0, eid='Q.572.L3')
q_584_l3 = Quadrupole(l=0.2136, k1=0.3005952661, tilt=0.0, eid='Q.584.L3')
q_596_l3 = Quadrupole(l=0.2136, k1=-0.3005952661, tilt=0.0, eid='Q.596.L3')
q_608_l3 = Quadrupole(l=0.2136, k1=0.3171476124, tilt=0.0, eid='Q.608.L3')
q_620_l3 = Quadrupole(l=0.2136, k1=-0.2941311798, tilt=0.0, eid='Q.620.L3')
q_635_l3 = Quadrupole(l=0.2136, k1=0.2903606742, tilt=0.0, eid='Q.635.L3')
q_647_l3 = Quadrupole(l=0.2136, k1=-0.306425, tilt=0.0, eid='Q.647.L3')
q_659_l3 = Quadrupole(l=0.2136, k1=0.3005952661, tilt=0.0, eid='Q.659.L3')
q_671_l3 = Quadrupole(l=0.2136, k1=-0.3005952661, tilt=0.0, eid='Q.671.L3')
q_683_l3 = Quadrupole(l=0.2136, k1=0.3005952661, tilt=0.0, eid='Q.683.L3')
q_695_l3 = Quadrupole(l=0.2136, k1=-0.3005952661, tilt=0.0, eid='Q.695.L3')
q_707_l3 = Quadrupole(l=0.2136, k1=0.3005952661, tilt=0.0, eid='Q.707.L3')
q_719_l3 = Quadrupole(l=0.2136, k1=-0.3005952661, tilt=0.0, eid='Q.719.L3')
q_731_l3 = Quadrupole(l=0.2136, k1=0.3005952661, tilt=0.0, eid='Q.731.L3')
q_743_l3 = Quadrupole(l=0.2136, k1=-0.3005952661, tilt=0.0, eid='Q.743.L3')
q_755_l3 = Quadrupole(l=0.2136, k1=0.3171476124, tilt=0.0, eid='Q.755.L3')
q_767_l3 = Quadrupole(l=0.2136, k1=-0.2941311798, tilt=0.0, eid='Q.767.L3')
q_782_l3 = Quadrupole(l=0.2136, k1=0.2903606742, tilt=0.0, eid='Q.782.L3')
q_794_l3 = Quadrupole(l=0.2136, k1=-0.306425, tilt=0.0, eid='Q.794.L3')
q_806_l3 = Quadrupole(l=0.2136, k1=0.3005952661, tilt=0.0, eid='Q.806.L3')
q_818_l3 = Quadrupole(l=0.2136, k1=-0.3005952661, tilt=0.0, eid='Q.818.L3')
q_830_l3 = Quadrupole(l=0.2136, k1=0.3005952661, tilt=0.0, eid='Q.830.L3')
q_842_l3 = Quadrupole(l=0.2136, k1=-0.3005952661, tilt=0.0, eid='Q.842.L3')
q_854_l3 = Quadrupole(l=0.2136, k1=0.3005952661, tilt=0.0, eid='Q.854.L3')
q_866_l3 = Quadrupole(l=0.2136, k1=-0.3005952661, tilt=0.0, eid='Q.866.L3')
q_878_l3 = Quadrupole(l=0.2136, k1=0.3005952661, tilt=0.0, eid='Q.878.L3')
q_890_l3 = Quadrupole(l=0.2136, k1=-0.3005952661, tilt=0.0, eid='Q.890.L3')
q_902_l3 = Quadrupole(l=0.2136, k1=0.3171476124, tilt=0.0, eid='Q.902.L3')
q_914_l3 = Quadrupole(l=0.2136, k1=-0.2941311798, tilt=0.0, eid='Q.914.L3')
q_929_l3 = Quadrupole(l=0.2136, k1=0.2903606742, tilt=0.0, eid='Q.929.L3')
q_941_l3 = Quadrupole(l=0.2136, k1=-0.306425, tilt=0.0, eid='Q.941.L3')
q_953_l3 = Quadrupole(l=0.2136, k1=0.3005952661, tilt=0.0, eid='Q.953.L3')
q_965_l3 = Quadrupole(l=0.2136, k1=-0.3005952661, tilt=0.0, eid='Q.965.L3')
q_977_l3 = Quadrupole(l=0.2136, k1=0.3005952661, tilt=0.0, eid='Q.977.L3')
q_989_l3 = Quadrupole(l=0.2136, k1=-0.3005952661, tilt=0.0, eid='Q.989.L3')
q_1001_l3 = Quadrupole(l=0.2136, k1=0.3005952661, tilt=0.0, eid='Q.1001.L3')
q_1013_l3 = Quadrupole(l=0.2136, k1=-0.3005952661, tilt=0.0, eid='Q.1013.L3')
q_1025_l3 = Quadrupole(l=0.2136, k1=0.3005952661, tilt=0.0, eid='Q.1025.L3')
q_1037_l3 = Quadrupole(l=0.2136, k1=-0.3005952661, tilt=0.0, eid='Q.1037.L3')
q_1049_l3 = Quadrupole(l=0.2136, k1=0.3171476124, tilt=0.0, eid='Q.1049.L3')
q_1061_l3 = Quadrupole(l=0.2136, k1=-0.2941311798, tilt=0.0, eid='Q.1061.L3')
q_1076_l3 = Quadrupole(l=0.2136, k1=0.2903606742, tilt=0.0, eid='Q.1076.L3')
q_1088_l3 = Quadrupole(l=0.2136, k1=-0.306425, tilt=0.0, eid='Q.1088.L3')
q_1100_l3 = Quadrupole(l=0.2136, k1=0.3005952661, tilt=0.0, eid='Q.1100.L3')
q_1112_l3 = Quadrupole(l=0.2136, k1=-0.3005952661, tilt=0.0, eid='Q.1112.L3')
q_1124_l3 = Quadrupole(l=0.2136, k1=0.3005952661, tilt=0.0, eid='Q.1124.L3')
q_1136_l3 = Quadrupole(l=0.2136, k1=-0.3005952661, tilt=0.0, eid='Q.1136.L3')
q_1147_l3 = Quadrupole(l=0.2136, k1=0.3005952661, tilt=0.0, eid='Q.1147.L3')
q_1159_l3 = Quadrupole(l=0.2136, k1=-0.3005952661, tilt=0.0, eid='Q.1159.L3')
q_1171_l3 = Quadrupole(l=0.2136, k1=0.3005952661, tilt=0.0, eid='Q.1171.L3')
q_1183_l3 = Quadrupole(l=0.2136, k1=-0.3005952661, tilt=0.0, eid='Q.1183.L3')
q_1195_l3 = Quadrupole(l=0.2136, k1=0.3171476124, tilt=0.0, eid='Q.1195.L3')
q_1207_l3 = Quadrupole(l=0.2136, k1=-0.2941311798, tilt=0.0, eid='Q.1207.L3')
q_1222_l3 = Quadrupole(l=0.2136, k1=0.2903606742, tilt=0.0, eid='Q.1222.L3')
q_1234_l3 = Quadrupole(l=0.2136, k1=-0.306425, tilt=0.0, eid='Q.1234.L3')
q_1246_l3 = Quadrupole(l=0.2136, k1=0.3005952661, tilt=0.0, eid='Q.1246.L3')
q_1258_l3 = Quadrupole(l=0.2136, k1=-0.3005952661, tilt=0.0, eid='Q.1258.L3')
q_1270_l3 = Quadrupole(l=0.2136, k1=0.3005952661, tilt=0.0, eid='Q.1270.L3')
q_1282_l3 = Quadrupole(l=0.2136, k1=-0.3005952661, tilt=0.0, eid='Q.1282.L3')
q_1294_l3 = Quadrupole(l=0.2136, k1=0.3005952661, tilt=0.0, eid='Q.1294.L3')
q_1306_l3 = Quadrupole(l=0.2136, k1=-0.3005952661, tilt=0.0, eid='Q.1306.L3')
q_1318_l3 = Quadrupole(l=0.2136, k1=0.3005952661, tilt=0.0, eid='Q.1318.L3')
q_1330_l3 = Quadrupole(l=0.2136, k1=-0.3005952661, tilt=0.0, eid='Q.1330.L3')
q_1342_l3 = Quadrupole(l=0.2136, k1=0.3171476124, tilt=0.0, eid='Q.1342.L3')
q_1354_l3 = Quadrupole(l=0.2136, k1=-0.2941311798, tilt=0.0, eid='Q.1354.L3')
q_1369_l3 = Quadrupole(l=0.2136, k1=0.2903606742, tilt=0.0, eid='Q.1369.L3')
q_1381_l3 = Quadrupole(l=0.2136, k1=-0.306425, tilt=0.0, eid='Q.1381.L3')
q_1393_l3 = Quadrupole(l=0.2136, k1=0.3005952661, tilt=0.0, eid='Q.1393.L3')
q_1405_l3 = Quadrupole(l=0.2136, k1=-0.3005952661, tilt=0.0, eid='Q.1405.L3')
q_1417_l3 = Quadrupole(l=0.2136, k1=0.3005952661, tilt=0.0, eid='Q.1417.L3')
q_1429_l3 = Quadrupole(l=0.2136, k1=-0.3005952661, tilt=0.0, eid='Q.1429.L3')
q_1441_l3 = Quadrupole(l=0.2136, k1=0.3005952661, tilt=0.0, eid='Q.1441.L3')
q_1453_l3 = Quadrupole(l=0.2136, k1=-0.3005952661, tilt=0.0, eid='Q.1453.L3')
qb_1475_l3 = Quadrupole(l=0.3289, k1=0.140392839, tilt=0.0, eid='QB.1475.L3')
qb_1499_l3 = Quadrupole(l=0.3289, k1=-0.1308389927, tilt=0.0, eid='QB.1499.L3')
qe_1542_l3 = Quadrupole(l=0.24, k1=0.1280915, tilt=0.0, eid='QE.1542.L3')
qe_1578_l3 = Quadrupole(l=0.24, k1=-0.1280915, tilt=0.0, eid='QE.1578.L3')
qe_1615_l3 = Quadrupole(l=0.24, k1=0.1280915, tilt=0.0, eid='QE.1615.L3')
qe_1629_l3 = Quadrupole(l=0.24, k1=0.0, tilt=0.0, eid='QE.1629.L3')
qf_1641_l3 = Quadrupole(l=0.5321, k1=0.0, tilt=0.0, eid='QF.1641.L3')
qf_1650_l3 = Quadrupole(l=0.5321, k1=-0.1795831498, tilt=0.0, eid='QF.1650.L3')
qf_1660_cl = Quadrupole(l=0.5321, k1=0.2241500814, tilt=0.0, eid='QF.1660.CL')
qh_1667_cl = Quadrupole(l=1.0291, k1=-0.0197060783, tilt=0.0, eid='QH.1667.CL')
qh_1669_cl = Quadrupole(l=1.0291, k1=-0.0197060783, tilt=0.0, eid='QH.1669.CL')
qh_1670_cl = Quadrupole(l=1.0291, k1=0.0, tilt=0.0, eid='QH.1670.CL')
qh_1671_cl = Quadrupole(l=1.0291, k1=0.0, tilt=0.0, eid='QH.1671.CL')
qf_1673_cl = Quadrupole(l=0.5321, k1=-0.3013036103, tilt=0.0, eid='QF.1673.CL')
qf_1682_cl = Quadrupole(l=0.5321, k1=0.3013036103, tilt=0.0, eid='QF.1682.CL')
qf_1691_cl = Quadrupole(l=0.5321, k1=-0.3013036103, tilt=0.0, eid='QF.1691.CL')
qf_1700_cl = Quadrupole(l=0.5321, k1=0.3013036103, tilt=0.0, eid='QF.1700.CL')
qf_1709_cl = Quadrupole(l=0.5321, k1=-0.3013036103, tilt=0.0, eid='QF.1709.CL')
qf_1718_cl = Quadrupole(l=0.5321, k1=0.3013036103, tilt=0.0, eid='QF.1718.CL')
qf_1727_cl = Quadrupole(l=0.5321, k1=-0.3013036103, tilt=0.0, eid='QF.1727.CL')
qf_1736_cl = Quadrupole(l=0.5321, k1=0.3013036103, tilt=0.0, eid='QF.1736.CL')
qf_1745_cl = Quadrupole(l=0.5321, k1=-0.3013036103, tilt=0.0, eid='QF.1745.CL')
qh_1748_cl = Quadrupole(l=1.0291, k1=0.0, tilt=0.0, eid='QH.1748.CL')
qh_1749_cl = Quadrupole(l=1.0291, k1=0.0, tilt=0.0, eid='QH.1749.CL')
qh_1751_cl = Quadrupole(l=1.0291, k1=0.0, tilt=0.0, eid='QH.1751.CL')
qh_1752_cl = Quadrupole(l=1.0291, k1=0.0, tilt=0.0, eid='QH.1752.CL')
qf_1754_cl = Quadrupole(l=0.5321, k1=0.3013036103, tilt=0.0, eid='QF.1754.CL')
qf_1759_cl = Quadrupole(l=0.5321, k1=0.0, tilt=0.0, eid='QF.1759.CL')
qf_1763_cl = Quadrupole(l=0.5321, k1=-0.3013173384, tilt=0.0, eid='QF.1763.CL')
qf_1767_cl = Quadrupole(l=0.5321, k1=0.0, tilt=0.0, eid='QF.1767.CL')
qf_1772_cl = Quadrupole(l=0.5321, k1=0.3013036103, tilt=0.0, eid='QF.1772.CL')
qh_1775_cl = Quadrupole(l=1.0291, k1=0.0, tilt=0.0, eid='QH.1775.CL')
qh_1776_cl = Quadrupole(l=1.0291, k1=0.0, tilt=0.0, eid='QH.1776.CL')
qh_1778_cl = Quadrupole(l=1.0291, k1=0.0, tilt=0.0, eid='QH.1778.CL')
qh_1779_cl = Quadrupole(l=1.0291, k1=0.0, tilt=0.0, eid='QH.1779.CL')
qf_1781_cl = Quadrupole(l=0.5321, k1=-0.3013036103, tilt=0.0, eid='QF.1781.CL')
qf_1790_cl = Quadrupole(l=0.5321, k1=0.3013036103, tilt=0.0, eid='QF.1790.CL')
qf_1799_cl = Quadrupole(l=0.5321, k1=-0.3013036103, tilt=0.0, eid='QF.1799.CL')
qf_1808_cl = Quadrupole(l=0.5321, k1=0.3013036103, tilt=0.0, eid='QF.1808.CL')
qf_1817_cl = Quadrupole(l=0.5321, k1=-0.3013036103, tilt=0.0, eid='QF.1817.CL')
qf_1826_cl = Quadrupole(l=0.5321, k1=0.3013036103, tilt=0.0, eid='QF.1826.CL')
qf_1835_cl = Quadrupole(l=0.5321, k1=-0.3013036103, tilt=0.0, eid='QF.1835.CL')
qf_1844_cl = Quadrupole(l=0.5321, k1=0.3013036103, tilt=0.0, eid='QF.1844.CL')
qf_1853_cl = Quadrupole(l=0.5321, k1=-0.3013036103, tilt=0.0, eid='QF.1853.CL')
qh_1855_tl = Quadrupole(l=1.0291, k1=0.1743333753, tilt=0.0, eid='QH.1855.TL')
qh_1857_tl = Quadrupole(l=1.0291, k1=0.0, tilt=0.0, eid='QH.1857.TL')
qh_1858_tl = Quadrupole(l=1.0291, k1=-0.1495443481, tilt=0.0, eid='QH.1858.TL')
qh_1859_tl = Quadrupole(l=1.0291, k1=0.0, tilt=0.0, eid='QH.1859.TL')
qf_1864_tl = Quadrupole(l=0.5321, k1=0.2654122951, tilt=0.0, eid='QF.1864.TL')
qf_1868_tl = Quadrupole(l=0.5321, k1=-0.1946873567, tilt=0.0, eid='QF.1868.TL')
qf_1873_tl = Quadrupole(l=0.5321, k1=0.1899001353, tilt=0.0, eid='QF.1873.TL')
qf_1881_tl = Quadrupole(l=0.5321, k1=-0.2093190845, tilt=0.0, eid='QF.1881.TL')
qf_1892_tl = Quadrupole(l=0.5321, k1=0.1791908476, tilt=0.0, eid='QF.1892.TL')
qf_1907_tl = Quadrupole(l=0.5321, k1=-0.1791908476, tilt=0.0, eid='QF.1907.TL')
qf_1922_tl = Quadrupole(l=0.5321, k1=0.1791908476, tilt=0.0, eid='QF.1922.TL')
qf_1937_tl = Quadrupole(l=0.5321, k1=-0.1791908476, tilt=0.0, eid='QF.1937.TL')
qf_1952_tl = Quadrupole(l=0.5321, k1=0.1791908476, tilt=0.0, eid='QF.1952.TL')
qf_1967_tl = Quadrupole(l=0.5321, k1=-0.1791908476, tilt=0.0, eid='QF.1967.TL')

# bending magnets 
be_1678_cl = SBend(l = 2.5, angle=0.006233024763, e1=0.003116512, e2=0.003116512, gap=0, tilt=1.570796327, fint=0.0, fintx=0.0, eid='BE.1678.CL')
bl_1688_cl = SBend(l = 0.2, angle=-0.000737152538, e1=-0.000368576, e2=-0.000368576, gap=0, tilt=1.570796327, fint=0.0, fintx=0.0, eid='BL.1688.CL')
bl_1695_cl = SBend(l = 0.2, angle=-0.000737152538, e1=-0.000368576, e2=-0.000368576, gap=0, tilt=1.570796327, fint=0.0, fintx=0.0, eid='BL.1695.CL')
be_1705_cl = SBend(l = 2.5, angle=0.006233024763, e1=0.003116512, e2=0.003116512, gap=0, tilt=1.570796327, fint=0.0, fintx=0.0, eid='BE.1705.CL')
be_1714_cl = SBend(l = 2.5, angle=0.006233024763, e1=0.003116512, e2=0.003116512, gap=0, tilt=1.570796327, fint=0.0, fintx=0.0, eid='BE.1714.CL')
bl_1724_cl = SBend(l = 0.2, angle=-0.000737152538, e1=-0.000368576, e2=-0.000368576, gap=0, tilt=1.570796327, fint=0.0, fintx=0.0, eid='BL.1724.CL')
bl_1731_cl = SBend(l = 0.2, angle=-0.000737152538, e1=-0.000368576, e2=-0.000368576, gap=0, tilt=1.570796327, fint=0.0, fintx=0.0, eid='BL.1731.CL')
be_1741_cl = SBend(l = 2.5, angle=0.006233024763, e1=0.003116512, e2=0.003116512, gap=0, tilt=1.570796327, fint=0.0, fintx=0.0, eid='BE.1741.CL')
be_1786_cl = SBend(l = 2.5, angle=-0.006129494209, e1=-0.003064747, e2=-0.003064747, gap=0, tilt=1.570796327, fint=0.0, fintx=0.0, eid='BE.1786.CL')
bl_1796_cl = SBend(l = 0.2, angle=0.000724902792, e1=0.000362451, e2=0.000362451, gap=0, tilt=1.570796327, fint=0.0, fintx=0.0, eid='BL.1796.CL')
bl_1803_cl = SBend(l = 0.2, angle=0.000724902792, e1=0.000362451, e2=0.000362451, gap=0, tilt=1.570796327, fint=0.0, fintx=0.0, eid='BL.1803.CL')
be_1813_cl = SBend(l = 2.5, angle=-0.006129494209, e1=-0.003064747, e2=-0.003064747, gap=0, tilt=1.570796327, fint=0.0, fintx=0.0, eid='BE.1813.CL')
be_1822_cl = SBend(l = 2.5, angle=-0.006129494209, e1=-0.003064747, e2=-0.003064747, gap=0, tilt=1.570796327, fint=0.0, fintx=0.0, eid='BE.1822.CL')
bl_1832_cl = SBend(l = 0.2, angle=0.000724902792, e1=0.000362451, e2=0.000362451, gap=0, tilt=1.570796327, fint=0.0, fintx=0.0, eid='BL.1832.CL')
bl_1839_cl = SBend(l = 0.2, angle=0.000724902792, e1=0.000362451, e2=0.000362451, gap=0, tilt=1.570796327, fint=0.0, fintx=0.0, eid='BL.1839.CL')
be_1849_cl = SBend(l = 2.5, angle=-0.006129494209, e1=-0.003064747, e2=-0.003064747, gap=0, tilt=1.570796327, fint=0.0, fintx=0.0, eid='BE.1849.CL')

# correctors 
ccy_470_b2 = Vcor(l=0.1, angle=0.0, eid='CCY.470.B2')
cx_488_l3 = Hcor(l=0.0, angle=0.0, eid='CX.488.L3')
cy_500_l3 = Vcor(l=0.0, angle=0.0, eid='CY.500.L3')
cx_512_l3 = Hcor(l=0.0, angle=0.0, eid='CX.512.L3')
cy_524_l3 = Vcor(l=0.0, angle=0.0, eid='CY.524.L3')
cx_536_l3 = Hcor(l=0.0, angle=0.0, eid='CX.536.L3')
cy_548_l3 = Vcor(l=0.0, angle=0.0, eid='CY.548.L3')
cx_560_l3 = Hcor(l=0.0, angle=0.0, eid='CX.560.L3')
cy_572_l3 = Vcor(l=0.0, angle=0.0, eid='CY.572.L3')
cx_584_l3 = Hcor(l=0.0, angle=0.0, eid='CX.584.L3')
cy_596_l3 = Vcor(l=0.0, angle=0.0, eid='CY.596.L3')
cx_608_l3 = Hcor(l=0.0, angle=0.0, eid='CX.608.L3')
cy_620_l3 = Vcor(l=0.0, angle=0.0, eid='CY.620.L3')
cx_635_l3 = Hcor(l=0.0, angle=0.0, eid='CX.635.L3')
cy_647_l3 = Vcor(l=0.0, angle=0.0, eid='CY.647.L3')
cx_659_l3 = Hcor(l=0.0, angle=0.0, eid='CX.659.L3')
cy_671_l3 = Vcor(l=0.0, angle=0.0, eid='CY.671.L3')
cx_683_l3 = Hcor(l=0.0, angle=0.0, eid='CX.683.L3')
cy_695_l3 = Vcor(l=0.0, angle=0.0, eid='CY.695.L3')
cx_707_l3 = Hcor(l=0.0, angle=0.0, eid='CX.707.L3')
cy_719_l3 = Vcor(l=0.0, angle=0.0, eid='CY.719.L3')
cx_731_l3 = Hcor(l=0.0, angle=0.0, eid='CX.731.L3')
cy_743_l3 = Vcor(l=0.0, angle=0.0, eid='CY.743.L3')
cx_755_l3 = Hcor(l=0.0, angle=0.0, eid='CX.755.L3')
cy_767_l3 = Vcor(l=0.0, angle=0.0, eid='CY.767.L3')
cx_782_l3 = Hcor(l=0.0, angle=0.0, eid='CX.782.L3')
cy_794_l3 = Vcor(l=0.0, angle=0.0, eid='CY.794.L3')
cx_806_l3 = Hcor(l=0.0, angle=0.0, eid='CX.806.L3')
cy_818_l3 = Vcor(l=0.0, angle=0.0, eid='CY.818.L3')
cx_830_l3 = Hcor(l=0.0, angle=0.0, eid='CX.830.L3')
cy_842_l3 = Vcor(l=0.0, angle=0.0, eid='CY.842.L3')
cx_854_l3 = Hcor(l=0.0, angle=0.0, eid='CX.854.L3')
cy_866_l3 = Vcor(l=0.0, angle=0.0, eid='CY.866.L3')
cx_878_l3 = Hcor(l=0.0, angle=0.0, eid='CX.878.L3')
cy_890_l3 = Vcor(l=0.0, angle=0.0, eid='CY.890.L3')
cx_902_l3 = Hcor(l=0.0, angle=0.0, eid='CX.902.L3')
cy_914_l3 = Vcor(l=0.0, angle=0.0, eid='CY.914.L3')
cx_929_l3 = Hcor(l=0.0, angle=0.0, eid='CX.929.L3')
cy_941_l3 = Vcor(l=0.0, angle=0.0, eid='CY.941.L3')
cx_953_l3 = Hcor(l=0.0, angle=0.0, eid='CX.953.L3')
cy_965_l3 = Vcor(l=0.0, angle=0.0, eid='CY.965.L3')
cx_977_l3 = Hcor(l=0.0, angle=0.0, eid='CX.977.L3')
cy_989_l3 = Vcor(l=0.0, angle=0.0, eid='CY.989.L3')
cx_1001_l3 = Hcor(l=0.0, angle=0.0, eid='CX.1001.L3')
cy_1013_l3 = Vcor(l=0.0, angle=0.0, eid='CY.1013.L3')
cx_1025_l3 = Hcor(l=0.0, angle=0.0, eid='CX.1025.L3')
cy_1037_l3 = Vcor(l=0.0, angle=0.0, eid='CY.1037.L3')
cx_1049_l3 = Hcor(l=0.0, angle=0.0, eid='CX.1049.L3')
cy_1061_l3 = Vcor(l=0.0, angle=0.0, eid='CY.1061.L3')
cx_1076_l3 = Hcor(l=0.0, angle=0.0, eid='CX.1076.L3')
cy_1088_l3 = Vcor(l=0.0, angle=0.0, eid='CY.1088.L3')
cx_1100_l3 = Hcor(l=0.0, angle=0.0, eid='CX.1100.L3')
cy_1112_l3 = Vcor(l=0.0, angle=0.0, eid='CY.1112.L3')
cx_1124_l3 = Hcor(l=0.0, angle=0.0, eid='CX.1124.L3')
cx_1148_l3 = Hcor(l=0.0, angle=0.0, eid='CX.1148.L3')
cy_1148_l3 = Vcor(l=0.0, angle=0.0, eid='CY.1148.L3')
cy_1160_l3 = Vcor(l=0.0, angle=0.0, eid='CY.1160.L3')
cx_1172_l3 = Hcor(l=0.0, angle=0.0, eid='CX.1172.L3')
cy_1184_l3 = Vcor(l=0.0, angle=0.0, eid='CY.1184.L3')
cx_1196_l3 = Hcor(l=0.0, angle=0.0, eid='CX.1196.L3')
cy_1208_l3 = Vcor(l=0.0, angle=0.0, eid='CY.1208.L3')
cx_1223_l3 = Hcor(l=0.0, angle=0.0, eid='CX.1223.L3')
cy_1235_l3 = Vcor(l=0.0, angle=0.0, eid='CY.1235.L3')
cx_1247_l3 = Hcor(l=0.0, angle=0.0, eid='CX.1247.L3')
cy_1259_l3 = Vcor(l=0.0, angle=0.0, eid='CY.1259.L3')
cx_1271_l3 = Hcor(l=0.0, angle=0.0, eid='CX.1271.L3')
cy_1283_l3 = Vcor(l=0.0, angle=0.0, eid='CY.1283.L3')
cx_1295_l3 = Hcor(l=0.0, angle=0.0, eid='CX.1295.L3')
cy_1307_l3 = Vcor(l=0.0, angle=0.0, eid='CY.1307.L3')
cx_1319_l3 = Hcor(l=0.0, angle=0.0, eid='CX.1319.L3')
cy_1331_l3 = Vcor(l=0.0, angle=0.0, eid='CY.1331.L3')
cx_1343_l3 = Hcor(l=0.0, angle=0.0, eid='CX.1343.L3')
cy_1355_l3 = Vcor(l=0.0, angle=0.0, eid='CY.1355.L3')
cx_1369_l3 = Hcor(l=0.0, angle=0.0, eid='CX.1369.L3')
cy_1381_l3 = Vcor(l=0.0, angle=0.0, eid='CY.1381.L3')
cx_1393_l3 = Hcor(l=0.0, angle=0.0, eid='CX.1393.L3')
cy_1405_l3 = Vcor(l=0.0, angle=0.0, eid='CY.1405.L3')
cx_1417_l3 = Hcor(l=0.0, angle=0.0, eid='CX.1417.L3')
cy_1429_l3 = Vcor(l=0.0, angle=0.0, eid='CY.1429.L3')
cx_1441_l3 = Hcor(l=0.0, angle=0.0, eid='CX.1441.L3')
cy_1453_l3 = Vcor(l=0.0, angle=0.0, eid='CY.1453.L3')
cmx_1476_l3 = Hcor(l=0.3, angle=0.0, eid='CMX.1476.L3')
cmy_1500_l3 = Vcor(l=0.3, angle=0.0, eid='CMY.1500.L3')
cex_1542_l3 = Hcor(l=0.1, angle=0.0, eid='CEX.1542.L3')
cey_1579_l3 = Vcor(l=0.1, angle=0.0, eid='CEY.1579.L3')
cex_1615_l3 = Hcor(l=0.1, angle=0.0, eid='CEX.1615.L3')
cey_1629_l3 = Vcor(l=0.1, angle=0.0, eid='CEY.1629.L3')
cfx_1642_l3 = Hcor(l=0.1, angle=0.0, eid='CFX.1642.L3')
cfy_1651_l3 = Vcor(l=0.1, angle=0.0, eid='CFY.1651.L3')
cfx_1660_cl = Hcor(l=0.1, angle=0.0, eid='CFX.1660.CL')
chy_1667_cl = Vcor(l=0.2, angle=0.0, eid='CHY.1667.CL')
chx_1672_cl = Hcor(l=0.2, angle=0.0, eid='CHX.1672.CL')
cfy_1674_cl = Vcor(l=0.1, angle=0.0, eid='CFY.1674.CL')
cfx_1683_cl = Hcor(l=0.1, angle=0.0, eid='CFX.1683.CL')
cfy_1692_cl = Vcor(l=0.1, angle=0.0, eid='CFY.1692.CL')
cfx_1701_cl = Hcor(l=0.1, angle=0.0, eid='CFX.1701.CL')
cfy_1710_cl = Vcor(l=0.1, angle=0.0, eid='CFY.1710.CL')
cfx_1719_cl = Hcor(l=0.1, angle=0.0, eid='CFX.1719.CL')
cfy_1728_cl = Vcor(l=0.1, angle=0.0, eid='CFY.1728.CL')
cfx_1737_cl = Hcor(l=0.1, angle=0.0, eid='CFX.1737.CL')
cfy_1746_cl = Vcor(l=0.1, angle=0.0, eid='CFY.1746.CL')
chx_1747_cl = Hcor(l=0.2, angle=0.0, eid='CHX.1747.CL')
chy_1753_cl = Vcor(l=0.2, angle=0.0, eid='CHY.1753.CL')
cfx_1755_cl = Hcor(l=0.1, angle=0.0, eid='CFX.1755.CL')
cfy_1760_cl = Vcor(l=0.1, angle=0.0, eid='CFY.1760.CL')
cfx_1764_cl = Hcor(l=0.1, angle=0.0, eid='CFX.1764.CL')
cfy_1768_cl = Vcor(l=0.1, angle=0.0, eid='CFY.1768.CL')
cfx_1773_cl = Hcor(l=0.1, angle=0.0, eid='CFX.1773.CL')
chy_1774_cl = Vcor(l=0.2, angle=0.0, eid='CHY.1774.CL')
chx_1780_cl = Hcor(l=0.2, angle=0.0, eid='CHX.1780.CL')
cfy_1782_cl = Vcor(l=0.1, angle=0.0, eid='CFY.1782.CL')
cfx_1791_cl = Hcor(l=0.1, angle=0.0, eid='CFX.1791.CL')
cfy_1800_cl = Vcor(l=0.1, angle=0.0, eid='CFY.1800.CL')
cfx_1809_cl = Hcor(l=0.1, angle=0.0, eid='CFX.1809.CL')
cfy_1818_cl = Vcor(l=0.1, angle=0.0, eid='CFY.1818.CL')
cfx_1827_cl = Hcor(l=0.1, angle=0.0, eid='CFX.1827.CL')
cfy_1836_cl = Vcor(l=0.1, angle=0.0, eid='CFY.1836.CL')
cfx_1845_cl = Hcor(l=0.1, angle=0.0, eid='CFX.1845.CL')
cfy_1854_tl = Vcor(l=0.1, angle=0.0, eid='CFY.1854.TL')
chx_1855_tl = Hcor(l=0.2, angle=0.0, eid='CHX.1855.TL')
chy_1861_tl = Vcor(l=0.2, angle=0.0, eid='CHY.1861.TL')
cfx_1864_tl = Hcor(l=0.1, angle=0.0, eid='CFX.1864.TL')
cfy_1869_tl = Vcor(l=0.1, angle=0.0, eid='CFY.1869.TL')
cfx_1873_tl = Hcor(l=0.1, angle=0.0, eid='CFX.1873.TL')
cfy_1884_tl = Vcor(l=0.1, angle=0.0, eid='CFY.1884.TL')
cfx_1894_tl = Hcor(l=0.1, angle=0.0, eid='CFX.1894.TL')
cfy_1910_tl = Vcor(l=0.1, angle=0.0, eid='CFY.1910.TL')
cfx_1925_tl = Hcor(l=0.1, angle=0.0, eid='CFX.1925.TL')
cfy_1937_tl = Vcor(l=0.1, angle=0.0, eid='CFY.1937.TL')
bl_1939_tl = Vcor(l=0.2, angle=0.0, eid='BL.1939.TL')
bl_1964_tl = Vcor(l=0.2, angle=0.0, eid='BL.1964.TL')
chx_1965_tl = Hcor(l=0.2, angle=0.0, eid='CHX.1965.TL')
chx_1967_tl = Hcor(l=0.2, angle=0.0, eid='CHX.1967.TL')
chy_1967_tl = Vcor(l=0.2, angle=0.0, eid='CHY.1967.TL')
cnx_1977_tl = Hcor(l=0.3, angle=0.0, eid='CNX.1977.TL')
cny_1977_tl = Vcor(l=0.3, angle=0.0, eid='CNY.1977.TL')

# markers 
stsub_466_b2 = Marker(eid='STSUB.466.B2')
dcm_471_b2 = Marker(eid='DCM.471.B2')
tora_471_b2 = Marker(eid='TORA.471.B2')
enblock_473_b2 = Marker(eid='ENBLOCK.473.B2')
ensub_473_b2 = Marker(eid='ENSUB.473.B2')
ensec_473_b2 = Marker(eid='ENSEC.473.B2')
stsec_473_l3 = Marker(eid='STSEC.473.L3')
stac_477_l3 = Marker(eid='STAC.477.L3')
enac_489_l3 = Marker(eid='ENAC.489.L3')
stac_489_l3 = Marker(eid='STAC.489.L3')
enac_501_l3 = Marker(eid='ENAC.501.L3')
stac_501_l3 = Marker(eid='STAC.501.L3')
enac_513_l3 = Marker(eid='ENAC.513.L3')
stac_513_l3 = Marker(eid='STAC.513.L3')
enac_525_l3 = Marker(eid='ENAC.525.L3')
match_525_l3 = Marker(eid='MATCH.525.L3')
stac_525_l3 = Marker(eid='STAC.525.L3')
enac_537_l3 = Marker(eid='ENAC.537.L3')
stac_537_l3 = Marker(eid='STAC.537.L3')
enac_549_l3 = Marker(eid='ENAC.549.L3')
stac_549_l3 = Marker(eid='STAC.549.L3')
enac_561_l3 = Marker(eid='ENAC.561.L3')
stac_561_l3 = Marker(eid='STAC.561.L3')
enac_573_l3 = Marker(eid='ENAC.573.L3')
stac_573_l3 = Marker(eid='STAC.573.L3')
enac_585_l3 = Marker(eid='ENAC.585.L3')
stac_585_l3 = Marker(eid='STAC.585.L3')
enac_597_l3 = Marker(eid='ENAC.597.L3')
stac_597_l3 = Marker(eid='STAC.597.L3')
enac_609_l3 = Marker(eid='ENAC.609.L3')
stac_609_l3 = Marker(eid='STAC.609.L3')
enac_621_l3 = Marker(eid='ENAC.621.L3')
stac_624_l3 = Marker(eid='STAC.624.L3')
enac_636_l3 = Marker(eid='ENAC.636.L3')
stac_636_l3 = Marker(eid='STAC.636.L3')
enac_648_l3 = Marker(eid='ENAC.648.L3')
stac_648_l3 = Marker(eid='STAC.648.L3')
enac_660_l3 = Marker(eid='ENAC.660.L3')
stac_660_l3 = Marker(eid='STAC.660.L3')
enac_672_l3 = Marker(eid='ENAC.672.L3')
stac_672_l3 = Marker(eid='STAC.672.L3')
enac_684_l3 = Marker(eid='ENAC.684.L3')
stac_684_l3 = Marker(eid='STAC.684.L3')
enac_696_l3 = Marker(eid='ENAC.696.L3')
stac_696_l3 = Marker(eid='STAC.696.L3')
enac_707_l3 = Marker(eid='ENAC.707.L3')
stac_707_l3 = Marker(eid='STAC.707.L3')
enac_719_l3 = Marker(eid='ENAC.719.L3')
stac_719_l3 = Marker(eid='STAC.719.L3')
enac_731_l3 = Marker(eid='ENAC.731.L3')
stac_731_l3 = Marker(eid='STAC.731.L3')
enac_743_l3 = Marker(eid='ENAC.743.L3')
stac_743_l3 = Marker(eid='STAC.743.L3')
enac_755_l3 = Marker(eid='ENAC.755.L3')
stac_755_l3 = Marker(eid='STAC.755.L3')
enac_767_l3 = Marker(eid='ENAC.767.L3')
stac_770_l3 = Marker(eid='STAC.770.L3')
enac_782_l3 = Marker(eid='ENAC.782.L3')
stac_782_l3 = Marker(eid='STAC.782.L3')
enac_794_l3 = Marker(eid='ENAC.794.L3')
stac_794_l3 = Marker(eid='STAC.794.L3')
enac_806_l3 = Marker(eid='ENAC.806.L3')
stac_806_l3 = Marker(eid='STAC.806.L3')
enac_818_l3 = Marker(eid='ENAC.818.L3')
stac_818_l3 = Marker(eid='STAC.818.L3')
enac_830_l3 = Marker(eid='ENAC.830.L3')
stac_830_l3 = Marker(eid='STAC.830.L3')
enac_842_l3 = Marker(eid='ENAC.842.L3')
stac_842_l3 = Marker(eid='STAC.842.L3')
enac_854_l3 = Marker(eid='ENAC.854.L3')
stac_854_l3 = Marker(eid='STAC.854.L3')
enac_866_l3 = Marker(eid='ENAC.866.L3')
stac_866_l3 = Marker(eid='STAC.866.L3')
enac_878_l3 = Marker(eid='ENAC.878.L3')
stac_878_l3 = Marker(eid='STAC.878.L3')
enac_890_l3 = Marker(eid='ENAC.890.L3')
stac_890_l3 = Marker(eid='STAC.890.L3')
enac_902_l3 = Marker(eid='ENAC.902.L3')
stac_902_l3 = Marker(eid='STAC.902.L3')
enac_914_l3 = Marker(eid='ENAC.914.L3')
stac_917_l3 = Marker(eid='STAC.917.L3')
enac_929_l3 = Marker(eid='ENAC.929.L3')
stac_929_l3 = Marker(eid='STAC.929.L3')
enac_941_l3 = Marker(eid='ENAC.941.L3')
stac_941_l3 = Marker(eid='STAC.941.L3')
enac_953_l3 = Marker(eid='ENAC.953.L3')
stac_953_l3 = Marker(eid='STAC.953.L3')
enac_965_l3 = Marker(eid='ENAC.965.L3')
stac_965_l3 = Marker(eid='STAC.965.L3')
enac_977_l3 = Marker(eid='ENAC.977.L3')
stac_977_l3 = Marker(eid='STAC.977.L3')
enac_989_l3 = Marker(eid='ENAC.989.L3')
stac_989_l3 = Marker(eid='STAC.989.L3')
enac_1001_l3 = Marker(eid='ENAC.1001.L3')
stac_1001_l3 = Marker(eid='STAC.1001.L3')
enac_1013_l3 = Marker(eid='ENAC.1013.L3')
stac_1013_l3 = Marker(eid='STAC.1013.L3')
enac_1025_l3 = Marker(eid='ENAC.1025.L3')
stac_1025_l3 = Marker(eid='STAC.1025.L3')
enac_1037_l3 = Marker(eid='ENAC.1037.L3')
stac_1037_l3 = Marker(eid='STAC.1037.L3')
enac_1049_l3 = Marker(eid='ENAC.1049.L3')
stac_1049_l3 = Marker(eid='STAC.1049.L3')
enac_1061_l3 = Marker(eid='ENAC.1061.L3')
stac_1064_l3 = Marker(eid='STAC.1064.L3')
enac_1076_l3 = Marker(eid='ENAC.1076.L3')
stac_1076_l3 = Marker(eid='STAC.1076.L3')
enac_1088_l3 = Marker(eid='ENAC.1088.L3')
stac_1088_l3 = Marker(eid='STAC.1088.L3')
enac_1100_l3 = Marker(eid='ENAC.1100.L3')
stac_1100_l3 = Marker(eid='STAC.1100.L3')
enac_1112_l3 = Marker(eid='ENAC.1112.L3')
stac_1112_l3 = Marker(eid='STAC.1112.L3')
enac_1124_l3 = Marker(eid='ENAC.1124.L3')
stac_1124_l3 = Marker(eid='STAC.1124.L3')
enac_1136_l3 = Marker(eid='ENAC.1136.L3')
stac_1136_l3 = Marker(eid='STAC.1136.L3')
enac_1148_l3 = Marker(eid='ENAC.1148.L3')
stac_1148_l3 = Marker(eid='STAC.1148.L3')
enac_1160_l3 = Marker(eid='ENAC.1160.L3')
stac_1160_l3 = Marker(eid='STAC.1160.L3')
enac_1172_l3 = Marker(eid='ENAC.1172.L3')
stac_1172_l3 = Marker(eid='STAC.1172.L3')
enac_1184_l3 = Marker(eid='ENAC.1184.L3')
stac_1184_l3 = Marker(eid='STAC.1184.L3')
enac_1196_l3 = Marker(eid='ENAC.1196.L3')
stac_1196_l3 = Marker(eid='STAC.1196.L3')
enac_1208_l3 = Marker(eid='ENAC.1208.L3')
stac_1211_l3 = Marker(eid='STAC.1211.L3')
enac_1223_l3 = Marker(eid='ENAC.1223.L3')
stac_1223_l3 = Marker(eid='STAC.1223.L3')
enac_1235_l3 = Marker(eid='ENAC.1235.L3')
stac_1235_l3 = Marker(eid='STAC.1235.L3')
enac_1247_l3 = Marker(eid='ENAC.1247.L3')
stac_1247_l3 = Marker(eid='STAC.1247.L3')
enac_1259_l3 = Marker(eid='ENAC.1259.L3')
stac_1259_l3 = Marker(eid='STAC.1259.L3')
enac_1271_l3 = Marker(eid='ENAC.1271.L3')
stac_1271_l3 = Marker(eid='STAC.1271.L3')
enac_1283_l3 = Marker(eid='ENAC.1283.L3')
stac_1283_l3 = Marker(eid='STAC.1283.L3')
enac_1295_l3 = Marker(eid='ENAC.1295.L3')
stac_1295_l3 = Marker(eid='STAC.1295.L3')
enac_1307_l3 = Marker(eid='ENAC.1307.L3')
stac_1307_l3 = Marker(eid='STAC.1307.L3')
enac_1319_l3 = Marker(eid='ENAC.1319.L3')
stac_1319_l3 = Marker(eid='STAC.1319.L3')
enac_1331_l3 = Marker(eid='ENAC.1331.L3')
stac_1331_l3 = Marker(eid='STAC.1331.L3')
enac_1343_l3 = Marker(eid='ENAC.1343.L3')
stac_1343_l3 = Marker(eid='STAC.1343.L3')
enac_1355_l3 = Marker(eid='ENAC.1355.L3')
stac_1358_l3 = Marker(eid='STAC.1358.L3')
enac_1370_l3 = Marker(eid='ENAC.1370.L3')
stac_1370_l3 = Marker(eid='STAC.1370.L3')
enac_1382_l3 = Marker(eid='ENAC.1382.L3')
stac_1382_l3 = Marker(eid='STAC.1382.L3')
enac_1394_l3 = Marker(eid='ENAC.1394.L3')
stac_1394_l3 = Marker(eid='STAC.1394.L3')
enac_1406_l3 = Marker(eid='ENAC.1406.L3')
stac_1406_l3 = Marker(eid='STAC.1406.L3')
enac_1418_l3 = Marker(eid='ENAC.1418.L3')
stac_1418_l3 = Marker(eid='STAC.1418.L3')
enac_1430_l3 = Marker(eid='ENAC.1430.L3')
stac_1430_l3 = Marker(eid='STAC.1430.L3')
enac_1442_l3 = Marker(eid='ENAC.1442.L3')
stac_1442_l3 = Marker(eid='STAC.1442.L3')
enac_1454_l3 = Marker(eid='ENAC.1454.L3')
stsub_1457_l3 = Marker(eid='STSUB.1457.L3')
tora_1459_l3 = Marker(eid='TORA.1459.L3')
otrbw_1523_l3 = Marker(eid='OTRBW.1523.L3')
otrbw_1597_l3 = Marker(eid='OTRBW.1597.L3')
otrbw_1635_l3 = Marker(eid='OTRBW.1635.L3')
ensub_1652_l3 = Marker(eid='ENSUB.1652.L3')
ensec_1652_l3 = Marker(eid='ENSEC.1652.L3')
stsec_1652_cl = Marker(eid='STSEC.1652.CL')
stblock_1652_cl = Marker(eid='STBLOCK.1652.CL')
tora_1658_cl = Marker(eid='TORA.1658.CL')
dcm_1659_cl = Marker(eid='DCM.1659.CL')
match_1673_cl = Marker(eid='MATCH.1673.CL')
mpbpmi_1675_cl = Marker(eid='MPBPMI.1675.CL')
otrb_1689_cl = Marker(eid='OTRB.1689.CL')
mpbpmi_1693_cl = Marker(eid='MPBPMI.1693.CL')
otrb_1725_cl = Marker(eid='OTRB.1725.CL')
mpbpmi_1729_cl = Marker(eid='MPBPMI.1729.CL')
tora_1765_cl = Marker(eid='TORA.1765.CL')
otrb_1797_cl = Marker(eid='OTRB.1797.CL')
otrb_1833_cl = Marker(eid='OTRB.1833.CL')
mpbpmi_1837_cl = Marker(eid='MPBPMI.1837.CL')
ensec_1854_cl = Marker(eid='ENSEC.1854.CL')
stsec_1854_tl = Marker(eid='STSEC.1854.TL')
stsub_1854_tl = Marker(eid='STSUB.1854.TL')
mpbpmi_1861_tl = Marker(eid='MPBPMI.1861.TL')
mpbpmi_1863_tl = Marker(eid='MPBPMI.1863.TL')
tora_1865_tl = Marker(eid='TORA.1865.TL')
dcm_1865_tl = Marker(eid='DCM.1865.TL')
mpbpmi_1878_tl = Marker(eid='MPBPMI.1878.TL')
mpbpmi_1889_tl = Marker(eid='MPBPMI.1889.TL')
enblock_1891_cl = Marker(eid='ENBLOCK.1891.CL')
otrbw_1899_tl = Marker(eid='OTRBW.1899.TL')
mpbpmi_1910_tl = Marker(eid='MPBPMI.1910.TL')
otrbw_1914_tl = Marker(eid='OTRBW.1914.TL')
mpbpmi_1925_tl = Marker(eid='MPBPMI.1925.TL')
otrbw_1929_tl = Marker(eid='OTRBW.1929.TL')
mpbpmi_1930_tl = Marker(eid='MPBPMI.1930.TL')
bam_1931_tl = Marker(eid='BAM.1931.TL')
bam_1932_tl = Marker(eid='BAM.1932.TL')
crd_1934_tl = Marker(eid='CRD.1934.TL')
mpbpmi_1939_tl = Marker(eid='MPBPMI.1939.TL')
ensub_1940_tl = Marker(eid='ENSUB.1940.TL')
stsub_1940_tl = Marker(eid='STSUB.1940.TL')
otre_1978_tl = Marker(eid='OTRE.1978.TL')
ensub_1980_tl = Marker(eid='ENSUB.1980.TL')

# monitor 
bpma_471_b2 = Monitor(eid='BPMA.471.B2')
bpmc_488_l3 = Monitor(eid='BPMC.488.L3')
bpmc_500_l3 = Monitor(eid='BPMC.500.L3')
bpmc_512_l3 = Monitor(eid='BPMC.512.L3')
bpmc_524_l3 = Monitor(eid='BPMC.524.L3')
bpmc_536_l3 = Monitor(eid='BPMC.536.L3')
bpmc_548_l3 = Monitor(eid='BPMC.548.L3')
bpmc_560_l3 = Monitor(eid='BPMC.560.L3')
bpmr_572_l3 = Monitor(eid='BPMR.572.L3')
bpmc_584_l3 = Monitor(eid='BPMC.584.L3')
bpmc_596_l3 = Monitor(eid='BPMC.596.L3')
bpmr_608_l3 = Monitor(eid='BPMR.608.L3')
bpmc_620_l3 = Monitor(eid='BPMC.620.L3')
bpmc_635_l3 = Monitor(eid='BPMC.635.L3')
bpmc_647_l3 = Monitor(eid='BPMC.647.L3')
bpmc_659_l3 = Monitor(eid='BPMC.659.L3')
bpmc_671_l3 = Monitor(eid='BPMC.671.L3')
bpmc_683_l3 = Monitor(eid='BPMC.683.L3')
bpmr_695_l3 = Monitor(eid='BPMR.695.L3')
bpmr_707_l3 = Monitor(eid='BPMR.707.L3')
bpmc_719_l3 = Monitor(eid='BPMC.719.L3')
bpmc_731_l3 = Monitor(eid='BPMC.731.L3')
bpmc_743_l3 = Monitor(eid='BPMC.743.L3')
bpmr_755_l3 = Monitor(eid='BPMR.755.L3')
bpmc_767_l3 = Monitor(eid='BPMC.767.L3')
bpmc_782_l3 = Monitor(eid='BPMC.782.L3')
bpmc_794_l3 = Monitor(eid='BPMC.794.L3')
bpmr_806_l3 = Monitor(eid='BPMR.806.L3')
bpmr_818_l3 = Monitor(eid='BPMR.818.L3')
bpmc_830_l3 = Monitor(eid='BPMC.830.L3')
bpmc_842_l3 = Monitor(eid='BPMC.842.L3')
bpmc_854_l3 = Monitor(eid='BPMC.854.L3')
bpmc_866_l3 = Monitor(eid='BPMC.866.L3')
bpmc_878_l3 = Monitor(eid='BPMC.878.L3')
bpmc_890_l3 = Monitor(eid='BPMC.890.L3')
bpmc_902_l3 = Monitor(eid='BPMC.902.L3')
bpmc_914_l3 = Monitor(eid='BPMC.914.L3')
bpmc_929_l3 = Monitor(eid='BPMC.929.L3')
bpmc_941_l3 = Monitor(eid='BPMC.941.L3')
bpmc_953_l3 = Monitor(eid='BPMC.953.L3')
bpmc_965_l3 = Monitor(eid='BPMC.965.L3')
bpmc_977_l3 = Monitor(eid='BPMC.977.L3')
bpmc_989_l3 = Monitor(eid='BPMC.989.L3')
bpmc_1001_l3 = Monitor(eid='BPMC.1001.L3')
bpmc_1013_l3 = Monitor(eid='BPMC.1013.L3')
bpmc_1025_l3 = Monitor(eid='BPMC.1025.L3')
bpmc_1037_l3 = Monitor(eid='BPMC.1037.L3')
bpmc_1049_l3 = Monitor(eid='BPMC.1049.L3')
bpmc_1061_l3 = Monitor(eid='BPMC.1061.L3')
bpmc_1076_l3 = Monitor(eid='BPMC.1076.L3')
bpmr_1088_l3 = Monitor(eid='BPMR.1088.L3')
bpmc_1100_l3 = Monitor(eid='BPMC.1100.L3')
bpmr_1112_l3 = Monitor(eid='BPMR.1112.L3')
bpmc_1124_l3 = Monitor(eid='BPMC.1124.L3')
bpmc_1136_l3 = Monitor(eid='BPMC.1136.L3')
bpmc_1148_l3 = Monitor(eid='BPMC.1148.L3')
bpmc_1160_l3 = Monitor(eid='BPMC.1160.L3')
bpmr_1172_l3 = Monitor(eid='BPMR.1172.L3')
bpmr_1184_l3 = Monitor(eid='BPMR.1184.L3')
bpmc_1196_l3 = Monitor(eid='BPMC.1196.L3')
bpmc_1208_l3 = Monitor(eid='BPMC.1208.L3')
bpmr_1223_l3 = Monitor(eid='BPMR.1223.L3')
bpmc_1235_l3 = Monitor(eid='BPMC.1235.L3')
bpmc_1247_l3 = Monitor(eid='BPMC.1247.L3')
bpmc_1259_l3 = Monitor(eid='BPMC.1259.L3')
bpmc_1271_l3 = Monitor(eid='BPMC.1271.L3')
bpmc_1283_l3 = Monitor(eid='BPMC.1283.L3')
bpmc_1295_l3 = Monitor(eid='BPMC.1295.L3')
bpmr_1307_l3 = Monitor(eid='BPMR.1307.L3')
bpmc_1319_l3 = Monitor(eid='BPMC.1319.L3')
bpmc_1331_l3 = Monitor(eid='BPMC.1331.L3')
bpmc_1343_l3 = Monitor(eid='BPMC.1343.L3')
bpmc_1355_l3 = Monitor(eid='BPMC.1355.L3')
bpmc_1370_l3 = Monitor(eid='BPMC.1370.L3')
bpmc_1382_l3 = Monitor(eid='BPMC.1382.L3')
bpmc_1394_l3 = Monitor(eid='BPMC.1394.L3')
bpmr_1406_l3 = Monitor(eid='BPMR.1406.L3')
bpmc_1418_l3 = Monitor(eid='BPMC.1418.L3')
bpmr_1430_l3 = Monitor(eid='BPMR.1430.L3')
bpmc_1442_l3 = Monitor(eid='BPMC.1442.L3')
bpmc_1454_l3 = Monitor(eid='BPMC.1454.L3')
bpma_1475_l3 = Monitor(eid='BPMA.1475.L3')
bpma_1499_l3 = Monitor(eid='BPMA.1499.L3')
bpma_1541_l3 = Monitor(eid='BPMA.1541.L3')
bpma_1578_l3 = Monitor(eid='BPMA.1578.L3')
bpma_1615_l3 = Monitor(eid='BPMA.1615.L3')
bpma_1628_l3 = Monitor(eid='BPMA.1628.L3')
bpma_1641_l3 = Monitor(eid='BPMA.1641.L3')
bpma_1650_l3 = Monitor(eid='BPMA.1650.L3')
bpma_1659_cl = Monitor(eid='BPMA.1659.CL')
bpma_1669_cl = Monitor(eid='BPMA.1669.CL')
bpmi_1675_cl = Monitor(eid='BPMI.1675.CL')
bpma_1684_cl = Monitor(eid='BPMA.1684.CL')
bpmi_1693_cl = Monitor(eid='BPMI.1693.CL')
bpma_1702_cl = Monitor(eid='BPMA.1702.CL')
bpma_1711_cl = Monitor(eid='BPMA.1711.CL')
bpma_1720_cl = Monitor(eid='BPMA.1720.CL')
bpmi_1729_cl = Monitor(eid='BPMI.1729.CL')
bpma_1738_cl = Monitor(eid='BPMA.1738.CL')
bpma_1746_cl = Monitor(eid='BPMA.1746.CL')
bpma_1750_cl = Monitor(eid='BPMA.1750.CL')
bpma_1756_cl = Monitor(eid='BPMA.1756.CL')
bpma_1761_cl = Monitor(eid='BPMA.1761.CL')
bpma_1765_cl = Monitor(eid='BPMA.1765.CL')
bpma_1769_cl = Monitor(eid='BPMA.1769.CL')
bpma_1773_cl = Monitor(eid='BPMA.1773.CL')
bpma_1777_cl = Monitor(eid='BPMA.1777.CL')
bpma_1783_cl = Monitor(eid='BPMA.1783.CL')
bpma_1792_cl = Monitor(eid='BPMA.1792.CL')
bpma_1801_cl = Monitor(eid='BPMA.1801.CL')
bpma_1810_cl = Monitor(eid='BPMA.1810.CL')
bpma_1819_cl = Monitor(eid='BPMA.1819.CL')
bpma_1828_cl = Monitor(eid='BPMA.1828.CL')
bpmi_1837_cl = Monitor(eid='BPMI.1837.CL')
bpma_1846_cl = Monitor(eid='BPMA.1846.CL')
bpma_1853_cl = Monitor(eid='BPMA.1853.CL')
bpmi_1860_tl = Monitor(eid='BPMI.1860.TL')
bpmi_1863_tl = Monitor(eid='BPMI.1863.TL')
bpma_1868_tl = Monitor(eid='BPMA.1868.TL')
bpma_1873_tl = Monitor(eid='BPMA.1873.TL')
bpmi_1878_tl = Monitor(eid='BPMI.1878.TL')
bpmi_1889_tl = Monitor(eid='BPMI.1889.TL')
bpmi_1910_tl = Monitor(eid='BPMI.1910.TL')
bpmi_1925_tl = Monitor(eid='BPMI.1925.TL')
bpmi_1930_tl = Monitor(eid='BPMI.1930.TL')
bpmi_1939_tl = Monitor(eid='BPMI.1939.TL')
bpma_1966_tl = Monitor(eid='BPMA.1966.TL')
bpmd_1977_tl = Monitor(eid='BPMD.1977.TL')

# sextupoles 
sa_1674_cl = Sextupole(l=0.3164, k2=5.577060799324, tilt=1.570796327, eid='SA.1674.CL')
sa_1683_cl = Sextupole(l=0.3164, k2=-4.689136800824, tilt=1.570796327, eid='SA.1683.CL')
sa_1691_cl = Sextupole(l=0.3164, k2=0.903939326774, tilt=1.570796327, eid='SA.1691.CL')
sa_1692_cl = Sextupole(l=0.3164, k2=0.903939326774, tilt=1.570796327, eid='SA.1692.CL')
sa_1700_cl = Sextupole(l=0.3164, k2=-4.689136800824, tilt=1.570796327, eid='SA.1700.CL')
sa_1708_cl = Sextupole(l=0.3164, k2=5.577060799324, tilt=1.570796327, eid='SA.1708.CL')
sa_1710_cl = Sextupole(l=0.3164, k2=5.577060799324, tilt=1.570796327, eid='SA.1710.CL')
sa_1719_cl = Sextupole(l=0.3164, k2=-4.689136800824, tilt=1.570796327, eid='SA.1719.CL')
sa_1726_cl = Sextupole(l=0.3164, k2=0.903939326774, tilt=1.570796327, eid='SA.1726.CL')
sa_1728_cl = Sextupole(l=0.3164, k2=0.903939326774, tilt=1.570796327, eid='SA.1728.CL')
sa_1736_cl = Sextupole(l=0.3164, k2=-4.689136800824, tilt=1.570796327, eid='SA.1736.CL')
sa_1744_cl = Sextupole(l=0.3164, k2=5.577060799324, tilt=1.570796327, eid='SA.1744.CL')
sa_1782_cl = Sextupole(l=0.3164, k2=-5.577060799324, tilt=1.570796327, eid='SA.1782.CL')
sa_1791_cl = Sextupole(l=0.3164, k2=4.689136800824, tilt=1.570796327, eid='SA.1791.CL')
sa_1798_cl = Sextupole(l=0.3164, k2=-0.903939326774, tilt=1.570796327, eid='SA.1798.CL')
sa_1800_cl = Sextupole(l=0.3164, k2=-0.903939326774, tilt=1.570796327, eid='SA.1800.CL')
sa_1808_cl = Sextupole(l=0.3164, k2=4.689136800824, tilt=1.570796327, eid='SA.1808.CL')
sa_1816_cl = Sextupole(l=0.3164, k2=-5.577060799324, tilt=1.570796327, eid='SA.1816.CL')
sa_1818_cl = Sextupole(l=0.3164, k2=-5.577060799324, tilt=1.570796327, eid='SA.1818.CL')
sa_1827_cl = Sextupole(l=0.3164, k2=4.689136800824, tilt=1.570796327, eid='SA.1827.CL')
sa_1834_cl = Sextupole(l=0.3164, k2=-0.903939326774, tilt=1.570796327, eid='SA.1834.CL')
sa_1836_cl = Sextupole(l=0.3164, k2=-0.903939326774, tilt=1.570796327, eid='SA.1836.CL')
sa_1844_cl = Sextupole(l=0.3164, k2=4.689136800824, tilt=1.570796327, eid='SA.1844.CL')
sa_1852_cl = Sextupole(l=0.3164, k2=-5.577060799324, tilt=1.570796327, eid='SA.1852.CL')

# octupole 

# undulator 

# cavity
k_e = 0
c_a6_1_1_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A6.1.1.L3')
c_a6_1_2_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A6.1.2.L3')
c_a6_1_3_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A6.1.3.L3')
c_a6_1_4_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A6.1.4.L3')
c_a6_1_5_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A6.1.5.L3')
c_a6_1_6_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A6.1.6.L3')
c_a6_1_7_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A6.1.7.L3')
c_a6_1_8_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A6.1.8.L3')
c_a6_2_1_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A6.2.1.L3')
c_a6_2_2_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A6.2.2.L3')
c_a6_2_3_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A6.2.3.L3')
c_a6_2_4_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A6.2.4.L3')
c_a6_2_5_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A6.2.5.L3')
c_a6_2_6_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A6.2.6.L3')
c_a6_2_7_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A6.2.7.L3')
c_a6_2_8_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A6.2.8.L3')
c_a6_3_1_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A6.3.1.L3')
c_a6_3_2_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A6.3.2.L3')
c_a6_3_3_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A6.3.3.L3')
c_a6_3_4_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A6.3.4.L3')
c_a6_3_5_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A6.3.5.L3')
c_a6_3_6_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A6.3.6.L3')
c_a6_3_7_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A6.3.7.L3')
c_a6_3_8_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A6.3.8.L3')
c_a6_4_1_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A6.4.1.L3')
c_a6_4_2_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A6.4.2.L3')
c_a6_4_3_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A6.4.3.L3')
c_a6_4_4_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A6.4.4.L3')
c_a6_4_5_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A6.4.5.L3')
c_a6_4_6_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A6.4.6.L3')
c_a6_4_7_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A6.4.7.L3')
c_a6_4_8_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A6.4.8.L3')
c_a7_1_1_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A7.1.1.L3')
c_a7_1_2_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A7.1.2.L3')
c_a7_1_3_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A7.1.3.L3')
c_a7_1_4_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A7.1.4.L3')
c_a7_1_5_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A7.1.5.L3')
c_a7_1_6_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A7.1.6.L3')
c_a7_1_7_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A7.1.7.L3')
c_a7_1_8_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A7.1.8.L3')
c_a7_2_1_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A7.2.1.L3')
c_a7_2_2_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A7.2.2.L3')
c_a7_2_3_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A7.2.3.L3')
c_a7_2_4_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A7.2.4.L3')
c_a7_2_5_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A7.2.5.L3')
c_a7_2_6_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A7.2.6.L3')
c_a7_2_7_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A7.2.7.L3')
c_a7_2_8_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A7.2.8.L3')
c_a7_3_1_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A7.3.1.L3')
c_a7_3_2_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A7.3.2.L3')
c_a7_3_3_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A7.3.3.L3')
c_a7_3_4_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A7.3.4.L3')
c_a7_3_5_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A7.3.5.L3')
c_a7_3_6_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A7.3.6.L3')
c_a7_3_7_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A7.3.7.L3')
c_a7_3_8_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A7.3.8.L3')
c_a7_4_1_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A7.4.1.L3')
c_a7_4_2_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A7.4.2.L3')
c_a7_4_3_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A7.4.3.L3')
c_a7_4_4_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A7.4.4.L3')
c_a7_4_5_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A7.4.5.L3')
c_a7_4_6_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A7.4.6.L3')
c_a7_4_7_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A7.4.7.L3')
c_a7_4_8_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A7.4.8.L3')
c_a8_1_1_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A8.1.1.L3')
c_a8_1_2_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A8.1.2.L3')
c_a8_1_3_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A8.1.3.L3')
c_a8_1_4_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A8.1.4.L3')
c_a8_1_5_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A8.1.5.L3')
c_a8_1_6_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A8.1.6.L3')
c_a8_1_7_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A8.1.7.L3')
c_a8_1_8_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A8.1.8.L3')
c_a8_2_1_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A8.2.1.L3')
c_a8_2_2_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A8.2.2.L3')
c_a8_2_3_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A8.2.3.L3')
c_a8_2_4_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A8.2.4.L3')
c_a8_2_5_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A8.2.5.L3')
c_a8_2_6_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A8.2.6.L3')
c_a8_2_7_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A8.2.7.L3')
c_a8_2_8_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A8.2.8.L3')
c_a8_3_1_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A8.3.1.L3')
c_a8_3_2_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A8.3.2.L3')
c_a8_3_3_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A8.3.3.L3')
c_a8_3_4_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A8.3.4.L3')
c_a8_3_5_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A8.3.5.L3')
c_a8_3_6_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A8.3.6.L3')
c_a8_3_7_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A8.3.7.L3')
c_a8_3_8_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A8.3.8.L3')
c_a8_4_1_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A8.4.1.L3')
c_a8_4_2_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A8.4.2.L3')
c_a8_4_3_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A8.4.3.L3')
c_a8_4_4_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A8.4.4.L3')
c_a8_4_5_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A8.4.5.L3')
c_a8_4_6_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A8.4.6.L3')
c_a8_4_7_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A8.4.7.L3')
c_a8_4_8_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A8.4.8.L3')
c_a9_1_1_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A9.1.1.L3')
c_a9_1_2_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A9.1.2.L3')
c_a9_1_3_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A9.1.3.L3')
c_a9_1_4_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A9.1.4.L3')
c_a9_1_5_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A9.1.5.L3')
c_a9_1_6_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A9.1.6.L3')
c_a9_1_7_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A9.1.7.L3')
c_a9_1_8_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A9.1.8.L3')
c_a9_2_1_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A9.2.1.L3')
c_a9_2_2_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A9.2.2.L3')
c_a9_2_3_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A9.2.3.L3')
c_a9_2_4_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A9.2.4.L3')
c_a9_2_5_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A9.2.5.L3')
c_a9_2_6_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A9.2.6.L3')
c_a9_2_7_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A9.2.7.L3')
c_a9_2_8_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A9.2.8.L3')
c_a9_3_1_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A9.3.1.L3')
c_a9_3_2_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A9.3.2.L3')
c_a9_3_3_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A9.3.3.L3')
c_a9_3_4_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A9.3.4.L3')
c_a9_3_5_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A9.3.5.L3')
c_a9_3_6_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A9.3.6.L3')
c_a9_3_7_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A9.3.7.L3')
c_a9_3_8_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A9.3.8.L3')
c_a9_4_1_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A9.4.1.L3')
c_a9_4_2_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A9.4.2.L3')
c_a9_4_3_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A9.4.3.L3')
c_a9_4_4_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A9.4.4.L3')
c_a9_4_5_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A9.4.5.L3')
c_a9_4_6_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A9.4.6.L3')
c_a9_4_7_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A9.4.7.L3')
c_a9_4_8_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A9.4.8.L3')
c_a10_1_1_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A10.1.1.L3')
c_a10_1_2_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A10.1.2.L3')
c_a10_1_3_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A10.1.3.L3')
c_a10_1_4_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A10.1.4.L3')
c_a10_1_5_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A10.1.5.L3')
c_a10_1_6_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A10.1.6.L3')
c_a10_1_7_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A10.1.7.L3')
c_a10_1_8_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A10.1.8.L3')
c_a10_2_1_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A10.2.1.L3')
c_a10_2_2_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A10.2.2.L3')
c_a10_2_3_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A10.2.3.L3')
c_a10_2_4_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A10.2.4.L3')
c_a10_2_5_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A10.2.5.L3')
c_a10_2_6_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A10.2.6.L3')
c_a10_2_7_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A10.2.7.L3')
c_a10_2_8_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A10.2.8.L3')
c_a10_3_1_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A10.3.1.L3')
c_a10_3_2_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A10.3.2.L3')
c_a10_3_3_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A10.3.3.L3')
c_a10_3_4_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A10.3.4.L3')
c_a10_3_5_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A10.3.5.L3')
c_a10_3_6_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A10.3.6.L3')
c_a10_3_7_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A10.3.7.L3')
c_a10_3_8_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A10.3.8.L3')
c_a10_4_1_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A10.4.1.L3')
c_a10_4_2_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A10.4.2.L3')
c_a10_4_3_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A10.4.3.L3')
c_a10_4_4_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A10.4.4.L3')
c_a10_4_5_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A10.4.5.L3')
c_a10_4_6_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A10.4.6.L3')
c_a10_4_7_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A10.4.7.L3')
c_a10_4_8_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A10.4.8.L3')
c_a11_1_1_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A11.1.1.L3')
c_a11_1_2_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A11.1.2.L3')
c_a11_1_3_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A11.1.3.L3')
c_a11_1_4_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A11.1.4.L3')
c_a11_1_5_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A11.1.5.L3')
c_a11_1_6_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A11.1.6.L3')
c_a11_1_7_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A11.1.7.L3')
c_a11_1_8_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A11.1.8.L3')
c_a11_2_1_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A11.2.1.L3')
c_a11_2_2_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A11.2.2.L3')
c_a11_2_3_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A11.2.3.L3')
c_a11_2_4_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A11.2.4.L3')
c_a11_2_5_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A11.2.5.L3')
c_a11_2_6_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A11.2.6.L3')
c_a11_2_7_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A11.2.7.L3')
c_a11_2_8_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A11.2.8.L3')
c_a11_3_1_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A11.3.1.L3')
c_a11_3_2_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A11.3.2.L3')
c_a11_3_3_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A11.3.3.L3')
c_a11_3_4_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A11.3.4.L3')
c_a11_3_5_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A11.3.5.L3')
c_a11_3_6_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A11.3.6.L3')
c_a11_3_7_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A11.3.7.L3')
c_a11_3_8_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A11.3.8.L3')
c_a11_4_1_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A11.4.1.L3')
c_a11_4_2_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A11.4.2.L3')
c_a11_4_3_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A11.4.3.L3')
c_a11_4_4_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A11.4.4.L3')
c_a11_4_5_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A11.4.5.L3')
c_a11_4_6_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A11.4.6.L3')
c_a11_4_7_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A11.4.7.L3')
c_a11_4_8_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A11.4.8.L3')
c_a12_1_1_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A12.1.1.L3')
c_a12_1_2_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A12.1.2.L3')
c_a12_1_3_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A12.1.3.L3')
c_a12_1_4_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A12.1.4.L3')
c_a12_1_5_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A12.1.5.L3')
c_a12_1_6_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A12.1.6.L3')
c_a12_1_7_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A12.1.7.L3')
c_a12_1_8_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A12.1.8.L3')
c_a12_2_1_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A12.2.1.L3')
c_a12_2_2_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A12.2.2.L3')
c_a12_2_3_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A12.2.3.L3')
c_a12_2_4_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A12.2.4.L3')
c_a12_2_5_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A12.2.5.L3')
c_a12_2_6_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A12.2.6.L3')
c_a12_2_7_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A12.2.7.L3')
c_a12_2_8_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A12.2.8.L3')
c_a12_3_1_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A12.3.1.L3')
c_a12_3_2_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A12.3.2.L3')
c_a12_3_3_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A12.3.3.L3')
c_a12_3_4_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A12.3.4.L3')
c_a12_3_5_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A12.3.5.L3')
c_a12_3_6_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A12.3.6.L3')
c_a12_3_7_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A12.3.7.L3')
c_a12_3_8_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A12.3.8.L3')
c_a12_4_1_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A12.4.1.L3')
c_a12_4_2_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A12.4.2.L3')
c_a12_4_3_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A12.4.3.L3')
c_a12_4_4_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A12.4.4.L3')
c_a12_4_5_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A12.4.5.L3')
c_a12_4_6_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A12.4.6.L3')
c_a12_4_7_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A12.4.7.L3')
c_a12_4_8_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A12.4.8.L3')
c_a13_1_1_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A13.1.1.L3')
c_a13_1_2_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A13.1.2.L3')
c_a13_1_3_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A13.1.3.L3')
c_a13_1_4_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A13.1.4.L3')
c_a13_1_5_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A13.1.5.L3')
c_a13_1_6_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A13.1.6.L3')
c_a13_1_7_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A13.1.7.L3')
c_a13_1_8_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A13.1.8.L3')
c_a13_2_1_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A13.2.1.L3')
c_a13_2_2_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A13.2.2.L3')
c_a13_2_3_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A13.2.3.L3')
c_a13_2_4_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A13.2.4.L3')
c_a13_2_5_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A13.2.5.L3')
c_a13_2_6_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A13.2.6.L3')
c_a13_2_7_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A13.2.7.L3')
c_a13_2_8_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A13.2.8.L3')
c_a13_3_1_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A13.3.1.L3')
c_a13_3_2_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A13.3.2.L3')
c_a13_3_3_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A13.3.3.L3')
c_a13_3_4_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A13.3.4.L3')
c_a13_3_5_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A13.3.5.L3')
c_a13_3_6_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A13.3.6.L3')
c_a13_3_7_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A13.3.7.L3')
c_a13_3_8_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A13.3.8.L3')
c_a13_4_1_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A13.4.1.L3')
c_a13_4_2_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A13.4.2.L3')
c_a13_4_3_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A13.4.3.L3')
c_a13_4_4_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A13.4.4.L3')
c_a13_4_5_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A13.4.5.L3')
c_a13_4_6_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A13.4.6.L3')
c_a13_4_7_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A13.4.7.L3')
c_a13_4_8_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A13.4.8.L3')
c_a14_1_1_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A14.1.1.L3')
c_a14_1_2_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A14.1.2.L3')
c_a14_1_3_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A14.1.3.L3')
c_a14_1_4_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A14.1.4.L3')
c_a14_1_5_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A14.1.5.L3')
c_a14_1_6_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A14.1.6.L3')
c_a14_1_7_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A14.1.7.L3')
c_a14_1_8_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A14.1.8.L3')
c_a14_2_1_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A14.2.1.L3')
c_a14_2_2_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A14.2.2.L3')
c_a14_2_3_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A14.2.3.L3')
c_a14_2_4_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A14.2.4.L3')
c_a14_2_5_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A14.2.5.L3')
c_a14_2_6_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A14.2.6.L3')
c_a14_2_7_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A14.2.7.L3')
c_a14_2_8_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A14.2.8.L3')
c_a14_3_1_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A14.3.1.L3')
c_a14_3_2_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A14.3.2.L3')
c_a14_3_3_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A14.3.3.L3')
c_a14_3_4_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A14.3.4.L3')
c_a14_3_5_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A14.3.5.L3')
c_a14_3_6_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A14.3.6.L3')
c_a14_3_7_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A14.3.7.L3')
c_a14_3_8_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A14.3.8.L3')
c_a14_4_1_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A14.4.1.L3')
c_a14_4_2_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A14.4.2.L3')
c_a14_4_3_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A14.4.3.L3')
c_a14_4_4_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A14.4.4.L3')
c_a14_4_5_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A14.4.5.L3')
c_a14_4_6_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A14.4.6.L3')
c_a14_4_7_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A14.4.7.L3')
c_a14_4_8_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A14.4.8.L3')
c_a15_1_1_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A15.1.1.L3')
c_a15_1_2_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A15.1.2.L3')
c_a15_1_3_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A15.1.3.L3')
c_a15_1_4_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A15.1.4.L3')
c_a15_1_5_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A15.1.5.L3')
c_a15_1_6_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A15.1.6.L3')
c_a15_1_7_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A15.1.7.L3')
c_a15_1_8_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A15.1.8.L3')
c_a15_2_1_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A15.2.1.L3')
c_a15_2_2_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A15.2.2.L3')
c_a15_2_3_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A15.2.3.L3')
c_a15_2_4_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A15.2.4.L3')
c_a15_2_5_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A15.2.5.L3')
c_a15_2_6_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A15.2.6.L3')
c_a15_2_7_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A15.2.7.L3')
c_a15_2_8_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A15.2.8.L3')
c_a15_3_1_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A15.3.1.L3')
c_a15_3_2_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A15.3.2.L3')
c_a15_3_3_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A15.3.3.L3')
c_a15_3_4_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A15.3.4.L3')
c_a15_3_5_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A15.3.5.L3')
c_a15_3_6_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A15.3.6.L3')
c_a15_3_7_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A15.3.7.L3')
c_a15_3_8_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A15.3.8.L3')
c_a15_4_1_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A15.4.1.L3')
c_a15_4_2_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A15.4.2.L3')
c_a15_4_3_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A15.4.3.L3')
c_a15_4_4_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A15.4.4.L3')
c_a15_4_5_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A15.4.5.L3')
c_a15_4_6_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A15.4.6.L3')
c_a15_4_7_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A15.4.7.L3')
c_a15_4_8_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A15.4.8.L3')
c_a16_1_1_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A16.1.1.L3')
c_a16_1_2_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A16.1.2.L3')
c_a16_1_3_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A16.1.3.L3')
c_a16_1_4_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A16.1.4.L3')
c_a16_1_5_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A16.1.5.L3')
c_a16_1_6_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A16.1.6.L3')
c_a16_1_7_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A16.1.7.L3')
c_a16_1_8_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A16.1.8.L3')
c_a16_2_1_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A16.2.1.L3')
c_a16_2_2_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A16.2.2.L3')
c_a16_2_3_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A16.2.3.L3')
c_a16_2_4_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A16.2.4.L3')
c_a16_2_5_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A16.2.5.L3')
c_a16_2_6_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A16.2.6.L3')
c_a16_2_7_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A16.2.7.L3')
c_a16_2_8_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A16.2.8.L3')
c_a16_3_1_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A16.3.1.L3')
c_a16_3_2_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A16.3.2.L3')
c_a16_3_3_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A16.3.3.L3')
c_a16_3_4_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A16.3.4.L3')
c_a16_3_5_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A16.3.5.L3')
c_a16_3_6_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A16.3.6.L3')
c_a16_3_7_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A16.3.7.L3')
c_a16_3_8_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A16.3.8.L3')
c_a16_4_1_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A16.4.1.L3')
c_a16_4_2_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A16.4.2.L3')
c_a16_4_3_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A16.4.3.L3')
c_a16_4_4_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A16.4.4.L3')
c_a16_4_5_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A16.4.5.L3')
c_a16_4_6_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A16.4.6.L3')
c_a16_4_7_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A16.4.7.L3')
c_a16_4_8_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A16.4.8.L3')
c_a17_1_1_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A17.1.1.L3')
c_a17_1_2_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A17.1.2.L3')
c_a17_1_3_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A17.1.3.L3')
c_a17_1_4_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A17.1.4.L3')
c_a17_1_5_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A17.1.5.L3')
c_a17_1_6_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A17.1.6.L3')
c_a17_1_7_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A17.1.7.L3')
c_a17_1_8_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A17.1.8.L3')
c_a17_2_1_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A17.2.1.L3')
c_a17_2_2_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A17.2.2.L3')
c_a17_2_3_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A17.2.3.L3')
c_a17_2_4_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A17.2.4.L3')
c_a17_2_5_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A17.2.5.L3')
c_a17_2_6_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A17.2.6.L3')
c_a17_2_7_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A17.2.7.L3')
c_a17_2_8_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A17.2.8.L3')
c_a17_3_1_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A17.3.1.L3')
c_a17_3_2_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A17.3.2.L3')
c_a17_3_3_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A17.3.3.L3')
c_a17_3_4_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A17.3.4.L3')
c_a17_3_5_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A17.3.5.L3')
c_a17_3_6_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A17.3.6.L3')
c_a17_3_7_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A17.3.7.L3')
c_a17_3_8_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A17.3.8.L3')
c_a17_4_1_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A17.4.1.L3')
c_a17_4_2_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A17.4.2.L3')
c_a17_4_3_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A17.4.3.L3')
c_a17_4_4_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A17.4.4.L3')
c_a17_4_5_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A17.4.5.L3')
c_a17_4_6_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A17.4.6.L3')
c_a17_4_7_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A17.4.7.L3')
c_a17_4_8_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A17.4.8.L3')
c_a18_1_1_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A18.1.1.L3')
c_a18_1_2_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A18.1.2.L3')
c_a18_1_3_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A18.1.3.L3')
c_a18_1_4_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A18.1.4.L3')
c_a18_1_5_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A18.1.5.L3')
c_a18_1_6_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A18.1.6.L3')
c_a18_1_7_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A18.1.7.L3')
c_a18_1_8_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A18.1.8.L3')
c_a18_2_1_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A18.2.1.L3')
c_a18_2_2_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A18.2.2.L3')
c_a18_2_3_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A18.2.3.L3')
c_a18_2_4_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A18.2.4.L3')
c_a18_2_5_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A18.2.5.L3')
c_a18_2_6_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A18.2.6.L3')
c_a18_2_7_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A18.2.7.L3')
c_a18_2_8_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A18.2.8.L3')
c_a18_3_1_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A18.3.1.L3')
c_a18_3_2_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A18.3.2.L3')
c_a18_3_3_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A18.3.3.L3')
c_a18_3_4_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A18.3.4.L3')
c_a18_3_5_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A18.3.5.L3')
c_a18_3_6_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A18.3.6.L3')
c_a18_3_7_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A18.3.7.L3')
c_a18_3_8_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A18.3.8.L3')
c_a18_4_1_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A18.4.1.L3')
c_a18_4_2_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A18.4.2.L3')
c_a18_4_3_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A18.4.3.L3')
c_a18_4_4_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A18.4.4.L3')
c_a18_4_5_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A18.4.5.L3')
c_a18_4_6_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A18.4.6.L3')
c_a18_4_7_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A18.4.7.L3')
c_a18_4_8_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A18.4.8.L3')
c_a19_1_1_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A19.1.1.L3')
c_a19_1_2_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A19.1.2.L3')
c_a19_1_3_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A19.1.3.L3')
c_a19_1_4_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A19.1.4.L3')
c_a19_1_5_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A19.1.5.L3')
c_a19_1_6_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A19.1.6.L3')
c_a19_1_7_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A19.1.7.L3')
c_a19_1_8_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A19.1.8.L3')
c_a19_2_1_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A19.2.1.L3')
c_a19_2_2_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A19.2.2.L3')
c_a19_2_3_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A19.2.3.L3')
c_a19_2_4_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A19.2.4.L3')
c_a19_2_5_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A19.2.5.L3')
c_a19_2_6_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A19.2.6.L3')
c_a19_2_7_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A19.2.7.L3')
c_a19_2_8_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A19.2.8.L3')
c_a19_3_1_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A19.3.1.L3')
c_a19_3_2_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A19.3.2.L3')
c_a19_3_3_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A19.3.3.L3')
c_a19_3_4_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A19.3.4.L3')
c_a19_3_5_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A19.3.5.L3')
c_a19_3_6_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A19.3.6.L3')
c_a19_3_7_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A19.3.7.L3')
c_a19_3_8_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A19.3.8.L3')
c_a19_4_1_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A19.4.1.L3')
c_a19_4_2_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A19.4.2.L3')
c_a19_4_3_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A19.4.3.L3')
c_a19_4_4_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A19.4.4.L3')
c_a19_4_5_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A19.4.5.L3')
c_a19_4_6_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A19.4.6.L3')
c_a19_4_7_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A19.4.7.L3')
c_a19_4_8_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A19.4.8.L3')
c_a20_1_1_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A20.1.1.L3')
c_a20_1_2_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A20.1.2.L3')
c_a20_1_3_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A20.1.3.L3')
c_a20_1_4_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A20.1.4.L3')
c_a20_1_5_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A20.1.5.L3')
c_a20_1_6_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A20.1.6.L3')
c_a20_1_7_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A20.1.7.L3')
c_a20_1_8_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A20.1.8.L3')
c_a20_2_1_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A20.2.1.L3')
c_a20_2_2_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A20.2.2.L3')
c_a20_2_3_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A20.2.3.L3')
c_a20_2_4_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A20.2.4.L3')
c_a20_2_5_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A20.2.5.L3')
c_a20_2_6_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A20.2.6.L3')
c_a20_2_7_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A20.2.7.L3')
c_a20_2_8_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A20.2.8.L3')
c_a20_3_1_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A20.3.1.L3')
c_a20_3_2_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A20.3.2.L3')
c_a20_3_3_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A20.3.3.L3')
c_a20_3_4_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A20.3.4.L3')
c_a20_3_5_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A20.3.5.L3')
c_a20_3_6_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A20.3.6.L3')
c_a20_3_7_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A20.3.7.L3')
c_a20_3_8_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A20.3.8.L3')
c_a20_4_1_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A20.4.1.L3')
c_a20_4_2_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A20.4.2.L3')
c_a20_4_3_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A20.4.3.L3')
c_a20_4_4_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A20.4.4.L3')
c_a20_4_5_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A20.4.5.L3')
c_a20_4_6_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A20.4.6.L3')
c_a20_4_7_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A20.4.7.L3')
c_a20_4_8_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A20.4.8.L3')
c_a21_1_1_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A21.1.1.L3')
c_a21_1_2_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A21.1.2.L3')
c_a21_1_3_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A21.1.3.L3')
c_a21_1_4_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A21.1.4.L3')
c_a21_1_5_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A21.1.5.L3')
c_a21_1_6_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A21.1.6.L3')
c_a21_1_7_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A21.1.7.L3')
c_a21_1_8_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A21.1.8.L3')
c_a21_2_1_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A21.2.1.L3')
c_a21_2_2_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A21.2.2.L3')
c_a21_2_3_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A21.2.3.L3')
c_a21_2_4_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A21.2.4.L3')
c_a21_2_5_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A21.2.5.L3')
c_a21_2_6_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A21.2.6.L3')
c_a21_2_7_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A21.2.7.L3')
c_a21_2_8_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A21.2.8.L3')
c_a21_3_1_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A21.3.1.L3')
c_a21_3_2_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A21.3.2.L3')
c_a21_3_3_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A21.3.3.L3')
c_a21_3_4_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A21.3.4.L3')
c_a21_3_5_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A21.3.5.L3')
c_a21_3_6_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A21.3.6.L3')
c_a21_3_7_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A21.3.7.L3')
c_a21_3_8_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A21.3.8.L3')
c_a21_4_1_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A21.4.1.L3')
c_a21_4_2_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A21.4.2.L3')
c_a21_4_3_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A21.4.3.L3')
c_a21_4_4_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A21.4.4.L3')
c_a21_4_5_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A21.4.5.L3')
c_a21_4_6_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A21.4.6.L3')
c_a21_4_7_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A21.4.7.L3')
c_a21_4_8_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A21.4.8.L3')
c_a22_1_1_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A22.1.1.L3')
c_a22_1_2_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A22.1.2.L3')
c_a22_1_3_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A22.1.3.L3')
c_a22_1_4_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A22.1.4.L3')
c_a22_1_5_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A22.1.5.L3')
c_a22_1_6_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A22.1.6.L3')
c_a22_1_7_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A22.1.7.L3')
c_a22_1_8_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A22.1.8.L3')
c_a22_2_1_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A22.2.1.L3')
c_a22_2_2_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A22.2.2.L3')
c_a22_2_3_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A22.2.3.L3')
c_a22_2_4_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A22.2.4.L3')
c_a22_2_5_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A22.2.5.L3')
c_a22_2_6_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A22.2.6.L3')
c_a22_2_7_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A22.2.7.L3')
c_a22_2_8_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A22.2.8.L3')
c_a22_3_1_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A22.3.1.L3')
c_a22_3_2_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A22.3.2.L3')
c_a22_3_3_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A22.3.3.L3')
c_a22_3_4_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A22.3.4.L3')
c_a22_3_5_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A22.3.5.L3')
c_a22_3_6_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A22.3.6.L3')
c_a22_3_7_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A22.3.7.L3')
c_a22_3_8_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A22.3.8.L3')
c_a22_4_1_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A22.4.1.L3')
c_a22_4_2_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A22.4.2.L3')
c_a22_4_3_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A22.4.3.L3')
c_a22_4_4_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A22.4.4.L3')
c_a22_4_5_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A22.4.5.L3')
c_a22_4_6_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A22.4.6.L3')
c_a22_4_7_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A22.4.7.L3')
c_a22_4_8_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A22.4.8.L3')
c_a23_1_1_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A23.1.1.L3')
c_a23_1_2_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A23.1.2.L3')
c_a23_1_3_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A23.1.3.L3')
c_a23_1_4_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A23.1.4.L3')
c_a23_1_5_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A23.1.5.L3')
c_a23_1_6_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A23.1.6.L3')
c_a23_1_7_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A23.1.7.L3')
c_a23_1_8_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A23.1.8.L3')
c_a23_2_1_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A23.2.1.L3')
c_a23_2_2_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A23.2.2.L3')
c_a23_2_3_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A23.2.3.L3')
c_a23_2_4_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A23.2.4.L3')
c_a23_2_5_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A23.2.5.L3')
c_a23_2_6_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A23.2.6.L3')
c_a23_2_7_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A23.2.7.L3')
c_a23_2_8_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A23.2.8.L3')
c_a23_3_1_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A23.3.1.L3')
c_a23_3_2_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A23.3.2.L3')
c_a23_3_3_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A23.3.3.L3')
c_a23_3_4_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A23.3.4.L3')
c_a23_3_5_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A23.3.5.L3')
c_a23_3_6_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A23.3.6.L3')
c_a23_3_7_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A23.3.7.L3')
c_a23_3_8_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A23.3.8.L3')
c_a23_4_1_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A23.4.1.L3')
c_a23_4_2_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A23.4.2.L3')
c_a23_4_3_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A23.4.3.L3')
c_a23_4_4_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A23.4.4.L3')
c_a23_4_5_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A23.4.5.L3')
c_a23_4_6_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A23.4.6.L3')
c_a23_4_7_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A23.4.7.L3')
c_a23_4_8_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A23.4.8.L3')
c_a24_1_1_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A24.1.1.L3')
c_a24_1_2_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A24.1.2.L3')
c_a24_1_3_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A24.1.3.L3')
c_a24_1_4_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A24.1.4.L3')
c_a24_1_5_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A24.1.5.L3')
c_a24_1_6_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A24.1.6.L3')
c_a24_1_7_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A24.1.7.L3')
c_a24_1_8_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A24.1.8.L3')
c_a24_2_1_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A24.2.1.L3')
c_a24_2_2_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A24.2.2.L3')
c_a24_2_3_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A24.2.3.L3')
c_a24_2_4_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A24.2.4.L3')
c_a24_2_5_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A24.2.5.L3')
c_a24_2_6_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A24.2.6.L3')
c_a24_2_7_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A24.2.7.L3')
c_a24_2_8_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A24.2.8.L3')
c_a24_3_1_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A24.3.1.L3')
c_a24_3_2_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A24.3.2.L3')
c_a24_3_3_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A24.3.3.L3')
c_a24_3_4_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A24.3.4.L3')
c_a24_3_5_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A24.3.5.L3')
c_a24_3_6_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A24.3.6.L3')
c_a24_3_7_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A24.3.7.L3')
c_a24_3_8_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A24.3.8.L3')
c_a24_4_1_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A24.4.1.L3')
c_a24_4_2_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A24.4.2.L3')
c_a24_4_3_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A24.4.3.L3')
c_a24_4_4_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A24.4.4.L3')
c_a24_4_5_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A24.4.5.L3')
c_a24_4_6_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A24.4.6.L3')
c_a24_4_7_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A24.4.7.L3')
c_a24_4_8_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A24.4.8.L3')
c_a25_1_1_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A25.1.1.L3')
c_a25_1_2_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A25.1.2.L3')
c_a25_1_3_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A25.1.3.L3')
c_a25_1_4_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A25.1.4.L3')
c_a25_1_5_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A25.1.5.L3')
c_a25_1_6_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A25.1.6.L3')
c_a25_1_7_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A25.1.7.L3')
c_a25_1_8_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A25.1.8.L3')
c_a25_2_1_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A25.2.1.L3')
c_a25_2_2_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A25.2.2.L3')
c_a25_2_3_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A25.2.3.L3')
c_a25_2_4_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A25.2.4.L3')
c_a25_2_5_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A25.2.5.L3')
c_a25_2_6_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A25.2.6.L3')
c_a25_2_7_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A25.2.7.L3')
c_a25_2_8_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A25.2.8.L3')
c_a25_3_1_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A25.3.1.L3')
c_a25_3_2_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A25.3.2.L3')
c_a25_3_3_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A25.3.3.L3')
c_a25_3_4_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A25.3.4.L3')
c_a25_3_5_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A25.3.5.L3')
c_a25_3_6_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A25.3.6.L3')
c_a25_3_7_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A25.3.7.L3')
c_a25_3_8_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A25.3.8.L3')
c_a25_4_1_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A25.4.1.L3')
c_a25_4_2_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A25.4.2.L3')
c_a25_4_3_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A25.4.3.L3')
c_a25_4_4_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A25.4.4.L3')
c_a25_4_5_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A25.4.5.L3')
c_a25_4_6_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A25.4.6.L3')
c_a25_4_7_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A25.4.7.L3')
c_a25_4_8_l3 = Cavity(l=1.0377, v=k_e*0.02359375, freq=1300000.0, phi=0.0, eid='C.A25.4.8.L3')

# UnknowElement 

# Matrices 

# Solenoids 

# lattice 
cell_l3 = (stsub_466_b2, d_1, qd_470_b2, d_2, ccy_470_b2, d_3, dcm_471_b2,
d_4, tora_471_b2, d_5, bpma_471_b2, d_6, qd_472_b2, d_7, enblock_473_b2, 
ensub_473_b2, ensec_473_b2, stsec_473_l3, d_8, stac_477_l3, d_9, c_a6_1_1_l3, d_10, 
c_a6_1_2_l3, d_10, c_a6_1_3_l3, d_10, c_a6_1_4_l3, d_10, c_a6_1_5_l3, d_10, 
c_a6_1_6_l3, d_10, c_a6_1_7_l3, d_10, c_a6_1_8_l3, d_17, q_488_l3, d_18, 
cx_488_l3, d_19, bpmc_488_l3, d_20, enac_489_l3, stac_489_l3, d_9, c_a6_2_1_l3, 
d_10, c_a6_2_2_l3, d_10, c_a6_2_3_l3, d_10, c_a6_2_4_l3, d_10, c_a6_2_5_l3, 
d_10, c_a6_2_6_l3, d_10, c_a6_2_7_l3, d_10, c_a6_2_8_l3, d_17, q_500_l3, 
d_18, cy_500_l3, d_19, bpmc_500_l3, d_20, enac_501_l3, stac_501_l3, d_9, 
c_a6_3_1_l3, d_10, c_a6_3_2_l3, d_10, c_a6_3_3_l3, d_10, c_a6_3_4_l3, d_10, 
c_a6_3_5_l3, d_10, c_a6_3_6_l3, d_10, c_a6_3_7_l3, d_10, c_a6_3_8_l3, d_17, 
q_512_l3, d_18, cx_512_l3, d_19, bpmc_512_l3, d_20, enac_513_l3, stac_513_l3, 
d_9, c_a6_4_1_l3, d_10, c_a6_4_2_l3, d_10, c_a6_4_3_l3, d_10, c_a6_4_4_l3, 
d_10, c_a6_4_5_l3, d_10, c_a6_4_6_l3, d_10, c_a6_4_7_l3, d_10, c_a6_4_8_l3, 
d_17, q_524_l3, d_18, cy_524_l3, d_19, bpmc_524_l3, d_20, enac_525_l3, 
match_525_l3, stac_525_l3, d_9, c_a7_1_1_l3, d_10, c_a7_1_2_l3, d_10, c_a7_1_3_l3, 
d_10, c_a7_1_4_l3, d_10, c_a7_1_5_l3, d_10, c_a7_1_6_l3, d_10, c_a7_1_7_l3, 
d_10, c_a7_1_8_l3, d_17, q_536_l3, d_18, cx_536_l3, d_19, bpmc_536_l3, 
d_20, enac_537_l3, stac_537_l3, d_9, c_a7_2_1_l3, d_10, c_a7_2_2_l3, d_10, 
c_a7_2_3_l3, d_10, c_a7_2_4_l3, d_10, c_a7_2_5_l3, d_10, c_a7_2_6_l3, d_10, 
c_a7_2_7_l3, d_10, c_a7_2_8_l3, d_17, q_548_l3, d_18, cy_548_l3, d_19, 
bpmc_548_l3, d_20, enac_549_l3, stac_549_l3, d_9, c_a7_3_1_l3, d_10, c_a7_3_2_l3, 
d_10, c_a7_3_3_l3, d_10, c_a7_3_4_l3, d_10, c_a7_3_5_l3, d_10, c_a7_3_6_l3, 
d_10, c_a7_3_7_l3, d_10, c_a7_3_8_l3, d_17, q_560_l3, d_18, cx_560_l3, 
d_19, bpmc_560_l3, d_20, enac_561_l3, stac_561_l3, d_9, c_a7_4_1_l3, d_10, 
c_a7_4_2_l3, d_10, c_a7_4_3_l3, d_10, c_a7_4_4_l3, d_10, c_a7_4_5_l3, d_10, 
c_a7_4_6_l3, d_10, c_a7_4_7_l3, d_10, c_a7_4_8_l3, d_17, q_572_l3, d_18, 
cy_572_l3, d_19, bpmr_572_l3, d_20, enac_573_l3, stac_573_l3, d_9, c_a8_1_1_l3, 
d_10, c_a8_1_2_l3, d_10, c_a8_1_3_l3, d_10, c_a8_1_4_l3, d_10, c_a8_1_5_l3, 
d_10, c_a8_1_6_l3, d_10, c_a8_1_7_l3, d_10, c_a8_1_8_l3, d_17, q_584_l3, 
d_18, cx_584_l3, d_19, bpmc_584_l3, d_20, enac_585_l3, stac_585_l3, d_9, 
c_a8_2_1_l3, d_10, c_a8_2_2_l3, d_10, c_a8_2_3_l3, d_10, c_a8_2_4_l3, d_10, 
c_a8_2_5_l3, d_10, c_a8_2_6_l3, d_10, c_a8_2_7_l3, d_10, c_a8_2_8_l3, d_17, 
q_596_l3, d_18, cy_596_l3, d_19, bpmc_596_l3, d_20, enac_597_l3, stac_597_l3, 
d_9, c_a8_3_1_l3, d_10, c_a8_3_2_l3, d_10, c_a8_3_3_l3, d_10, c_a8_3_4_l3, 
d_10, c_a8_3_5_l3, d_10, c_a8_3_6_l3, d_10, c_a8_3_7_l3, d_10, c_a8_3_8_l3, 
d_17, q_608_l3, d_18, cx_608_l3, d_19, bpmr_608_l3, d_20, enac_609_l3, 
stac_609_l3, d_9, c_a8_4_1_l3, d_10, c_a8_4_2_l3, d_10, c_a8_4_3_l3, d_10, 
c_a8_4_4_l3, d_10, c_a8_4_5_l3, d_10, c_a8_4_6_l3, d_10, c_a8_4_7_l3, d_10, 
c_a8_4_8_l3, d_17, q_620_l3, d_18, cy_620_l3, d_19, bpmc_620_l3, d_20, 
enac_621_l3, d_153, stac_624_l3, d_9, c_a9_1_1_l3, d_10, c_a9_1_2_l3, d_10, 
c_a9_1_3_l3, d_10, c_a9_1_4_l3, d_10, c_a9_1_5_l3, d_10, c_a9_1_6_l3, d_10, 
c_a9_1_7_l3, d_10, c_a9_1_8_l3, d_17, q_635_l3, d_18, cx_635_l3, d_19, 
bpmc_635_l3, d_20, enac_636_l3, stac_636_l3, d_9, c_a9_2_1_l3, d_10, c_a9_2_2_l3, 
d_10, c_a9_2_3_l3, d_10, c_a9_2_4_l3, d_10, c_a9_2_5_l3, d_10, c_a9_2_6_l3, 
d_10, c_a9_2_7_l3, d_10, c_a9_2_8_l3, d_17, q_647_l3, d_18, cy_647_l3, 
d_19, bpmc_647_l3, d_20, enac_648_l3, stac_648_l3, d_9, c_a9_3_1_l3, d_10, 
c_a9_3_2_l3, d_10, c_a9_3_3_l3, d_10, c_a9_3_4_l3, d_10, c_a9_3_5_l3, d_10, 
c_a9_3_6_l3, d_10, c_a9_3_7_l3, d_10, c_a9_3_8_l3, d_17, q_659_l3, d_18, 
cx_659_l3, d_19, bpmc_659_l3, d_20, enac_660_l3, stac_660_l3, d_9, c_a9_4_1_l3, 
d_10, c_a9_4_2_l3, d_10, c_a9_4_3_l3, d_10, c_a9_4_4_l3, d_10, c_a9_4_5_l3, 
d_10, c_a9_4_6_l3, d_10, c_a9_4_7_l3, d_10, c_a9_4_8_l3, d_17, q_671_l3, 
d_18, cy_671_l3, d_19, bpmc_671_l3, d_20, enac_672_l3, stac_672_l3, d_9, 
c_a10_1_1_l3, d_10, c_a10_1_2_l3, d_10, c_a10_1_3_l3, d_10, c_a10_1_4_l3, d_10, 
c_a10_1_5_l3, d_10, c_a10_1_6_l3, d_10, c_a10_1_7_l3, d_10, c_a10_1_8_l3, d_17, 
q_683_l3, d_18, cx_683_l3, d_19, bpmc_683_l3, d_20, enac_684_l3, stac_684_l3, 
d_9, c_a10_2_1_l3, d_10, c_a10_2_2_l3, d_10, c_a10_2_3_l3, d_10, c_a10_2_4_l3, 
d_10, c_a10_2_5_l3, d_10, c_a10_2_6_l3, d_10, c_a10_2_7_l3, d_10, c_a10_2_8_l3, 
d_17, q_695_l3, d_18, cy_695_l3, d_19, bpmr_695_l3, d_20, enac_696_l3, 
stac_696_l3, d_9, c_a10_3_1_l3, d_10, c_a10_3_2_l3, d_10, c_a10_3_3_l3, d_10, 
c_a10_3_4_l3, d_10, c_a10_3_5_l3, d_10, c_a10_3_6_l3, d_10, c_a10_3_7_l3, d_10, 
c_a10_3_8_l3, d_17, q_707_l3, d_18, cx_707_l3, d_19, bpmr_707_l3, d_20, 
enac_707_l3, stac_707_l3, d_9, c_a10_4_1_l3, d_10, c_a10_4_2_l3, d_10, c_a10_4_3_l3, 
d_10, c_a10_4_4_l3, d_10, c_a10_4_5_l3, d_10, c_a10_4_6_l3, d_10, c_a10_4_7_l3, 
d_10, c_a10_4_8_l3, d_17, q_719_l3, d_18, cy_719_l3, d_19, bpmc_719_l3, 
d_20, enac_719_l3, stac_719_l3, d_9, c_a11_1_1_l3, d_10, c_a11_1_2_l3, d_10, 
c_a11_1_3_l3, d_10, c_a11_1_4_l3, d_10, c_a11_1_5_l3, d_10, c_a11_1_6_l3, d_10, 
c_a11_1_7_l3, d_10, c_a11_1_8_l3, d_17, q_731_l3, d_18, cx_731_l3, d_19, 
bpmc_731_l3, d_20, enac_731_l3, stac_731_l3, d_9, c_a11_2_1_l3, d_10, c_a11_2_2_l3, 
d_10, c_a11_2_3_l3, d_10, c_a11_2_4_l3, d_10, c_a11_2_5_l3, d_10, c_a11_2_6_l3, 
d_10, c_a11_2_7_l3, d_10, c_a11_2_8_l3, d_17, q_743_l3, d_18, cy_743_l3, 
d_19, bpmc_743_l3, d_20, enac_743_l3, stac_743_l3, d_9, c_a11_3_1_l3, d_10, 
c_a11_3_2_l3, d_10, c_a11_3_3_l3, d_10, c_a11_3_4_l3, d_10, c_a11_3_5_l3, d_10, 
c_a11_3_6_l3, d_10, c_a11_3_7_l3, d_10, c_a11_3_8_l3, d_17, q_755_l3, d_18, 
cx_755_l3, d_19, bpmr_755_l3, d_20, enac_755_l3, stac_755_l3, d_9, c_a11_4_1_l3, 
d_10, c_a11_4_2_l3, d_10, c_a11_4_3_l3, d_10, c_a11_4_4_l3, d_10, c_a11_4_5_l3, 
d_10, c_a11_4_6_l3, d_10, c_a11_4_7_l3, d_10, c_a11_4_8_l3, d_17, q_767_l3, 
d_18, cy_767_l3, d_19, bpmc_767_l3, d_20, enac_767_l3, d_153, stac_770_l3, 
d_9, c_a12_1_1_l3, d_10, c_a12_1_2_l3, d_10, c_a12_1_3_l3, d_10, c_a12_1_4_l3, 
d_10, c_a12_1_5_l3, d_10, c_a12_1_6_l3, d_10, c_a12_1_7_l3, d_10, c_a12_1_8_l3, 
d_17, q_782_l3, d_18, cx_782_l3, d_19, bpmc_782_l3, d_20, enac_782_l3, 
stac_782_l3, d_9, c_a12_2_1_l3, d_10, c_a12_2_2_l3, d_10, c_a12_2_3_l3, d_10, 
c_a12_2_4_l3, d_10, c_a12_2_5_l3, d_10, c_a12_2_6_l3, d_10, c_a12_2_7_l3, d_10, 
c_a12_2_8_l3, d_17, q_794_l3, d_18, cy_794_l3, d_19, bpmc_794_l3, d_20, 
enac_794_l3, stac_794_l3, d_9, c_a12_3_1_l3, d_10, c_a12_3_2_l3, d_10, c_a12_3_3_l3, 
d_10, c_a12_3_4_l3, d_10, c_a12_3_5_l3, d_10, c_a12_3_6_l3, d_10, c_a12_3_7_l3, 
d_10, c_a12_3_8_l3, d_17, q_806_l3, d_18, cx_806_l3, d_19, bpmr_806_l3, 
d_20, enac_806_l3, stac_806_l3, d_9, c_a12_4_1_l3, d_10, c_a12_4_2_l3, d_10, 
c_a12_4_3_l3, d_10, c_a12_4_4_l3, d_10, c_a12_4_5_l3, d_10, c_a12_4_6_l3, d_10, 
c_a12_4_7_l3, d_10, c_a12_4_8_l3, d_17, q_818_l3, d_18, cy_818_l3, d_19, 
bpmr_818_l3, d_20, enac_818_l3, stac_818_l3, d_9, c_a13_1_1_l3, d_10, c_a13_1_2_l3, 
d_10, c_a13_1_3_l3, d_10, c_a13_1_4_l3, d_10, c_a13_1_5_l3, d_10, c_a13_1_6_l3, 
d_10, c_a13_1_7_l3, d_10, c_a13_1_8_l3, d_17, q_830_l3, d_18, cx_830_l3, 
d_19, bpmc_830_l3, d_20, enac_830_l3, stac_830_l3, d_9, c_a13_2_1_l3, d_10, 
c_a13_2_2_l3, d_10, c_a13_2_3_l3, d_10, c_a13_2_4_l3, d_10, c_a13_2_5_l3, d_10, 
c_a13_2_6_l3, d_10, c_a13_2_7_l3, d_10, c_a13_2_8_l3, d_17, q_842_l3, d_18, 
cy_842_l3, d_19, bpmc_842_l3, d_20, enac_842_l3, stac_842_l3, d_9, c_a13_3_1_l3, 
d_10, c_a13_3_2_l3, d_10, c_a13_3_3_l3, d_10, c_a13_3_4_l3, d_10, c_a13_3_5_l3, 
d_10, c_a13_3_6_l3, d_10, c_a13_3_7_l3, d_10, c_a13_3_8_l3, d_17, q_854_l3, 
d_18, cx_854_l3, d_19, bpmc_854_l3, d_20, enac_854_l3, stac_854_l3, d_9, 
c_a13_4_1_l3, d_10, c_a13_4_2_l3, d_10, c_a13_4_3_l3, d_10, c_a13_4_4_l3, d_10, 
c_a13_4_5_l3, d_10, c_a13_4_6_l3, d_10, c_a13_4_7_l3, d_10, c_a13_4_8_l3, d_17, 
q_866_l3, d_18, cy_866_l3, d_19, bpmc_866_l3, d_20, enac_866_l3, stac_866_l3, 
d_9, c_a14_1_1_l3, d_10, c_a14_1_2_l3, d_10, c_a14_1_3_l3, d_10, c_a14_1_4_l3, 
d_10, c_a14_1_5_l3, d_10, c_a14_1_6_l3, d_10, c_a14_1_7_l3, d_10, c_a14_1_8_l3, 
d_17, q_878_l3, d_18, cx_878_l3, d_19, bpmc_878_l3, d_20, enac_878_l3, 
stac_878_l3, d_9, c_a14_2_1_l3, d_10, c_a14_2_2_l3, d_10, c_a14_2_3_l3, d_10, 
c_a14_2_4_l3, d_10, c_a14_2_5_l3, d_10, c_a14_2_6_l3, d_10, c_a14_2_7_l3, d_10, 
c_a14_2_8_l3, d_17, q_890_l3, d_18, cy_890_l3, d_19, bpmc_890_l3, d_20, 
enac_890_l3, stac_890_l3, d_9, c_a14_3_1_l3, d_10, c_a14_3_2_l3, d_10, c_a14_3_3_l3, 
d_10, c_a14_3_4_l3, d_10, c_a14_3_5_l3, d_10, c_a14_3_6_l3, d_10, c_a14_3_7_l3, 
d_10, c_a14_3_8_l3, d_17, q_902_l3, d_18, cx_902_l3, d_19, bpmc_902_l3, 
d_20, enac_902_l3, stac_902_l3, d_9, c_a14_4_1_l3, d_10, c_a14_4_2_l3, d_10, 
c_a14_4_3_l3, d_10, c_a14_4_4_l3, d_10, c_a14_4_5_l3, d_10, c_a14_4_6_l3, d_10, 
c_a14_4_7_l3, d_10, c_a14_4_8_l3, d_17, q_914_l3, d_18, cy_914_l3, d_19, 
bpmc_914_l3, d_20, enac_914_l3, d_153, stac_917_l3, d_9, c_a15_1_1_l3, d_10, 
c_a15_1_2_l3, d_10, c_a15_1_3_l3, d_10, c_a15_1_4_l3, d_10, c_a15_1_5_l3, d_10, 
c_a15_1_6_l3, d_10, c_a15_1_7_l3, d_10, c_a15_1_8_l3, d_17, q_929_l3, d_18, 
cx_929_l3, d_19, bpmc_929_l3, d_20, enac_929_l3, stac_929_l3, d_9, c_a15_2_1_l3, 
d_10, c_a15_2_2_l3, d_10, c_a15_2_3_l3, d_10, c_a15_2_4_l3, d_10, c_a15_2_5_l3, 
d_10, c_a15_2_6_l3, d_10, c_a15_2_7_l3, d_10, c_a15_2_8_l3, d_17, q_941_l3, 
d_18, cy_941_l3, d_19, bpmc_941_l3, d_20, enac_941_l3, stac_941_l3, d_9, 
c_a15_3_1_l3, d_10, c_a15_3_2_l3, d_10, c_a15_3_3_l3, d_10, c_a15_3_4_l3, d_10, 
c_a15_3_5_l3, d_10, c_a15_3_6_l3, d_10, c_a15_3_7_l3, d_10, c_a15_3_8_l3, d_17, 
q_953_l3, d_18, cx_953_l3, d_19, bpmc_953_l3, d_20, enac_953_l3, stac_953_l3, 
d_9, c_a15_4_1_l3, d_10, c_a15_4_2_l3, d_10, c_a15_4_3_l3, d_10, c_a15_4_4_l3, 
d_10, c_a15_4_5_l3, d_10, c_a15_4_6_l3, d_10, c_a15_4_7_l3, d_10, c_a15_4_8_l3, 
d_17, q_965_l3, d_18, cy_965_l3, d_19, bpmc_965_l3, d_20, enac_965_l3, 
stac_965_l3, d_9, c_a16_1_1_l3, d_10, c_a16_1_2_l3, d_10, c_a16_1_3_l3, d_10, 
c_a16_1_4_l3, d_10, c_a16_1_5_l3, d_10, c_a16_1_6_l3, d_10, c_a16_1_7_l3, d_10, 
c_a16_1_8_l3, d_17, q_977_l3, d_18, cx_977_l3, d_19, bpmc_977_l3, d_20, 
enac_977_l3, stac_977_l3, d_9, c_a16_2_1_l3, d_10, c_a16_2_2_l3, d_10, c_a16_2_3_l3, 
d_10, c_a16_2_4_l3, d_10, c_a16_2_5_l3, d_10, c_a16_2_6_l3, d_10, c_a16_2_7_l3, 
d_10, c_a16_2_8_l3, d_17, q_989_l3, d_18, cy_989_l3, d_19, bpmc_989_l3, 
d_20, enac_989_l3, stac_989_l3, d_9, c_a16_3_1_l3, d_10, c_a16_3_2_l3, d_10, 
c_a16_3_3_l3, d_10, c_a16_3_4_l3, d_10, c_a16_3_5_l3, d_10, c_a16_3_6_l3, d_10, 
c_a16_3_7_l3, d_10, c_a16_3_8_l3, d_17, q_1001_l3, d_18, cx_1001_l3, d_19, 
bpmc_1001_l3, d_20, enac_1001_l3, stac_1001_l3, d_9, c_a16_4_1_l3, d_10, c_a16_4_2_l3, 
d_10, c_a16_4_3_l3, d_10, c_a16_4_4_l3, d_10, c_a16_4_5_l3, d_10, c_a16_4_6_l3, 
d_10, c_a16_4_7_l3, d_10, c_a16_4_8_l3, d_17, q_1013_l3, d_18, cy_1013_l3, 
d_19, bpmc_1013_l3, d_20, enac_1013_l3, stac_1013_l3, d_9, c_a17_1_1_l3, d_10, 
c_a17_1_2_l3, d_10, c_a17_1_3_l3, d_10, c_a17_1_4_l3, d_10, c_a17_1_5_l3, d_10, 
c_a17_1_6_l3, d_10, c_a17_1_7_l3, d_10, c_a17_1_8_l3, d_17, q_1025_l3, d_18, 
cx_1025_l3, d_19, bpmc_1025_l3, d_20, enac_1025_l3, stac_1025_l3, d_9, c_a17_2_1_l3, 
d_10, c_a17_2_2_l3, d_10, c_a17_2_3_l3, d_10, c_a17_2_4_l3, d_10, c_a17_2_5_l3, 
d_10, c_a17_2_6_l3, d_10, c_a17_2_7_l3, d_10, c_a17_2_8_l3, d_17, q_1037_l3, 
d_18, cy_1037_l3, d_19, bpmc_1037_l3, d_20, enac_1037_l3, stac_1037_l3, d_9, 
c_a17_3_1_l3, d_10, c_a17_3_2_l3, d_10, c_a17_3_3_l3, d_10, c_a17_3_4_l3, d_10, 
c_a17_3_5_l3, d_10, c_a17_3_6_l3, d_10, c_a17_3_7_l3, d_10, c_a17_3_8_l3, d_17, 
q_1049_l3, d_18, cx_1049_l3, d_19, bpmc_1049_l3, d_20, enac_1049_l3, stac_1049_l3, 
d_9, c_a17_4_1_l3, d_10, c_a17_4_2_l3, d_10, c_a17_4_3_l3, d_10, c_a17_4_4_l3, 
d_10, c_a17_4_5_l3, d_10, c_a17_4_6_l3, d_10, c_a17_4_7_l3, d_10, c_a17_4_8_l3, 
d_17, q_1061_l3, d_18, cy_1061_l3, d_19, bpmc_1061_l3, d_20, enac_1061_l3, 
d_153, stac_1064_l3, d_9, c_a18_1_1_l3, d_10, c_a18_1_2_l3, d_10, c_a18_1_3_l3, 
d_10, c_a18_1_4_l3, d_10, c_a18_1_5_l3, d_10, c_a18_1_6_l3, d_10, c_a18_1_7_l3, 
d_10, c_a18_1_8_l3, d_17, q_1076_l3, d_18, cx_1076_l3, d_19, bpmc_1076_l3, 
d_20, enac_1076_l3, stac_1076_l3, d_9, c_a18_2_1_l3, d_10, c_a18_2_2_l3, d_10, 
c_a18_2_3_l3, d_10, c_a18_2_4_l3, d_10, c_a18_2_5_l3, d_10, c_a18_2_6_l3, d_10, 
c_a18_2_7_l3, d_10, c_a18_2_8_l3, d_17, q_1088_l3, d_18, cy_1088_l3, d_19, 
bpmr_1088_l3, d_20, enac_1088_l3, stac_1088_l3, d_9, c_a18_3_1_l3, d_10, c_a18_3_2_l3, 
d_10, c_a18_3_3_l3, d_10, c_a18_3_4_l3, d_10, c_a18_3_5_l3, d_10, c_a18_3_6_l3, 
d_10, c_a18_3_7_l3, d_10, c_a18_3_8_l3, d_17, q_1100_l3, d_18, cx_1100_l3, 
d_19, bpmc_1100_l3, d_20, enac_1100_l3, stac_1100_l3, d_9, c_a18_4_1_l3, d_10, 
c_a18_4_2_l3, d_10, c_a18_4_3_l3, d_10, c_a18_4_4_l3, d_10, c_a18_4_5_l3, d_10, 
c_a18_4_6_l3, d_10, c_a18_4_7_l3, d_10, c_a18_4_8_l3, d_17, q_1112_l3, d_18, 
cy_1112_l3, d_19, bpmr_1112_l3, d_20, enac_1112_l3, stac_1112_l3, d_9, c_a19_1_1_l3, 
d_10, c_a19_1_2_l3, d_10, c_a19_1_3_l3, d_10, c_a19_1_4_l3, d_10, c_a19_1_5_l3, 
d_10, c_a19_1_6_l3, d_10, c_a19_1_7_l3, d_10, c_a19_1_8_l3, d_17, q_1124_l3, 
d_18, cx_1124_l3, d_19, bpmc_1124_l3, d_20, enac_1124_l3, stac_1124_l3, d_9, 
c_a19_2_1_l3, d_10, c_a19_2_2_l3, d_10, c_a19_2_3_l3, d_10, c_a19_2_4_l3, d_10, 
c_a19_2_5_l3, d_10, c_a19_2_6_l3, d_10, c_a19_2_7_l3, d_10, c_a19_2_8_l3, d_17, 
q_1136_l3, d_658, bpmc_1136_l3, d_20, enac_1136_l3, stac_1136_l3, d_9, c_a19_3_1_l3, 
d_10, c_a19_3_2_l3, d_10, c_a19_3_3_l3, d_10, c_a19_3_4_l3, d_10, c_a19_3_5_l3, 
d_10, c_a19_3_6_l3, d_10, c_a19_3_7_l3, d_10, c_a19_3_8_l3, d_17, q_1147_l3, 
d_18, cx_1148_l3, cy_1148_l3, d_19, bpmc_1148_l3, d_20, enac_1148_l3, stac_1148_l3, 
d_9, c_a19_4_1_l3, d_10, c_a19_4_2_l3, d_10, c_a19_4_3_l3, d_10, c_a19_4_4_l3, 
d_10, c_a19_4_5_l3, d_10, c_a19_4_6_l3, d_10, c_a19_4_7_l3, d_10, c_a19_4_8_l3, 
d_17, q_1159_l3, d_18, cy_1160_l3, d_19, bpmc_1160_l3, d_20, enac_1160_l3, 
stac_1160_l3, d_9, c_a20_1_1_l3, d_10, c_a20_1_2_l3, d_10, c_a20_1_3_l3, d_10, 
c_a20_1_4_l3, d_10, c_a20_1_5_l3, d_10, c_a20_1_6_l3, d_10, c_a20_1_7_l3, d_10, 
c_a20_1_8_l3, d_17, q_1171_l3, d_18, cx_1172_l3, d_19, bpmr_1172_l3, d_20, 
enac_1172_l3, stac_1172_l3, d_9, c_a20_2_1_l3, d_10, c_a20_2_2_l3, d_10, c_a20_2_3_l3, 
d_10, c_a20_2_4_l3, d_10, c_a20_2_5_l3, d_10, c_a20_2_6_l3, d_10, c_a20_2_7_l3, 
d_10, c_a20_2_8_l3, d_17, q_1183_l3, d_18, cy_1184_l3, d_19, bpmr_1184_l3, 
d_20, enac_1184_l3, stac_1184_l3, d_9, c_a20_3_1_l3, d_10, c_a20_3_2_l3, d_10, 
c_a20_3_3_l3, d_10, c_a20_3_4_l3, d_10, c_a20_3_5_l3, d_10, c_a20_3_6_l3, d_10, 
c_a20_3_7_l3, d_10, c_a20_3_8_l3, d_17, q_1195_l3, d_18, cx_1196_l3, d_19, 
bpmc_1196_l3, d_20, enac_1196_l3, stac_1196_l3, d_9, c_a20_4_1_l3, d_10, c_a20_4_2_l3, 
d_10, c_a20_4_3_l3, d_10, c_a20_4_4_l3, d_10, c_a20_4_5_l3, d_10, c_a20_4_6_l3, 
d_10, c_a20_4_7_l3, d_10, c_a20_4_8_l3, d_17, q_1207_l3, d_18, cy_1208_l3, 
d_19, bpmc_1208_l3, d_20, enac_1208_l3, d_153, stac_1211_l3, d_9, c_a21_1_1_l3, 
d_10, c_a21_1_2_l3, d_10, c_a21_1_3_l3, d_10, c_a21_1_4_l3, d_10, c_a21_1_5_l3, 
d_10, c_a21_1_6_l3, d_10, c_a21_1_7_l3, d_10, c_a21_1_8_l3, d_17, q_1222_l3, 
d_18, cx_1223_l3, d_19, bpmr_1223_l3, d_20, enac_1223_l3, stac_1223_l3, d_9, 
c_a21_2_1_l3, d_10, c_a21_2_2_l3, d_10, c_a21_2_3_l3, d_10, c_a21_2_4_l3, d_10, 
c_a21_2_5_l3, d_10, c_a21_2_6_l3, d_10, c_a21_2_7_l3, d_10, c_a21_2_8_l3, d_17, 
q_1234_l3, d_18, cy_1235_l3, d_19, bpmc_1235_l3, d_20, enac_1235_l3, stac_1235_l3, 
d_9, c_a21_3_1_l3, d_10, c_a21_3_2_l3, d_10, c_a21_3_3_l3, d_10, c_a21_3_4_l3, 
d_10, c_a21_3_5_l3, d_10, c_a21_3_6_l3, d_10, c_a21_3_7_l3, d_10, c_a21_3_8_l3, 
d_17, q_1246_l3, d_18, cx_1247_l3, d_19, bpmc_1247_l3, d_20, enac_1247_l3, 
stac_1247_l3, d_9, c_a21_4_1_l3, d_10, c_a21_4_2_l3, d_10, c_a21_4_3_l3, d_10, 
c_a21_4_4_l3, d_10, c_a21_4_5_l3, d_10, c_a21_4_6_l3, d_10, c_a21_4_7_l3, d_10, 
c_a21_4_8_l3, d_17, q_1258_l3, d_18, cy_1259_l3, d_19, bpmc_1259_l3, d_20, 
enac_1259_l3, stac_1259_l3, d_9, c_a22_1_1_l3, d_10, c_a22_1_2_l3, d_10, c_a22_1_3_l3, 
d_10, c_a22_1_4_l3, d_10, c_a22_1_5_l3, d_10, c_a22_1_6_l3, d_10, c_a22_1_7_l3, 
d_10, c_a22_1_8_l3, d_17, q_1270_l3, d_18, cx_1271_l3, d_19, bpmc_1271_l3, 
d_20, enac_1271_l3, stac_1271_l3, d_9, c_a22_2_1_l3, d_10, c_a22_2_2_l3, d_10, 
c_a22_2_3_l3, d_10, c_a22_2_4_l3, d_10, c_a22_2_5_l3, d_10, c_a22_2_6_l3, d_10, 
c_a22_2_7_l3, d_10, c_a22_2_8_l3, d_17, q_1282_l3, d_18, cy_1283_l3, d_19, 
bpmc_1283_l3, d_20, enac_1283_l3, stac_1283_l3, d_9, c_a22_3_1_l3, d_10, c_a22_3_2_l3, 
d_10, c_a22_3_3_l3, d_10, c_a22_3_4_l3, d_10, c_a22_3_5_l3, d_10, c_a22_3_6_l3, 
d_10, c_a22_3_7_l3, d_10, c_a22_3_8_l3, d_17, q_1294_l3, d_18, cx_1295_l3, 
d_19, bpmc_1295_l3, d_20, enac_1295_l3, stac_1295_l3, d_9, c_a22_4_1_l3, d_10, 
c_a22_4_2_l3, d_10, c_a22_4_3_l3, d_10, c_a22_4_4_l3, d_10, c_a22_4_5_l3, d_10, 
c_a22_4_6_l3, d_10, c_a22_4_7_l3, d_10, c_a22_4_8_l3, d_17, q_1306_l3, d_18, 
cy_1307_l3, d_19, bpmr_1307_l3, d_20, enac_1307_l3, stac_1307_l3, d_9, c_a23_1_1_l3, 
d_10, c_a23_1_2_l3, d_10, c_a23_1_3_l3, d_10, c_a23_1_4_l3, d_10, c_a23_1_5_l3, 
d_10, c_a23_1_6_l3, d_10, c_a23_1_7_l3, d_10, c_a23_1_8_l3, d_17, q_1318_l3, 
d_18, cx_1319_l3, d_19, bpmc_1319_l3, d_20, enac_1319_l3, stac_1319_l3, d_9, 
c_a23_2_1_l3, d_10, c_a23_2_2_l3, d_10, c_a23_2_3_l3, d_10, c_a23_2_4_l3, d_10, 
c_a23_2_5_l3, d_10, c_a23_2_6_l3, d_10, c_a23_2_7_l3, d_10, c_a23_2_8_l3, d_17, 
q_1330_l3, d_18, cy_1331_l3, d_19, bpmc_1331_l3, d_20, enac_1331_l3, stac_1331_l3, 
d_9, c_a23_3_1_l3, d_10, c_a23_3_2_l3, d_10, c_a23_3_3_l3, d_10, c_a23_3_4_l3, 
d_10, c_a23_3_5_l3, d_10, c_a23_3_6_l3, d_10, c_a23_3_7_l3, d_10, c_a23_3_8_l3, 
d_17, q_1342_l3, d_18, cx_1343_l3, d_19, bpmc_1343_l3, d_20, enac_1343_l3, 
stac_1343_l3, d_9, c_a23_4_1_l3, d_10, c_a23_4_2_l3, d_10, c_a23_4_3_l3, d_10, 
c_a23_4_4_l3, d_10, c_a23_4_5_l3, d_10, c_a23_4_6_l3, d_10, c_a23_4_7_l3, d_10, 
c_a23_4_8_l3, d_17, q_1354_l3, d_18, cy_1355_l3, d_19, bpmc_1355_l3, d_20, 
enac_1355_l3, d_153, stac_1358_l3, d_9, c_a24_1_1_l3, d_10, c_a24_1_2_l3, d_10, 
c_a24_1_3_l3, d_10, c_a24_1_4_l3, d_10, c_a24_1_5_l3, d_10, c_a24_1_6_l3, d_10, 
c_a24_1_7_l3, d_10, c_a24_1_8_l3, d_17, q_1369_l3, d_18, cx_1369_l3, d_19, 
bpmc_1370_l3, d_20, enac_1370_l3, stac_1370_l3, d_9, c_a24_2_1_l3, d_10, c_a24_2_2_l3, 
d_10, c_a24_2_3_l3, d_10, c_a24_2_4_l3, d_10, c_a24_2_5_l3, d_10, c_a24_2_6_l3, 
d_10, c_a24_2_7_l3, d_10, c_a24_2_8_l3, d_17, q_1381_l3, d_18, cy_1381_l3, 
d_19, bpmc_1382_l3, d_20, enac_1382_l3, stac_1382_l3, d_9, c_a24_3_1_l3, d_10, 
c_a24_3_2_l3, d_10, c_a24_3_3_l3, d_10, c_a24_3_4_l3, d_10, c_a24_3_5_l3, d_10, 
c_a24_3_6_l3, d_10, c_a24_3_7_l3, d_10, c_a24_3_8_l3, d_17, q_1393_l3, d_18, 
cx_1393_l3, d_19, bpmc_1394_l3, d_20, enac_1394_l3, stac_1394_l3, d_9, c_a24_4_1_l3, 
d_10, c_a24_4_2_l3, d_10, c_a24_4_3_l3, d_10, c_a24_4_4_l3, d_10, c_a24_4_5_l3, 
d_10, c_a24_4_6_l3, d_10, c_a24_4_7_l3, d_10, c_a24_4_8_l3, d_17, q_1405_l3, 
d_18, cy_1405_l3, d_19, bpmr_1406_l3, d_20, enac_1406_l3, stac_1406_l3, d_9, 
c_a25_1_1_l3, d_10, c_a25_1_2_l3, d_10, c_a25_1_3_l3, d_10, c_a25_1_4_l3, d_10, 
c_a25_1_5_l3, d_10, c_a25_1_6_l3, d_10, c_a25_1_7_l3, d_10, c_a25_1_8_l3, d_17, 
q_1417_l3, d_18, cx_1417_l3, d_19, bpmc_1418_l3, d_20, enac_1418_l3, stac_1418_l3, 
d_9, c_a25_2_1_l3, d_10, c_a25_2_2_l3, d_10, c_a25_2_3_l3, d_10, c_a25_2_4_l3, 
d_10, c_a25_2_5_l3, d_10, c_a25_2_6_l3, d_10, c_a25_2_7_l3, d_10, c_a25_2_8_l3, 
d_17, q_1429_l3, d_18, cy_1429_l3, d_19, bpmr_1430_l3, d_20, enac_1430_l3, 
stac_1430_l3, d_9, c_a25_3_1_l3, d_10, c_a25_3_2_l3, d_10, c_a25_3_3_l3, d_10, 
c_a25_3_4_l3, d_10, c_a25_3_5_l3, d_10, c_a25_3_6_l3, d_10, c_a25_3_7_l3, d_10, 
c_a25_3_8_l3, d_17, q_1441_l3, d_18, cx_1441_l3, d_19, bpmc_1442_l3, d_20, 
enac_1442_l3, stac_1442_l3, d_9, c_a25_4_1_l3, d_10, c_a25_4_2_l3, d_10, c_a25_4_3_l3, 
d_10, c_a25_4_4_l3, d_10, c_a25_4_5_l3, d_10, c_a25_4_6_l3, d_10, c_a25_4_7_l3, 
d_10, c_a25_4_8_l3, d_17, q_1453_l3, d_18, cy_1453_l3, d_19, bpmc_1454_l3, 
d_20, enac_1454_l3, d_974, stsub_1457_l3, d_975, tora_1459_l3, d_976, bpma_1475_l3, 
d_977, qb_1475_l3, d_978, cmx_1476_l3, d_979, bpma_1499_l3, d_977, qb_1499_l3, 
d_978, cmy_1500_l3, d_982, otrbw_1523_l3, d_983, bpma_1541_l3, d_984, qe_1542_l3, 
d_985, cex_1542_l3, d_986, bpma_1578_l3, d_984, qe_1578_l3, d_985, cey_1579_l3, 
d_989, otrbw_1597_l3, d_983, bpma_1615_l3, d_984, qe_1615_l3, d_985, cex_1615_l3, 
d_993, bpma_1628_l3, d_984, qe_1629_l3, d_985, cey_1629_l3, d_996, otrbw_1635_l3, 
d_997, bpma_1641_l3, d_998, qf_1641_l3, d_999, cfx_1642_l3, d_1000, bpma_1650_l3, 
d_998, qf_1650_l3, d_999, cfy_1651_l3, d_1003, ensub_1652_l3, ensec_1652_l3, stsec_1652_cl, 
stblock_1652_cl, d_1004, tora_1658_cl, d_1005, dcm_1659_cl, d_1006, bpma_1659_cl, d_998, 
qf_1660_cl, d_999, cfx_1660_cl, d_1009, chy_1667_cl, d_1010, qh_1667_cl, d_1011, 
qh_1669_cl, d_1012, bpma_1669_cl, d_1013, qh_1670_cl, d_1011, qh_1671_cl, d_1010, 
chx_1672_cl, d_1016, match_1673_cl, qf_1673_cl, d_999, cfy_1674_cl, d_1018, sa_1674_cl, 
d_1019, bpmi_1675_cl, d_1020, mpbpmi_1675_cl, d_1021, be_1678_cl, d_1022, qf_1682_cl, 
d_999, cfx_1683_cl, d_1018, sa_1683_cl, d_1019, bpma_1684_cl, d_1026, d_1027, 
bl_1688_cl, d_1028, otrb_1689_cl, d_1029, sa_1691_cl, d_1030, qf_1691_cl, d_999, 
cfy_1692_cl, d_1018, sa_1692_cl, d_1019, bpmi_1693_cl, d_1020, mpbpmi_1693_cl, d_1035, 
d_1027, bl_1695_cl, d_1037, sa_1700_cl, d_1030, qf_1700_cl, d_999, cfx_1701_cl, 
d_1040, bpma_1702_cl, d_1041, be_1705_cl, d_1042, sa_1708_cl, d_1030, qf_1709_cl, 
d_999, cfy_1710_cl, d_1018, sa_1710_cl, d_1019, bpma_1711_cl, d_1047, be_1714_cl, 
d_1022, qf_1718_cl, d_999, cfx_1719_cl, d_1018, sa_1719_cl, d_1019, bpma_1720_cl, 
d_1026, d_1027, bl_1724_cl, d_1028, otrb_1725_cl, d_1029, sa_1726_cl, d_1030, 
qf_1727_cl, d_999, cfy_1728_cl, d_1018, sa_1728_cl, d_1019, bpmi_1729_cl, d_1020, 
mpbpmi_1729_cl, d_1035, d_1027, bl_1731_cl, d_1037, sa_1736_cl, d_1030, qf_1736_cl, 
d_999, cfx_1737_cl, d_1040, bpma_1738_cl, d_1041, be_1741_cl, d_1042, sa_1744_cl, 
d_1030, qf_1745_cl, d_999, cfy_1746_cl, d_1071, bpma_1746_cl, d_1072, chx_1747_cl, 
d_1010, qh_1748_cl, d_1011, qh_1749_cl, d_1012, bpma_1750_cl, d_1013, qh_1751_cl, 
d_1011, qh_1752_cl, d_1010, chy_1753_cl, d_1079, qf_1754_cl, d_999, cfx_1755_cl, 
d_1040, bpma_1756_cl, d_1082, qf_1759_cl, d_999, cfy_1760_cl, d_1040, bpma_1761_cl, 
d_1085, qf_1763_cl, d_999, cfx_1764_cl, d_1040, bpma_1765_cl, d_1088, tora_1765_cl, 
d_1089, qf_1767_cl, d_999, cfy_1768_cl, d_1040, bpma_1769_cl, d_1082, qf_1772_cl, 
d_999, cfx_1773_cl, d_1071, bpma_1773_cl, d_1095, chy_1774_cl, d_1010, qh_1775_cl, 
d_1011, qh_1776_cl, d_1012, bpma_1777_cl, d_1013, qh_1778_cl, d_1011, qh_1779_cl, 
d_1010, chx_1780_cl, d_1102, qf_1781_cl, d_999, cfy_1782_cl, d_1018, sa_1782_cl, 
d_1019, bpma_1783_cl, d_1047, be_1786_cl, d_1022, qf_1790_cl, d_999, cfx_1791_cl, 
d_1018, sa_1791_cl, d_1019, bpma_1792_cl, d_1026, d_1027, bl_1796_cl, d_1028, 
otrb_1797_cl, d_1029, sa_1798_cl, d_1030, qf_1799_cl, d_999, cfy_1800_cl, d_1018, 
sa_1800_cl, d_1019, bpma_1801_cl, d_1119, d_1027, bl_1803_cl, d_1037, sa_1808_cl, 
d_1030, qf_1808_cl, d_999, cfx_1809_cl, d_1040, bpma_1810_cl, d_1041, be_1813_cl, 
d_1042, sa_1816_cl, d_1030, qf_1817_cl, d_999, cfy_1818_cl, d_1018, sa_1818_cl, 
d_1019, bpma_1819_cl, d_1047, be_1822_cl, d_1022, qf_1826_cl, d_999, cfx_1827_cl, 
d_1018, sa_1827_cl, d_1019, bpma_1828_cl, d_1026, d_1027, bl_1832_cl, d_1028, 
otrb_1833_cl, d_1029, sa_1834_cl, d_1030, qf_1835_cl, d_999, cfy_1836_cl, d_1018, 
sa_1836_cl, d_1019, bpmi_1837_cl, d_1020, mpbpmi_1837_cl, d_1035, d_1027, bl_1839_cl, 
d_1037, sa_1844_cl, d_1030, qf_1844_cl, d_999, cfx_1845_cl, d_1040, bpma_1846_cl, 
d_1041, be_1849_cl, d_1042, sa_1852_cl, d_1153, bpma_1853_cl, d_998, qf_1853_cl, 
ensec_1854_cl, stsec_1854_tl, stsub_1854_tl, d_999, cfy_1854_tl, d_1156, chx_1855_tl, d_1010, 
qh_1855_tl, d_1011, qh_1857_tl, d_1159, qh_1858_tl, d_1011, qh_1859_tl, d_1161, 
bpmi_1860_tl, d_1020, mpbpmi_1861_tl, d_1163, chy_1861_tl, d_1164, mpbpmi_1863_tl, d_1020, 
bpmi_1863_tl, d_1166, qf_1864_tl, d_999, cfx_1864_tl, d_1040, tora_1865_tl, d_1005, 
dcm_1865_tl, d_1170, bpma_1868_tl, d_998, qf_1868_tl, d_999, cfy_1869_tl, d_1173, 
bpma_1873_tl, d_998, qf_1873_tl, d_999, cfx_1873_tl, d_1176, bpmi_1878_tl, d_1020, 
mpbpmi_1878_tl, d_1178, qf_1881_tl, d_1179, cfy_1884_tl, d_1180, bpmi_1889_tl, d_1020, 
mpbpmi_1889_tl, d_1178, enblock_1891_cl, qf_1892_tl, d_1183, cfx_1894_tl, d_1184, otrbw_1899_tl, 
d_1185, qf_1907_tl, d_1186, bpmi_1910_tl, d_1020, mpbpmi_1910_tl, d_1163, cfy_1910_tl, 
d_1189, otrbw_1914_tl, d_1185, qf_1922_tl, d_1186, bpmi_1925_tl, d_1020, mpbpmi_1925_tl, 
d_1163, cfx_1925_tl, d_1189, otrbw_1929_tl, d_1195, bpmi_1930_tl, d_1020, mpbpmi_1930_tl, 
d_1197, bam_1931_tl, d_1198, bam_1932_tl, d_1199, crd_1934_tl, d_1200, qf_1937_tl, 
d_999, cfy_1937_tl, d_1202, bpmi_1939_tl, d_1020, mpbpmi_1939_tl, d_1204, bl_1939_tl, 
d_1205, ensub_1940_tl, stsub_1940_tl, d_1206, qf_1952_tl, d_1207, bl_1964_tl, d_1208, 
chx_1965_tl, d_1209, bpma_1966_tl, d_1210, qf_1967_tl, d_1211, chx_1967_tl, d_1212, 
chy_1967_tl, d_1213, cnx_1977_tl, d_1005, cny_1977_tl, d_1215, bpmd_1977_tl, d_1212, 
otre_1978_tl, d_1217, ensub_1980_tl)
# power supplies 

#  
qd_470_b2.ps_id = 'QD.24.B2'
qd_472_b2.ps_id = 'QD.25.B2'
q_488_l3.ps_id = 'Q.A6.1.L3'
q_500_l3.ps_id = 'Q.A6.2.L3'
q_512_l3.ps_id = 'Q.A6.3.L3'
q_524_l3.ps_id = 'Q.A6.4.L3'
q_536_l3.ps_id = 'Q.A7.1.L3'
q_548_l3.ps_id = 'Q.A7.2.L3'
q_560_l3.ps_id = 'Q.A7.3.L3'
q_572_l3.ps_id = 'Q.A7.4.L3'
q_584_l3.ps_id = 'Q.A8.1.L3'
q_596_l3.ps_id = 'Q.A8.2.L3'
q_608_l3.ps_id = 'Q.A8.3.L3'
q_620_l3.ps_id = 'Q.A8.4.L3'
q_635_l3.ps_id = 'Q.A9.1.L3'
q_647_l3.ps_id = 'Q.A9.2.L3'
q_659_l3.ps_id = 'Q.A9.3.L3'
q_671_l3.ps_id = 'Q.A9.4.L3'
q_683_l3.ps_id = 'Q.A10.1.L3'
q_695_l3.ps_id = 'Q.A10.2.L3'
q_707_l3.ps_id = 'Q.A10.3.L3'
q_719_l3.ps_id = 'Q.A10.4.L3'
q_731_l3.ps_id = 'Q.A11.1.L3'
q_743_l3.ps_id = 'Q.A11.2.L3'
q_755_l3.ps_id = 'Q.A11.3.L3'
q_767_l3.ps_id = 'Q.A11.4.L3'
q_782_l3.ps_id = 'Q.A12.1.L3'
q_794_l3.ps_id = 'Q.A12.2.L3'
q_806_l3.ps_id = 'Q.A12.3.L3'
q_818_l3.ps_id = 'Q.A12.4.L3'
q_830_l3.ps_id = 'Q.A13.1.L3'
q_842_l3.ps_id = 'Q.A13.2.L3'
q_854_l3.ps_id = 'Q.A13.3.L3'
q_866_l3.ps_id = 'Q.A13.4.L3'
q_878_l3.ps_id = 'Q.A14.1.L3'
q_890_l3.ps_id = 'Q.A14.2.L3'
q_902_l3.ps_id = 'Q.A14.3.L3'
q_914_l3.ps_id = 'Q.A14.4.L3'
q_929_l3.ps_id = 'Q.A15.1.L3'
q_941_l3.ps_id = 'Q.A15.2.L3'
q_953_l3.ps_id = 'Q.A15.3.L3'
q_965_l3.ps_id = 'Q.A15.4.L3'
q_977_l3.ps_id = 'Q.A16.1.L3'
q_989_l3.ps_id = 'Q.A16.2.L3'
q_1001_l3.ps_id = 'Q.A16.3.L3'
q_1013_l3.ps_id = 'Q.A16.4.L3'
q_1025_l3.ps_id = 'Q.A17.1.L3'
q_1037_l3.ps_id = 'Q.A17.2.L3'
q_1049_l3.ps_id = 'Q.A17.3.L3'
q_1061_l3.ps_id = 'Q.A17.4.L3'
q_1076_l3.ps_id = 'Q.A18.1.L3'
q_1088_l3.ps_id = 'Q.A18.2.L3'
q_1100_l3.ps_id = 'Q.A18.3.L3'
q_1112_l3.ps_id = 'Q.A18.4.L3'
q_1124_l3.ps_id = 'Q.A19.1.L3'
q_1136_l3.ps_id = 'Q.A19.2.L3'
q_1147_l3.ps_id = 'Q.A19.3.L3'
q_1159_l3.ps_id = 'Q.A19.4.L3'
q_1171_l3.ps_id = 'Q.A20.1.L3'
q_1183_l3.ps_id = 'Q.A20.2.L3'
q_1195_l3.ps_id = 'Q.A20.3.L3'
q_1207_l3.ps_id = 'Q.A20.4.L3'
q_1222_l3.ps_id = 'Q.A21.1.L3'
q_1234_l3.ps_id = 'Q.A21.2.L3'
q_1246_l3.ps_id = 'Q.A21.3.L3'
q_1258_l3.ps_id = 'Q.A21.4.L3'
q_1270_l3.ps_id = 'Q.A22.1.L3'
q_1282_l3.ps_id = 'Q.A22.2.L3'
q_1294_l3.ps_id = 'Q.A22.3.L3'
q_1306_l3.ps_id = 'Q.A22.4.L3'
q_1318_l3.ps_id = 'Q.A23.1.L3'
q_1330_l3.ps_id = 'Q.A23.2.L3'
q_1342_l3.ps_id = 'Q.A23.3.L3'
q_1354_l3.ps_id = 'Q.A23.4.L3'
q_1369_l3.ps_id = 'Q.A24.1.L3'
q_1381_l3.ps_id = 'Q.A24.2.L3'
q_1393_l3.ps_id = 'Q.A24.3.L3'
q_1405_l3.ps_id = 'Q.A24.4.L3'
q_1417_l3.ps_id = 'Q.A25.1.L3'
q_1429_l3.ps_id = 'Q.A25.2.L3'
q_1441_l3.ps_id = 'Q.A25.3.L3'
q_1453_l3.ps_id = 'Q.A25.4.L3'
qb_1475_l3.ps_id = 'QB.1.L3'
qb_1499_l3.ps_id = 'QB.2.L3'
qe_1542_l3.ps_id = 'QE.1.L3'
qe_1578_l3.ps_id = 'QE.1.L3'
qe_1615_l3.ps_id = 'QE.1.L3'
qe_1629_l3.ps_id = 'QE.2.L3'
qf_1641_l3.ps_id = 'QF.1.L3'
qf_1650_l3.ps_id = 'QF.2.L3'
qf_1660_cl.ps_id = 'QF.3.CL'
qh_1667_cl.ps_id = 'QH.1.CL'
qh_1669_cl.ps_id = 'QH.1.CL'
qh_1670_cl.ps_id = 'QH.2.CL'
qh_1671_cl.ps_id = 'QH.2.CL'
qf_1673_cl.ps_id = 'QF.4.CL'
qf_1682_cl.ps_id = 'QF.4.CL'
qf_1691_cl.ps_id = 'QF.4.CL'
qf_1700_cl.ps_id = 'QF.4.CL'
qf_1709_cl.ps_id = 'QF.4.CL'
qf_1718_cl.ps_id = 'QF.4.CL'
qf_1727_cl.ps_id = 'QF.4.CL'
qf_1736_cl.ps_id = 'QF.4.CL'
qf_1745_cl.ps_id = 'QF.4.CL'
qh_1748_cl.ps_id = 'QH.3.CL'
qh_1749_cl.ps_id = 'QH.3.CL'
qh_1751_cl.ps_id = 'QH.4.CL'
qh_1752_cl.ps_id = 'QH.4.CL'
qf_1754_cl.ps_id = 'QF.5.CL'
qf_1759_cl.ps_id = 'QF.6.CL'
qf_1763_cl.ps_id = 'QF.7.CL'
qf_1767_cl.ps_id = 'QF.6.CL'
qf_1772_cl.ps_id = 'QF.5.CL'
qh_1775_cl.ps_id = 'QH.4.CL'
qh_1776_cl.ps_id = 'QH.4.CL'
qh_1778_cl.ps_id = 'QH.3.CL'
qh_1779_cl.ps_id = 'QH.3.CL'
qf_1781_cl.ps_id = 'QF.4.CL'
qf_1790_cl.ps_id = 'QF.4.CL'
qf_1799_cl.ps_id = 'QF.4.CL'
qf_1808_cl.ps_id = 'QF.4.CL'
qf_1817_cl.ps_id = 'QF.4.CL'
qf_1826_cl.ps_id = 'QF.4.CL'
qf_1835_cl.ps_id = 'QF.4.CL'
qf_1844_cl.ps_id = 'QF.4.CL'
qf_1853_cl.ps_id = 'QF.4.CL'
qh_1855_tl.ps_id = 'QH.5.TL'
qh_1857_tl.ps_id = 'QH.6.TL'
qh_1858_tl.ps_id = 'QH.7.TL'
qh_1859_tl.ps_id = 'QH.8.TL'
qf_1864_tl.ps_id = 'QF.8.TL'
qf_1868_tl.ps_id = 'QF.9.TL'
qf_1873_tl.ps_id = 'QF.10.TL'
qf_1881_tl.ps_id = 'QF.11.TL'
qf_1892_tl.ps_id = 'QF.1.TL'
qf_1907_tl.ps_id = 'QF.2.TL'
qf_1922_tl.ps_id = 'QF.1.TL'
qf_1937_tl.ps_id = 'QF.2.TL'
qf_1952_tl.ps_id = 'QF.1.TL'
qf_1967_tl.ps_id = 'QF.2.TL'

#  
sa_1674_cl.ps_id = 'SA.1.CL'
sa_1683_cl.ps_id = 'SA.2.CL'
sa_1691_cl.ps_id = 'SA.3.CL'
sa_1692_cl.ps_id = 'SA.3.CL'
sa_1700_cl.ps_id = 'SA.2.CL'
sa_1708_cl.ps_id = 'SA.1.CL'
sa_1710_cl.ps_id = 'SA.1.CL'
sa_1719_cl.ps_id = 'SA.2.CL'
sa_1726_cl.ps_id = 'SA.3.CL'
sa_1728_cl.ps_id = 'SA.3.CL'
sa_1736_cl.ps_id = 'SA.2.CL'
sa_1744_cl.ps_id = 'SA.1.CL'
sa_1782_cl.ps_id = 'SA.4.CL'
sa_1791_cl.ps_id = 'SA.5.CL'
sa_1798_cl.ps_id = 'SA.6.CL'
sa_1800_cl.ps_id = 'SA.6.CL'
sa_1808_cl.ps_id = 'SA.5.CL'
sa_1816_cl.ps_id = 'SA.4.CL'
sa_1818_cl.ps_id = 'SA.4.CL'
sa_1827_cl.ps_id = 'SA.5.CL'
sa_1834_cl.ps_id = 'SA.6.CL'
sa_1836_cl.ps_id = 'SA.6.CL'
sa_1844_cl.ps_id = 'SA.5.CL'
sa_1852_cl.ps_id = 'SA.4.CL'

#  

#  
c_a6_1_1_l3.ps_id = 'C.A6.L3'
c_a6_1_2_l3.ps_id = 'C.A6.L3'
c_a6_1_3_l3.ps_id = 'C.A6.L3'
c_a6_1_4_l3.ps_id = 'C.A6.L3'
c_a6_1_5_l3.ps_id = 'C.A6.L3'
c_a6_1_6_l3.ps_id = 'C.A6.L3'
c_a6_1_7_l3.ps_id = 'C.A6.L3'
c_a6_1_8_l3.ps_id = 'C.A6.L3'
c_a6_2_1_l3.ps_id = 'C.A6.L3'
c_a6_2_2_l3.ps_id = 'C.A6.L3'
c_a6_2_3_l3.ps_id = 'C.A6.L3'
c_a6_2_4_l3.ps_id = 'C.A6.L3'
c_a6_2_5_l3.ps_id = 'C.A6.L3'
c_a6_2_6_l3.ps_id = 'C.A6.L3'
c_a6_2_7_l3.ps_id = 'C.A6.L3'
c_a6_2_8_l3.ps_id = 'C.A6.L3'
c_a6_3_1_l3.ps_id = 'C.A6.L3'
c_a6_3_2_l3.ps_id = 'C.A6.L3'
c_a6_3_3_l3.ps_id = 'C.A6.L3'
c_a6_3_4_l3.ps_id = 'C.A6.L3'
c_a6_3_5_l3.ps_id = 'C.A6.L3'
c_a6_3_6_l3.ps_id = 'C.A6.L3'
c_a6_3_7_l3.ps_id = 'C.A6.L3'
c_a6_3_8_l3.ps_id = 'C.A6.L3'
c_a6_4_1_l3.ps_id = 'C.A6.L3'
c_a6_4_2_l3.ps_id = 'C.A6.L3'
c_a6_4_3_l3.ps_id = 'C.A6.L3'
c_a6_4_4_l3.ps_id = 'C.A6.L3'
c_a6_4_5_l3.ps_id = 'C.A6.L3'
c_a6_4_6_l3.ps_id = 'C.A6.L3'
c_a6_4_7_l3.ps_id = 'C.A6.L3'
c_a6_4_8_l3.ps_id = 'C.A6.L3'
c_a7_1_1_l3.ps_id = 'C.A7.L3'
c_a7_1_2_l3.ps_id = 'C.A7.L3'
c_a7_1_3_l3.ps_id = 'C.A7.L3'
c_a7_1_4_l3.ps_id = 'C.A7.L3'
c_a7_1_5_l3.ps_id = 'C.A7.L3'
c_a7_1_6_l3.ps_id = 'C.A7.L3'
c_a7_1_7_l3.ps_id = 'C.A7.L3'
c_a7_1_8_l3.ps_id = 'C.A7.L3'
c_a7_2_1_l3.ps_id = 'C.A7.L3'
c_a7_2_2_l3.ps_id = 'C.A7.L3'
c_a7_2_3_l3.ps_id = 'C.A7.L3'
c_a7_2_4_l3.ps_id = 'C.A7.L3'
c_a7_2_5_l3.ps_id = 'C.A7.L3'
c_a7_2_6_l3.ps_id = 'C.A7.L3'
c_a7_2_7_l3.ps_id = 'C.A7.L3'
c_a7_2_8_l3.ps_id = 'C.A7.L3'
c_a7_3_1_l3.ps_id = 'C.A7.L3'
c_a7_3_2_l3.ps_id = 'C.A7.L3'
c_a7_3_3_l3.ps_id = 'C.A7.L3'
c_a7_3_4_l3.ps_id = 'C.A7.L3'
c_a7_3_5_l3.ps_id = 'C.A7.L3'
c_a7_3_6_l3.ps_id = 'C.A7.L3'
c_a7_3_7_l3.ps_id = 'C.A7.L3'
c_a7_3_8_l3.ps_id = 'C.A7.L3'
c_a7_4_1_l3.ps_id = 'C.A7.L3'
c_a7_4_2_l3.ps_id = 'C.A7.L3'
c_a7_4_3_l3.ps_id = 'C.A7.L3'
c_a7_4_4_l3.ps_id = 'C.A7.L3'
c_a7_4_5_l3.ps_id = 'C.A7.L3'
c_a7_4_6_l3.ps_id = 'C.A7.L3'
c_a7_4_7_l3.ps_id = 'C.A7.L3'
c_a7_4_8_l3.ps_id = 'C.A7.L3'
c_a8_1_1_l3.ps_id = 'C.A8.L3'
c_a8_1_2_l3.ps_id = 'C.A8.L3'
c_a8_1_3_l3.ps_id = 'C.A8.L3'
c_a8_1_4_l3.ps_id = 'C.A8.L3'
c_a8_1_5_l3.ps_id = 'C.A8.L3'
c_a8_1_6_l3.ps_id = 'C.A8.L3'
c_a8_1_7_l3.ps_id = 'C.A8.L3'
c_a8_1_8_l3.ps_id = 'C.A8.L3'
c_a8_2_1_l3.ps_id = 'C.A8.L3'
c_a8_2_2_l3.ps_id = 'C.A8.L3'
c_a8_2_3_l3.ps_id = 'C.A8.L3'
c_a8_2_4_l3.ps_id = 'C.A8.L3'
c_a8_2_5_l3.ps_id = 'C.A8.L3'
c_a8_2_6_l3.ps_id = 'C.A8.L3'
c_a8_2_7_l3.ps_id = 'C.A8.L3'
c_a8_2_8_l3.ps_id = 'C.A8.L3'
c_a8_3_1_l3.ps_id = 'C.A8.L3'
c_a8_3_2_l3.ps_id = 'C.A8.L3'
c_a8_3_3_l3.ps_id = 'C.A8.L3'
c_a8_3_4_l3.ps_id = 'C.A8.L3'
c_a8_3_5_l3.ps_id = 'C.A8.L3'
c_a8_3_6_l3.ps_id = 'C.A8.L3'
c_a8_3_7_l3.ps_id = 'C.A8.L3'
c_a8_3_8_l3.ps_id = 'C.A8.L3'
c_a8_4_1_l3.ps_id = 'C.A8.L3'
c_a8_4_2_l3.ps_id = 'C.A8.L3'
c_a8_4_3_l3.ps_id = 'C.A8.L3'
c_a8_4_4_l3.ps_id = 'C.A8.L3'
c_a8_4_5_l3.ps_id = 'C.A8.L3'
c_a8_4_6_l3.ps_id = 'C.A8.L3'
c_a8_4_7_l3.ps_id = 'C.A8.L3'
c_a8_4_8_l3.ps_id = 'C.A8.L3'
c_a9_1_1_l3.ps_id = 'C.A9.L3'
c_a9_1_2_l3.ps_id = 'C.A9.L3'
c_a9_1_3_l3.ps_id = 'C.A9.L3'
c_a9_1_4_l3.ps_id = 'C.A9.L3'
c_a9_1_5_l3.ps_id = 'C.A9.L3'
c_a9_1_6_l3.ps_id = 'C.A9.L3'
c_a9_1_7_l3.ps_id = 'C.A9.L3'
c_a9_1_8_l3.ps_id = 'C.A9.L3'
c_a9_2_1_l3.ps_id = 'C.A9.L3'
c_a9_2_2_l3.ps_id = 'C.A9.L3'
c_a9_2_3_l3.ps_id = 'C.A9.L3'
c_a9_2_4_l3.ps_id = 'C.A9.L3'
c_a9_2_5_l3.ps_id = 'C.A9.L3'
c_a9_2_6_l3.ps_id = 'C.A9.L3'
c_a9_2_7_l3.ps_id = 'C.A9.L3'
c_a9_2_8_l3.ps_id = 'C.A9.L3'
c_a9_3_1_l3.ps_id = 'C.A9.L3'
c_a9_3_2_l3.ps_id = 'C.A9.L3'
c_a9_3_3_l3.ps_id = 'C.A9.L3'
c_a9_3_4_l3.ps_id = 'C.A9.L3'
c_a9_3_5_l3.ps_id = 'C.A9.L3'
c_a9_3_6_l3.ps_id = 'C.A9.L3'
c_a9_3_7_l3.ps_id = 'C.A9.L3'
c_a9_3_8_l3.ps_id = 'C.A9.L3'
c_a9_4_1_l3.ps_id = 'C.A9.L3'
c_a9_4_2_l3.ps_id = 'C.A9.L3'
c_a9_4_3_l3.ps_id = 'C.A9.L3'
c_a9_4_4_l3.ps_id = 'C.A9.L3'
c_a9_4_5_l3.ps_id = 'C.A9.L3'
c_a9_4_6_l3.ps_id = 'C.A9.L3'
c_a9_4_7_l3.ps_id = 'C.A9.L3'
c_a9_4_8_l3.ps_id = 'C.A9.L3'
c_a10_1_1_l3.ps_id = 'C.A10.L3'
c_a10_1_2_l3.ps_id = 'C.A10.L3'
c_a10_1_3_l3.ps_id = 'C.A10.L3'
c_a10_1_4_l3.ps_id = 'C.A10.L3'
c_a10_1_5_l3.ps_id = 'C.A10.L3'
c_a10_1_6_l3.ps_id = 'C.A10.L3'
c_a10_1_7_l3.ps_id = 'C.A10.L3'
c_a10_1_8_l3.ps_id = 'C.A10.L3'
c_a10_2_1_l3.ps_id = 'C.A10.L3'
c_a10_2_2_l3.ps_id = 'C.A10.L3'
c_a10_2_3_l3.ps_id = 'C.A10.L3'
c_a10_2_4_l3.ps_id = 'C.A10.L3'
c_a10_2_5_l3.ps_id = 'C.A10.L3'
c_a10_2_6_l3.ps_id = 'C.A10.L3'
c_a10_2_7_l3.ps_id = 'C.A10.L3'
c_a10_2_8_l3.ps_id = 'C.A10.L3'
c_a10_3_1_l3.ps_id = 'C.A10.L3'
c_a10_3_2_l3.ps_id = 'C.A10.L3'
c_a10_3_3_l3.ps_id = 'C.A10.L3'
c_a10_3_4_l3.ps_id = 'C.A10.L3'
c_a10_3_5_l3.ps_id = 'C.A10.L3'
c_a10_3_6_l3.ps_id = 'C.A10.L3'
c_a10_3_7_l3.ps_id = 'C.A10.L3'
c_a10_3_8_l3.ps_id = 'C.A10.L3'
c_a10_4_1_l3.ps_id = 'C.A10.L3'
c_a10_4_2_l3.ps_id = 'C.A10.L3'
c_a10_4_3_l3.ps_id = 'C.A10.L3'
c_a10_4_4_l3.ps_id = 'C.A10.L3'
c_a10_4_5_l3.ps_id = 'C.A10.L3'
c_a10_4_6_l3.ps_id = 'C.A10.L3'
c_a10_4_7_l3.ps_id = 'C.A10.L3'
c_a10_4_8_l3.ps_id = 'C.A10.L3'
c_a11_1_1_l3.ps_id = 'C.A11.L3'
c_a11_1_2_l3.ps_id = 'C.A11.L3'
c_a11_1_3_l3.ps_id = 'C.A11.L3'
c_a11_1_4_l3.ps_id = 'C.A11.L3'
c_a11_1_5_l3.ps_id = 'C.A11.L3'
c_a11_1_6_l3.ps_id = 'C.A11.L3'
c_a11_1_7_l3.ps_id = 'C.A11.L3'
c_a11_1_8_l3.ps_id = 'C.A11.L3'
c_a11_2_1_l3.ps_id = 'C.A11.L3'
c_a11_2_2_l3.ps_id = 'C.A11.L3'
c_a11_2_3_l3.ps_id = 'C.A11.L3'
c_a11_2_4_l3.ps_id = 'C.A11.L3'
c_a11_2_5_l3.ps_id = 'C.A11.L3'
c_a11_2_6_l3.ps_id = 'C.A11.L3'
c_a11_2_7_l3.ps_id = 'C.A11.L3'
c_a11_2_8_l3.ps_id = 'C.A11.L3'
c_a11_3_1_l3.ps_id = 'C.A11.L3'
c_a11_3_2_l3.ps_id = 'C.A11.L3'
c_a11_3_3_l3.ps_id = 'C.A11.L3'
c_a11_3_4_l3.ps_id = 'C.A11.L3'
c_a11_3_5_l3.ps_id = 'C.A11.L3'
c_a11_3_6_l3.ps_id = 'C.A11.L3'
c_a11_3_7_l3.ps_id = 'C.A11.L3'
c_a11_3_8_l3.ps_id = 'C.A11.L3'
c_a11_4_1_l3.ps_id = 'C.A11.L3'
c_a11_4_2_l3.ps_id = 'C.A11.L3'
c_a11_4_3_l3.ps_id = 'C.A11.L3'
c_a11_4_4_l3.ps_id = 'C.A11.L3'
c_a11_4_5_l3.ps_id = 'C.A11.L3'
c_a11_4_6_l3.ps_id = 'C.A11.L3'
c_a11_4_7_l3.ps_id = 'C.A11.L3'
c_a11_4_8_l3.ps_id = 'C.A11.L3'
c_a12_1_1_l3.ps_id = 'C.A12.L3'
c_a12_1_2_l3.ps_id = 'C.A12.L3'
c_a12_1_3_l3.ps_id = 'C.A12.L3'
c_a12_1_4_l3.ps_id = 'C.A12.L3'
c_a12_1_5_l3.ps_id = 'C.A12.L3'
c_a12_1_6_l3.ps_id = 'C.A12.L3'
c_a12_1_7_l3.ps_id = 'C.A12.L3'
c_a12_1_8_l3.ps_id = 'C.A12.L3'
c_a12_2_1_l3.ps_id = 'C.A12.L3'
c_a12_2_2_l3.ps_id = 'C.A12.L3'
c_a12_2_3_l3.ps_id = 'C.A12.L3'
c_a12_2_4_l3.ps_id = 'C.A12.L3'
c_a12_2_5_l3.ps_id = 'C.A12.L3'
c_a12_2_6_l3.ps_id = 'C.A12.L3'
c_a12_2_7_l3.ps_id = 'C.A12.L3'
c_a12_2_8_l3.ps_id = 'C.A12.L3'
c_a12_3_1_l3.ps_id = 'C.A12.L3'
c_a12_3_2_l3.ps_id = 'C.A12.L3'
c_a12_3_3_l3.ps_id = 'C.A12.L3'
c_a12_3_4_l3.ps_id = 'C.A12.L3'
c_a12_3_5_l3.ps_id = 'C.A12.L3'
c_a12_3_6_l3.ps_id = 'C.A12.L3'
c_a12_3_7_l3.ps_id = 'C.A12.L3'
c_a12_3_8_l3.ps_id = 'C.A12.L3'
c_a12_4_1_l3.ps_id = 'C.A12.L3'
c_a12_4_2_l3.ps_id = 'C.A12.L3'
c_a12_4_3_l3.ps_id = 'C.A12.L3'
c_a12_4_4_l3.ps_id = 'C.A12.L3'
c_a12_4_5_l3.ps_id = 'C.A12.L3'
c_a12_4_6_l3.ps_id = 'C.A12.L3'
c_a12_4_7_l3.ps_id = 'C.A12.L3'
c_a12_4_8_l3.ps_id = 'C.A12.L3'
c_a13_1_1_l3.ps_id = 'C.A13.L3'
c_a13_1_2_l3.ps_id = 'C.A13.L3'
c_a13_1_3_l3.ps_id = 'C.A13.L3'
c_a13_1_4_l3.ps_id = 'C.A13.L3'
c_a13_1_5_l3.ps_id = 'C.A13.L3'
c_a13_1_6_l3.ps_id = 'C.A13.L3'
c_a13_1_7_l3.ps_id = 'C.A13.L3'
c_a13_1_8_l3.ps_id = 'C.A13.L3'
c_a13_2_1_l3.ps_id = 'C.A13.L3'
c_a13_2_2_l3.ps_id = 'C.A13.L3'
c_a13_2_3_l3.ps_id = 'C.A13.L3'
c_a13_2_4_l3.ps_id = 'C.A13.L3'
c_a13_2_5_l3.ps_id = 'C.A13.L3'
c_a13_2_6_l3.ps_id = 'C.A13.L3'
c_a13_2_7_l3.ps_id = 'C.A13.L3'
c_a13_2_8_l3.ps_id = 'C.A13.L3'
c_a13_3_1_l3.ps_id = 'C.A13.L3'
c_a13_3_2_l3.ps_id = 'C.A13.L3'
c_a13_3_3_l3.ps_id = 'C.A13.L3'
c_a13_3_4_l3.ps_id = 'C.A13.L3'
c_a13_3_5_l3.ps_id = 'C.A13.L3'
c_a13_3_6_l3.ps_id = 'C.A13.L3'
c_a13_3_7_l3.ps_id = 'C.A13.L3'
c_a13_3_8_l3.ps_id = 'C.A13.L3'
c_a13_4_1_l3.ps_id = 'C.A13.L3'
c_a13_4_2_l3.ps_id = 'C.A13.L3'
c_a13_4_3_l3.ps_id = 'C.A13.L3'
c_a13_4_4_l3.ps_id = 'C.A13.L3'
c_a13_4_5_l3.ps_id = 'C.A13.L3'
c_a13_4_6_l3.ps_id = 'C.A13.L3'
c_a13_4_7_l3.ps_id = 'C.A13.L3'
c_a13_4_8_l3.ps_id = 'C.A13.L3'
c_a14_1_1_l3.ps_id = 'C.A14.L3'
c_a14_1_2_l3.ps_id = 'C.A14.L3'
c_a14_1_3_l3.ps_id = 'C.A14.L3'
c_a14_1_4_l3.ps_id = 'C.A14.L3'
c_a14_1_5_l3.ps_id = 'C.A14.L3'
c_a14_1_6_l3.ps_id = 'C.A14.L3'
c_a14_1_7_l3.ps_id = 'C.A14.L3'
c_a14_1_8_l3.ps_id = 'C.A14.L3'
c_a14_2_1_l3.ps_id = 'C.A14.L3'
c_a14_2_2_l3.ps_id = 'C.A14.L3'
c_a14_2_3_l3.ps_id = 'C.A14.L3'
c_a14_2_4_l3.ps_id = 'C.A14.L3'
c_a14_2_5_l3.ps_id = 'C.A14.L3'
c_a14_2_6_l3.ps_id = 'C.A14.L3'
c_a14_2_7_l3.ps_id = 'C.A14.L3'
c_a14_2_8_l3.ps_id = 'C.A14.L3'
c_a14_3_1_l3.ps_id = 'C.A14.L3'
c_a14_3_2_l3.ps_id = 'C.A14.L3'
c_a14_3_3_l3.ps_id = 'C.A14.L3'
c_a14_3_4_l3.ps_id = 'C.A14.L3'
c_a14_3_5_l3.ps_id = 'C.A14.L3'
c_a14_3_6_l3.ps_id = 'C.A14.L3'
c_a14_3_7_l3.ps_id = 'C.A14.L3'
c_a14_3_8_l3.ps_id = 'C.A14.L3'
c_a14_4_1_l3.ps_id = 'C.A14.L3'
c_a14_4_2_l3.ps_id = 'C.A14.L3'
c_a14_4_3_l3.ps_id = 'C.A14.L3'
c_a14_4_4_l3.ps_id = 'C.A14.L3'
c_a14_4_5_l3.ps_id = 'C.A14.L3'
c_a14_4_6_l3.ps_id = 'C.A14.L3'
c_a14_4_7_l3.ps_id = 'C.A14.L3'
c_a14_4_8_l3.ps_id = 'C.A14.L3'
c_a15_1_1_l3.ps_id = 'C.A15.L3'
c_a15_1_2_l3.ps_id = 'C.A15.L3'
c_a15_1_3_l3.ps_id = 'C.A15.L3'
c_a15_1_4_l3.ps_id = 'C.A15.L3'
c_a15_1_5_l3.ps_id = 'C.A15.L3'
c_a15_1_6_l3.ps_id = 'C.A15.L3'
c_a15_1_7_l3.ps_id = 'C.A15.L3'
c_a15_1_8_l3.ps_id = 'C.A15.L3'
c_a15_2_1_l3.ps_id = 'C.A15.L3'
c_a15_2_2_l3.ps_id = 'C.A15.L3'
c_a15_2_3_l3.ps_id = 'C.A15.L3'
c_a15_2_4_l3.ps_id = 'C.A15.L3'
c_a15_2_5_l3.ps_id = 'C.A15.L3'
c_a15_2_6_l3.ps_id = 'C.A15.L3'
c_a15_2_7_l3.ps_id = 'C.A15.L3'
c_a15_2_8_l3.ps_id = 'C.A15.L3'
c_a15_3_1_l3.ps_id = 'C.A15.L3'
c_a15_3_2_l3.ps_id = 'C.A15.L3'
c_a15_3_3_l3.ps_id = 'C.A15.L3'
c_a15_3_4_l3.ps_id = 'C.A15.L3'
c_a15_3_5_l3.ps_id = 'C.A15.L3'
c_a15_3_6_l3.ps_id = 'C.A15.L3'
c_a15_3_7_l3.ps_id = 'C.A15.L3'
c_a15_3_8_l3.ps_id = 'C.A15.L3'
c_a15_4_1_l3.ps_id = 'C.A15.L3'
c_a15_4_2_l3.ps_id = 'C.A15.L3'
c_a15_4_3_l3.ps_id = 'C.A15.L3'
c_a15_4_4_l3.ps_id = 'C.A15.L3'
c_a15_4_5_l3.ps_id = 'C.A15.L3'
c_a15_4_6_l3.ps_id = 'C.A15.L3'
c_a15_4_7_l3.ps_id = 'C.A15.L3'
c_a15_4_8_l3.ps_id = 'C.A15.L3'
c_a16_1_1_l3.ps_id = 'C.A16.L3'
c_a16_1_2_l3.ps_id = 'C.A16.L3'
c_a16_1_3_l3.ps_id = 'C.A16.L3'
c_a16_1_4_l3.ps_id = 'C.A16.L3'
c_a16_1_5_l3.ps_id = 'C.A16.L3'
c_a16_1_6_l3.ps_id = 'C.A16.L3'
c_a16_1_7_l3.ps_id = 'C.A16.L3'
c_a16_1_8_l3.ps_id = 'C.A16.L3'
c_a16_2_1_l3.ps_id = 'C.A16.L3'
c_a16_2_2_l3.ps_id = 'C.A16.L3'
c_a16_2_3_l3.ps_id = 'C.A16.L3'
c_a16_2_4_l3.ps_id = 'C.A16.L3'
c_a16_2_5_l3.ps_id = 'C.A16.L3'
c_a16_2_6_l3.ps_id = 'C.A16.L3'
c_a16_2_7_l3.ps_id = 'C.A16.L3'
c_a16_2_8_l3.ps_id = 'C.A16.L3'
c_a16_3_1_l3.ps_id = 'C.A16.L3'
c_a16_3_2_l3.ps_id = 'C.A16.L3'
c_a16_3_3_l3.ps_id = 'C.A16.L3'
c_a16_3_4_l3.ps_id = 'C.A16.L3'
c_a16_3_5_l3.ps_id = 'C.A16.L3'
c_a16_3_6_l3.ps_id = 'C.A16.L3'
c_a16_3_7_l3.ps_id = 'C.A16.L3'
c_a16_3_8_l3.ps_id = 'C.A16.L3'
c_a16_4_1_l3.ps_id = 'C.A16.L3'
c_a16_4_2_l3.ps_id = 'C.A16.L3'
c_a16_4_3_l3.ps_id = 'C.A16.L3'
c_a16_4_4_l3.ps_id = 'C.A16.L3'
c_a16_4_5_l3.ps_id = 'C.A16.L3'
c_a16_4_6_l3.ps_id = 'C.A16.L3'
c_a16_4_7_l3.ps_id = 'C.A16.L3'
c_a16_4_8_l3.ps_id = 'C.A16.L3'
c_a17_1_1_l3.ps_id = 'C.A17.L3'
c_a17_1_2_l3.ps_id = 'C.A17.L3'
c_a17_1_3_l3.ps_id = 'C.A17.L3'
c_a17_1_4_l3.ps_id = 'C.A17.L3'
c_a17_1_5_l3.ps_id = 'C.A17.L3'
c_a17_1_6_l3.ps_id = 'C.A17.L3'
c_a17_1_7_l3.ps_id = 'C.A17.L3'
c_a17_1_8_l3.ps_id = 'C.A17.L3'
c_a17_2_1_l3.ps_id = 'C.A17.L3'
c_a17_2_2_l3.ps_id = 'C.A17.L3'
c_a17_2_3_l3.ps_id = 'C.A17.L3'
c_a17_2_4_l3.ps_id = 'C.A17.L3'
c_a17_2_5_l3.ps_id = 'C.A17.L3'
c_a17_2_6_l3.ps_id = 'C.A17.L3'
c_a17_2_7_l3.ps_id = 'C.A17.L3'
c_a17_2_8_l3.ps_id = 'C.A17.L3'
c_a17_3_1_l3.ps_id = 'C.A17.L3'
c_a17_3_2_l3.ps_id = 'C.A17.L3'
c_a17_3_3_l3.ps_id = 'C.A17.L3'
c_a17_3_4_l3.ps_id = 'C.A17.L3'
c_a17_3_5_l3.ps_id = 'C.A17.L3'
c_a17_3_6_l3.ps_id = 'C.A17.L3'
c_a17_3_7_l3.ps_id = 'C.A17.L3'
c_a17_3_8_l3.ps_id = 'C.A17.L3'
c_a17_4_1_l3.ps_id = 'C.A17.L3'
c_a17_4_2_l3.ps_id = 'C.A17.L3'
c_a17_4_3_l3.ps_id = 'C.A17.L3'
c_a17_4_4_l3.ps_id = 'C.A17.L3'
c_a17_4_5_l3.ps_id = 'C.A17.L3'
c_a17_4_6_l3.ps_id = 'C.A17.L3'
c_a17_4_7_l3.ps_id = 'C.A17.L3'
c_a17_4_8_l3.ps_id = 'C.A17.L3'
c_a18_1_1_l3.ps_id = 'C.A18.L3'
c_a18_1_2_l3.ps_id = 'C.A18.L3'
c_a18_1_3_l3.ps_id = 'C.A18.L3'
c_a18_1_4_l3.ps_id = 'C.A18.L3'
c_a18_1_5_l3.ps_id = 'C.A18.L3'
c_a18_1_6_l3.ps_id = 'C.A18.L3'
c_a18_1_7_l3.ps_id = 'C.A18.L3'
c_a18_1_8_l3.ps_id = 'C.A18.L3'
c_a18_2_1_l3.ps_id = 'C.A18.L3'
c_a18_2_2_l3.ps_id = 'C.A18.L3'
c_a18_2_3_l3.ps_id = 'C.A18.L3'
c_a18_2_4_l3.ps_id = 'C.A18.L3'
c_a18_2_5_l3.ps_id = 'C.A18.L3'
c_a18_2_6_l3.ps_id = 'C.A18.L3'
c_a18_2_7_l3.ps_id = 'C.A18.L3'
c_a18_2_8_l3.ps_id = 'C.A18.L3'
c_a18_3_1_l3.ps_id = 'C.A18.L3'
c_a18_3_2_l3.ps_id = 'C.A18.L3'
c_a18_3_3_l3.ps_id = 'C.A18.L3'
c_a18_3_4_l3.ps_id = 'C.A18.L3'
c_a18_3_5_l3.ps_id = 'C.A18.L3'
c_a18_3_6_l3.ps_id = 'C.A18.L3'
c_a18_3_7_l3.ps_id = 'C.A18.L3'
c_a18_3_8_l3.ps_id = 'C.A18.L3'
c_a18_4_1_l3.ps_id = 'C.A18.L3'
c_a18_4_2_l3.ps_id = 'C.A18.L3'
c_a18_4_3_l3.ps_id = 'C.A18.L3'
c_a18_4_4_l3.ps_id = 'C.A18.L3'
c_a18_4_5_l3.ps_id = 'C.A18.L3'
c_a18_4_6_l3.ps_id = 'C.A18.L3'
c_a18_4_7_l3.ps_id = 'C.A18.L3'
c_a18_4_8_l3.ps_id = 'C.A18.L3'
c_a19_1_1_l3.ps_id = 'C.A19.L3'
c_a19_1_2_l3.ps_id = 'C.A19.L3'
c_a19_1_3_l3.ps_id = 'C.A19.L3'
c_a19_1_4_l3.ps_id = 'C.A19.L3'
c_a19_1_5_l3.ps_id = 'C.A19.L3'
c_a19_1_6_l3.ps_id = 'C.A19.L3'
c_a19_1_7_l3.ps_id = 'C.A19.L3'
c_a19_1_8_l3.ps_id = 'C.A19.L3'
c_a19_2_1_l3.ps_id = 'C.A19.L3'
c_a19_2_2_l3.ps_id = 'C.A19.L3'
c_a19_2_3_l3.ps_id = 'C.A19.L3'
c_a19_2_4_l3.ps_id = 'C.A19.L3'
c_a19_2_5_l3.ps_id = 'C.A19.L3'
c_a19_2_6_l3.ps_id = 'C.A19.L3'
c_a19_2_7_l3.ps_id = 'C.A19.L3'
c_a19_2_8_l3.ps_id = 'C.A19.L3'
c_a19_3_1_l3.ps_id = 'C.A19.L3'
c_a19_3_2_l3.ps_id = 'C.A19.L3'
c_a19_3_3_l3.ps_id = 'C.A19.L3'
c_a19_3_4_l3.ps_id = 'C.A19.L3'
c_a19_3_5_l3.ps_id = 'C.A19.L3'
c_a19_3_6_l3.ps_id = 'C.A19.L3'
c_a19_3_7_l3.ps_id = 'C.A19.L3'
c_a19_3_8_l3.ps_id = 'C.A19.L3'
c_a19_4_1_l3.ps_id = 'C.A19.L3'
c_a19_4_2_l3.ps_id = 'C.A19.L3'
c_a19_4_3_l3.ps_id = 'C.A19.L3'
c_a19_4_4_l3.ps_id = 'C.A19.L3'
c_a19_4_5_l3.ps_id = 'C.A19.L3'
c_a19_4_6_l3.ps_id = 'C.A19.L3'
c_a19_4_7_l3.ps_id = 'C.A19.L3'
c_a19_4_8_l3.ps_id = 'C.A19.L3'
c_a20_1_1_l3.ps_id = 'C.A20.L3'
c_a20_1_2_l3.ps_id = 'C.A20.L3'
c_a20_1_3_l3.ps_id = 'C.A20.L3'
c_a20_1_4_l3.ps_id = 'C.A20.L3'
c_a20_1_5_l3.ps_id = 'C.A20.L3'
c_a20_1_6_l3.ps_id = 'C.A20.L3'
c_a20_1_7_l3.ps_id = 'C.A20.L3'
c_a20_1_8_l3.ps_id = 'C.A20.L3'
c_a20_2_1_l3.ps_id = 'C.A20.L3'
c_a20_2_2_l3.ps_id = 'C.A20.L3'
c_a20_2_3_l3.ps_id = 'C.A20.L3'
c_a20_2_4_l3.ps_id = 'C.A20.L3'
c_a20_2_5_l3.ps_id = 'C.A20.L3'
c_a20_2_6_l3.ps_id = 'C.A20.L3'
c_a20_2_7_l3.ps_id = 'C.A20.L3'
c_a20_2_8_l3.ps_id = 'C.A20.L3'
c_a20_3_1_l3.ps_id = 'C.A20.L3'
c_a20_3_2_l3.ps_id = 'C.A20.L3'
c_a20_3_3_l3.ps_id = 'C.A20.L3'
c_a20_3_4_l3.ps_id = 'C.A20.L3'
c_a20_3_5_l3.ps_id = 'C.A20.L3'
c_a20_3_6_l3.ps_id = 'C.A20.L3'
c_a20_3_7_l3.ps_id = 'C.A20.L3'
c_a20_3_8_l3.ps_id = 'C.A20.L3'
c_a20_4_1_l3.ps_id = 'C.A20.L3'
c_a20_4_2_l3.ps_id = 'C.A20.L3'
c_a20_4_3_l3.ps_id = 'C.A20.L3'
c_a20_4_4_l3.ps_id = 'C.A20.L3'
c_a20_4_5_l3.ps_id = 'C.A20.L3'
c_a20_4_6_l3.ps_id = 'C.A20.L3'
c_a20_4_7_l3.ps_id = 'C.A20.L3'
c_a20_4_8_l3.ps_id = 'C.A20.L3'
c_a21_1_1_l3.ps_id = 'C.A21.L3'
c_a21_1_2_l3.ps_id = 'C.A21.L3'
c_a21_1_3_l3.ps_id = 'C.A21.L3'
c_a21_1_4_l3.ps_id = 'C.A21.L3'
c_a21_1_5_l3.ps_id = 'C.A21.L3'
c_a21_1_6_l3.ps_id = 'C.A21.L3'
c_a21_1_7_l3.ps_id = 'C.A21.L3'
c_a21_1_8_l3.ps_id = 'C.A21.L3'
c_a21_2_1_l3.ps_id = 'C.A21.L3'
c_a21_2_2_l3.ps_id = 'C.A21.L3'
c_a21_2_3_l3.ps_id = 'C.A21.L3'
c_a21_2_4_l3.ps_id = 'C.A21.L3'
c_a21_2_5_l3.ps_id = 'C.A21.L3'
c_a21_2_6_l3.ps_id = 'C.A21.L3'
c_a21_2_7_l3.ps_id = 'C.A21.L3'
c_a21_2_8_l3.ps_id = 'C.A21.L3'
c_a21_3_1_l3.ps_id = 'C.A21.L3'
c_a21_3_2_l3.ps_id = 'C.A21.L3'
c_a21_3_3_l3.ps_id = 'C.A21.L3'
c_a21_3_4_l3.ps_id = 'C.A21.L3'
c_a21_3_5_l3.ps_id = 'C.A21.L3'
c_a21_3_6_l3.ps_id = 'C.A21.L3'
c_a21_3_7_l3.ps_id = 'C.A21.L3'
c_a21_3_8_l3.ps_id = 'C.A21.L3'
c_a21_4_1_l3.ps_id = 'C.A21.L3'
c_a21_4_2_l3.ps_id = 'C.A21.L3'
c_a21_4_3_l3.ps_id = 'C.A21.L3'
c_a21_4_4_l3.ps_id = 'C.A21.L3'
c_a21_4_5_l3.ps_id = 'C.A21.L3'
c_a21_4_6_l3.ps_id = 'C.A21.L3'
c_a21_4_7_l3.ps_id = 'C.A21.L3'
c_a21_4_8_l3.ps_id = 'C.A21.L3'
c_a22_1_1_l3.ps_id = 'C.A22.L3'
c_a22_1_2_l3.ps_id = 'C.A22.L3'
c_a22_1_3_l3.ps_id = 'C.A22.L3'
c_a22_1_4_l3.ps_id = 'C.A22.L3'
c_a22_1_5_l3.ps_id = 'C.A22.L3'
c_a22_1_6_l3.ps_id = 'C.A22.L3'
c_a22_1_7_l3.ps_id = 'C.A22.L3'
c_a22_1_8_l3.ps_id = 'C.A22.L3'
c_a22_2_1_l3.ps_id = 'C.A22.L3'
c_a22_2_2_l3.ps_id = 'C.A22.L3'
c_a22_2_3_l3.ps_id = 'C.A22.L3'
c_a22_2_4_l3.ps_id = 'C.A22.L3'
c_a22_2_5_l3.ps_id = 'C.A22.L3'
c_a22_2_6_l3.ps_id = 'C.A22.L3'
c_a22_2_7_l3.ps_id = 'C.A22.L3'
c_a22_2_8_l3.ps_id = 'C.A22.L3'
c_a22_3_1_l3.ps_id = 'C.A22.L3'
c_a22_3_2_l3.ps_id = 'C.A22.L3'
c_a22_3_3_l3.ps_id = 'C.A22.L3'
c_a22_3_4_l3.ps_id = 'C.A22.L3'
c_a22_3_5_l3.ps_id = 'C.A22.L3'
c_a22_3_6_l3.ps_id = 'C.A22.L3'
c_a22_3_7_l3.ps_id = 'C.A22.L3'
c_a22_3_8_l3.ps_id = 'C.A22.L3'
c_a22_4_1_l3.ps_id = 'C.A22.L3'
c_a22_4_2_l3.ps_id = 'C.A22.L3'
c_a22_4_3_l3.ps_id = 'C.A22.L3'
c_a22_4_4_l3.ps_id = 'C.A22.L3'
c_a22_4_5_l3.ps_id = 'C.A22.L3'
c_a22_4_6_l3.ps_id = 'C.A22.L3'
c_a22_4_7_l3.ps_id = 'C.A22.L3'
c_a22_4_8_l3.ps_id = 'C.A22.L3'
c_a23_1_1_l3.ps_id = 'C.A23.L3'
c_a23_1_2_l3.ps_id = 'C.A23.L3'
c_a23_1_3_l3.ps_id = 'C.A23.L3'
c_a23_1_4_l3.ps_id = 'C.A23.L3'
c_a23_1_5_l3.ps_id = 'C.A23.L3'
c_a23_1_6_l3.ps_id = 'C.A23.L3'
c_a23_1_7_l3.ps_id = 'C.A23.L3'
c_a23_1_8_l3.ps_id = 'C.A23.L3'
c_a23_2_1_l3.ps_id = 'C.A23.L3'
c_a23_2_2_l3.ps_id = 'C.A23.L3'
c_a23_2_3_l3.ps_id = 'C.A23.L3'
c_a23_2_4_l3.ps_id = 'C.A23.L3'
c_a23_2_5_l3.ps_id = 'C.A23.L3'
c_a23_2_6_l3.ps_id = 'C.A23.L3'
c_a23_2_7_l3.ps_id = 'C.A23.L3'
c_a23_2_8_l3.ps_id = 'C.A23.L3'
c_a23_3_1_l3.ps_id = 'C.A23.L3'
c_a23_3_2_l3.ps_id = 'C.A23.L3'
c_a23_3_3_l3.ps_id = 'C.A23.L3'
c_a23_3_4_l3.ps_id = 'C.A23.L3'
c_a23_3_5_l3.ps_id = 'C.A23.L3'
c_a23_3_6_l3.ps_id = 'C.A23.L3'
c_a23_3_7_l3.ps_id = 'C.A23.L3'
c_a23_3_8_l3.ps_id = 'C.A23.L3'
c_a23_4_1_l3.ps_id = 'C.A23.L3'
c_a23_4_2_l3.ps_id = 'C.A23.L3'
c_a23_4_3_l3.ps_id = 'C.A23.L3'
c_a23_4_4_l3.ps_id = 'C.A23.L3'
c_a23_4_5_l3.ps_id = 'C.A23.L3'
c_a23_4_6_l3.ps_id = 'C.A23.L3'
c_a23_4_7_l3.ps_id = 'C.A23.L3'
c_a23_4_8_l3.ps_id = 'C.A23.L3'
c_a24_1_1_l3.ps_id = 'C.A24.L3'
c_a24_1_2_l3.ps_id = 'C.A24.L3'
c_a24_1_3_l3.ps_id = 'C.A24.L3'
c_a24_1_4_l3.ps_id = 'C.A24.L3'
c_a24_1_5_l3.ps_id = 'C.A24.L3'
c_a24_1_6_l3.ps_id = 'C.A24.L3'
c_a24_1_7_l3.ps_id = 'C.A24.L3'
c_a24_1_8_l3.ps_id = 'C.A24.L3'
c_a24_2_1_l3.ps_id = 'C.A24.L3'
c_a24_2_2_l3.ps_id = 'C.A24.L3'
c_a24_2_3_l3.ps_id = 'C.A24.L3'
c_a24_2_4_l3.ps_id = 'C.A24.L3'
c_a24_2_5_l3.ps_id = 'C.A24.L3'
c_a24_2_6_l3.ps_id = 'C.A24.L3'
c_a24_2_7_l3.ps_id = 'C.A24.L3'
c_a24_2_8_l3.ps_id = 'C.A24.L3'
c_a24_3_1_l3.ps_id = 'C.A24.L3'
c_a24_3_2_l3.ps_id = 'C.A24.L3'
c_a24_3_3_l3.ps_id = 'C.A24.L3'
c_a24_3_4_l3.ps_id = 'C.A24.L3'
c_a24_3_5_l3.ps_id = 'C.A24.L3'
c_a24_3_6_l3.ps_id = 'C.A24.L3'
c_a24_3_7_l3.ps_id = 'C.A24.L3'
c_a24_3_8_l3.ps_id = 'C.A24.L3'
c_a24_4_1_l3.ps_id = 'C.A24.L3'
c_a24_4_2_l3.ps_id = 'C.A24.L3'
c_a24_4_3_l3.ps_id = 'C.A24.L3'
c_a24_4_4_l3.ps_id = 'C.A24.L3'
c_a24_4_5_l3.ps_id = 'C.A24.L3'
c_a24_4_6_l3.ps_id = 'C.A24.L3'
c_a24_4_7_l3.ps_id = 'C.A24.L3'
c_a24_4_8_l3.ps_id = 'C.A24.L3'
c_a25_1_1_l3.ps_id = 'C.A25.L3'
c_a25_1_2_l3.ps_id = 'C.A25.L3'
c_a25_1_3_l3.ps_id = 'C.A25.L3'
c_a25_1_4_l3.ps_id = 'C.A25.L3'
c_a25_1_5_l3.ps_id = 'C.A25.L3'
c_a25_1_6_l3.ps_id = 'C.A25.L3'
c_a25_1_7_l3.ps_id = 'C.A25.L3'
c_a25_1_8_l3.ps_id = 'C.A25.L3'
c_a25_2_1_l3.ps_id = 'C.A25.L3'
c_a25_2_2_l3.ps_id = 'C.A25.L3'
c_a25_2_3_l3.ps_id = 'C.A25.L3'
c_a25_2_4_l3.ps_id = 'C.A25.L3'
c_a25_2_5_l3.ps_id = 'C.A25.L3'
c_a25_2_6_l3.ps_id = 'C.A25.L3'
c_a25_2_7_l3.ps_id = 'C.A25.L3'
c_a25_2_8_l3.ps_id = 'C.A25.L3'
c_a25_3_1_l3.ps_id = 'C.A25.L3'
c_a25_3_2_l3.ps_id = 'C.A25.L3'
c_a25_3_3_l3.ps_id = 'C.A25.L3'
c_a25_3_4_l3.ps_id = 'C.A25.L3'
c_a25_3_5_l3.ps_id = 'C.A25.L3'
c_a25_3_6_l3.ps_id = 'C.A25.L3'
c_a25_3_7_l3.ps_id = 'C.A25.L3'
c_a25_3_8_l3.ps_id = 'C.A25.L3'
c_a25_4_1_l3.ps_id = 'C.A25.L3'
c_a25_4_2_l3.ps_id = 'C.A25.L3'
c_a25_4_3_l3.ps_id = 'C.A25.L3'
c_a25_4_4_l3.ps_id = 'C.A25.L3'
c_a25_4_5_l3.ps_id = 'C.A25.L3'
c_a25_4_6_l3.ps_id = 'C.A25.L3'
c_a25_4_7_l3.ps_id = 'C.A25.L3'
c_a25_4_8_l3.ps_id = 'C.A25.L3'

#  
be_1678_cl.ps_id = 'BE.1.CL'
bl_1688_cl.ps_id = 'BL.1.CL'
bl_1695_cl.ps_id = 'BL.1.CL'
be_1705_cl.ps_id = 'BE.1.CL'
be_1714_cl.ps_id = 'BE.1.CL'
bl_1724_cl.ps_id = 'BL.1.CL'
bl_1731_cl.ps_id = 'BL.1.CL'
be_1741_cl.ps_id = 'BE.1.CL'
be_1786_cl.ps_id = 'BE.2.CL'
bl_1796_cl.ps_id = 'BL.2.CL'
bl_1803_cl.ps_id = 'BL.2.CL'
be_1813_cl.ps_id = 'BE.2.CL'
be_1822_cl.ps_id = 'BE.2.CL'
bl_1832_cl.ps_id = 'BL.2.CL'
bl_1839_cl.ps_id = 'BL.2.CL'
be_1849_cl.ps_id = 'BE.2.CL'
