from ocelot import * 
#tws = Twiss()
#tws.beta_x  = 37.357790549982305
#tws.beta_y  = 52.30227486751415
#tws.alpha_x = 1.4161509971676498
#tws.alpha_y = -1.5624042646645238
#tws.E = 17.5

tws = Twiss()
tws.beta_x  = 42.0646995916
tws.beta_y  = 58.0284165718
tws.alpha_x = -0.996413599281
tws.alpha_y = 2.16792724498

tws.beta_x  = 40.41944144648599
tws.beta_y  = 57.830286580189686
tws.alpha_x = -1.1237381492887348
tws.alpha_y = 2.1689790108436324

tws.E = 14

# Drifts
d_1 = Drift(l=6.3887, eid='D_1')
d_2 = Drift(l=0.8, eid='D_2')
d_3 = Drift(l=0.20895, eid='D_3')
d_4 = Drift(l=0.15395, eid='D_4')
d_5 = Drift(l=6.21, eid='D_5')
d_6 = Drift(l=0.15545, eid='D_6')
d_7 = Drift(l=0.2209, eid='D_7')
d_8 = Drift(l=0.21045, eid='D_8')
d_9 = Drift(l=0.36045, eid='D_9')
d_12 = Drift(l=0.74395, eid='D_12')
d_14 = Drift(l=0.1718, eid='D_14')
d_15 = Drift(l=0.5378, eid='D_15')
d_16 = Drift(l=1.954002, eid='D_16')
d_17 = Drift(l=2.733952, eid='D_17')
d_20 = Drift(l=0.4418, eid='D_20')
d_21 = Drift(l=4.2, eid='D_21')
d_22 = Drift(l=0.45, eid='D_22')
d_23 = Drift(l=1.6918, eid='D_23')
d_24 = Drift(l=0.42575, eid='D_24')
d_28 = Drift(l=1.604, eid='D_28')
d_29 = Drift(l=4.6418, eid='D_29')
d_32 = Drift(l=0.93, eid='D_32')
d_33 = Drift(l=1.550002, eid='D_33')
d_34 = Drift(l=2.491802, eid='D_34')
d_39 = Drift(l=2.050002, eid='D_39')
d_60 = Drift(l=0.38, eid='D_60')
d_61 = Drift(l=0.675, eid='D_61')
d_68 = Drift(l=1.31895, eid='D_68')
d_71 = Drift(l=3.28395, eid='D_71')
d_74 = Drift(l=2.28395, eid='D_74')
d_77 = Drift(l=0.4343, eid='D_77')
d_78 = Drift(l=1.849647, eid='D_78')
d_84 = Drift(l=0.685, eid='D_84')
d_91 = Drift(l=1.30895, eid='D_91')
d_107 = Drift(l=1.7, eid='D_107')
d_137 = Drift(l=0.2168, eid='D_137')
d_140 = Drift(l=0.69, eid='D_140')
d_143 = Drift(l=0.5709, eid='D_143')
d_145 = Drift(l=0.50895, eid='D_145')
d_146 = Drift(l=0.3015, eid='D_146')
d_147 = Drift(l=2.0865, eid='D_147')
d_148 = Drift(l=0.43245, eid='D_148')
d_151 = Drift(l=2.425, eid='D_151')
d_154 = Drift(l=3.855, eid='D_154')
d_157 = Drift(l=4.9485, eid='D_157')
d_158 = Drift(l=2.61545, eid='D_158')
d_159 = Drift(l=2.50395, eid='D_159')
d_160 = Drift(l=4.4485, eid='D_160')
d_162 = Drift(l=2.53395, eid='D_162')
d_163 = Drift(l=4.1, eid='D_163')
d_164 = Drift(l=7.73395, eid='D_164')
d_165 = Drift(l=2.80745, eid='D_165')
d_167 = Drift(l=3.525, eid='D_167')
d_172 = Drift(l=1.3735, eid='D_172')
d_173 = Drift(l=6.36045, eid='D_173')
d_175 = Drift(l=1.5985, eid='D_175')
d_176 = Drift(l=0.4815, eid='D_176')
d_177 = Drift(l=11.933951, eid='D_177')
d_179 = Drift(l=0.64, eid='D_179')
d_180 = Drift(l=1.285, eid='D_180')
d_181 = Drift(l=0.208951, eid='D_181')
d_182 = Drift(l=0.153951, eid='D_182')
d_183 = Drift(l=0.2, eid='D_183')
d_184 = Drift(l=9.0692, eid='D_184')
d_185 = Drift(l=0.1, eid='D_185')
d_186 = Drift(l=0.15, eid='D_186')
d_188 = Drift(l=1.86074, eid='D_188')

# Quadrupoles
qf_1660_cl = Quadrupole(l=0.5321, k1=0.17818864536741214, eid='QF.1660.CL')
qh_1667_cl = Quadrupole(l=1.0291, k1=-0.17335257992420564, eid='QH.1667.CL')
qh_1669_cl = Quadrupole(l=1.0291, k1=-0.17335257992420564, eid='QH.1669.CL')
qh_1670_cl = Quadrupole(l=1.0291, k1=0.3395033707, eid='QH.1670.CL')
qh_1671_cl = Quadrupole(l=1.0291, k1=0.3395033707, eid='QH.1671.CL')
qf_1673_cl = Quadrupole(l=0.5321, k1=-0.30131733847021236, eid='QF.1673.CL')
qf_1682_cl = Quadrupole(l=0.5321, k1=0.30131733847021236, eid='QF.1682.CL')
qf_1691_cl = Quadrupole(l=0.5321, k1=-0.30131733847021236, eid='QF.1691.CL')
qf_1700_cl = Quadrupole(l=0.5321, k1=0.30131733847021236, eid='QF.1700.CL')
qf_1709_cl = Quadrupole(l=0.5321, k1=-0.30131733847021236, eid='QF.1709.CL')
qf_1718_cl = Quadrupole(l=0.5321, k1=0.30131733847021236, eid='QF.1718.CL')
qf_1727_cl = Quadrupole(l=0.5321, k1=-0.30131733847021236, eid='QF.1727.CL')
qf_1736_cl = Quadrupole(l=0.5321, k1=0.30131733847021236, eid='QF.1736.CL')
qf_1745_cl = Quadrupole(l=0.5321, k1=-0.30131733847021236, eid='QF.1745.CL')
qh_1748_cl = Quadrupole(l=1.0291, k1=0.3239105019, eid='QH.1748.CL')
qh_1749_cl = Quadrupole(l=1.0291, k1=0.3239105019, eid='QH.1749.CL')
qh_1751_cl = Quadrupole(l=1.0291, k1=-0.2257174548, eid='QH.1751.CL')
qh_1752_cl = Quadrupole(l=1.0291, k1=-0.2257174548, eid='QH.1752.CL')
qf_1754_cl = Quadrupole(l=0.5321, k1=0.14203992877278707, eid='QF.1754.CL')
qf_1759_cl = Quadrupole(l=0.5321, k1=0.1625880644, eid='QF.1759.CL')
qf_1763_cl = Quadrupole(l=0.5321, k1=-0.22123286957338845, eid='QF.1763.CL')
qf_1767_cl = Quadrupole(l=0.5321, k1=0.1625880644, eid='QF.1767.CL')
qf_1772_cl = Quadrupole(l=0.5321, k1=0.14203992877278707, eid='QF.1772.CL')
qh_1775_cl = Quadrupole(l=1.0291, k1=-0.2257174548, eid='QH.1775.CL')
qh_1776_cl = Quadrupole(l=1.0291, k1=-0.2257174548, eid='QH.1776.CL')
qh_1778_cl = Quadrupole(l=1.0291, k1=0.3239105019, eid='QH.1778.CL')
qh_1779_cl = Quadrupole(l=1.0291, k1=0.3239105019, eid='QH.1779.CL')
qf_1781_cl = Quadrupole(l=0.5321, k1=-0.30131733847021236, eid='QF.1781.CL')
qf_1790_cl = Quadrupole(l=0.5321, k1=0.30131733847021236, eid='QF.1790.CL')
qf_1799_cl = Quadrupole(l=0.5321, k1=-0.30131733847021236, eid='QF.1799.CL')
qf_1808_cl = Quadrupole(l=0.5321, k1=0.30131733847021236, eid='QF.1808.CL')
qf_1817_cl = Quadrupole(l=0.5321, k1=-0.30131733847021236, eid='QF.1817.CL')
qf_1826_cl = Quadrupole(l=0.5321, k1=0.30131733847021236, eid='QF.1826.CL')
qf_1835_cl = Quadrupole(l=0.5321, k1=-0.30131733847021236, eid='QF.1835.CL')
qf_1844_cl = Quadrupole(l=0.5321, k1=0.30131733847021236, eid='QF.1844.CL')
qf_1853_cl = Quadrupole(l=0.5321, k1=-0.30131733847021236, eid='QF.1853.CL')
qh_1855_tl = Quadrupole(l=1.0291, k1=0.37166334156058695, eid='QH.1855.TL')
qh_1857_tl = Quadrupole(l=1.0291, k1=0.3460558121, eid='QH.1857.TL')
qh_1858_tl = Quadrupole(l=1.0291, k1=-0.3787301584879993, eid='QH.1858.TL')
qh_1859_tl = Quadrupole(l=1.0291, k1=-0.0527740841,  eid='QH.1859.TL')
qf_1864_tl = Quadrupole(l=0.5321, k1=0.1858986038338658, eid='QF.1864.TL')
qf_1868_tl = Quadrupole(l=0.5321, k1=-0.05512587126479985, eid='QF.1868.TL')
qf_1873_tl = Quadrupole(l=0.5321, k1=0.11992892914865626, eid='QF.1873.TL')
qf_1881_tl = Quadrupole(l=0.5321, k1=-0.2009347130238677, eid='QF.1881.TL')
qf_1892_tl = Quadrupole(l=0.5321, k1=0.1791908475850404, eid='QF.1892.TL')
qf_1907_tl = Quadrupole(l=0.5321, k1=-0.1791908475850404, eid='QF.1907.TL')
qf_1922_tl = Quadrupole(l=0.5321, k1=0.1791908475850404, eid='QF.1922.TL')
qf_1937_tl = Quadrupole(l=0.5321, k1=-0.1791908475850404, eid='QF.1937.TL')
qf_1952_tl = Quadrupole(l=0.5321, k1=0.1791908475850404, eid='QF.1952.TL')
qf_1967_tl = Quadrupole(l=0.5321, k1=-0.1791908475850404, eid='QF.1967.TL')

# SBends
be_1678_cl = SBend(l=2.5, angle=0.006233024763, e1=0.003116512, e2=0.003116512, tilt=1.570796327, eid='BE.1678.CL')
bl_1688_cl = SBend(l=0.2, angle=-0.000737152538, e1=-0.000368576, e2=-0.000368576, tilt=1.570796327, eid='BL.1688.CL')
bl_1695_cl = SBend(l=0.2, angle=-0.000737152538, e1=-0.000368576, e2=-0.000368576, tilt=1.570796327, eid='BL.1695.CL')
be_1705_cl = SBend(l=2.5, angle=0.006233024763, e1=0.003116512, e2=0.003116512, tilt=1.570796327, eid='BE.1705.CL')
be_1714_cl = SBend(l=2.5, angle=0.006233024763, e1=0.003116512, e2=0.003116512, tilt=1.570796327, eid='BE.1714.CL')
bl_1724_cl = SBend(l=0.2, angle=-0.000737152538, e1=-0.000368576, e2=-0.000368576, tilt=1.570796327, eid='BL.1724.CL')
bl_1731_cl = SBend(l=0.2, angle=-0.000737152538, e1=-0.000368576, e2=-0.000368576, tilt=1.570796327, eid='BL.1731.CL')
be_1741_cl = SBend(l=2.5, angle=0.006233024763, e1=0.003116512, e2=0.003116512, tilt=1.570796327, eid='BE.1741.CL')
be_1786_cl = SBend(l=2.5, angle=-0.006129494209, e1=-0.003064747, e2=-0.003064747, tilt=1.570796327, eid='BE.1786.CL')
bl_1796_cl = SBend(l=0.2, angle=0.000724902792, e1=0.000362451, e2=0.000362451, tilt=1.570796327, eid='BL.1796.CL')
bl_1803_cl = SBend(l=0.2, angle=0.000724902792, e1=0.000362451, e2=0.000362451, tilt=1.570796327, eid='BL.1803.CL')
be_1813_cl = SBend(l=2.5, angle=-0.006129494209, e1=-0.003064747, e2=-0.003064747, tilt=1.570796327, eid='BE.1813.CL')
be_1822_cl = SBend(l=2.5, angle=-0.006129494209, e1=-0.003064747, e2=-0.003064747, tilt=1.570796327, eid='BE.1822.CL')
bl_1832_cl = SBend(l=0.2, angle=0.000724902792, e1=0.000362451, e2=0.000362451, tilt=1.570796327, eid='BL.1832.CL')
bl_1839_cl = SBend(l=0.2, angle=0.000724902792, e1=0.000362451, e2=0.000362451, tilt=1.570796327, eid='BL.1839.CL')
be_1849_cl = SBend(l=2.5, angle=-0.006129494209, e1=-0.003064747, e2=-0.003064747, tilt=1.570796327, eid='BE.1849.CL')

# Sextupoles
sa_1674_cl = Sextupole(l=0.3164, k2=17.626614410000002, tilt=1.570796327, eid='SA.1674.CL')
sa_1683_cl = Sextupole(l=0.3164, k2=-14.820280660000002, tilt=1.570796327, eid='SA.1683.CL')
sa_1691_cl = Sextupole(l=0.3164, k2=2.8569510959987356, tilt=1.570796327, eid='SA.1691.CL')
sa_1692_cl = Sextupole(l=0.3164, k2=2.8569510959987356, tilt=1.570796327, eid='SA.1692.CL')
sa_1700_cl = Sextupole(l=0.3164, k2=-14.820280660000002, tilt=1.570796327, eid='SA.1700.CL')
sa_1708_cl = Sextupole(l=0.3164, k2=17.626614410000002, tilt=1.570796327, eid='SA.1708.CL')
sa_1710_cl = Sextupole(l=0.3164, k2=17.626614410000002, tilt=1.570796327, eid='SA.1710.CL')
sa_1719_cl = Sextupole(l=0.3164, k2=-14.820280660000002, tilt=1.570796327, eid='SA.1719.CL')
sa_1726_cl = Sextupole(l=0.3164, k2=2.8569510959987356, tilt=1.570796327, eid='SA.1726.CL')
sa_1728_cl = Sextupole(l=0.3164, k2=2.8569510959987356, tilt=1.570796327, eid='SA.1728.CL')
sa_1736_cl = Sextupole(l=0.3164, k2=-14.820280660000002, tilt=1.570796327, eid='SA.1736.CL')
sa_1744_cl = Sextupole(l=0.3164, k2=17.626614410000002, tilt=1.570796327, eid='SA.1744.CL')
sa_1782_cl = Sextupole(l=0.3164, k2=-17.626614410000002, tilt=1.570796327, eid='SA.1782.CL')
sa_1791_cl = Sextupole(l=0.3164, k2=14.820280660000002, tilt=1.570796327, eid='SA.1791.CL')
sa_1798_cl = Sextupole(l=0.3164, k2=-2.8569510959987356, tilt=1.570796327, eid='SA.1798.CL')
sa_1800_cl = Sextupole(l=0.3164, k2=-2.8569510959987356, tilt=1.570796327, eid='SA.1800.CL')
sa_1808_cl = Sextupole(l=0.3164, k2=14.820280660000002, tilt=1.570796327, eid='SA.1808.CL')
sa_1816_cl = Sextupole(l=0.3164, k2=-17.626614410000002, tilt=1.570796327, eid='SA.1816.CL')
sa_1818_cl = Sextupole(l=0.3164, k2=-17.626614410000002, tilt=1.570796327, eid='SA.1818.CL')
sa_1827_cl = Sextupole(l=0.3164, k2=14.820280660000002, tilt=1.570796327, eid='SA.1827.CL')
sa_1834_cl = Sextupole(l=0.3164, k2=-2.8569510959987356, tilt=1.570796327, eid='SA.1834.CL')
sa_1836_cl = Sextupole(l=0.3164, k2=-2.8569510959987356, tilt=1.570796327, eid='SA.1836.CL')
sa_1844_cl = Sextupole(l=0.3164, k2=14.820280660000002, tilt=1.570796327, eid='SA.1844.CL')
sa_1852_cl = Sextupole(l=0.3164, k2=-17.626614410000002, tilt=1.570796327, eid='SA.1852.CL')

# Hcors
cfx_1660_cl = Hcor(l=0.1, eid='CFX.1660.CL')
chx_1672_cl = Hcor(l=0.2, eid='CHX.1672.CL')
cfx_1683_cl = Hcor(l=0.1, eid='CFX.1683.CL')
cfx_1701_cl = Hcor(l=0.1, eid='CFX.1701.CL')
cfx_1719_cl = Hcor(l=0.1, eid='CFX.1719.CL')
cfx_1737_cl = Hcor(l=0.1, eid='CFX.1737.CL')
chx_1747_cl = Hcor(l=0.2, eid='CHX.1747.CL')
cfx_1755_cl = Hcor(l=0.1, eid='CFX.1755.CL')
cfx_1764_cl = Hcor(l=0.1, eid='CFX.1764.CL')
cfx_1773_cl = Hcor(l=0.1, eid='CFX.1773.CL')
chx_1780_cl = Hcor(l=0.2, eid='CHX.1780.CL')
cfx_1791_cl = Hcor(l=0.1, eid='CFX.1791.CL')
cfx_1809_cl = Hcor(l=0.1, eid='CFX.1809.CL')
cfx_1827_cl = Hcor(l=0.1, eid='CFX.1827.CL')
cfx_1845_cl = Hcor(l=0.1, eid='CFX.1845.CL')
chx_1855_tl = Hcor(l=0.2, eid='CHX.1855.TL')
cfx_1864_tl = Hcor(l=0.1, eid='CFX.1864.TL')
cfx_1873_tl = Hcor(l=0.1, eid='CFX.1873.TL')
cfx_1894_tl = Hcor(l=0.1, eid='CFX.1894.TL')
cfx_1925_tl = Hcor(l=0.1, eid='CFX.1925.TL')
bl_1939_tl = Hcor(l=0.2, eid='BL.1939.TL')
bl_1964_tl = Hcor(l=0.2, eid='BL.1964.TL')
chx_1965_tl = Hcor(l=0.2, eid='CHX.1965.TL')
chx_1967_tl = Hcor(l=0.2, eid='CHX.1967.TL')
cnx_1977_tl = Hcor(l=0.3, eid='CNX.1977.TL')

# Vcors
chy_1667_cl = Vcor(l=0.2, eid='CHY.1667.CL')
cfy_1674_cl = Vcor(l=0.1, eid='CFY.1674.CL')
cfy_1692_cl = Vcor(l=0.1, eid='CFY.1692.CL')
cfy_1710_cl = Vcor(l=0.1, eid='CFY.1710.CL')
cfy_1728_cl = Vcor(l=0.1, eid='CFY.1728.CL')
cfy_1746_cl = Vcor(l=0.1, eid='CFY.1746.CL')
chy_1753_cl = Vcor(l=0.2, eid='CHY.1753.CL')
cfy_1760_cl = Vcor(l=0.1, eid='CFY.1760.CL')
cfy_1768_cl = Vcor(l=0.1, eid='CFY.1768.CL')
chy_1774_cl = Vcor(l=0.2, eid='CHY.1774.CL')
cfy_1782_cl = Vcor(l=0.1, eid='CFY.1782.CL')
cfy_1800_cl = Vcor(l=0.1, eid='CFY.1800.CL')
cfy_1818_cl = Vcor(l=0.1, eid='CFY.1818.CL')
cfy_1836_cl = Vcor(l=0.1, eid='CFY.1836.CL')
cfy_1854_tl = Vcor(l=0.1, eid='CFY.1854.TL')
chy_1861_tl = Vcor(l=0.2, eid='CHY.1861.TL')
cfy_1869_tl = Vcor(l=0.1, eid='CFY.1869.TL')
cfy_1884_tl = Vcor(l=0.1, eid='CFY.1884.TL')
cfy_1910_tl = Vcor(l=0.1, eid='CFY.1910.TL')
cfy_1937_tl = Vcor(l=0.1, eid='CFY.1937.TL')
chy_1967_tl = Vcor(l=0.2, eid='CHY.1967.TL')
cny_1977_tl = Vcor(l=0.3, eid='CNY.1977.TL')

# Monitors
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

# Markers
tora_1658_cl = Marker(eid='TORA.1658.CL')
match_1673_cl = Marker(eid='MATCH.1673.CL')
otrb_1689_cl = Marker(eid='OTRB.1689.CL')
otrb_1725_cl = Marker(eid='OTRB.1725.CL')
tora_1765_cl = Marker(eid='TORA.1765.CL')
otrb_1797_cl = Marker(eid='OTRB.1797.CL')
otrb_1833_cl = Marker(eid='OTRB.1833.CL')
tora_1865_tl = Marker(eid='TORA.1865.TL')
otrbw_1899_tl = Marker(eid='OTRBW.1899.TL')
otrbw_1914_tl = Marker(eid='OTRBW.1914.TL')
otrbw_1929_tl = Marker(eid='OTRBW.1929.TL')
otre_1978_tl = Marker(eid='OTRE.1978.TL')
ensub_1980_tl = Marker(eid='ENSUB.1980.TL')

# Lattice 
cell = (d_1, tora_1658_cl, d_2, bpma_1659_cl, d_3, qf_1660_cl, d_4, cfx_1660_cl, d_5, 
chy_1667_cl, d_6, qh_1667_cl, d_7, qh_1669_cl, d_8, bpma_1669_cl, d_9, qh_1670_cl, d_7, 
qh_1671_cl, d_6, chx_1672_cl, d_12, match_1673_cl, qf_1673_cl, d_4, cfy_1674_cl, d_14, sa_1674_cl, 
d_15, bpmi_1675_cl, d_16, be_1678_cl, d_17, qf_1682_cl, d_4, cfx_1683_cl, d_14, sa_1683_cl, 
d_20, bpma_1684_cl, d_21, bl_1688_cl, d_22, otrb_1689_cl, d_23, sa_1691_cl, d_24, qf_1691_cl, 
d_4, cfy_1692_cl, d_14, sa_1692_cl, d_15, bpmi_1693_cl, d_28, bl_1695_cl, d_29, sa_1700_cl, 
d_24, qf_1700_cl, d_4, cfx_1701_cl, d_32, bpma_1702_cl, d_33, be_1705_cl, d_34, sa_1708_cl, 
d_24, qf_1709_cl, d_4, cfy_1710_cl, d_14, sa_1710_cl, d_20, bpma_1711_cl, d_39, be_1714_cl, 
d_17, qf_1718_cl, d_4, cfx_1719_cl, d_14, sa_1719_cl, d_20, bpma_1720_cl, d_21, bl_1724_cl, 
d_22, otrb_1725_cl, d_23, sa_1726_cl, d_24, qf_1727_cl, d_4, cfy_1728_cl, d_14, sa_1728_cl, 
d_15, bpmi_1729_cl, d_28, bl_1731_cl, d_29, sa_1736_cl, d_24, qf_1736_cl, d_4, cfx_1737_cl, 
d_32, bpma_1738_cl, d_33, be_1741_cl, d_34, sa_1744_cl, d_24, qf_1745_cl, d_4, cfy_1746_cl, 
d_60, bpma_1746_cl, d_61, chx_1747_cl, d_6, qh_1748_cl, d_7, qh_1749_cl, d_8, bpma_1750_cl, 
d_9, qh_1751_cl, d_7, qh_1752_cl, d_6, chy_1753_cl, d_68, qf_1754_cl, d_4, cfx_1755_cl, 
d_32, bpma_1756_cl, d_71, qf_1759_cl, d_4, cfy_1760_cl, d_32, bpma_1761_cl, d_74, qf_1763_cl, 
d_4, cfx_1764_cl, d_32, bpma_1765_cl, d_77, tora_1765_cl, d_78, qf_1767_cl, d_4, cfy_1768_cl, 
d_32, bpma_1769_cl, d_71, qf_1772_cl, d_4, cfx_1773_cl, d_60, bpma_1773_cl, d_84, chy_1774_cl, 
d_6, qh_1775_cl, d_7, qh_1776_cl, d_8, bpma_1777_cl, d_9, qh_1778_cl, d_7, qh_1779_cl, 
d_6, chx_1780_cl, d_91, qf_1781_cl, d_4, cfy_1782_cl, d_14, sa_1782_cl, d_20, bpma_1783_cl, 
d_39, be_1786_cl, d_17, qf_1790_cl, d_4, cfx_1791_cl, d_14, sa_1791_cl, d_20, bpma_1792_cl, 
d_21, bl_1796_cl, d_22, otrb_1797_cl, d_23, sa_1798_cl, d_24, qf_1799_cl, d_4, cfy_1800_cl, 
d_14, sa_1800_cl, d_20, bpma_1801_cl, d_107, bl_1803_cl, d_29, sa_1808_cl, d_24, qf_1808_cl, 
d_4, cfx_1809_cl, d_32, bpma_1810_cl, d_33, be_1813_cl, d_34, sa_1816_cl, d_24, qf_1817_cl, 
d_4, cfy_1818_cl, d_14, sa_1818_cl, d_20, bpma_1819_cl, d_39, be_1822_cl, d_17, qf_1826_cl, 
d_4, cfx_1827_cl, d_14, sa_1827_cl, d_20, bpma_1828_cl, d_21, bl_1832_cl, d_22, otrb_1833_cl, 
d_23, sa_1834_cl, d_24, qf_1835_cl, d_4, cfy_1836_cl, d_14, sa_1836_cl, d_15, bpmi_1837_cl, 
d_28, bl_1839_cl, d_29, sa_1844_cl, d_24, qf_1844_cl, d_4, cfx_1845_cl, d_32, bpma_1846_cl, 
d_33, be_1849_cl, d_34, sa_1852_cl, d_137, bpma_1853_cl, d_3, qf_1853_cl, d_4, cfy_1854_tl, 
d_140, chx_1855_tl, d_6, qh_1855_tl, d_7, qh_1857_tl, d_143, qh_1858_tl, d_7, qh_1859_tl, 
d_145, bpmi_1860_tl, d_146, chy_1861_tl, d_147, bpmi_1863_tl, d_148, qf_1864_tl, d_4, cfx_1864_tl, 
d_32, tora_1865_tl, d_151, bpma_1868_tl, d_3, qf_1868_tl, d_4, cfy_1869_tl, d_154, bpma_1873_tl, 
d_3, qf_1873_tl, d_4, cfx_1873_tl, d_157, bpmi_1878_tl, d_158, qf_1881_tl, d_159, cfy_1884_tl, 
d_160, bpmi_1889_tl, d_158, qf_1892_tl, d_162, cfx_1894_tl, d_163, otrbw_1899_tl, d_164, qf_1907_tl, 
d_165, bpmi_1910_tl, d_146, cfy_1910_tl, d_167, otrbw_1914_tl, d_164, qf_1922_tl, d_165, bpmi_1925_tl, 
d_146, cfx_1925_tl, d_167, otrbw_1929_tl, d_172, bpmi_1930_tl, d_173, qf_1937_tl, d_4, cfy_1937_tl, 
d_175, bpmi_1939_tl, d_176, bl_1939_tl, d_177, qf_1952_tl, d_177, bl_1964_tl, d_179, chx_1965_tl, 
d_180, bpma_1966_tl, d_181, qf_1967_tl, d_182, chx_1967_tl, d_183, chy_1967_tl, d_184, cnx_1977_tl, 
d_185, cny_1977_tl, d_186, bpmd_1977_tl, d_183, otre_1978_tl, d_188, ensub_1980_tl)

# power supplies 

#  
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
