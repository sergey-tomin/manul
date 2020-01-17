from ocelot import * 

# Drifts
d_1 = Drift(l=1.0, eid='D_1')
d_2 = Drift(l=12.4714, eid='D_2')
d_3 = Drift(l=15.515, eid='D_3')
d_4 = Drift(l=0.20895, eid='D_4')
d_5 = Drift(l=0.15395, eid='D_5')
d_6 = Drift(l=11.205, eid='D_6')
d_9 = Drift(l=60.205, eid='D_9')
d_12 = Drift(l=5.36, eid='D_12')
d_14 = Drift(l=0.35995, eid='D_14')
d_15 = Drift(l=0.1108, eid='D_15')
d_16 = Drift(l=0.515921, eid='D_16')
d_17 = Drift(l=0.500198, eid='D_17')
d_18 = Drift(l=1.930099, eid='D_18')
d_19 = Drift(l=0.1424, eid='D_19')
d_20 = Drift(l=0.1974, eid='D_20')
d_21 = Drift(l=0.5535, eid='D_21')
d_22 = Drift(l=0.9035, eid='D_22')
d_23 = Drift(l=0.8535, eid='D_23')
d_28 = Drift(l=0.500199, eid='D_28')
d_29 = Drift(l=0.611799, eid='D_29')
d_30 = Drift(l=0.1607, eid='D_30')
d_31 = Drift(l=0.3448, eid='D_31')
d_34 = Drift(l=0.2144, eid='D_34')
d_35 = Drift(l=0.558, eid='D_35')
d_36 = Drift(l=0.5, eid='D_36')
d_37 = Drift(l=0.822, eid='D_37')
d_38 = Drift(l=0.2, eid='D_38')
d_39 = Drift(l=4.633, eid='D_39')
d_40 = Drift(l=4.26774, eid='D_40')

# Quadrupoles
qe_3052_t5d = Quadrupole(l=0.24, k1=0.17811070166666665, eid='QE.3052.T5D')
qf_3068_t5d = Quadrupole(l=0.5321, k1=-0.17408057188498402, eid='QF.3068.T5D')
qf_3081_t5d = Quadrupole(l=0.5321, k1=0.041949297500469836, eid='QF.3081.T5D')
qf_3142_t5d = Quadrupole(l=0.5321, k1=0.15234501841759066, eid='QF.3142.T5D')
qf_3148_t5d = Quadrupole(l=0.5321, k1=-0.08121677316293929, eid='QF.3148.T5D')
qk_3158_t5d = Quadrupole(l=1.0552, k1=-0.17299443034495832, eid='QK.3158.T5D')
qk_3163_t5d = Quadrupole(l=1.0552, k1=-0.17299443034495832, eid='QK.3163.T5D')
qk_3172_t5d = Quadrupole(l=1.0552, k1=-0.18514803487490525, eid='QK.3172.T5D')
qk_3174_t5d = Quadrupole(l=1.0552, k1=-0.18514803487490525, eid='QK.3174.T5D')
qk_3175_t5d = Quadrupole(l=1.0552, k1=-0.18514803487490525, eid='QK.3175.T5D')
qk_3177_t5d = Quadrupole(l=1.0552, k1=-0.18514803487490525, eid='QK.3177.T5D')

# SBends
bv_3151_t5d = SBend(l=2.5, angle=0.043633231, e1=0.021816616, e2=0.021816616, tilt=1.570796327, eid='BV.3151.T5D')
bv_3154_t5d = SBend(l=2.5, angle=0.043633231, e1=0.021816616, e2=0.021816616, tilt=1.570796327, eid='BV.3154.T5D')
bv_3167_t5d = SBend(l=2.5, angle=0.043633231, e1=0.021816616, e2=0.021816616, tilt=1.570796327, eid='BV.3167.T5D')
bv_3170_t5d = SBend(l=2.5, angle=0.043633231, e1=0.021816616, e2=0.021816616, tilt=1.570796327, eid='BV.3170.T5D')

# RBends
sweep_3178_t5d = RBend(l=0.64, tilt=-1.570796327, eid='SWEEP.3178.T5D')
sweep_3179_t5d = RBend(l=0.64, eid='SWEEP.3179.T5D')

# Sextupoles
sk_3159_t5d = Sextupole(l=0.343, k2=2.020228531, tilt=1.570796327, eid='SK.3159.T5D')
sk_3161_t5d = Sextupole(l=0.343, k2=2.020228531, tilt=1.570796327, eid='SK.3161.T5D')

# Hcors
cfx_3081_t5d = Hcor(l=0.1, eid='CFX.3081.T5D')
cfx_3142_t5d = Hcor(l=0.1, eid='CFX.3142.T5D')
cnx_3157_t5d = Hcor(l=0.3, eid='CNX.3157.T5D')

# Vcors
cfy_3069_t5d = Vcor(l=0.1, eid='CFY.3069.T5D')
cfy_3148_t5d = Vcor(l=0.1, eid='CFY.3148.T5D')
cny_3164_t5d = Vcor(l=0.3, eid='CNY.3164.T5D')

# Monitors
bpma_3068_t5d = Monitor(eid='BPMA.3068.T5D')
bpma_3080_t5d = Monitor(eid='BPMA.3080.T5D')
bpma_3141_t5d = Monitor(eid='BPMA.3141.T5D')
bpmf_3149_t5d = Monitor(eid='BPMF.3149.T5D')
bpmd_3159_t5d = Monitor(eid='BPMD.3159.T5D')
bpmd_3162_t5d = Monitor(eid='BPMD.3162.T5D')
bpmd_3172_t5d = Monitor(eid='BPMD.3172.T5D')
bpmd_3177_t5d = Monitor(eid='BPMD.3177.T5D')
bpmd_3180_t5d = Monitor(eid='BPMD.3180.T5D')
bpmw_3185_t5d = Monitor(eid='BPMW.3185.T5D')

# Markers
tora_3040_t5d = Marker(eid='TORA.3040.T5D')
tora_3149_t5d = Marker(eid='TORA.3149.T5D')
otrd_3160_t5d = Marker(eid='OTRD.3160.T5D')
otrd_3181_t5d = Marker(eid='OTRD.3181.T5D')
ensec_3189_t5d = Marker(eid='ENSEC.3189.T5D')

# Lattice 
cell = (d_1, tora_3040_t5d, d_2, qe_3052_t5d, d_3, bpma_3068_t5d, d_4, qf_3068_t5d, d_5, 
cfy_3069_t5d, d_6, bpma_3080_t5d, d_4, qf_3081_t5d, d_5, cfx_3081_t5d, d_9, bpma_3141_t5d, d_4, 
qf_3142_t5d, d_5, cfx_3142_t5d, d_12, cfy_3148_t5d, d_5, qf_3148_t5d, d_14, bpmf_3149_t5d, d_15, 
tora_3149_t5d, d_16, bv_3151_t5d, d_17, bv_3154_t5d, d_18, cnx_3157_t5d, d_19, qk_3158_t5d, d_20, 
bpmd_3159_t5d, d_21, sk_3159_t5d, d_22, otrd_3160_t5d, d_23, sk_3161_t5d, d_21, bpmd_3162_t5d, d_20, 
qk_3163_t5d, d_19, cny_3164_t5d, d_18, bv_3167_t5d, d_28, bv_3170_t5d, d_29, bpmd_3172_t5d, d_30, 
qk_3172_t5d, d_31, qk_3174_t5d, d_31, qk_3175_t5d, d_31, qk_3177_t5d, d_34, bpmd_3177_t5d, d_35, 
sweep_3178_t5d, d_36, sweep_3179_t5d, d_37, bpmd_3180_t5d, d_38, otrd_3181_t5d, d_39, bpmw_3185_t5d, d_40, 
ensec_3189_t5d)

# power supplies 

#  
qe_3052_t5d.ps_id = 'QE.1.T5D'
qf_3068_t5d.ps_id = 'QF.1.T5D'
qf_3081_t5d.ps_id = 'QF.2.T5D'
qf_3142_t5d.ps_id = 'QF.3.T5D'
qf_3148_t5d.ps_id = 'QF.4.T5D'
qk_3158_t5d.ps_id = 'QK.1.T5D'
qk_3163_t5d.ps_id = 'QK.1.T5D'
qk_3172_t5d.ps_id = 'QK.6.T5D'
qk_3174_t5d.ps_id = 'QK.6.T5D'
qk_3175_t5d.ps_id = 'QK.6.T5D'
qk_3177_t5d.ps_id = 'QK.6.T5D'

#  
sk_3159_t5d.ps_id = 'SK.1.T5D'
sk_3161_t5d.ps_id = 'SK.1.T5D'

#  

#  

#  
bv_3151_t5d.ps_id = 'BV.1.T5D'
bv_3154_t5d.ps_id = 'BV.1.T5D'
bv_3167_t5d.ps_id = 'BV.1.T5D'
bv_3170_t5d.ps_id = 'BV.1.T5D'
sweep_3178_t5d.ps_id = 'SWEEP.1.T5D'
sweep_3179_t5d.ps_id = 'SWEEP.1.T5D'
