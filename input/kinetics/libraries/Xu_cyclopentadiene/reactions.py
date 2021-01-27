#!/usr/bin/env python
# encoding: utf-8

name = "Xu_cyclopentadiene"
shortDesc = "Cyclopentadiene and C5 alkene reactions obtained from Xu et al."
longDesc = """
Kinetic parameters for reactions among C5 compounds
were obtained from regression analysis of experimental
reaction data from Xu et al. DOI: 10.1021/acs.iecr.9b04018
Ind. Eng. Chem. Res. 2019, 58, 22516−22525
"""
entry(
    index = 0,
    label = 'CPD + CPD <=> DCPD_endo',
    kinetics = Arrhenius(
        A = (8.49e+7, 'L/(mol*min)', '+|-', 0.11e+7),
        n = 0,
        Ea = (68.8, 'kJ/mol', '+|-', 0.7),
        T0 = (1, 'K'),
    ),
    shortDesc = "Obtained experimentally by Xu et al.",
    longDesc = """Kinetic parameters for reactions among C5 compounds
were obtained from regression analysis of experimental
reaction data from Xu et al. Table 1 entry 1 in DOI: 10.1021/acs.iecr.9b04018
Ind. Eng. Chem. Res. 2019, 58, 22516−22525"""
)

entry(
    index = 1,
    label = 'ISP + ISP <=> DISP_1',
    kinetics = Arrhenius(
        A = (3.05e+8, 'L/(mol*min)', '+|-', 0.06e+8),
        n = 0,
        Ea = (105.2, 'kJ/mol', '+|-', 1.2),
        T0 = (1, 'K'),
    ),
    shortDesc = "Obtained from experimental data by Xu et al.",
    longDesc = """Kinetic parameters for reactions among C5 compounds
were obtained from regression analysis of experimental
reaction data from Xu et al. Table 1 entry 4 in DOI: 10.1021/acs.iecr.9b04018
Ind. Eng. Chem. Res. 2019, 58, 22516−22525"""
)

entry(
    index = 2,
    label = 'ISP + ISP <=> DISP_2',
    kinetics = Arrhenius(
        A = (2.50e+9, 'L/(mol*min)', '+|-', 0.13e+9),
        n = 0,
        Ea = (109.7, 'kJ/mol', '+|-', 3.7),
        T0 = (1, 'K'),
    ),
    shortDesc = "Obtained from experimental data by Xu et al.",
    longDesc = """Kinetic parameters for reactions among C5 compounds
were obtained from regression analysis of experimental
reaction data from Xu et al. Table 1 entry 5 in DOI: 10.1021/acs.iecr.9b04018
Ind. Eng. Chem. Res. 2019, 58, 22516−22525"""
)

entry(
    index = 3,
    label = 'ISP + ISP <=> DISP_3',
    kinetics = Arrhenius(
        A = (2.54e+7, 'L/(mol*min)', '+|-', 0.06e+7),
        n = 0,
        Ea = (90.3, 'kJ/mol', '+|-', 1.4),
        T0 = (1, 'K'),
    ),
    shortDesc = "Obtained from experimental data by Xu et al.",
    longDesc = """Kinetic parameters for reactions among C5 compounds
were obtained from regression analysis of experimental
reaction data from Xu et al. Table 1 entry 6 in DOI: 10.1021/acs.iecr.9b04018
Ind. Eng. Chem. Res. 2019, 58, 22516−22525"""
)

entry(
    index = 4,
    label = 'ISP + ISP <=> DISP_4',
    kinetics = Arrhenius(
        A = (1.26e+8, 'L/(mol*min)', '+|-', 0.03e+8),
        n = 0,
        Ea = (96.9, 'kJ/mol', '+|-', 1.5),
        T0 = (1, 'K'),
    ),
    shortDesc = "Obtained from experimental data by Xu et al.",
    longDesc = """Kinetic parameters for reactions among C5 compounds
were obtained from regression analysis of experimental
reaction data from Xu et al. Table 1 entry 7 in DOI: 10.1021/acs.iecr.9b04018
Ind. Eng. Chem. Res. 2019, 58, 22516−22525"""
)

entry(
    index = 8,
    label = 'CPD + ISP <=> CPD-ISP_2',
    kinetics = Arrhenius(
        A = (6.57e+7, 'L/(mol*min)', '+|-', 0.16e+7),
        n = 0,
        Ea = (81.1, 'kJ/mol', '+|-', 1.5),
        T0 = (1, 'K'),
    ),
    shortDesc = "Obtained from experimental data by Xu et al.",
    longDesc = """Kinetic parameters for reactions among C5 compounds
were obtained from regression analysis of experimental
reaction data from Xu et al. Table 1 entry 10 in DOI: 10.1021/acs.iecr.9b04018
Ind. Eng. Chem. Res. 2019, 58, 22516−22525"""
)

entry(
    index = 9,
    label = 'CPD + ISP <=> CPD-ISP_3',
    kinetics = Arrhenius(
        A = (5.08e+6, 'L/(mol*min)', '+|-', 0.18e+6),
        n = 0,
        Ea = (77.9, 'kJ/mol', '+|-', 2.0),
        T0 = (1, 'K'),
    ),
    shortDesc = "Obtained from experimental data by Xu et al.",
    longDesc = """Kinetic parameters for reactions among C5 compounds
were obtained from regression analysis of experimental
reaction data from Xu et al. Table 1 entry 11 in DOI: 10.1021/acs.iecr.9b04018
Ind. Eng. Chem. Res. 2019, 58, 22516−22525"""
)

entry(
    index = 10,
    label = 'CPD-ISP_2 <=> CPD-ISP_3',
    kinetics = Arrhenius(
        A = (1.05e+16, '1/min', '+|-', 0.04e+16),
        n = 0,
        Ea = (151.8, 'kJ/mol', '+|-', 5.2),
        T0 = (1, 'K'),
    ),
    shortDesc = "Obtained from experimental data by Xu et al.",
    longDesc = """Kinetic parameters for reactions among C5 compounds
were obtained from regression analysis of experimental
reaction data from Xu et al. Table 1 entry 12 in DOI: 10.1021/acs.iecr.9b04018
Ind. Eng. Chem. Res. 2019, 58, 22516−22525"""
)

entry(
    index = 12,
    label = 'CPD + ISP <=> CPD-ISP_6',
    kinetics = Arrhenius(
        A = (2.30e+4, 'L/(mol*min)', '+|-', 0.65e+4),
        n = 0,
        Ea = (67.5, 'kJ/mol', '+|-', 9.5),
        T0 = (1, 'K'),
    ),
    shortDesc = "Obtained from experimental data by Xu et al.",
    longDesc = """Kinetic parameters for reactions among C5 compounds
were obtained from regression analysis of experimental
reaction data from Xu et al. Table 1 entry 14 in DOI: 10.1021/acs.iecr.9b04018
Ind. Eng. Chem. Res. 2019, 58, 22516−22525"""
)

entry(
    index = 13,
    label = 'tP + tP <=> DtP_1',
    kinetics = Arrhenius(
        A = (3.88e+7, 'L/(mol*min)', '+|-', 0.66e+7),
        n = 0,
        Ea = (100.7, 'kJ/mol', '+|-', 2.5),
        T0 = (1, 'K'),
    ),
    shortDesc = "Obtained from experimental data by Xu et al.",
    longDesc = """Kinetic parameters for reactions among C5 compounds
were obtained from regression analysis of experimental
reaction data from Xu et al. Table 1 entry 15 in DOI: 10.1021/acs.iecr.9b04018
Ind. Eng. Chem. Res. 2019, 58, 22516−22525"""
)

entry(
    index = 14,
    label = 'tP + tP <=> DtP_2',
    kinetics = Arrhenius(
        A = (3.18e+8, 'L/(mol*min)', '+|-', 0.14e+8),
        n = 0,
        Ea = (108.2, 'kJ/mol', '+|-', 2.9),
        T0 = (1, 'K'),
    ),
    shortDesc = "Obtained from experimental data by Xu et al.",
    longDesc = """Kinetic parameters for reactions among C5 compounds
were obtained from regression analysis of experimental
reaction data from Xu et al. Table 1 entry 16 in DOI: 10.1021/acs.iecr.9b04018
Ind. Eng. Chem. Res. 2019, 58, 22516−22525"""
)

entry(
    index = 16,
    label = 'tP +tP <=> DtP_4',
    kinetics = Arrhenius(
        A = (1.27e+7, 'L/(mol*min)', '+|-', 0.13e+7),
        n = 0,
        Ea = (97.5, 'kJ/mol', '+|-', 5.8),
        T0 = (1, 'K'),
    ),
    shortDesc = "Obtained from experimental data by Xu et al.",
    longDesc = """Kinetic parameters for reactions among C5 compounds
were obtained from regression analysis of experimental
reaction data from Xu et al. Table 1 entry 18 in DOI: 10.1021/acs.iecr.9b04018
Ind. Eng. Chem. Res. 2019, 58, 22516−22525"""
)

entry(
    index = 18,
    label = 'tP +tP <=> DtP_6',
    kinetics = Arrhenius(
        A = (8.09e+6, 'L/(mol*min)', '+|-', 0.21e+6),
        n = 0,
        Ea = (89.6, 'kJ/mol', '+|-', 1.4),
        T0 = (1, 'K'),
    ),
    shortDesc = "Obtained from experimental data by Xu et al.",
    longDesc = """Kinetic parameters for reactions among C5 compounds
were obtained from regression analysis of experimental
reaction data from Xu et al. Table 1 entry 20 in DOI: 10.1021/acs.iecr.9b04018
Ind. Eng. Chem. Res. 2019, 58, 22516−22525"""
)

entry(
    index = 20,
    label = 'CPD + tP <=> CPD-tP_1',
    kinetics = Arrhenius(
        A = (9.62e+6, 'L/(mol*min)', '+|-', 0.64e+6),
        n = 0,
        Ea = (88.2, 'kJ/mol', '+|-', 3.5),
        T0 = (1, 'K'),
    ),
    shortDesc = "Obtained from experimental data by Xu et al.",
    longDesc = """Kinetic parameters for reactions among C5 compounds
were obtained from regression analysis of experimental
reaction data from Xu et al. Table 1 entry 22 in DOI: 10.1021/acs.iecr.9b04018
Ind. Eng. Chem. Res. 2019, 58, 22516−22525"""
)

entry(
    index = 22,
    label = 'CPD +tP <=> CPD-tP_3',
    kinetics = Arrhenius(
        A = (1.76e+7, 'L/(mol*min)', '+|-', 0.05e+7),
        n = 0,
        Ea = (80.3, 'kJ/mol', '+|-', 1.6),
        T0 = (1, 'K'),
    ),
    shortDesc = "Obtained from experimental data by Xu et al.",
    longDesc = """Kinetic parameters for reactions among C5 compounds
were obtained from regression analysis of experimental
reaction data from Xu et al. Table 1 entry 24 in DOI: 10.1021/acs.iecr.9b04018
Ind. Eng. Chem. Res. 2019, 58, 22516−22525"""
)

entry(
    index = 24,
    label = 'CPD + tP <=> CPD-tP_5',
    kinetics = Arrhenius(
        A = (4.58e+7, 'L/(mol*min)', '+|-', 0.47e+7),
        n = 0,
        Ea = (96.1, 'kJ/mol', '+|-', 5.9),
        T0 = (1, 'K'),
    ),
    shortDesc = "Obtained from experimental data by Xu et al.",
    longDesc = """Kinetic parameters for reactions among C5 compounds
were obtained from regression analysis of experimental
reaction data from Xu et al. Table 1 entry 26 in DOI: 10.1021/acs.iecr.9b04018
Ind. Eng. Chem. Res. 2019, 58, 22516−22525"""
)

entry(
    index = 25,
    label = 'CPD + tP <=> CPD-tP_6',
    kinetics = Arrhenius(
        A = (2.46e+8, 'L/(mol*min)', '+|-', 0.11e+8),
        n = 0,
        Ea = (93.3, 'kJ/mol', '+|-', 2.8),
        T0 = (1, 'K'),
    ),
    shortDesc = "Obtained from experimental data by Xu et al.",
    longDesc = """Kinetic parameters for reactions among C5 compounds
were obtained from regression analysis of experimental
reaction data from Xu et al. Table 1 entry 27 in DOI: 10.1021/acs.iecr.9b04018
Ind. Eng. Chem. Res. 2019, 58, 22516−22525"""
)

entry(
    index = 27,
    label = 'CPD + 1P <=> CPD-1P_2',
    kinetics = Arrhenius(
        A = (7.93e+5, 'L/(mol*min)', '+|-', 0.35e+5),
        n = 0,
        Ea = (79.7, 'kJ/mol', '+|-', 2.0),
        T0 = (1, 'K'),
    ),
    shortDesc = "Obtained from experimental data by Xu et al.",
    longDesc = """Kinetic parameters for reactions among C5 compounds
were obtained from regression analysis of experimental
reaction data from Xu et al. Table 1 entry 29 in DOI: 10.1021/acs.iecr.9b04018
Ind. Eng. Chem. Res. 2019, 58, 22516−22525"""
)

entry(
    index = 28,
    label = 'CPD + t2P <=> CPD-t2P_1',
    kinetics = Arrhenius(
        A = (1.76e+7, 'L/(mol*min)', '+|-', 0.13e+7),
        n = 0,
        Ea = (96.5, 'kJ/mol', '+|-', 4.1),
        T0 = (1, 'K'),
    ),
    shortDesc = "Obtained from experimental data by Xu et al.",
    longDesc = """Kinetic parameters for reactions among C5 compounds
were obtained from regression analysis of experimental
reaction data from Xu et al. Table 1 entry 30 in DOI: 10.1021/acs.iecr.9b04018
Ind. Eng. Chem. Res. 2019, 58, 22516−22525"""
)

entry(
    index = 30,
    label = 'CPD + 2B <=> CPD-2B',
    kinetics = Arrhenius(
        A = (2.65e+9, 'L/(mol*min)'),
        n = 0,
        Ea = (109.5, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = "Obtained from experimental data by Xu et al.",
    longDesc = """Kinetic parameters for reactions among C5 compounds
were obtained from regression analysis of experimental
reaction data from Xu et al. Table 1 entry 33 in DOI: 10.1021/acs.iecr.9b04018
Ind. Eng. Chem. Res. 2019, 58, 22516−22525"""
)

entry(
    index = 31,
    label = 'CPD + 1B <=> CPD-1B',
    kinetics = Arrhenius(
        A = (1.11e+9, 'L/(mol*min)'),
        n = 0,
        Ea = (105.9, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = "Obtained from experimental data by Xu et al.",
    longDesc = """Kinetic parameters for reactions among C5 compounds
were obtained from regression analysis of experimental
reaction data from Xu et al. Table 1 entry 34 in DOI: 10.1021/acs.iecr.9b04018
Ind. Eng. Chem. Res. 2019, 58, 22516−22525"""
)
