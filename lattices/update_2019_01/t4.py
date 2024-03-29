from ocelot import * 
tws = Twiss()
tws.beta_x  = 25.49358672503274
tws.beta_y  = 37.14160272262846
tws.alpha_x = -0.7889996283225933
tws.alpha_y = 1.1585816457654505
tws.E = 14
tws.s        = 2461.7170390000133
# Drifts
d_1 = Drift(l=1.3805, eid='D_1')
d_2 = Drift(l=5.678, eid='D_2')
d_3 = Drift(l=0.205, eid='D_3')
d_4 = Drift(l=0.14, eid='D_4')
d_5 = Drift(l=11.925, eid='D_5')
d_14 = Drift(l=19.01, eid='D_14')
d_17 = Drift(l=21.065, eid='D_17')
d_20 = Drift(l=18.72, eid='D_20')
d_21 = Drift(l=0.21045, eid='D_21')
d_22 = Drift(l=0.15545, eid='D_22')
d_23 = Drift(l=1.545, eid='D_23')
d_26 = Drift(l=9.06, eid='D_26')
d_27 = Drift(l=0.185, eid='D_27')
d_28 = Drift(l=0.19, eid='D_28')
d_30 = Drift(l=0.38545, eid='D_30')
d_31 = Drift(l=7e-06, eid='D_31')
d_32 = Drift(l=1.070157, eid='D_32')
d_33 = Drift(l=3.59515, eid='D_33')
d_34 = Drift(l=0.34515, eid='D_34')
d_35 = Drift(l=0.29015, eid='D_35')
d_36 = Drift(l=0.6718, eid='D_36')
d_37 = Drift(l=2.1168, eid='D_37')
d_40 = Drift(l=1.3218, eid='D_40')
d_41 = Drift(l=1.0768, eid='D_41')
d_44 = Drift(l=0.369898, eid='D_44')
d_45 = Drift(l=0.875266, eid='D_45')
d_48 = Drift(l=9.835, eid='D_48')
d_54 = Drift(l=18.61, eid='D_54')
d_66 = Drift(l=10.79, eid='D_66')
d_67 = Drift(l=10.275, eid='D_67')
d_70 = Drift(l=20.165, eid='D_70')
d_71 = Drift(l=0.20895, eid='D_71')
d_72 = Drift(l=0.15395, eid='D_72')
d_73 = Drift(l=5.48, eid='D_73')
d_74 = Drift(l=5.525, eid='D_74')
d_77 = Drift(l=11.005, eid='D_77')
d_84 = Drift(l=4.239987, eid='D_84')
d_85 = Drift(l=2.850703, eid='D_85')
d_86 = Drift(l=0.8065, eid='D_86')
d_87 = Drift(l=0.21815, eid='D_87')
d_88 = Drift(l=0.17815, eid='D_88')
d_89 = Drift(l=0.125, eid='D_89')
d_90 = Drift(l=2.1675, eid='D_90')
d_91 = Drift(l=1.8267, eid='D_91')
d_92 = Drift(l=0.15, eid='D_92')
d_93 = Drift(l=0.4323, eid='D_93')
d_94 = Drift(l=0.18665, eid='D_94')
d_95 = Drift(l=0.04015, eid='D_95')

# Quadrupoles
qe_2468_t4 = Quadrupole(l=0.24, k1=0.2226231875, eid='QE.2468.T4')
qe_2481_t4 = Quadrupole(l=0.24, k1=-0.20601194416666668, eid='QE.2481.T4')
qe_2493_t4 = Quadrupole(l=0.24, k1=0.24094500458333334, eid='QE.2493.T4')
qe_2506_t4 = Quadrupole(l=0.24, k1=-0.22885621708333334, eid='QE.2506.T4')
qe_2526_t4 = Quadrupole(l=0.24, k1=0.19227955166666666, eid='QE.2526.T4')
qe_2548_t4 = Quadrupole(l=0.24, k1=-0.19227955166666666, eid='QE.2548.T4')
qh_2567_t4 = Quadrupole(l=1.0291, k1=0.19653155320182686, eid='QH.2567.T4')
qh_2570_t4 = Quadrupole(l=1.0291, k1=-0.19652613827616366, eid='QH.2570.T4')
qh_2582_t4 = Quadrupole(l=1.0291, k1=0.2948896440579147, eid='QH.2582.T4')
qm_2587_t4 = Quadrupole(l=1.0597, k1=-0.288466077474757, eid='QM.2587.T4')
qm_2592_t4 = Quadrupole(l=1.0597, k1=0.28822914541851463, eid='QM.2592.T4')
qm_2597_t4 = Quadrupole(l=1.0597, k1=-0.288466077474757, eid='QM.2597.T4')
qm_2602_t4 = Quadrupole(l=1.0597, k1=0.28822914541851463, eid='QM.2602.T4')
qh_2607_t4 = Quadrupole(l=1.0291, k1=-0.2948267903022058, eid='QH.2607.T4')
qh_2618_t4 = Quadrupole(l=1.0291, k1=0.19653155320182686, eid='QH.2618.T4')
qh_2621_t4 = Quadrupole(l=1.0291, k1=-0.19652613827616366, eid='QH.2621.T4')
qe_2641_t4 = Quadrupole(l=0.24, k1=0.19227955166666666, eid='QE.2641.T4')
qe_2663_t4 = Quadrupole(l=0.24, k1=-0.19227955166666666, eid='QE.2663.T4')
qe_2685_t4 = Quadrupole(l=0.24, k1=0.19227955166666666, eid='QE.2685.T4')
qe_2707_t4 = Quadrupole(l=0.24, k1=-0.19227955166666666, eid='QE.2707.T4')
qe_2728_t4 = Quadrupole(l=0.24, k1=0.19227955166666666, eid='QE.2728.T4')
qf_2749_t4 = Quadrupole(l=0.5321, k1=-0.11560315185115579, eid='QF.2749.T4')
qf_2761_t4 = Quadrupole(l=0.5321, k1=0.14753906577710957, eid='QF.2761.T4')
qf_2773_t4 = Quadrupole(l=0.5321, k1=-0.1505125916181169, eid='QF.2773.T4')
qf_2785_t4 = Quadrupole(l=0.5321, k1=0.18363453467393348, eid='QF.2785.T4')
qa_2794_t4 = Quadrupole(l=0.1137, k1=-1.1165777862796835, eid='QA.2794.T4')
qa_2800_t4 = Quadrupole(l=0.1137, k1=1.2438986684256816, eid='QA.2800.T4')

# SBends
be_2584_t4 = SBend(l=2.5, angle=0.0115035, e1=0.00575175, e2=0.00575175, eid='BE.2584.T4')
be_2604_t4 = SBend(l=2.5, angle=0.0115035, e1=0.00575175, e2=0.00575175, eid='BE.2604.T4')

# Sextupoles
saox_2594_t4 = Sextupole(l=0.3164, k2=23.92225032, eid='SAOX.2594.T4')
saox_2599_t4 = Sextupole(l=0.3164, k2=8.44816687700063, eid='SAOX.2599.T4')

# Hcors
cex_2469_t4 = Hcor(l=0.1, eid='CEX.2469.T4')
cex_2494_t4 = Hcor(l=0.1, eid='CEX.2494.T4')
cex_2526_t4 = Hcor(l=0.1, eid='CEX.2526.T4')
chx_2568_t4 = Hcor(l=0.2, eid='CHX.2568.T4')
chx_2581_t4 = Hcor(l=0.2, eid='CHX.2581.T4')
chx_2593_t4 = Hcor(l=0.2, eid='CHX.2593.T4')
chx_2601_t4 = Hcor(l=0.2, eid='CHX.2601.T4')
chx_2619_t4 = Hcor(l=0.2, eid='CHX.2619.T4')
cex_2642_t4 = Hcor(l=0.1, eid='CEX.2642.T4')
cex_2685_t4 = Hcor(l=0.1, eid='CEX.2685.T4')
cex_2729_t4 = Hcor(l=0.1, eid='CEX.2729.T4')
cfx_2762_t4 = Hcor(l=0.1, eid='CFX.2762.T4')
cfx_2786_t4 = Hcor(l=0.1, eid='CFX.2786.T4')
cex_2795_t4 = Hcor(l=0.1, eid='CEX.2795.T4')
cex_2799_t4 = Hcor(l=0.1, eid='CEX.2799.T4')

# Vcors
cey_2481_t4 = Vcor(l=0.1, eid='CEY.2481.T4')
cey_2506_t4 = Vcor(l=0.1, eid='CEY.2506.T4')
cey_2548_t4 = Vcor(l=0.1, eid='CEY.2548.T4')
chy_2571_t4 = Vcor(l=0.2, eid='CHY.2571.T4')
chy_2581_t4 = Vcor(l=0.2, eid='CHY.2581.T4')
chy_2598_t4 = Vcor(l=0.2, eid='CHY.2598.T4')
chy_2608_t4 = Vcor(l=0.2, eid='CHY.2608.T4')
chy_2622_t4 = Vcor(l=0.2, eid='CHY.2622.T4')
cey_2663_t4 = Vcor(l=0.1, eid='CEY.2663.T4')
cey_2707_t4 = Vcor(l=0.1, eid='CEY.2707.T4')
cfy_2750_t4 = Vcor(l=0.1, eid='CFY.2750.T4')
cfy_2774_t4 = Vcor(l=0.1, eid='CFY.2774.T4')
cny_2794_t4 = Vcor(l=0.3, eid='CNY.2794.T4')
cny_2799_t4 = Vcor(l=0.3, eid='CNY.2799.T4')

# Undulators
u40s_2797_t4 = Undulator(lperiod=0.04, nperiods=3.0, eid='U40S.2797.T4')

# Monitors
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
bpma_2790_t4 = Monitor(eid='BPMA.2790.T4')
bpme_2794_t4 = Monitor(eid='BPME.2794.T4')
bpme_2800_t4 = Monitor(eid='BPME.2800.T4')

# Markers
tora_2462_t4 = Marker(eid='TORA.2462.T4')
stsub_2583_t4 = Marker(eid='STSUB.2583.T4')
otrbw_2718_t4 = Marker(eid='OTRBW.2718.T4')
otrbw_2755_t4 = Marker(eid='OTRBW.2755.T4')
otrbw_2779_t4 = Marker(eid='OTRBW.2779.T4')
tora_2793_t4 = Marker(eid='TORA.2793.T4')
ensub_2800_t4 = Marker(eid='ENSUB.2800.T4')

# Lattice 
cell = (d_1, tora_2462_t4, d_2, bpma_2468_t4, d_3, qe_2468_t4, d_4, cex_2469_t4, d_5, 
bpma_2481_t4, d_3, qe_2481_t4, d_4, cey_2481_t4, d_5, bpma_2493_t4, d_3, qe_2493_t4, d_4, 
cex_2494_t4, d_5, bpma_2506_t4, d_3, qe_2506_t4, d_4, cey_2506_t4, d_14, bpma_2525_t4, d_3, 
qe_2526_t4, d_4, cex_2526_t4, d_17, bpma_2547_t4, d_3, qe_2548_t4, d_4, cey_2548_t4, d_20, 
bpma_2567_t4, d_21, qh_2567_t4, d_22, chx_2568_t4, d_23, bpma_2570_t4, d_21, qh_2570_t4, d_22, 
chy_2571_t4, d_26, chx_2581_t4, d_27, chy_2581_t4, d_28, bpma_2581_t4, d_21, qh_2582_t4, d_30, 
stsub_2583_t4, d_31, be_2584_t4, d_32, qm_2587_t4, d_33, bpma_2591_t4, d_34, qm_2592_t4, d_35, 
chx_2593_t4, d_36, saox_2594_t4, d_37, bpma_2596_t4, d_34, qm_2597_t4, d_35, chy_2598_t4, d_40, 
saox_2599_t4, d_41, chx_2601_t4, d_28, bpma_2601_t4, d_34, qm_2602_t4, d_44, be_2604_t4, d_45, 
bpma_2606_t4, d_21, qh_2607_t4, d_22, chy_2608_t4, d_48, bpma_2618_t4, d_21, qh_2618_t4, d_22, 
chx_2619_t4, d_23, bpma_2621_t4, d_21, qh_2621_t4, d_22, chy_2622_t4, d_54, bpma_2641_t4, d_3, 
qe_2641_t4, d_4, cex_2642_t4, d_17, bpma_2663_t4, d_3, qe_2663_t4, d_4, cey_2663_t4, d_17, 
bpma_2684_t4, d_3, qe_2685_t4, d_4, cex_2685_t4, d_17, bpma_2706_t4, d_3, qe_2707_t4, d_4, 
cey_2707_t4, d_66, otrbw_2718_t4, d_67, bpma_2728_t4, d_3, qe_2728_t4, d_4, cex_2729_t4, d_70, 
bpma_2749_t4, d_71, qf_2749_t4, d_72, cfy_2750_t4, d_73, otrbw_2755_t4, d_74, bpma_2761_t4, d_71, 
qf_2761_t4, d_72, cfx_2762_t4, d_77, bpma_2773_t4, d_71, qf_2773_t4, d_72, cfy_2774_t4, d_73, 
otrbw_2779_t4, d_74, bpma_2785_t4, d_71, qf_2785_t4, d_72, cfx_2786_t4, d_84, bpma_2790_t4, d_85, 
tora_2793_t4, d_86, bpme_2794_t4, d_87, qa_2794_t4, d_88, cny_2794_t4, d_89, cex_2795_t4, d_90, 
u40s_2797_t4, d_91, cny_2799_t4, d_92, cex_2799_t4, d_93, bpme_2800_t4, d_94, qa_2800_t4, d_95, 
ensub_2800_t4)

# power supplies 

#  
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
be_2584_t4.ps_id = 'BE.1.T4'
be_2604_t4.ps_id = 'BE.1.T4'
