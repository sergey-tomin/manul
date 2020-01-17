from ocelot import * 
from ocelot.cpbd.elements import *
tws = Twiss()
tws.beta_x  = 10.785966482613036
tws.beta_y  = 42.698893189438415
tws.alpha_x = 0.6830890784580208
tws.alpha_y = -2.1778114814176694
tws.E = 14

# Drifts
d_1 = Drift(l=0.472401, eid='D_1')
d_2 = Drift(l=1.972421, eid='D_2')
d_3 = Drift(l=0.5, eid='D_3')
d_5 = Drift(l=4.750006, eid='D_5')
d_7 = Drift(l=1.775, eid='D_7')
d_8 = Drift(l=0.20895, eid='D_8')
d_9 = Drift(l=0.15395, eid='D_9')
d_10 = Drift(l=1.22435, eid='D_10')
d_11 = Drift(l=1.710028, eid='D_11')
d_14 = Drift(l=4.379405, eid='D_14')
d_15 = Drift(l=0.8568, eid='D_15')
d_16 = Drift(l=2.976816, eid='D_16')
d_19 = Drift(l=0.22435, eid='D_19')
d_20 = Drift(l=5.029084, eid='D_20')
d_21 = Drift(l=0.275, eid='D_21')
d_24 = Drift(l=3.3318, eid='D_24')
d_25 = Drift(l=1.277982, eid='D_25')
d_28 = Drift(l=7.218425, eid='D_28')
d_29 = Drift(l=0.500002, eid='D_29')
d_30 = Drift(l=0.500001, eid='D_30')
d_32 = Drift(l=0.275002, eid='D_32')
d_35 = Drift(l=0.23, eid='D_35')
d_36 = Drift(l=3.62, eid='D_36')
d_37 = Drift(l=0.27, eid='D_37')
d_38 = Drift(l=3.42, eid='D_38')
d_40 = Drift(l=3.72, eid='D_40')
d_44 = Drift(l=11.005, eid='D_44')
d_47 = Drift(l=6.73, eid='D_47')
d_48 = Drift(l=6.775, eid='D_48')
d_51 = Drift(l=13.505, eid='D_51')
d_62 = Drift(l=5.43, eid='D_62')
d_63 = Drift(l=5.475, eid='D_63')
d_66 = Drift(l=4.02, eid='D_66')
d_67 = Drift(l=5.594625, eid='D_67')
d_68 = Drift(l=0.8065, eid='D_68')
d_69 = Drift(l=0.21815, eid='D_69')
d_70 = Drift(l=0.17815, eid='D_70')
d_71 = Drift(l=0.125, eid='D_71')
d_72 = Drift(l=2.1675, eid='D_72')
d_73 = Drift(l=1.8267, eid='D_73')
d_74 = Drift(l=0.15, eid='D_74')
d_75 = Drift(l=0.4323, eid='D_75')
d_76 = Drift(l=0.18665, eid='D_76')
d_77 = Drift(l=0.04015, eid='D_77')

# Quadrupoles
qf_2041_t1 = Quadrupole(l=0.5321, k1=0.31524314207855664, eid='QF.2041.T1')
qf_2045_t1 = Quadrupole(l=0.5321, k1=-0.3236115910543131, eid='QF.2045.T1')
qf_2055_t1 = Quadrupole(l=0.5321, k1=0.15441795019733132, eid='QF.2055.T1')
qf_2063_t1 = Quadrupole(l=0.5321, k1=-0.33882318887427176, eid='QF.2063.T1')
qf_2069_t1 = Quadrupole(l=0.5321, k1=0.2823186838940049, eid='QF.2069.T1')
qf_2083_t1 = Quadrupole(l=0.5321, k1=-0.19493844953956022, eid='QF.2083.T1')
qf_2098_t1 = Quadrupole(l=0.5321, k1=0.1716515493328322, eid='QF.2098.T1')
qf_2110_t1 = Quadrupole(l=0.5321, k1=-0.16684571509114826, eid='QF.2110.T1')
qf_2124_t1 = Quadrupole(l=0.5321, k1=0.13010246344672052, eid='QF.2124.T1')
qf_2139_t1 = Quadrupole(l=0.5321, k1=-0.12309674610035708, eid='QF.2139.T1')
qf_2153_t1 = Quadrupole(l=0.5321, k1=0.11725887032512684, eid='QF.2153.T1')
qf_2168_t1 = Quadrupole(l=0.5321, k1=-0.12597771603082125, eid='QF.2168.T1')
qf_2180_t1 = Quadrupole(l=0.5321, k1=0.12100529092275887, eid='QF.2180.T1')
qa_2191_t1 = Quadrupole(l=0.1137, k1=-0.5445788786279684, eid='QA.2191.T1')
qa_2197_t1 = Quadrupole(l=0.1137, k1=0.5501622374670185, eid='QA.2197.T1')

# SBends
bz_2025_t1 = SBend(l=1.0, angle=-0.00550002773, e2=-0.005500028, tilt=0.21321543, eid='BZ.2025.T1')
bz_2030_t1 = SBend(l=1.0, angle=-0.00550002773, e1=-0.002750014, e2=-0.002750014, eid='BZ.2030.T1')
bz_2031_t1 = SBend(l=1.0, angle=-0.00550002773, e1=-0.002750014, e2=-0.002750014, eid='BZ.2031.T1')
bz_2033_t1 = SBend(l=1.0, angle=-0.00550002773, e1=-0.002750014, e2=-0.002750014, eid='BZ.2033.T1')
bd_2050_t1 = SBend(l=1.0, angle=0.00303654925, e1=0.001518275, e2=0.001518275, eid='BD.2050.T1')
bd_2062_t1 = SBend(l=1.0, angle=0.00303654925, e1=0.001518275, e2=0.001518275, eid='BD.2062.T1')
bd_2077_t1 = SBend(l=1.0, angle=-0.005827964456, e1=-0.002913982, e2=-0.002913982, eid='BD.2077.T1')
bd_2079_t1 = SBend(l=1.0, angle=-0.005827964456, e1=-0.002913982, e2=-0.002913982, eid='BD.2079.T1')
bd_2080_t1 = SBend(l=1.0, angle=-0.005827964456, e1=-0.002913982, e2=-0.002913982, eid='BD.2080.T1')
bd_2082_t1 = SBend(l=1.0, angle=-0.005827964456, e1=-0.002913982, e2=-0.002913982, eid='BD.2082.T1')
bd_2084_t1 = SBend(l=1.0, angle=0.001913314532, e1=0.000956657, e2=0.000956657, tilt=1.570796327, eid='BD.2084.T1')
bd_2097_t1 = SBend(l=1.0, angle=-0.001913314532, e1=-0.000956657, e2=-0.000956657, tilt=1.570796327, eid='BD.2097.T1')

# Sextupoles
sa_2052_t1 = Sextupole(l=0.3164, k2=-5.974177089001264, tilt=-0.095993109, eid='SA.2052.T1')
sa_2067_t1 = Sextupole(l=0.3164, k2=-1.7090884390012642, tilt=-0.322885912, eid='SA.2067.T1')

# Octupoles
oa_2042_t1 = Octupole(l=0.2113, k3=-132.8835386, tilt=-0.13962634, eid='OA.2042.T1')
oa_2056_t1 = Octupole(l=0.2113, k3=-186.9089832, tilt=-0.270526034, eid='OA.2056.T1')

# Hcors
cfx_2041_t1 = Hcor(l=0.1, eid='CFX.2041.T1')
cfx_2056_t1 = Hcor(l=0.1, eid='CFX.2056.T1')
cfx_2069_t1 = Hcor(l=0.1, eid='CFX.2069.T1')
cfx_2089_t1 = Hcor(l=0.1, eid='CFX.2089.T1')
cfx_2098_t1 = Hcor(l=0.1, eid='CFX.2098.T1')
cfx_2125_t1 = Hcor(l=0.1, eid='CFX.2125.T1')
cfx_2154_t1 = Hcor(l=0.1, eid='CFX.2154.T1')
cfx_2180_t1 = Hcor(l=0.1, eid='CFX.2180.T1')
cex_2192_t1 = Hcor(l=0.1, eid='CEX.2192.T1')
cex_2196_t1 = Hcor(l=0.1, eid='CEX.2196.T1')

# Vcors
cfy_2045_t1 = Vcor(l=0.1, eid='CFY.2045.T1')
cfy_2063_t1 = Vcor(l=0.1, eid='CFY.2063.T1')
cfy_2083_t1 = Vcor(l=0.1, eid='CFY.2083.T1')
cfy_2092_t1 = Vcor(l=0.1, eid='CFY.2092.T1')
cfy_2110_t1 = Vcor(l=0.1, eid='CFY.2110.T1')
cfy_2139_t1 = Vcor(l=0.1, eid='CFY.2139.T1')
cfy_2168_t1 = Vcor(l=0.1, eid='CFY.2168.T1')
cny_2191_t1 = Vcor(l=0.3, eid='CNY.2191.T1')
cny_2196_t1 = Vcor(l=0.3, eid='CNY.2196.T1')

# Undulators
u40s_2194_t1 = Undulator(lperiod=0.04, nperiods=3.0, Kx=3, eid='U40S.2194.T1')

# Monitors
bpma_2040_t1 = Monitor(eid='BPMA.2040.T1')
bpma_2044_t1 = Monitor(eid='BPMA.2044.T1')
bpma_2055_t1 = Monitor(eid='BPMA.2055.T1')
bpma_2062_t1 = Monitor(eid='BPMA.2062.T1')
bpma_2068_t1 = Monitor(eid='BPMA.2068.T1')
bpma_2082_t1 = Monitor(eid='BPMA.2082.T1')
bpma_2088_t1 = Monitor(eid='BPMA.2088.T1')
bpma_2092_t1 = Monitor(eid='BPMA.2092.T1')
bpma_2097_t1 = Monitor(eid='BPMA.2097.T1')
bpma_2109_t1 = Monitor(eid='BPMA.2109.T1')
bpma_2124_t1 = Monitor(eid='BPMA.2124.T1')
bpma_2138_t1 = Monitor(eid='BPMA.2138.T1')
bpma_2153_t1 = Monitor(eid='BPMA.2153.T1')
bpma_2167_t1 = Monitor(eid='BPMA.2167.T1')
bpma_2179_t1 = Monitor(eid='BPMA.2179.T1')
bpma_2184_t1 = Monitor(eid='BPMA.2184.T1')
bpme_2191_t1 = Monitor(eid='BPME.2191.T1')
bpme_2197_t1 = Monitor(eid='BPME.2197.T1')

# Markers
stsec_2025_t1 = Marker(eid='STSEC.2025.T1')
tora_2038_t1 = Marker(eid='TORA.2038.T1')
otra_2038_t1 = Marker(eid='OTRA.2038.T1')
otrb_2117_t1 = Marker(eid='OTRB.2117.T1')
otrbw_2146_t1 = Marker(eid='OTRBW.2146.T1')
otrbw_2161_t1 = Marker(eid='OTRBW.2161.T1')
otrbw_2174_t1 = Marker(eid='OTRBW.2174.T1')
tora_2190_t1 = Marker(eid='TORA.2190.T1')
ensec_2197_t1 = Marker(eid='ENSEC.2197.T1')

# XYQuadrupoles
qk_2027_tl = XYQuadrupole(l=1.0552, x_offs=0.0081538, y_offs=0.02356075, k1=-0.09035541, eid='QK.2027.TL')

# Lattice 
cell = (stsec_2025_t1, bz_2025_t1, d_1, qk_2027_tl, d_2, bz_2030_t1, d_3, bz_2031_t1, d_3, 
bz_2033_t1, d_5, tora_2038_t1, d_3, otra_2038_t1, d_7, bpma_2040_t1, d_8, qf_2041_t1, d_9, 
cfx_2041_t1, d_10, oa_2042_t1, d_11, bpma_2044_t1, d_8, qf_2045_t1, d_9, cfy_2045_t1, d_14, 
bd_2050_t1, d_15, sa_2052_t1, d_16, bpma_2055_t1, d_8, qf_2055_t1, d_9, cfx_2056_t1, d_19, 
oa_2056_t1, d_20, bd_2062_t1, d_21, bpma_2062_t1, d_8, qf_2063_t1, d_9, cfy_2063_t1, d_24, 
sa_2067_t1, d_25, bpma_2068_t1, d_8, qf_2069_t1, d_9, cfx_2069_t1, d_28, bd_2077_t1, d_29, 
bd_2079_t1, d_30, bd_2080_t1, d_3, bd_2082_t1, d_32, bpma_2082_t1, d_8, qf_2083_t1, d_9, 
cfy_2083_t1, d_35, bd_2084_t1, d_36, bpma_2088_t1, d_37, cfx_2089_t1, d_38, bpma_2092_t1, d_37, 
cfy_2092_t1, d_40, bd_2097_t1, d_21, bpma_2097_t1, d_8, qf_2098_t1, d_9, cfx_2098_t1, d_44, 
bpma_2109_t1, d_8, qf_2110_t1, d_9, cfy_2110_t1, d_47, otrb_2117_t1, d_48, bpma_2124_t1, d_8, 
qf_2124_t1, d_9, cfx_2125_t1, d_51, bpma_2138_t1, d_8, qf_2139_t1, d_9, cfy_2139_t1, d_47, 
otrbw_2146_t1, d_48, bpma_2153_t1, d_8, qf_2153_t1, d_9, cfx_2154_t1, d_47, otrbw_2161_t1, d_48, 
bpma_2167_t1, d_8, qf_2168_t1, d_9, cfy_2168_t1, d_62, otrbw_2174_t1, d_63, bpma_2179_t1, d_8, 
qf_2180_t1, d_9, cfx_2180_t1, d_66, bpma_2184_t1, d_67, tora_2190_t1, d_68, bpme_2191_t1, d_69, 
qa_2191_t1, d_70, cny_2191_t1, d_71, cex_2192_t1, d_72, u40s_2194_t1, d_73, cny_2196_t1, d_74, 
cex_2196_t1, d_75, bpme_2197_t1, d_76, qa_2197_t1, d_77, ensec_2197_t1)

# power supplies 

#  
qf_2041_t1.ps_id = 'QF.1.T1'
qf_2045_t1.ps_id = 'QF.2.T1'
qf_2055_t1.ps_id = 'QF.3.T1'
qf_2063_t1.ps_id = 'QF.4.T1'
qf_2069_t1.ps_id = 'QF.5.T1'
qf_2083_t1.ps_id = 'QF.6.T1'
qf_2098_t1.ps_id = 'QF.7.T1'
qf_2110_t1.ps_id = 'QF.8.T1'
qf_2124_t1.ps_id = 'QF.9.T1'
qf_2139_t1.ps_id = 'QF.10.T1'
qf_2153_t1.ps_id = 'QF.11.T1'
qf_2168_t1.ps_id = 'QF.12.T1'
qf_2180_t1.ps_id = 'QF.13.T1'
qa_2191_t1.ps_id = 'QA.1.T1'
qa_2197_t1.ps_id = 'QA.2.T1'

#  
sa_2052_t1.ps_id = 'SA.1.T1'
sa_2067_t1.ps_id = 'SA.2.T1'

#  
oa_2042_t1.ps_id = 'OA.1.T1'
oa_2056_t1.ps_id = 'OA.2.T1'

#  

#  
bz_2025_t1.ps_id = 'BZ.1.T1'
bz_2030_t1.ps_id = 'BZ.2.T1'
bz_2031_t1.ps_id = 'BZ.2.T1'
bz_2033_t1.ps_id = 'BZ.2.T1'
bd_2050_t1.ps_id = 'BD.2.T1'
bd_2062_t1.ps_id = 'BD.2.T1'
bd_2077_t1.ps_id = 'BD.1.T1'
bd_2079_t1.ps_id = 'BD.1.T1'
bd_2080_t1.ps_id = 'BD.1.T1'
bd_2082_t1.ps_id = 'BD.1.T1'
bd_2084_t1.ps_id = 'BD.3.T1'
bd_2097_t1.ps_id = 'BD.4.T1'
