from ocelot import *

tws_sase1 = Twiss()
tws_sase1.beta_x  = 42.548281572
tws_sase1.beta_y  = 11.0277770725
tws_sase1.alpha_x = -2.18143348313
tws_sase1.alpha_y = 0.703868806111
tws_sase1.E       = 17.4999999889
#tws_sase1.s        = 1957.1856390000232
tws_t4 = Twiss()
tws_t4.beta_x  = 25.9318680453
tws_t4.beta_y  = 38.3782827028
tws_t4.alpha_x = -0.840495296807
tws_t4.alpha_y = 1.22012853464
tws_t4.E       = 2.39999998888
#tws_t4.s        = 2438.5169790000195


# drifts 
d_1 = Drift(l=1.472401, eid='D_1')
d_2 = Drift(l=13.047401, eid='D_2')
d_3 = Drift(l=1.15895, eid='D_3')
d_4 = Drift(l=0.15395, eid='D_4')
d_5 = Drift(l=6.505, eid='D_5')
d_6 = Drift(l=6.5, eid='D_6')
d_7 = Drift(l=0.4457, eid='D_7')
d_8 = Drift(l=0.1543, eid='D_8')
d_9 = Drift(l=0.208951, eid='D_9')
d_10 = Drift(l=0.153951, eid='D_10')
d_11 = Drift(l=0.2, eid='D_11')
d_12 = Drift(l=7.7847, eid='D_12')
d_13 = Drift(l=0.1, eid='D_13')
d_14 = Drift(l=1.4347, eid='D_14')
d_16 = Drift(l=1.86072, eid='D_16')
d_18 = Drift(l=13.997421, eid='D_18')
d_21 = Drift(l=11.37, eid='D_21')
d_22 = Drift(l=0.17, eid='D_22')
d_23 = Drift(l=0.27, eid='D_23')
d_24 = Drift(l=1.742401, eid='D_24')
d_25 = Drift(l=0.472441, eid='D_25')
d_26 = Drift(l=13.525, eid='D_26')
d_27 = Drift(l=0.20895, eid='D_27')
d_29 = Drift(l=6.405, eid='D_29')
d_30 = Drift(l=6.6, eid='D_30')
d_33 = Drift(l=14.005, eid='D_33')
d_36 = Drift(l=14.0051, eid='D_36')
d_39 = Drift(l=14.705, eid='D_39')
d_42 = Drift(l=12.105, eid='D_42')
d_45 = Drift(l=15.205, eid='D_45')
d_48 = Drift(l=6.98, eid='D_48')
d_49 = Drift(l=7.025, eid='D_49')
d_59 = Drift(l=5.38, eid='D_59')
d_60 = Drift(l=5.425, eid='D_60')
d_63 = Drift(l=9.03255, eid='D_63')
d_64 = Drift(l=0.8065, eid='D_64')
d_65 = Drift(l=0.21815, eid='D_65')
d_66 = Drift(l=0.17815, eid='D_66')
d_67 = Drift(l=0.125, eid='D_67')
d_68 = Drift(l=2.1675, eid='D_68')
d_69 = Drift(l=1.8267, eid='D_69')
d_70 = Drift(l=0.15, eid='D_70')
d_71 = Drift(l=0.4323, eid='D_71')
d_72 = Drift(l=0.18665, eid='D_72')
d_73 = Drift(l=0.04015, eid='D_73')
d_74 = Drift(l=2.8905, eid='D_74')
d_75 = Drift(l=2.869, eid='D_75')
d_77 = Drift(l=2.93065, eid='D_77')
d_81 = Drift(l=0.31772, eid='D_81')
d_82 = Drift(l=0.07278, eid='D_82')
d_83 = Drift(l=0.0717, eid='D_83')
d_84 = Drift(l=0.2973, eid='D_84')
d_86 = Drift(l=0.35787, eid='D_86')
d_257 = Drift(l=1.3805, eid='D_257')
d_258 = Drift(l=5.678, eid='D_258')
d_259 = Drift(l=0.205, eid='D_259')
d_260 = Drift(l=0.14, eid='D_260')
d_261 = Drift(l=11.925, eid='D_261')
d_270 = Drift(l=19.01, eid='D_270')
d_273 = Drift(l=21.065, eid='D_273')
d_276 = Drift(l=18.72, eid='D_276')
d_277 = Drift(l=0.21045, eid='D_277')
d_278 = Drift(l=0.15545, eid='D_278')
d_279 = Drift(l=1.545, eid='D_279')
d_282 = Drift(l=9.06, eid='D_282')
d_283 = Drift(l=0.185, eid='D_283')
d_284 = Drift(l=0.19, eid='D_284')
d_286 = Drift(l=0.38545, eid='D_286')
d_287 = Drift(l=7e-06, eid='D_287')
d_288 = Drift(l=1.070157, eid='D_288')
d_289 = Drift(l=3.59515, eid='D_289')
d_290 = Drift(l=0.34515, eid='D_290')
d_291 = Drift(l=0.29015, eid='D_291')
d_292 = Drift(l=0.6718, eid='D_292')
d_293 = Drift(l=2.1168, eid='D_293')
d_296 = Drift(l=1.3218, eid='D_296')
d_297 = Drift(l=1.0768, eid='D_297')
d_300 = Drift(l=0.369898, eid='D_300')
d_301 = Drift(l=0.875266, eid='D_301')
d_304 = Drift(l=9.835, eid='D_304')
d_310 = Drift(l=18.61, eid='D_310')
d_322 = Drift(l=10.79, eid='D_322')
d_323 = Drift(l=10.275, eid='D_323')
d_326 = Drift(l=20.165, eid='D_326')
d_329 = Drift(l=5.48, eid='D_329')
d_330 = Drift(l=5.525, eid='D_330')
d_333 = Drift(l=11.005, eid='D_333')
d_340 = Drift(l=7.0907, eid='D_340')

# quadrupoles 
qk_1982_tl = Quadrupole(l=1.0552, k1=0.0903596001, tilt=0.0, eid='QK.1982.TL')
qf_1997_tl = Quadrupole(l=0.5321, k1=-0.1791908476, tilt=0.0, eid='QF.1997.TL')
qf_2012_tl = Quadrupole(l=0.5321, k1=0.1791908476, tilt=0.0, eid='QF.2012.TL')
qk_2027_tl = Quadrupole(l=1.0552, k1=-0.0903596001, tilt=0.0, eid='QK.2027.TL')
qf_2042_tl = Quadrupole(l=0.5321, k1=0.1791908476, tilt=0.0, eid='QF.2042.TL')
qk_2057_tl = Quadrupole(l=1.0552, k1=-0.0903596001, tilt=0.0, eid='QK.2057.TL')
qf_2072_t2 = Quadrupole(l=0.5321, k1=0.1791908476, tilt=0.0, eid='QF.2072.T2')
qf_2087_t2 = Quadrupole(l=0.5321, k1=-0.1791908476, tilt=0.0, eid='QF.2087.T2')
qf_2102_t2 = Quadrupole(l=0.5321, k1=0.1791908476, tilt=0.0, eid='QF.2102.T2')
qf_2117_t2 = Quadrupole(l=0.5321, k1=-0.1791908476, tilt=0.0, eid='QF.2117.T2')
qf_2132_t2 = Quadrupole(l=0.5321, k1=0.1791908476, tilt=0.0, eid='QF.2132.T2')
qf_2145_t2 = Quadrupole(l=0.5321, k1=-0.1791908476, tilt=0.0, eid='QF.2145.T2')
qf_2162_t2 = Quadrupole(l=0.5321, k1=0.1791908476, tilt=0.0, eid='QF.2162.T2')
qf_2177_t2 = Quadrupole(l=0.5321, k1=-0.1550803182, tilt=0.0, eid='QF.2177.T2')
qf_2192_t2 = Quadrupole(l=0.5321, k1=0.1524541549, tilt=0.0, eid='QF.2192.T2')
qf_2207_t2 = Quadrupole(l=0.5321, k1=-0.1286716831, tilt=0.0, eid='QF.2207.T2')
qf_2218_t2 = Quadrupole(l=0.5321, k1=0.1206127216, tilt=0.0, eid='QF.2218.T2')
qa_2229_t2 = Quadrupole(l=0.1137, k1=-0.5620550639, tilt=0.0, eid='QA.2229.T2')
qa_2235_t2 = Quadrupole(l=0.1137, k1=0.5620550639, tilt=0.0, eid='QA.2235.T2')
qa_2241_sa1 = Quadrupole(l=0.1137, k1=-0.5620550639, tilt=0.0, eid='QA.2241.SA1')
qa_2247_sa1 = Quadrupole(l=0.1137, k1=0.5620550639, tilt=0.0, eid='QA.2247.SA1')
qa_2253_sa1 = Quadrupole(l=0.1137, k1=-0.5620550639, tilt=0.0, eid='QA.2253.SA1')
qa_2259_sa1 = Quadrupole(l=0.1137, k1=0.5620550639, tilt=0.0, eid='QA.2259.SA1')
qa_2266_sa1 = Quadrupole(l=0.1137, k1=-0.5620550639, tilt=0.0, eid='QA.2266.SA1')
qa_2272_sa1 = Quadrupole(l=0.1137, k1=0.5620550639, tilt=0.0, eid='QA.2272.SA1')
qa_2278_sa1 = Quadrupole(l=0.1137, k1=-0.5620550639, tilt=0.0, eid='QA.2278.SA1')
qa_2284_sa1 = Quadrupole(l=0.1137, k1=0.5620550639, tilt=0.0, eid='QA.2284.SA1')
qa_2290_sa1 = Quadrupole(l=0.1137, k1=-0.5620550639, tilt=0.0, eid='QA.2290.SA1')
qa_2296_sa1 = Quadrupole(l=0.1137, k1=0.5620550639, tilt=0.0, eid='QA.2296.SA1')
qa_2302_sa1 = Quadrupole(l=0.1137, k1=-0.5620550639, tilt=0.0, eid='QA.2302.SA1')
qa_2308_sa1 = Quadrupole(l=0.1137, k1=0.5620550639, tilt=0.0, eid='QA.2308.SA1')
qa_2314_sa1 = Quadrupole(l=0.1137, k1=-0.5620550639, tilt=0.0, eid='QA.2314.SA1')
qa_2320_sa1 = Quadrupole(l=0.1137, k1=0.5620550639, tilt=0.0, eid='QA.2320.SA1')
qa_2327_sa1 = Quadrupole(l=0.1137, k1=-0.5620550639, tilt=0.0, eid='QA.2327.SA1')
qa_2333_sa1 = Quadrupole(l=0.1137, k1=0.5620550639, tilt=0.0, eid='QA.2333.SA1')
qa_2339_sa1 = Quadrupole(l=0.1137, k1=-0.5620550639, tilt=0.0, eid='QA.2339.SA1')
qa_2345_sa1 = Quadrupole(l=0.1137, k1=0.5620550639, tilt=0.0, eid='QA.2345.SA1')
qa_2351_sa1 = Quadrupole(l=0.1137, k1=-0.5620550639, tilt=0.0, eid='QA.2351.SA1')
qa_2357_sa1 = Quadrupole(l=0.1137, k1=0.5620550639, tilt=0.0, eid='QA.2357.SA1')
qa_2363_sa1 = Quadrupole(l=0.1137, k1=-0.5620550639, tilt=0.0, eid='QA.2363.SA1')
qa_2369_sa1 = Quadrupole(l=0.1137, k1=0.5620550639, tilt=0.0, eid='QA.2369.SA1')
qa_2375_sa1 = Quadrupole(l=0.1137, k1=-0.5620550639, tilt=0.0, eid='QA.2375.SA1')
qa_2381_sa1 = Quadrupole(l=0.1137, k1=0.5620550639, tilt=0.0, eid='QA.2381.SA1')
qa_2388_sa1 = Quadrupole(l=0.1137, k1=-0.5620550639, tilt=0.0, eid='QA.2388.SA1')
qa_2394_sa1 = Quadrupole(l=0.1137, k1=0.5620550639, tilt=0.0, eid='QA.2394.SA1')
qa_2400_sa1 = Quadrupole(l=0.1137, k1=-0.5620550639, tilt=0.0, eid='QA.2400.SA1')
qa_2406_sa1 = Quadrupole(l=0.1137, k1=0.5620550639, tilt=0.0, eid='QA.2406.SA1')
qa_2412_sa1 = Quadrupole(l=0.1137, k1=-0.5620550639, tilt=0.0, eid='QA.2412.SA1')
qa_2418_sa1 = Quadrupole(l=0.1137, k1=0.5620550639, tilt=0.0, eid='QA.2418.SA1')
qa_2424_sa1 = Quadrupole(l=0.1137, k1=-0.5620550639, tilt=0.0, eid='QA.2424.SA1')
qa_2430_sa1 = Quadrupole(l=0.1137, k1=0.5620550639, tilt=0.0, eid='QA.2430.SA1')
qa_2436_sa1 = Quadrupole(l=0.1137, k1=-0.5620550639, tilt=0.0, eid='QA.2436.SA1')
qa_2442_sa1 = Quadrupole(l=0.1137, k1=0.5620550639, tilt=0.0, eid='QA.2442.SA1')
qa_2449_sa1 = Quadrupole(l=0.1137, k1=-0.5620550639, tilt=0.0, eid='QA.2449.SA1')
qa_2455_sa1 = Quadrupole(l=0.1137, k1=0.5620550639, tilt=0.0, eid='QA.2455.SA1')
qa_2461_sa1 = Quadrupole(l=0.1137, k1=-0.5620550639, tilt=0.0, eid='QA.2461.SA1')
qe_2468_t4 = Quadrupole(l=0.24, k1=0.2237922517, tilt=0.0, eid='QE.2468.T4')
qe_2481_t4 = Quadrupole(l=0.24, k1=-0.2040914524, tilt=0.0, eid='QE.2481.T4')
qe_2493_t4 = Quadrupole(l=0.24, k1=0.2405963585, tilt=0.0, eid='QE.2493.T4')
qe_2506_t4 = Quadrupole(l=0.24, k1=-0.2306597606, tilt=0.0, eid='QE.2506.T4')
qe_2526_t4 = Quadrupole(l=0.24, k1=0.1922795516, tilt=0.0, eid='QE.2526.T4')
qe_2548_t4 = Quadrupole(l=0.24, k1=-0.1922795516, tilt=0.0, eid='QE.2548.T4')
qh_2567_t4 = Quadrupole(l=1.0291, k1=0.1965315532, tilt=0.0, eid='QH.2567.T4')
qh_2570_t4 = Quadrupole(l=1.0291, k1=-0.1965261383, tilt=0.0, eid='QH.2570.T4')
qh_2582_t4 = Quadrupole(l=1.0291, k1=0.2948896441, tilt=0.0, eid='QH.2582.T4')
qm_2587_t4 = Quadrupole(l=1.0597, k1=-0.2884660775, tilt=0.0, eid='QM.2587.T4')
qm_2592_t4 = Quadrupole(l=1.0597, k1=0.2882291454, tilt=0.0, eid='QM.2592.T4')
qm_2597_t4 = Quadrupole(l=1.0597, k1=-0.2884660775, tilt=0.0, eid='QM.2597.T4')
qm_2602_t4 = Quadrupole(l=1.0597, k1=0.2882291454, tilt=0.0, eid='QM.2602.T4')
qh_2607_t4 = Quadrupole(l=1.0291, k1=-0.2948267903, tilt=0.0, eid='QH.2607.T4')
qh_2618_t4 = Quadrupole(l=1.0291, k1=0.1965315532, tilt=0.0, eid='QH.2618.T4')
qh_2621_t4 = Quadrupole(l=1.0291, k1=-0.1965261383, tilt=0.0, eid='QH.2621.T4')
qe_2641_t4 = Quadrupole(l=0.24, k1=0.1922795516, tilt=0.0, eid='QE.2641.T4')
qe_2663_t4 = Quadrupole(l=0.24, k1=-0.1922795516, tilt=0.0, eid='QE.2663.T4')
qe_2685_t4 = Quadrupole(l=0.24, k1=0.1922795516, tilt=0.0, eid='QE.2685.T4')
qe_2707_t4 = Quadrupole(l=0.24, k1=-0.1922795516, tilt=0.0, eid='QE.2707.T4')
qe_2728_t4 = Quadrupole(l=0.24, k1=0.1922795516, tilt=0.0, eid='QE.2728.T4')
qf_2749_t4 = Quadrupole(l=0.5321, k1=-0.1156031519, tilt=0.0, eid='QF.2749.T4')
qf_2761_t4 = Quadrupole(l=0.5321, k1=0.1475390658, tilt=0.0, eid='QF.2761.T4')
qf_2773_t4 = Quadrupole(l=0.5321, k1=-0.1505125916, tilt=0.0, eid='QF.2773.T4')
qf_2785_t4 = Quadrupole(l=0.5321, k1=0.1836345346, tilt=0.0, eid='QF.2785.T4')
qa_2794_t4 = Quadrupole(l=0.1137, k1=-1.116577786, tilt=0.0, eid='QA.2794.T4')
qa_2800_t4 = Quadrupole(l=0.1137, k1=1.243898668, tilt=0.0, eid='QA.2800.T4')

# bending magnets 
bd_2079_t2 = RBend(l = 1.0, angle=0.0, e1=0.0, e2=0.0, gap=0, tilt=0, fint=0.0, fintx=0.0, eid='BD.2079.T2')
be_2584_t4 = SBend(l = 2.5, angle=0.0115035, e1=0.00575175, e2=0.00575175, gap=0, tilt=0.0, fint=0.0, fintx=0.0, eid='BE.2584.T4')
be_2604_t4 = SBend(l = 2.5, angle=0.0115035, e1=0.00575175, e2=0.00575175, gap=0, tilt=0.0, fint=0.0, fintx=0.0, eid='BE.2604.T4')

# correctors 
chy_1997_tl = Vcor(l=0.2, angle=0.0, eid='CHY.1997.TL')
chy_2004_tl = Vcor(l=0.2, angle=0.0, eid='CHY.2004.TL')
cfy_2010_tl = Vcor(l=0.1, angle=0.0, eid='CFY.2010.TL')
chx_2012_tl = Hcor(l=0.2, angle=0.0, eid='CHX.2012.TL')
chy_2012_tl = Vcor(l=0.2, angle=0.0, eid='CHY.2012.TL')
cnx_2021_tl = Hcor(l=0.3, angle=0.0, eid='CNX.2021.TL')
cny_2021_tl = Vcor(l=0.3, angle=0.0, eid='CNY.2021.TL')
cfx_2042_tl = Hcor(l=0.1, angle=0.0, eid='CFX.2042.TL')
chx_2054_tl = Hcor(l=0.2, angle=0.0, eid='CHX.2054.TL')
chy_2054_tl = Vcor(l=0.2, angle=0.0, eid='CHY.2054.TL')
cfx_2072_t2 = Hcor(l=0.1, angle=0.0, eid='CFX.2072.T2')
cfy_2087_t2 = Vcor(l=0.1, angle=0.0, eid='CFY.2087.T2')
cfx_2102_t2 = Hcor(l=0.1, angle=0.0, eid='CFX.2102.T2')
cfy_2117_t2 = Vcor(l=0.1, angle=0.0, eid='CFY.2117.T2')
cfx_2133_t2 = Hcor(l=0.1, angle=0.0, eid='CFX.2133.T2')
cfy_2146_t2 = Vcor(l=0.1, angle=0.0, eid='CFY.2146.T2')
cfx_2162_t2 = Hcor(l=0.1, angle=0.0, eid='CFX.2162.T2')
cfy_2177_t2 = Vcor(l=0.1, angle=0.0, eid='CFY.2177.T2')
cfx_2192_t2 = Hcor(l=0.1, angle=0.0, eid='CFX.2192.T2')
cfy_2207_t2 = Vcor(l=0.1, angle=0.0, eid='CFY.2207.T2')
cfx_2219_t2 = Hcor(l=0.1, angle=0.0, eid='CFX.2219.T2')
cny_2229_t2 = Vcor(l=0.3, angle=0.0, eid='CNY.2229.T2')
cex_2230_t2 = Hcor(l=0.1, angle=0.0, eid='CEX.2230.T2')
cny_2234_t2 = Vcor(l=0.3, angle=0.0, eid='CNY.2234.T2')
cex_2234_t2 = Hcor(l=0.1, angle=0.0, eid='CEX.2234.T2')
cux_2238_sa1 = Hcor(l=0.0, angle=0.0, eid='CUX.2238.SA1')
cux_2244_sa1 = Hcor(l=0.0, angle=0.0, eid='CUX.2244.SA1')
cax_2248_sa1 = Hcor(l=0.0, angle=0.0, eid='CAX.2248.SA1')
cay_2248_sa1 = Vcor(l=0.0, angle=0.0, eid='CAY.2248.SA1')
cbx_2253_sa1 = Hcor(l=0.0, angle=0.0, eid='CBX.2253.SA1')
cby_2253_sa1 = Vcor(l=0.0, angle=0.0, eid='CBY.2253.SA1')
cax_2254_sa1 = Hcor(l=0.0, angle=0.0, eid='CAX.2254.SA1')
cay_2254_sa1 = Vcor(l=0.0, angle=0.0, eid='CAY.2254.SA1')
cbx_2259_sa1 = Hcor(l=0.0, angle=0.0, eid='CBX.2259.SA1')
cby_2259_sa1 = Vcor(l=0.0, angle=0.0, eid='CBY.2259.SA1')
cax_2260_sa1 = Hcor(l=0.0, angle=0.0, eid='CAX.2260.SA1')
cay_2260_sa1 = Vcor(l=0.0, angle=0.0, eid='CAY.2260.SA1')
cbx_2265_sa1 = Hcor(l=0.0, angle=0.0, eid='CBX.2265.SA1')
cby_2265_sa1 = Vcor(l=0.0, angle=0.0, eid='CBY.2265.SA1')
cax_2267_sa1 = Hcor(l=0.0, angle=0.0, eid='CAX.2267.SA1')
cay_2267_sa1 = Vcor(l=0.0, angle=0.0, eid='CAY.2267.SA1')
cbx_2271_sa1 = Hcor(l=0.0, angle=0.0, eid='CBX.2271.SA1')
cby_2271_sa1 = Vcor(l=0.0, angle=0.0, eid='CBY.2271.SA1')
cax_2273_sa1 = Hcor(l=0.0, angle=0.0, eid='CAX.2273.SA1')
cay_2273_sa1 = Vcor(l=0.0, angle=0.0, eid='CAY.2273.SA1')
cbx_2277_sa1 = Hcor(l=0.0, angle=0.0, eid='CBX.2277.SA1')
cby_2277_sa1 = Vcor(l=0.0, angle=0.0, eid='CBY.2277.SA1')
cax_2279_sa1 = Hcor(l=0.0, angle=0.0, eid='CAX.2279.SA1')
cay_2279_sa1 = Vcor(l=0.0, angle=0.0, eid='CAY.2279.SA1')
cbx_2283_sa1 = Hcor(l=0.0, angle=0.0, eid='CBX.2283.SA1')
cby_2283_sa1 = Vcor(l=0.0, angle=0.0, eid='CBY.2283.SA1')
cax_2285_sa1 = Hcor(l=0.0, angle=0.0, eid='CAX.2285.SA1')
cay_2285_sa1 = Vcor(l=0.0, angle=0.0, eid='CAY.2285.SA1')
cbx_2289_sa1 = Hcor(l=0.0, angle=0.0, eid='CBX.2289.SA1')
cby_2289_sa1 = Vcor(l=0.0, angle=0.0, eid='CBY.2289.SA1')
cax_2291_sa1 = Hcor(l=0.0, angle=0.0, eid='CAX.2291.SA1')
cay_2291_sa1 = Vcor(l=0.0, angle=0.0, eid='CAY.2291.SA1')
cbx_2296_sa1 = Hcor(l=0.0, angle=0.0, eid='CBX.2296.SA1')
cby_2296_sa1 = Vcor(l=0.0, angle=0.0, eid='CBY.2296.SA1')
cax_2297_sa1 = Hcor(l=0.0, angle=0.0, eid='CAX.2297.SA1')
cay_2297_sa1 = Vcor(l=0.0, angle=0.0, eid='CAY.2297.SA1')
cbx_2302_sa1 = Hcor(l=0.0, angle=0.0, eid='CBX.2302.SA1')
cby_2302_sa1 = Vcor(l=0.0, angle=0.0, eid='CBY.2302.SA1')
cax_2303_sa1 = Hcor(l=0.0, angle=0.0, eid='CAX.2303.SA1')
cay_2303_sa1 = Vcor(l=0.0, angle=0.0, eid='CAY.2303.SA1')
cbx_2308_sa1 = Hcor(l=0.0, angle=0.0, eid='CBX.2308.SA1')
cby_2308_sa1 = Vcor(l=0.0, angle=0.0, eid='CBY.2308.SA1')
cax_2309_sa1 = Hcor(l=0.0, angle=0.0, eid='CAX.2309.SA1')
cay_2309_sa1 = Vcor(l=0.0, angle=0.0, eid='CAY.2309.SA1')
cbx_2314_sa1 = Hcor(l=0.0, angle=0.0, eid='CBX.2314.SA1')
cby_2314_sa1 = Vcor(l=0.0, angle=0.0, eid='CBY.2314.SA1')
cax_2315_sa1 = Hcor(l=0.0, angle=0.0, eid='CAX.2315.SA1')
cay_2315_sa1 = Vcor(l=0.0, angle=0.0, eid='CAY.2315.SA1')
cbx_2320_sa1 = Hcor(l=0.0, angle=0.0, eid='CBX.2320.SA1')
cby_2320_sa1 = Vcor(l=0.0, angle=0.0, eid='CBY.2320.SA1')
cax_2321_sa1 = Hcor(l=0.0, angle=0.0, eid='CAX.2321.SA1')
cay_2321_sa1 = Vcor(l=0.0, angle=0.0, eid='CAY.2321.SA1')
cbx_2326_sa1 = Hcor(l=0.0, angle=0.0, eid='CBX.2326.SA1')
cby_2326_sa1 = Vcor(l=0.0, angle=0.0, eid='CBY.2326.SA1')
cax_2328_sa1 = Hcor(l=0.0, angle=0.0, eid='CAX.2328.SA1')
cay_2328_sa1 = Vcor(l=0.0, angle=0.0, eid='CAY.2328.SA1')
cbx_2332_sa1 = Hcor(l=0.0, angle=0.0, eid='CBX.2332.SA1')
cby_2332_sa1 = Vcor(l=0.0, angle=0.0, eid='CBY.2332.SA1')
cax_2334_sa1 = Hcor(l=0.0, angle=0.0, eid='CAX.2334.SA1')
cay_2334_sa1 = Vcor(l=0.0, angle=0.0, eid='CAY.2334.SA1')
cbx_2338_sa1 = Hcor(l=0.0, angle=0.0, eid='CBX.2338.SA1')
cby_2338_sa1 = Vcor(l=0.0, angle=0.0, eid='CBY.2338.SA1')
cax_2340_sa1 = Hcor(l=0.0, angle=0.0, eid='CAX.2340.SA1')
cay_2340_sa1 = Vcor(l=0.0, angle=0.0, eid='CAY.2340.SA1')
cbx_2344_sa1 = Hcor(l=0.0, angle=0.0, eid='CBX.2344.SA1')
cby_2344_sa1 = Vcor(l=0.0, angle=0.0, eid='CBY.2344.SA1')
cax_2346_sa1 = Hcor(l=0.0, angle=0.0, eid='CAX.2346.SA1')
cay_2346_sa1 = Vcor(l=0.0, angle=0.0, eid='CAY.2346.SA1')
cbx_2350_sa1 = Hcor(l=0.0, angle=0.0, eid='CBX.2350.SA1')
cby_2350_sa1 = Vcor(l=0.0, angle=0.0, eid='CBY.2350.SA1')
cax_2352_sa1 = Hcor(l=0.0, angle=0.0, eid='CAX.2352.SA1')
cay_2352_sa1 = Vcor(l=0.0, angle=0.0, eid='CAY.2352.SA1')
cbx_2357_sa1 = Hcor(l=0.0, angle=0.0, eid='CBX.2357.SA1')
cby_2357_sa1 = Vcor(l=0.0, angle=0.0, eid='CBY.2357.SA1')
cax_2358_sa1 = Hcor(l=0.0, angle=0.0, eid='CAX.2358.SA1')
cay_2358_sa1 = Vcor(l=0.0, angle=0.0, eid='CAY.2358.SA1')
cbx_2363_sa1 = Hcor(l=0.0, angle=0.0, eid='CBX.2363.SA1')
cby_2363_sa1 = Vcor(l=0.0, angle=0.0, eid='CBY.2363.SA1')
cax_2364_sa1 = Hcor(l=0.0, angle=0.0, eid='CAX.2364.SA1')
cay_2364_sa1 = Vcor(l=0.0, angle=0.0, eid='CAY.2364.SA1')
cbx_2369_sa1 = Hcor(l=0.0, angle=0.0, eid='CBX.2369.SA1')
cby_2369_sa1 = Vcor(l=0.0, angle=0.0, eid='CBY.2369.SA1')
cax_2370_sa1 = Hcor(l=0.0, angle=0.0, eid='CAX.2370.SA1')
cay_2370_sa1 = Vcor(l=0.0, angle=0.0, eid='CAY.2370.SA1')
cbx_2375_sa1 = Hcor(l=0.0, angle=0.0, eid='CBX.2375.SA1')
cby_2375_sa1 = Vcor(l=0.0, angle=0.0, eid='CBY.2375.SA1')
cax_2376_sa1 = Hcor(l=0.0, angle=0.0, eid='CAX.2376.SA1')
cay_2376_sa1 = Vcor(l=0.0, angle=0.0, eid='CAY.2376.SA1')
cbx_2381_sa1 = Hcor(l=0.0, angle=0.0, eid='CBX.2381.SA1')
cby_2381_sa1 = Vcor(l=0.0, angle=0.0, eid='CBY.2381.SA1')
cax_2382_sa1 = Hcor(l=0.0, angle=0.0, eid='CAX.2382.SA1')
cay_2382_sa1 = Vcor(l=0.0, angle=0.0, eid='CAY.2382.SA1')
cbx_2387_sa1 = Hcor(l=0.0, angle=0.0, eid='CBX.2387.SA1')
cby_2387_sa1 = Vcor(l=0.0, angle=0.0, eid='CBY.2387.SA1')
cax_2389_sa1 = Hcor(l=0.0, angle=0.0, eid='CAX.2389.SA1')
cay_2389_sa1 = Vcor(l=0.0, angle=0.0, eid='CAY.2389.SA1')
cbx_2393_sa1 = Hcor(l=0.0, angle=0.0, eid='CBX.2393.SA1')
cby_2393_sa1 = Vcor(l=0.0, angle=0.0, eid='CBY.2393.SA1')
cax_2395_sa1 = Hcor(l=0.0, angle=0.0, eid='CAX.2395.SA1')
cay_2395_sa1 = Vcor(l=0.0, angle=0.0, eid='CAY.2395.SA1')
cbx_2399_sa1 = Hcor(l=0.0, angle=0.0, eid='CBX.2399.SA1')
cby_2399_sa1 = Vcor(l=0.0, angle=0.0, eid='CBY.2399.SA1')
cax_2401_sa1 = Hcor(l=0.0, angle=0.0, eid='CAX.2401.SA1')
cay_2401_sa1 = Vcor(l=0.0, angle=0.0, eid='CAY.2401.SA1')
cbx_2405_sa1 = Hcor(l=0.0, angle=0.0, eid='CBX.2405.SA1')
cby_2405_sa1 = Vcor(l=0.0, angle=0.0, eid='CBY.2405.SA1')
cax_2407_sa1 = Hcor(l=0.0, angle=0.0, eid='CAX.2407.SA1')
cay_2407_sa1 = Vcor(l=0.0, angle=0.0, eid='CAY.2407.SA1')
cbx_2411_sa1 = Hcor(l=0.0, angle=0.0, eid='CBX.2411.SA1')
cby_2411_sa1 = Vcor(l=0.0, angle=0.0, eid='CBY.2411.SA1')
cax_2413_sa1 = Hcor(l=0.0, angle=0.0, eid='CAX.2413.SA1')
cay_2413_sa1 = Vcor(l=0.0, angle=0.0, eid='CAY.2413.SA1')
cbx_2418_sa1 = Hcor(l=0.0, angle=0.0, eid='CBX.2418.SA1')
cby_2418_sa1 = Vcor(l=0.0, angle=0.0, eid='CBY.2418.SA1')
cax_2419_sa1 = Hcor(l=0.0, angle=0.0, eid='CAX.2419.SA1')
cay_2419_sa1 = Vcor(l=0.0, angle=0.0, eid='CAY.2419.SA1')
cbx_2424_sa1 = Hcor(l=0.0, angle=0.0, eid='CBX.2424.SA1')
cby_2424_sa1 = Vcor(l=0.0, angle=0.0, eid='CBY.2424.SA1')
cax_2425_sa1 = Hcor(l=0.0, angle=0.0, eid='CAX.2425.SA1')
cay_2425_sa1 = Vcor(l=0.0, angle=0.0, eid='CAY.2425.SA1')
cbx_2430_sa1 = Hcor(l=0.0, angle=0.0, eid='CBX.2430.SA1')
cby_2430_sa1 = Vcor(l=0.0, angle=0.0, eid='CBY.2430.SA1')
cax_2431_sa1 = Hcor(l=0.0, angle=0.0, eid='CAX.2431.SA1')
cay_2431_sa1 = Vcor(l=0.0, angle=0.0, eid='CAY.2431.SA1')
cbx_2436_sa1 = Hcor(l=0.0, angle=0.0, eid='CBX.2436.SA1')
cby_2436_sa1 = Vcor(l=0.0, angle=0.0, eid='CBY.2436.SA1')
cax_2437_sa1 = Hcor(l=0.0, angle=0.0, eid='CAX.2437.SA1')
cay_2437_sa1 = Vcor(l=0.0, angle=0.0, eid='CAY.2437.SA1')
cbx_2442_sa1 = Hcor(l=0.0, angle=0.0, eid='CBX.2442.SA1')
cby_2442_sa1 = Vcor(l=0.0, angle=0.0, eid='CBY.2442.SA1')
cax_2443_sa1 = Hcor(l=0.0, angle=0.0, eid='CAX.2443.SA1')
cay_2443_sa1 = Vcor(l=0.0, angle=0.0, eid='CAY.2443.SA1')
cbx_2448_sa1 = Hcor(l=0.0, angle=0.0, eid='CBX.2448.SA1')
cby_2448_sa1 = Vcor(l=0.0, angle=0.0, eid='CBY.2448.SA1')
cax_2450_sa1 = Hcor(l=0.0, angle=0.0, eid='CAX.2450.SA1')
cay_2450_sa1 = Vcor(l=0.0, angle=0.0, eid='CAY.2450.SA1')
cbx_2454_sa1 = Hcor(l=0.0, angle=0.0, eid='CBX.2454.SA1')
cby_2454_sa1 = Vcor(l=0.0, angle=0.0, eid='CBY.2454.SA1')
cax_2456_sa1 = Hcor(l=0.0, angle=0.0, eid='CAX.2456.SA1')
cay_2456_sa1 = Vcor(l=0.0, angle=0.0, eid='CAY.2456.SA1')
cbx_2460_sa1 = Hcor(l=0.0, angle=0.0, eid='CBX.2460.SA1')
cby_2460_sa1 = Vcor(l=0.0, angle=0.0, eid='CBY.2460.SA1')




cex_2469_t4 = Hcor(l=0.1, angle=0.0, eid='CEX.2469.T4')
cey_2481_t4 = Vcor(l=0.1, angle=0.0, eid='CEY.2481.T4')
cex_2494_t4 = Hcor(l=0.1, angle=0.0, eid='CEX.2494.T4')
cey_2506_t4 = Vcor(l=0.1, angle=0.0, eid='CEY.2506.T4')
cex_2526_t4 = Hcor(l=0.1, angle=0.0, eid='CEX.2526.T4')
cey_2548_t4 = Vcor(l=0.1, angle=0.0, eid='CEY.2548.T4')
chx_2568_t4 = Hcor(l=0.2, angle=0.0, eid='CHX.2568.T4')
chy_2571_t4 = Vcor(l=0.2, angle=0.0, eid='CHY.2571.T4')
chx_2581_t4 = Hcor(l=0.2, angle=0.0, eid='CHX.2581.T4')
chy_2581_t4 = Vcor(l=0.2, angle=0.0, eid='CHY.2581.T4')
chx_2593_t4 = Hcor(l=0.2, angle=0.0, eid='CHX.2593.T4')
chy_2598_t4 = Vcor(l=0.2, angle=0.0, eid='CHY.2598.T4')
chx_2601_t4 = Hcor(l=0.2, angle=0.0, eid='CHX.2601.T4')
chy_2608_t4 = Vcor(l=0.2, angle=0.0, eid='CHY.2608.T4')
chx_2619_t4 = Hcor(l=0.2, angle=0.0, eid='CHX.2619.T4')
chy_2622_t4 = Vcor(l=0.2, angle=0.0, eid='CHY.2622.T4')
cex_2642_t4 = Hcor(l=0.1, angle=0.0, eid='CEX.2642.T4')
cey_2663_t4 = Vcor(l=0.1, angle=0.0, eid='CEY.2663.T4')
cex_2685_t4 = Hcor(l=0.1, angle=0.0, eid='CEX.2685.T4')
cey_2707_t4 = Vcor(l=0.1, angle=0.0, eid='CEY.2707.T4')
cex_2729_t4 = Hcor(l=0.1, angle=0.0, eid='CEX.2729.T4')
cfy_2750_t4 = Vcor(l=0.1, angle=0.0, eid='CFY.2750.T4')
cfx_2762_t4 = Hcor(l=0.1, angle=0.0, eid='CFX.2762.T4')
cfy_2774_t4 = Vcor(l=0.1, angle=0.0, eid='CFY.2774.T4')
cfx_2786_t4 = Hcor(l=0.1, angle=0.0, eid='CFX.2786.T4')
cny_2794_t4 = Vcor(l=0.3, angle=0.0, eid='CNY.2794.T4')
cex_2795_t4 = Hcor(l=0.1, angle=0.0, eid='CEX.2795.T4')
cny_2799_t4 = Vcor(l=0.3, angle=0.0, eid='CNY.2799.T4')
cex_2799_t4 = Hcor(l=0.1, angle=0.0, eid='CEX.2799.T4')

# markers 
stsub_1980_tl = Marker(eid='STSUB.1980.TL')
ensub_1997_tl = Marker(eid='ENSUB.1997.TL')
stsub_1997_tl = Marker(eid='STSUB.1997.TL')
tora_2011_tl = Marker(eid='TORA.2011.TL')
otre_2023_tl = Marker(eid='OTRE.2023.TL')
ensub_2025_tl = Marker(eid='ENSUB.2025.TL')
stsub_2025_tl = Marker(eid='STSUB.2025.TL')
ensub_2058_tl = Marker(eid='ENSUB.2058.TL')
ensec_2058_tl = Marker(eid='ENSEC.2058.TL')
stsec_2058_t2 = Marker(eid='STSEC.2058.T2')
otrb_2169_t2 = Marker(eid='OTRB.2169.T2')
otrb_2199_t2 = Marker(eid='OTRB.2199.T2')
otrb_2212_t2 = Marker(eid='OTRB.2212.T2')
tora_2228_t2 = Marker(eid='TORA.2228.T2')
ensec_2235_t2 = Marker(eid='ENSEC.2235.T2')
stsec_2235_sa1 = Marker(eid='STSEC.2235.SA1')
match_2247_sa1 = Marker(eid='MATCH.2247.SA1')
ensec_2461_sa1 = Marker(eid='ENSEC.2461.SA1')
stsec_2461_t4 = Marker(eid='STSEC.2461.T4')
stsub_2461_t4 = Marker(eid='STSUB.2461.T4')
tora_2462_t4 = Marker(eid='TORA.2462.T4')
ensub_2583_t4 = Marker(eid='ENSUB.2583.T4')
stsub_2583_t4 = Marker(eid='STSUB.2583.T4')
otrbw_2718_t4 = Marker(eid='OTRBW.2718.T4')
otrbw_2755_t4 = Marker(eid='OTRBW.2755.T4')
otrbw_2779_t4 = Marker(eid='OTRBW.2779.T4')
tora_2793_t4 = Marker(eid='TORA.2793.T4')
ensub_2800_t4 = Marker(eid='ENSUB.2800.T4')

# monitor 
bpma_1995_tl = Monitor(eid='BPMA.1995.TL')
bpma_2011_tl = Monitor(eid='BPMA.2011.TL')
bpmd_2022_tl = Monitor(eid='BPMD.2022.TL')
bpma_2041_tl = Monitor(eid='BPMA.2041.TL')
bpma_2054_tl = Monitor(eid='BPMA.2054.TL')
bpma_2071_t2 = Monitor(eid='BPMA.2071.T2')
bpma_2086_t2 = Monitor(eid='BPMA.2086.T2')
bpma_2101_t2 = Monitor(eid='BPMA.2101.T2')
bpma_2116_t2 = Monitor(eid='BPMA.2116.T2')
bpma_2132_t2 = Monitor(eid='BPMA.2132.T2')
bpma_2145_t2 = Monitor(eid='BPMA.2145.T2')
bpma_2161_t2 = Monitor(eid='BPMA.2161.T2')
bpma_2176_t2 = Monitor(eid='BPMA.2176.T2')
bpma_2191_t2 = Monitor(eid='BPMA.2191.T2')
bpma_2206_t2 = Monitor(eid='BPMA.2206.T2')
bpma_2218_t2 = Monitor(eid='BPMA.2218.T2')
bpme_2229_t2 = Monitor(eid='BPME.2229.T2')
bpme_2235_t2 = Monitor(eid='BPME.2235.T2')
bpme_2241_sa1 = Monitor(eid='BPME.2241.SA1')
bpme_2247_sa1 = Monitor(eid='BPME.2247.SA1')
bpme_2253_sa1 = Monitor(eid='BPME.2253.SA1')
bpme_2259_sa1 = Monitor(eid='BPME.2259.SA1')
bpme_2265_sa1 = Monitor(eid='BPME.2265.SA1')
bpme_2271_sa1 = Monitor(eid='BPME.2271.SA1')
bpme_2278_sa1 = Monitor(eid='BPME.2278.SA1')
bpme_2284_sa1 = Monitor(eid='BPME.2284.SA1')
bpme_2290_sa1 = Monitor(eid='BPME.2290.SA1')
bpme_2296_sa1 = Monitor(eid='BPME.2296.SA1')
bpme_2302_sa1 = Monitor(eid='BPME.2302.SA1')
bpme_2308_sa1 = Monitor(eid='BPME.2308.SA1')
bpme_2314_sa1 = Monitor(eid='BPME.2314.SA1')
bpme_2320_sa1 = Monitor(eid='BPME.2320.SA1')
bpme_2326_sa1 = Monitor(eid='BPME.2326.SA1')
bpme_2332_sa1 = Monitor(eid='BPME.2332.SA1')
bpme_2339_sa1 = Monitor(eid='BPME.2339.SA1')
bpme_2345_sa1 = Monitor(eid='BPME.2345.SA1')
bpme_2351_sa1 = Monitor(eid='BPME.2351.SA1')
bpme_2357_sa1 = Monitor(eid='BPME.2357.SA1')
bpme_2363_sa1 = Monitor(eid='BPME.2363.SA1')
bpme_2369_sa1 = Monitor(eid='BPME.2369.SA1')
bpme_2375_sa1 = Monitor(eid='BPME.2375.SA1')
bpme_2381_sa1 = Monitor(eid='BPME.2381.SA1')
bpme_2387_sa1 = Monitor(eid='BPME.2387.SA1')
bpme_2393_sa1 = Monitor(eid='BPME.2393.SA1')
bpme_2400_sa1 = Monitor(eid='BPME.2400.SA1')
bpme_2406_sa1 = Monitor(eid='BPME.2406.SA1')
bpme_2412_sa1 = Monitor(eid='BPME.2412.SA1')
bpme_2418_sa1 = Monitor(eid='BPME.2418.SA1')
bpme_2424_sa1 = Monitor(eid='BPME.2424.SA1')
bpme_2430_sa1 = Monitor(eid='BPME.2430.SA1')
bpme_2436_sa1 = Monitor(eid='BPME.2436.SA1')
bpme_2442_sa1 = Monitor(eid='BPME.2442.SA1')
bpme_2448_sa1 = Monitor(eid='BPME.2448.SA1')
bpme_2454_sa1 = Monitor(eid='BPME.2454.SA1')
bpme_2461_sa1 = Monitor(eid='BPME.2461.SA1')



bpma_2468_t4 = Monitor(eid='BPMA.2468.T4')
bpma_2481_t4 = Monitor(eid='BPMA.2481.T4')
bpma_2493_t4 = Monitor(eid='BPMA.2493.T4')
bpma_2506_t4 = Monitor(eid='BPMA.2506.T4')
bpma_2525_t4 = Monitor(eid='BPMA.2525.T4')
bpma_2547_t4 = Monitor(eid='BPMA.2547.T4')
bpma_2567_t4 = Monitor(eid='BPMA.2567.T4')
bpma_2570_t4 = Monitor(eid='BPMA.2570.T4')
bpma_2581_t4 = Monitor(eid='BPMA.2581.T4')
bpma_2591_t4 = Monitor(eid='BPMA.2591.T4')
bpma_2596_t4 = Monitor(eid='BPMA.2596.T4')
bpma_2601_t4 = Monitor(eid='BPMA.2601.T4')
bpma_2606_t4 = Monitor(eid='BPMA.2606.T4')
bpma_2618_t4 = Monitor(eid='BPMA.2618.T4')
bpma_2621_t4 = Monitor(eid='BPMA.2621.T4')
bpma_2641_t4 = Monitor(eid='BPMA.2641.T4')
bpma_2663_t4 = Monitor(eid='BPMA.2663.T4')
bpma_2684_t4 = Monitor(eid='BPMA.2684.T4')
bpma_2706_t4 = Monitor(eid='BPMA.2706.T4')
bpma_2728_t4 = Monitor(eid='BPMA.2728.T4')
bpma_2749_t4 = Monitor(eid='BPMA.2749.T4')
bpma_2761_t4 = Monitor(eid='BPMA.2761.T4')
bpma_2773_t4 = Monitor(eid='BPMA.2773.T4')
bpma_2785_t4 = Monitor(eid='BPMA.2785.T4')
bpme_2794_t4 = Monitor(eid='BPME.2794.T4')
bpme_2800_t4 = Monitor(eid='BPME.2800.T4')

# sextupoles 
saox_2594_t4 = Sextupole(l=0.3164, k2=23.92225032, tilt=0.0, eid='SAOX.2594.T4')
saox_2599_t4 = Sextupole(l=0.3164, k2=8.44816687700063, tilt=0.0, eid='SAOX.2599.T4')

# octupole 

# undulator 
u40s_2232_t2 = Undulator(lperiod=0.04, nperiods=3, Kx=0.0, Ky=0.0, eid='U40S.2232.T2')
u40_2250_sa1 = Undulator(lperiod=0.04, nperiods=125, Kx=0.0, Ky=0.0, eid='U40.2250.SA1')
u40_2256_sa1 = Undulator(lperiod=0.04, nperiods=125, Kx=0.0, Ky=0.0, eid='U40.2256.SA1')
u40_2262_sa1 = Undulator(lperiod=0.04, nperiods=125, Kx=0.0, Ky=0.0, eid='U40.2262.SA1')
u40_2269_sa1 = Undulator(lperiod=0.04, nperiods=125, Kx=0.0, Ky=0.0, eid='U40.2269.SA1')
u40_2275_sa1 = Undulator(lperiod=0.04, nperiods=125, Kx=0.0, Ky=0.0, eid='U40.2275.SA1')
u40_2281_sa1 = Undulator(lperiod=0.04, nperiods=125, Kx=0.0, Ky=0.0, eid='U40.2281.SA1')
u40_2287_sa1 = Undulator(lperiod=0.04, nperiods=125, Kx=0.0, Ky=0.0, eid='U40.2287.SA1')
u40_2293_sa1 = Undulator(lperiod=0.04, nperiods=125, Kx=0.0, Ky=0.0, eid='U40.2293.SA1')
u40_2299_sa1 = Undulator(lperiod=0.04, nperiods=125, Kx=0.0, Ky=0.0, eid='U40.2299.SA1')
u40_2305_sa1 = Undulator(lperiod=0.04, nperiods=125, Kx=0.0, Ky=0.0, eid='U40.2305.SA1')
u40_2311_sa1 = Undulator(lperiod=0.04, nperiods=125, Kx=0.0, Ky=0.0, eid='U40.2311.SA1')
u40_2317_sa1 = Undulator(lperiod=0.04, nperiods=125, Kx=0.0, Ky=0.0, eid='U40.2317.SA1')
u40_2323_sa1 = Undulator(lperiod=0.04, nperiods=125, Kx=0.0, Ky=0.0, eid='U40.2323.SA1')
u40_2330_sa1 = Undulator(lperiod=0.04, nperiods=125, Kx=0.0, Ky=0.0, eid='U40.2330.SA1')
u40_2336_sa1 = Undulator(lperiod=0.04, nperiods=125, Kx=0.0, Ky=0.0, eid='U40.2336.SA1')
u40_2342_sa1 = Undulator(lperiod=0.04, nperiods=125, Kx=0.0, Ky=0.0, eid='U40.2342.SA1')
u40_2348_sa1 = Undulator(lperiod=0.04, nperiods=125, Kx=0.0, Ky=0.0, eid='U40.2348.SA1')
u40_2354_sa1 = Undulator(lperiod=0.04, nperiods=125, Kx=0.0, Ky=0.0, eid='U40.2354.SA1')
u40_2360_sa1 = Undulator(lperiod=0.04, nperiods=125, Kx=0.0, Ky=0.0, eid='U40.2360.SA1')
u40_2366_sa1 = Undulator(lperiod=0.04, nperiods=125, Kx=0.0, Ky=0.0, eid='U40.2366.SA1')
u40_2372_sa1 = Undulator(lperiod=0.04, nperiods=125, Kx=0.0, Ky=0.0, eid='U40.2372.SA1')
u40_2378_sa1 = Undulator(lperiod=0.04, nperiods=125, Kx=0.0, Ky=0.0, eid='U40.2378.SA1')
u40_2384_sa1 = Undulator(lperiod=0.04, nperiods=125, Kx=0.0, Ky=0.0, eid='U40.2384.SA1')
u40_2391_sa1 = Undulator(lperiod=0.04, nperiods=125, Kx=0.0, Ky=0.0, eid='U40.2391.SA1')
u40_2397_sa1 = Undulator(lperiod=0.04, nperiods=125, Kx=0.0, Ky=0.0, eid='U40.2397.SA1')
u40_2403_sa1 = Undulator(lperiod=0.04, nperiods=125, Kx=0.0, Ky=0.0, eid='U40.2403.SA1')
u40_2409_sa1 = Undulator(lperiod=0.04, nperiods=125, Kx=0.0, Ky=0.0, eid='U40.2409.SA1')
u40_2415_sa1 = Undulator(lperiod=0.04, nperiods=125, Kx=0.0, Ky=0.0, eid='U40.2415.SA1')
u40_2421_sa1 = Undulator(lperiod=0.04, nperiods=125, Kx=0.0, Ky=0.0, eid='U40.2421.SA1')
u40_2427_sa1 = Undulator(lperiod=0.04, nperiods=125, Kx=0.0, Ky=0.0, eid='U40.2427.SA1')
u40_2433_sa1 = Undulator(lperiod=0.04, nperiods=125, Kx=0.0, Ky=0.0, eid='U40.2433.SA1')
u40_2439_sa1 = Undulator(lperiod=0.04, nperiods=125, Kx=0.0, Ky=0.0, eid='U40.2439.SA1')
u40_2445_sa1 = Undulator(lperiod=0.04, nperiods=125, Kx=0.0, Ky=0.0, eid='U40.2445.SA1')
u40_2452_sa1 = Undulator(lperiod=0.04, nperiods=125, Kx=0.0, Ky=0.0, eid='U40.2452.SA1')
u40_2458_sa1 = Undulator(lperiod=0.04, nperiods=125, Kx=0.0, Ky=0.0, eid='U40.2458.SA1')
u40s_2797_t4 = Undulator(lperiod=0.04, nperiods=3, Kx=0.0, Ky=0.0, eid='U40S.2797.T4')

# cavity 

# UnknowElement 

# Matrices 

# Solenoids 

# lattice 
cell_sase1 = (stsub_1980_tl, d_1, qk_1982_tl, d_2, bpma_1995_tl, d_3, qf_1997_tl,
d_4, chy_1997_tl, ensub_1997_tl, stsub_1997_tl, d_5, chy_2004_tl, d_6, cfy_2010_tl, 
d_7, tora_2011_tl, d_8, bpma_2011_tl, d_9, qf_2012_tl, d_10, chx_2012_tl, 
d_11, chy_2012_tl, d_12, cnx_2021_tl, d_13, cny_2021_tl, d_14, bpmd_2022_tl, 
d_11, otre_2023_tl, d_16, ensub_2025_tl, stsub_2025_tl, d_1, qk_2027_tl, d_18, 
bpma_2041_tl, d_9, qf_2042_tl, d_10, cfx_2042_tl, d_21, chx_2054_tl, d_22, 
chy_2054_tl, d_23, bpma_2054_tl, d_24, qk_2057_tl, d_25, ensub_2058_tl, ensec_2058_tl, 
stsec_2058_t2, d_26, bpma_2071_t2, d_27, qf_2072_t2, d_4, cfx_2072_t2, d_29, 
bd_2079_t2, d_30, bpma_2086_t2, d_27, qf_2087_t2, d_4, cfy_2087_t2, d_33, 
bpma_2101_t2, d_27, qf_2102_t2, d_4, cfx_2102_t2, d_36, bpma_2116_t2, d_27, 
qf_2117_t2, d_4, cfy_2117_t2, d_39, bpma_2132_t2, d_27, qf_2132_t2, d_4, 
cfx_2133_t2, d_42, bpma_2145_t2, d_27, qf_2145_t2, d_4, cfy_2146_t2, d_45, 
bpma_2161_t2, d_27, qf_2162_t2, d_4, cfx_2162_t2, d_48, otrb_2169_t2, d_49, 
bpma_2176_t2, d_27, qf_2177_t2, d_4, cfy_2177_t2, d_33, bpma_2191_t2, d_27, 
qf_2192_t2, d_4, cfx_2192_t2, d_48, otrb_2199_t2, d_49, bpma_2206_t2, d_27, 
qf_2207_t2, d_4, cfy_2207_t2, d_59, otrb_2212_t2, d_60, bpma_2218_t2, d_27, 
qf_2218_t2, d_4, cfx_2219_t2, d_63, tora_2228_t2, d_64, bpme_2229_t2, d_65, 
qa_2229_t2, d_66, cny_2229_t2, d_67, cex_2230_t2, d_68, u40s_2232_t2, d_69, 
cny_2234_t2, d_70, cex_2234_t2, d_71, bpme_2235_t2, d_72, qa_2235_t2, d_73, 
ensec_2235_t2, stsec_2235_sa1, d_74, cux_2238_sa1, d_75, bpme_2241_sa1, d_72, qa_2241_sa1, 
d_77, cux_2244_sa1, d_75, bpme_2247_sa1, d_72, qa_2247_sa1, d_73, match_2247_sa1, 
d_81, cax_2248_sa1, cay_2248_sa1, d_82, u40_2250_sa1, d_83, cbx_2253_sa1, cby_2253_sa1, 
d_84, bpme_2253_sa1, d_72, qa_2253_sa1, d_86, cax_2254_sa1, cay_2254_sa1, d_82, 
u40_2256_sa1, d_83, cbx_2259_sa1, cby_2259_sa1, d_84, bpme_2259_sa1, d_72, qa_2259_sa1, 
d_86, cax_2260_sa1, cay_2260_sa1, d_82, u40_2262_sa1, d_83, cbx_2265_sa1, cby_2265_sa1, 
d_84, bpme_2265_sa1, d_72, qa_2266_sa1, d_86, cax_2267_sa1, cay_2267_sa1, d_82, 
u40_2269_sa1, d_83, cbx_2271_sa1, cby_2271_sa1, d_84, bpme_2271_sa1, d_72, qa_2272_sa1, 
d_86, cax_2273_sa1, cay_2273_sa1, d_82, u40_2275_sa1, d_83, cbx_2277_sa1, cby_2277_sa1, 
d_84, bpme_2278_sa1, d_72, qa_2278_sa1, d_86, cax_2279_sa1, cay_2279_sa1, d_82, 
u40_2281_sa1, d_83, cbx_2283_sa1, cby_2283_sa1, d_84, bpme_2284_sa1, d_72, qa_2284_sa1, 
d_86, cax_2285_sa1, cay_2285_sa1, d_82, u40_2287_sa1, d_83, cbx_2289_sa1, cby_2289_sa1, 
d_84, bpme_2290_sa1, d_72, qa_2290_sa1, d_86, cax_2291_sa1, cay_2291_sa1, d_82, 
u40_2293_sa1, d_83, cbx_2296_sa1, cby_2296_sa1, d_84, bpme_2296_sa1, d_72, qa_2296_sa1, 
d_86, cax_2297_sa1, cay_2297_sa1, d_82, u40_2299_sa1, d_83, cbx_2302_sa1, cby_2302_sa1, 
d_84, bpme_2302_sa1, d_72, qa_2302_sa1, d_86, cax_2303_sa1, cay_2303_sa1, d_82, 
u40_2305_sa1, d_83, cbx_2308_sa1, cby_2308_sa1, d_84, bpme_2308_sa1, d_72, qa_2308_sa1, 
d_86, cax_2309_sa1, cay_2309_sa1, d_82, u40_2311_sa1, d_83, cbx_2314_sa1, cby_2314_sa1, 
d_84, bpme_2314_sa1, d_72, qa_2314_sa1, d_86, cax_2315_sa1, cay_2315_sa1, d_82, 
u40_2317_sa1, d_83, cbx_2320_sa1, cby_2320_sa1, d_84, bpme_2320_sa1, d_72, qa_2320_sa1, 
d_86, cax_2321_sa1, cay_2321_sa1, d_82, u40_2323_sa1, d_83, cbx_2326_sa1, cby_2326_sa1, 
d_84, bpme_2326_sa1, d_72, qa_2327_sa1, d_86, cax_2328_sa1, cay_2328_sa1, d_82, 
u40_2330_sa1, d_83, cbx_2332_sa1, cby_2332_sa1, d_84, bpme_2332_sa1, d_72, qa_2333_sa1, 
d_86, cax_2334_sa1, cay_2334_sa1, d_82, u40_2336_sa1, d_83, cbx_2338_sa1, cby_2338_sa1, 
d_84, bpme_2339_sa1, d_72, qa_2339_sa1, d_86, cax_2340_sa1, cay_2340_sa1, d_82, 
u40_2342_sa1, d_83, cbx_2344_sa1, cby_2344_sa1, d_84, bpme_2345_sa1, d_72, qa_2345_sa1, 
d_86, cax_2346_sa1, cay_2346_sa1, d_82, u40_2348_sa1, d_83, cbx_2350_sa1, cby_2350_sa1, 
d_84, bpme_2351_sa1, d_72, qa_2351_sa1, d_86, cax_2352_sa1, cay_2352_sa1, d_82, 
u40_2354_sa1, d_83, cbx_2357_sa1, cby_2357_sa1, d_84, bpme_2357_sa1, d_72, qa_2357_sa1, 
d_86, cax_2358_sa1, cay_2358_sa1, d_82, u40_2360_sa1, d_83, cbx_2363_sa1, cby_2363_sa1, 
d_84, bpme_2363_sa1, d_72, qa_2363_sa1, d_86, cax_2364_sa1, cay_2364_sa1, d_82, 
u40_2366_sa1, d_83, cbx_2369_sa1, cby_2369_sa1, d_84, bpme_2369_sa1, d_72, qa_2369_sa1, 
d_86, cax_2370_sa1, cay_2370_sa1, d_82, u40_2372_sa1, d_83, cbx_2375_sa1, cby_2375_sa1, 
d_84, bpme_2375_sa1, d_72, qa_2375_sa1, d_86, cax_2376_sa1, cay_2376_sa1, d_82, 
u40_2378_sa1, d_83, cbx_2381_sa1, cby_2381_sa1, d_84, bpme_2381_sa1, d_72, qa_2381_sa1, 
d_86, cax_2382_sa1, cay_2382_sa1, d_82, u40_2384_sa1, d_83, cbx_2387_sa1, cby_2387_sa1, 
d_84, bpme_2387_sa1, d_72, qa_2388_sa1, d_86, cax_2389_sa1, cay_2389_sa1, d_82, 
u40_2391_sa1, d_83, cbx_2393_sa1, cby_2393_sa1, d_84, bpme_2393_sa1, d_72, qa_2394_sa1, 
d_86, cax_2395_sa1, cay_2395_sa1, d_82, u40_2397_sa1, d_83, cbx_2399_sa1, cby_2399_sa1, 
d_84, bpme_2400_sa1, d_72, qa_2400_sa1, d_86, cax_2401_sa1, cay_2401_sa1, d_82, 
u40_2403_sa1, d_83, cbx_2405_sa1, cby_2405_sa1, d_84, bpme_2406_sa1, d_72, qa_2406_sa1, 
d_86, cax_2407_sa1, cay_2407_sa1, d_82, u40_2409_sa1, d_83, cbx_2411_sa1, cby_2411_sa1, 
d_84, bpme_2412_sa1, d_72, qa_2412_sa1, d_86, cax_2413_sa1, cay_2413_sa1, d_82, 
u40_2415_sa1, d_83, cbx_2418_sa1, cby_2418_sa1, d_84, bpme_2418_sa1, d_72, qa_2418_sa1, 
d_86, cax_2419_sa1, cay_2419_sa1, d_82, u40_2421_sa1, d_83, cbx_2424_sa1, cby_2424_sa1, 
d_84, bpme_2424_sa1, d_72, qa_2424_sa1, d_86, cax_2425_sa1, cay_2425_sa1, d_82, 
u40_2427_sa1, d_83, cbx_2430_sa1, cby_2430_sa1, d_84, bpme_2430_sa1, d_72, qa_2430_sa1, 
d_86, cax_2431_sa1, cay_2431_sa1, d_82, u40_2433_sa1, d_83, cbx_2436_sa1, cby_2436_sa1, 
d_84, bpme_2436_sa1, d_72, qa_2436_sa1, d_86, cax_2437_sa1, cay_2437_sa1, d_82, 
u40_2439_sa1, d_83, cbx_2442_sa1, cby_2442_sa1, d_84, bpme_2442_sa1, d_72, qa_2442_sa1, 
d_86, cax_2443_sa1, cay_2443_sa1, d_82, u40_2445_sa1, d_83, cbx_2448_sa1, cby_2448_sa1, 
d_84, bpme_2448_sa1, d_72, qa_2449_sa1, d_86, cax_2450_sa1, cay_2450_sa1, d_82, 
u40_2452_sa1, d_83, cbx_2454_sa1, cby_2454_sa1, d_84, bpme_2454_sa1, d_72, qa_2455_sa1, 
d_86, cax_2456_sa1, cay_2456_sa1, d_82, u40_2458_sa1, d_83, cbx_2460_sa1, cby_2460_sa1, 
d_84, bpme_2461_sa1, d_72, qa_2461_sa1, d_73, ensec_2461_sa1)



cell_t4 = (stsec_2461_t4, stsub_2461_t4,
d_257, tora_2462_t4, d_258, bpma_2468_t4, d_259, qe_2468_t4, d_260, cex_2469_t4, 
d_261, bpma_2481_t4, d_259, qe_2481_t4, d_260, cey_2481_t4, d_261, bpma_2493_t4, 
d_259, qe_2493_t4, d_260, cex_2494_t4, d_261, bpma_2506_t4, d_259, qe_2506_t4, 
d_260, cey_2506_t4, d_270, bpma_2525_t4, d_259, qe_2526_t4, d_260, cex_2526_t4, 
d_273, bpma_2547_t4, d_259, qe_2548_t4, d_260, cey_2548_t4, d_276, bpma_2567_t4, 
d_277, qh_2567_t4, d_278, chx_2568_t4, d_279, bpma_2570_t4, d_277, qh_2570_t4, 
d_278, chy_2571_t4, d_282, chx_2581_t4, d_283, chy_2581_t4, d_284, bpma_2581_t4, 
d_277, qh_2582_t4, d_286, ensub_2583_t4, stsub_2583_t4, d_287, be_2584_t4, d_288, 
qm_2587_t4, d_289, bpma_2591_t4, d_290, qm_2592_t4, d_291, chx_2593_t4, d_292, 
saox_2594_t4, d_293, bpma_2596_t4, d_290, qm_2597_t4, d_291, chy_2598_t4, d_296, 
saox_2599_t4, d_297, chx_2601_t4, d_284, bpma_2601_t4, d_290, qm_2602_t4, d_300, 
be_2604_t4, d_301, bpma_2606_t4, d_277, qh_2607_t4, d_278, chy_2608_t4, d_304, 
bpma_2618_t4, d_277, qh_2618_t4, d_278, chx_2619_t4, d_279, bpma_2621_t4, d_277, 
qh_2621_t4, d_278, chy_2622_t4, d_310, bpma_2641_t4, d_259, qe_2641_t4, d_260, 
cex_2642_t4, d_273, bpma_2663_t4, d_259, qe_2663_t4, d_260, cey_2663_t4, d_273, 
bpma_2684_t4, d_259, qe_2685_t4, d_260, cex_2685_t4, d_273, bpma_2706_t4, d_259, 
qe_2707_t4, d_260, cey_2707_t4, d_322, otrbw_2718_t4, d_323, bpma_2728_t4, d_259, 
qe_2728_t4, d_260, cex_2729_t4, d_326, bpma_2749_t4, d_27, qf_2749_t4, d_4, 
cfy_2750_t4, d_329, otrbw_2755_t4, d_330, bpma_2761_t4, d_27, qf_2761_t4, d_4, 
cfx_2762_t4, d_333, bpma_2773_t4, d_27, qf_2773_t4, d_4, cfy_2774_t4, d_329, 
otrbw_2779_t4, d_330, bpma_2785_t4, d_27, qf_2785_t4, d_4, cfx_2786_t4, d_340, 
tora_2793_t4, d_64, bpme_2794_t4, d_65, qa_2794_t4, d_66, cny_2794_t4, d_67, 
cex_2795_t4, d_68, u40s_2797_t4, d_69, cny_2799_t4, d_70, cex_2799_t4, d_71, 
bpme_2800_t4, d_72, qa_2800_t4, d_73, ensub_2800_t4)
# power supplies 

#  
qk_1982_tl.ps_id = 'QK.1.TL'
qf_1997_tl.ps_id = 'QF.2.TL'
qf_2012_tl.ps_id = 'QF.1.TL'
qk_2027_tl.ps_id = 'QK.2.TL'
qf_2042_tl.ps_id = 'QF.1.TL'
qk_2057_tl.ps_id = 'QK.2.TL'
qf_2072_t2.ps_id = 'QF.1.T2'
qf_2087_t2.ps_id = 'QF.1.T2'
qf_2102_t2.ps_id = 'QF.1.T2'
qf_2117_t2.ps_id = 'QF.1.T2'
qf_2132_t2.ps_id = 'QF.1.T2'
qf_2145_t2.ps_id = 'QF.2.T2'
qf_2162_t2.ps_id = 'QF.2.T2'
qf_2177_t2.ps_id = 'QF.3.T2'
qf_2192_t2.ps_id = 'QF.4.T2'
qf_2207_t2.ps_id = 'QF.5.T2'
qf_2218_t2.ps_id = 'QF.6.T2'
qa_2229_t2.ps_id = 'QA.1.T2'
qa_2235_t2.ps_id = 'QA.2.T2'
qa_2241_sa1.ps_id = 'QA.1.SA1'
qa_2247_sa1.ps_id = 'QA.2.SA1'
qa_2253_sa1.ps_id = 'QA.1.SA1'
qa_2259_sa1.ps_id = 'QA.2.SA1'
qa_2266_sa1.ps_id = 'QA.1.SA1'
qa_2272_sa1.ps_id = 'QA.2.SA1'
qa_2278_sa1.ps_id = 'QA.1.SA1'
qa_2284_sa1.ps_id = 'QA.2.SA1'
qa_2290_sa1.ps_id = 'QA.1.SA1'
qa_2296_sa1.ps_id = 'QA.2.SA1'
qa_2302_sa1.ps_id = 'QA.1.SA1'
qa_2308_sa1.ps_id = 'QA.2.SA1'
qa_2314_sa1.ps_id = 'QA.1.SA1'
qa_2320_sa1.ps_id = 'QA.2.SA1'
qa_2327_sa1.ps_id = 'QA.1.SA1'
qa_2333_sa1.ps_id = 'QA.2.SA1'
qa_2339_sa1.ps_id = 'QA.1.SA1'
qa_2345_sa1.ps_id = 'QA.2.SA1'
qa_2351_sa1.ps_id = 'QA.1.SA1'
qa_2357_sa1.ps_id = 'QA.2.SA1'
qa_2363_sa1.ps_id = 'QA.1.SA1'
qa_2369_sa1.ps_id = 'QA.2.SA1'
qa_2375_sa1.ps_id = 'QA.1.SA1'
qa_2381_sa1.ps_id = 'QA.2.SA1'
qa_2388_sa1.ps_id = 'QA.1.SA1'
qa_2394_sa1.ps_id = 'QA.2.SA1'
qa_2400_sa1.ps_id = 'QA.1.SA1'
qa_2406_sa1.ps_id = 'QA.2.SA1'
qa_2412_sa1.ps_id = 'QA.1.SA1'
qa_2418_sa1.ps_id = 'QA.2.SA1'
qa_2424_sa1.ps_id = 'QA.1.SA1'
qa_2430_sa1.ps_id = 'QA.2.SA1'
qa_2436_sa1.ps_id = 'QA.1.SA1'
qa_2442_sa1.ps_id = 'QA.2.SA1'
qa_2449_sa1.ps_id = 'QA.1.SA1'
qa_2455_sa1.ps_id = 'QA.2.SA1'
qa_2461_sa1.ps_id = 'QA.1.SA1'
qe_2468_t4.ps_id = 'QE.3.T4'
qe_2481_t4.ps_id = 'QE.4.T4'
qe_2493_t4.ps_id = 'QE.5.T4'
qe_2506_t4.ps_id = 'QE.6.T4'
qe_2526_t4.ps_id = 'QE.2.T4'
qe_2548_t4.ps_id = 'QE.1.T4'
qh_2567_t4.ps_id = 'QH.4.T4'
qh_2570_t4.ps_id = 'QH.3.T4'
qh_2582_t4.ps_id = 'QH.1.T4'
qm_2587_t4.ps_id = 'QM.2.T4'
qm_2592_t4.ps_id = 'QM.1.T4'
qm_2597_t4.ps_id = 'QM.2.T4'
qm_2602_t4.ps_id = 'QM.1.T4'
qh_2607_t4.ps_id = 'QH.2.T4'
qh_2618_t4.ps_id = 'QH.4.T4'
qh_2621_t4.ps_id = 'QH.3.T4'
qe_2641_t4.ps_id = 'QE.2.T4'
qe_2663_t4.ps_id = 'QE.1.T4'
qe_2685_t4.ps_id = 'QE.2.T4'
qe_2707_t4.ps_id = 'QE.1.T4'
qe_2728_t4.ps_id = 'QE.2.T4'
qf_2749_t4.ps_id = 'QF.7.T4'
qf_2761_t4.ps_id = 'QF.8.T4'
qf_2773_t4.ps_id = 'QF.9.T4'
qf_2785_t4.ps_id = 'QF.10.T4'
qa_2794_t4.ps_id = 'QA.3.T4'
qa_2800_t4.ps_id = 'QA.4.T4'

#  
saox_2594_t4.ps_id = 'SAOX.1.T4'
saox_2599_t4.ps_id = 'SAOX.2.T4'

#  

#  

#  
bd_2079_t2.ps_id = 'BD.10.T2'
be_2584_t4.ps_id = 'BE.1.T4'
be_2604_t4.ps_id = 'BE.1.T4'
