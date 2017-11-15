from ocelot import *

tws = Twiss()
tws.beta_x  = 25.9318680453
tws.beta_y  = 38.3782827028
tws.alpha_x = -0.840495296807
tws.alpha_y = 1.22012853464
tws.E       = 2.39999998888
#tws.s        = 2438.5169790000195

d_4 = Drift(l=0.15395, eid='D_4')
d_27 = Drift(l=0.20895, eid='D_27')
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
qf_2749_t4 = Quadrupole(l=0.5321, k1=-0.1066206252, tilt=0.0, eid='QF.2749.T4')
qf_2761_t4 = Quadrupole(l=0.5321, k1=0.1094258961, tilt=0.0, eid='QF.2761.T4')
qf_2773_t4 = Quadrupole(l=0.5321, k1=-0.0911900698, tilt=0.0, eid='QF.2773.T4')
qf_2785_t4 = Quadrupole(l=0.5321, k1=0.1011603755, tilt=0.0, eid='QF.2785.T4')
qa_2794_t4 = Quadrupole(l=0.1137, k1=-0.5620550639, tilt=0.0, eid='QA.2794.T4')
qa_2800_t4 = Quadrupole(l=0.1137, k1=+0.5620550639, tilt=0.0, eid='QA.2800.T4')

be_2584_t4 = SBend(l = 2.5, angle=0.0115035, e1=0.00575175, e2=0.00575175, gap=0, tilt=0.0, fint=0.0, fintx=0.0, eid='BE.2584.T4')
be_2604_t4 = SBend(l = 2.5, angle=0.0115035, e1=0.00575175, e2=0.00575175, gap=0, tilt=0.0, fint=0.0, fintx=0.0, eid='BE.2604.T4')


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


u40s_2797_t4 = Undulator(lperiod=0.04, nperiods=3, Kx=3, Ky=0.0, eid='U40S.2797.T4')


cell = (stsec_2461_t4, stsub_2461_t4,
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

be_2584_t4.ps_id = 'BE.1.T4'
be_2604_t4.ps_id = 'BE.1.T4'