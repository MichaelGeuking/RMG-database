#!/usr/bin/env python
# encoding: utf-8

name = "H_Abstraction/rules"
shortDesc = u""
longDesc = u"""
General comments go at the top of the file,

or in a section(s) titled 'General'

.. the ID must match those in the rateLibrary AS A STRING (ie. '2' is different from '02')


.. [MRHCBSQB3RRHO] M.R. Harper (mrharper_at_mit_dot_edu or michael.harper.jr_at_gmail_dot_com)
The geometries of all reactants, products, and the transition state were optimized using the CBS-QB3 calculations.  The zero-point
energy is that computed by the CBS-QB3 calculations.  The frequencies were computed with B3LYP/CBSB7.
In computing k(T), an asymmetric tunneling correction was employed, the calculated frequencies were scaled by 0.99, and the 
temperatures used were: 300, 331, 370, 419, 482, 568, 692, 885, 1227, 2000 (evenly spaced on inverse temperature scale).

.. [Tsang1990] W. Tsang; "Chemical kinetic database for combustion chemistry. Part IV. Isobutane" J. Phys. Chem. Ref. Data 19 (1990) 1-68

.. [Tsang1991] W. Tsang; "Chemical kinetic database for combustion chemistry. Part V. Propene" J. Phys. Chem. Ref. Data 20 (1991) 221-273
"""
recommended = True

entry(
    index = 0,
    label = "X_H_or_Xrad_H;Y_rad_birad",
    group1 = "OR{X_H, Xrad_H}",
    group2 = "OR{Y_2centeradjbirad, Y_1centerbirad, Y_rad}",
    kinetics = ArrheniusEP(
        A = (100000, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (10, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = 
u"""
If a biradical CH2JJ can abstract from RCH4 to make RCH3J and CH3J 
then a Y_rad CH3J should be able to abstract from RCH3J which means X_H needs 
to include Xrad_H. I.e. you can abstract from a radical. To make this possible
a head node has been created X_H_or_Xrad_H which is a union of X_H and Xrad_H.
The kinetics for it have just been copied from X_H and are only defined for 
abstraction by Y_rad_birad. I.e. the top level very approximate guess.

Do better kinetics for this exist? Do we in fact use the reverse kinetics anyway?
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1,
    label = "X_H;Y_rad_birad",
    group1 = 
"""
1 *1 R 0 {2,S}
2 *2 H 0 {1,S}
""",
    group2 = "OR{Y_2centeradjbirad, Y_1centerbirad, Y_rad}",
    kinetics = ArrheniusEP(
        A = (100000, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (10, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 2,
    label = "X_H;H_rad",
    group1 = 
"""
1 *1 R 0 {2,S}
2 *2 H 0 {1,S}
""",
    group2 = 
"""
1 *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (240000000.0, 'cm^3/(mol*s)'),
        n = 1.5,
        alpha = 0.65,
        E0 = (9.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""Dean, A. M. [118]""",
    longDesc = 
u"""
[118] Dean, A.M. Development and application of Detailed Kinetic Mechanisms for Free Radical Systems.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 3,
    label = "X_H;O_atom_triplet",
    group1 = 
"""
1 *1 R 0 {2,S}
2 *2 H 0 {1,S}
""",
    group2 = 
"""
1 *3 O 2T
""",
    kinetics = ArrheniusEP(
        A = (170000000.0, 'cm^3/(mol*s)'),
        n = 1.5,
        alpha = 0.75,
        E0 = (6.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""Dean, A. M. [118]""",
    longDesc = 
u"""
[118] Dean, A.M. Development and application of Detailed Kinetic Mechanisms for Free Radical Systems.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 4,
    label = "X_H;O_pri_rad",
    group1 = 
"""
1 *1 R 0 {2,S}
2 *2 H 0 {1,S}
""",
    group2 = 
"""
1 *3 O 1 {2,S}
2    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1200000.0, 'cm^3/(mol*s)'),
        n = 2,
        alpha = 0.5,
        E0 = (10.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""Dean, A. M. [118]""",
    longDesc = 
u"""
[118] Dean, A.M. Development and application of Detailed Kinetic Mechanisms for Free Radical Systems.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 5,
    label = "X_H;O_sec_rad",
    group1 = 
"""
1 *1 R 0 {2,S}
2 *2 H 0 {1,S}
""",
    group2 = 
"""
1 *3 O   1 {2,S}
2    R!H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (14000, 'cm^3/(mol*s)'),
        n = 2.69,
        alpha = 0.6,
        E0 = (11.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""Dean, A. M. [118]""",
    longDesc = 
u"""
[118] Dean, A.M. Development and application of Detailed Kinetic Mechanisms for Free Radical Systems.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 6,
    label = "X_H;C_methyl",
    group1 = 
"""
1 *1 R 0 {2,S}
2 *2 H 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (810000, 'cm^3/(mol*s)'),
        n = 1.87,
        alpha = 0.65,
        E0 = (13, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""Dean, A. M. [118]""",
    longDesc = 
u"""
[118] Dean, A.M. Development and application of Detailed Kinetic Mechanisms for Free Radical Systems.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 7,
    label = "C/H/Cs3;C_rad/Cs3",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cs 0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.13, 'cm^3/(mol*s)'),
        n = 3.71,
        alpha = 0,
        E0 = (6.85, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy CBS-Q calculations. Rate expression per H atom.""",
    longDesc = 
u"""
Sumathy CBS-Q calculations. Rate expression per H atom.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 8,
    label = "C/H2/NonDeC;C_rad/Cs3",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cs 0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.26, 'cm^3/(mol*s)'),
        n = 3.55,
        alpha = 0,
        E0 = (8.31, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy CBS-Q calculations. Rate expression per H atom.""",
    longDesc = 
u"""
Sumathy CBS-Q calculations. Rate expression per H atom.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 9,
    label = "C/H3/Cs;C_rad/Cs3",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cs 0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (2.85, 'cm^3/(mol*s)'),
        n = 3.62,
        alpha = 0,
        E0 = (11.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy CBS-Q calculations. Rate expression per H atom.""",
    longDesc = 
u"""
Sumathy CBS-Q calculations. Rate expression per H atom.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 10,
    label = "C/H/Cs3;C_rad/H/NonDeC",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (55.8, 'cm^3/(mol*s)'),
        n = 3.01,
        alpha = 0,
        E0 = (7.34, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy CBS-Q calculations. Rate expression per H atom.""",
    longDesc = 
u"""
Sumathy CBS-Q calculations. Rate expression per H atom.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 11,
    label = "C/H2/NonDeC;C_rad/H/NonDeC",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (15.2, 'cm^3/(mol*s)'),
        n = 3.19,
        alpha = 0,
        E0 = (10.31, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy CBS-Q calculations. Rate expression per H atom.""",
    longDesc = 
u"""
Sumathy CBS-Q calculations. Rate expression per H atom.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 12,
    label = "C/H3/Cs;C_rad/H/NonDeC",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (47.1, 'cm^3/(mol*s)'),
        n = 3.23,
        alpha = 0,
        E0 = (12.27, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy CBS-Q calculations. Rate expression per H atom.""",
    longDesc = 
u"""
Sumathy CBS-Q calculations. Rate expression per H atom.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 13,
    label = "C/H/Cs3;C_rad/H2/Cs",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    H  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (4220, 'cm^3/(mol*s)'),
        n = 2.51,
        alpha = 0,
        E0 = (8.06, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy CBS-Q calculations. Rate expression per H atom.""",
    longDesc = 
u"""
Sumathy CBS-Q calculations. Rate expression per H atom.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 14,
    label = "C/H2/NonDeC;C_rad/H2/Cs",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    H  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1540, 'cm^3/(mol*s)'),
        n = 2.66,
        alpha = 0,
        E0 = (10.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy CBS-Q calculations. Rate expression per H atom.""",
    longDesc = 
u"""
Sumathy CBS-Q calculations. Rate expression per H atom.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 15,
    label = "C/H3/Cs;C_rad/H2/Cs",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    H  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (659, 'cm^3/(mol*s)'),
        n = 2.71,
        alpha = 0,
        E0 = (12.92, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy CBS-Q calculations. Rate expression per H atom.""",
    longDesc = 
u"""
Sumathy CBS-Q calculations. Rate expression per H atom.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 16,
    label = "C/H/Cs3;C_methyl",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (574000, 'cm^3/(mol*s)'),
        n = 1.83,
        alpha = 0,
        E0 = (6.94, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy CBS-Q calculations. Rate expression per H atom.""",
    longDesc = 
u"""
Sumathy CBS-Q calculations. Rate expression per H atom.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 17,
    label = "C/H2/NonDeC;C_methyl",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1450000.0, 'cm^3/(mol*s)'),
        n = 1.77,
        alpha = 0,
        E0 = (8.53, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy CBS-Q calculations. Rate expression per H atom.""",
    longDesc = 
u"""
Sumathy CBS-Q calculations. Rate expression per H atom.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 18,
    label = "C/H3/Cs;C_methyl",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (278000, 'cm^3/(mol*s)'),
        n = 1.9,
        alpha = 0,
        E0 = (11.05, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy CBS-Q calculations. Rate expression per H atom.""",
    longDesc = 
u"""
Sumathy CBS-Q calculations. Rate expression per H atom.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 19,
    label = "C_methane;C_methyl",
    group1 = 
"""
1 *1 C 0 {2,S} {3,S} {4,S} {5,S}
2 *2 H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
5    H 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (10100, 'cm^3/(mol*s)'),
        n = 2.47,
        alpha = 0,
        E0 = (13.96, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy CBS-Q calculations. Rate expression per H atom.""",
    longDesc = 
u"""
Sumathy CBS-Q calculations. Rate expression per H atom.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 20,
    label = "C/H/Cs3;H_rad",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (483000000.0, 'cm^3/(mol*s)'),
        n = 1.54,
        alpha = 0,
        E0 = (2.98, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy CBS-Q calculations. Rate expression per H atom.""",
    longDesc = 
u"""
Sumathy CBS-Q calculations. Rate expression per H atom.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 21,
    label = "C/H2/NonDeC;H_rad",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (130000000.0, 'cm^3/(mol*s)'),
        n = 1.69,
        alpha = 0,
        E0 = (4.78, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy CBS-Q calculations. Rate expression per H atom.""",
    longDesc = 
u"""
Sumathy CBS-Q calculations. Rate expression per H atom.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 22,
    label = "C/H3/Cs;H_rad",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (62800000.0, 'cm^3/(mol*s)'),
        n = 1.75,
        alpha = 0,
        E0 = (7.51, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy CBS-Q calculations. Rate expression per H atom.""",
    longDesc = 
u"""
Sumathy CBS-Q calculations. Rate expression per H atom.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 23,
    label = "C_methane;H_rad",
    group1 = 
"""
1 *1 C 0 {2,S} {3,S} {4,S} {5,S}
2 *2 H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
5    H 0 {1,S}
""",
    group2 = 
"""
1 *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (30600000.0, 'cm^3/(mol*s)'),
        n = 1.87,
        alpha = 0,
        E0 = (10.59, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy CBS-Q calculations. Rate expression per H atom.""",
    longDesc = 
u"""
Sumathy CBS-Q calculations. Rate expression per H atom.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 24,
    label = "H2;C_rad/H2/S",
    group1 = 
"""
1 *1 H 0 {2,S}
2 *2 H 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    S 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.008, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (13.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 24,
    label = "O/H/NonDeC;H_rad",
    group1 = 
"""
1 *1 O  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (870000000.0, 'cm^3/(mol*s)'),
        n = 1.39,
        alpha = 0,
        E0 = (10.07, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy CBS-Q calculations. Rate expression per H atom.""",
    longDesc = 
u"""
Sumathy CBS-Q calculations. Rate expression per H atom.
Sumathi, R.; Carstensen, H.-H.; Green, W.H. Jr.; J. Phys. Chem. A. 2001, 105, 8978

Table 8: Modified ArrHenius Fitted Parameters for GA Predicted Rates.

ROH + H --> RO + H2

Verified by Karma James
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 25,
    label = "CO_pri;H_rad",
    group1 = 
"""
1 *1 C 0 {2,D} {3,S} {4,S}
2    O 0 {1,D}
3 *2 H 0 {1,S}
4    H 0 {1,S}
""",
    group2 = 
"""
1 *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (54800000.0, 'cm^3/(mol*s)'),
        n = 1.82,
        alpha = 0,
        E0 = (2.44, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy CBS-Q calculations. Rate expression per H atom.""",
    longDesc = 
u"""
Sumathy CBS-Q calculations. Rate expression per H atom.
Sumathi, R.; Carstensen, H.-H.; Green, W.H. Jr.; J. Phys. Chem. A. 2001, 105, 8978

Table 8: Modified ArrHenius Fitted Parameters for GA Predicted Rates.

HCHO + H --> HCO + H2

Verified by Karma James
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 25,
    label = "H2;C_rad/H/CsS",
    group1 = 
"""
1 *1 H 0 {2,S}
2 *2 H 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0143, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (13.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 26,
    label = "CO/H/NonDe;H_rad",
    group1 = 
"""
1 *1 C        0 {2,D} {3,S} {4,S}
2    O        0 {1,D}
3 *2 H        0 {1,S}
4    {Cs,O,S} 0 {1,S}
""",
    group2 = 
"""
1 *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (80700000.0, 'cm^3/(mol*s)'),
        n = 1.76,
        alpha = 0,
        E0 = (0.67, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy CBS-Q calculations. Rate expression per H atom.""",
    longDesc = 
u"""
Sumathy CBS-Q calculations. Rate expression per H atom.
Sumathi, R.; Carstensen, H.-H.; Green, W.H. Jr.; J. Phys. Chem. A. 2001, 105, 8978

Table 8: Modified ArrHenius Fitted Parameters for GA Predicted Rates.

RCHO + H --> RCO + H2

Verified by Karma James
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 26,
    label = "H2;C_rad/Cs2S",
    group1 = 
"""
1 *1 H 0 {2,S}
2 *2 H 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    S  0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00576, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (12.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 27,
    label = "Cd_pri;H_rad",
    group1 = 
"""
1 *1 C 0 {2,D} {3,S} {4,S}
2    C 0 {1,D}
3 *2 H 0 {1,S}
4    H 0 {1,S}
""",
    group2 = 
"""
1 *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (25300000.0, 'cm^3/(mol*s)'),
        n = 1.98,
        alpha = 0,
        E0 = (11.78, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy CBS-Q calculations. Rate expression per H atom. Primary vinylic {Cd/H2}""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 27,
    label = "H2;Cd_rad/NonDeS",
    group1 = 
"""
1 *1 H 0 {2,S}
2 *2 H 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,D} {3,S}
2    C 0 {1,D}
3    S 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0478, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (5.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""
Sumathy CBS-Q calculations. Rate expression per H atom.
Sumathi, R.; Carstensen, H.-H.; Green, W.H. Jr.; J. Phys. Chem. A. 2001, 105, 8978

Table 8: Modified ArrHenius Fitted Parameters for GA Predicted Rates.

R2C=CH2 + H --> R2C=CH + H2

Verified by Karma James
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 28,
    label = "Cd_pri;H_rad",
    group1 = 
"""
1 *1 C 0 {2,D} {3,S} {4,S}
2    C 0 {1,D}
3 *2 H 0 {1,S}
4    H 0 {1,S}
""",
    group2 = 
"""
1 *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (4530, 'cm^3/(mol*s)'),
        n = 2.43,
        alpha = 0,
        E0 = (8.85, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy CBS-Q calculations. Rate expression per H atom. Ketene hydrogen {CCO/H2}""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 28,
    label = "H2;C_rad/H/CdS",
    group1 = 
"""
1 *1 H 0 {2,S}
2 *2 H 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cd 0 {1,S}
4    S  0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0789, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (24.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""
Sumathy CBS-Q calculations. Rate expression per H atom.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 29,
    label = "Cd_pri;H_rad",
    group1 = 
"""
1 *1 C 0 {2,D} {3,S} {4,S}
2    C 0 {1,D}
3 *2 H 0 {1,S}
4    H 0 {1,S}
""",
    group2 = 
"""
1 *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (14600000.0, 'cm^3/(mol*s)'),
        n = 2.09,
        alpha = 0,
        E0 = (5.49, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy CBS-Q calculations. Rate expression per H atom. Allene hydrogen {Cd/H2/Ca}""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 29,
    label = "H2;C_rad/CdCsS",
    group1 = 
"""
1 *1 H 0 {2,S}
2 *2 H 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cd 0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00997, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (24.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""
Sumathy CBS-Q calculations. Rate expression per H atom.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 30,
    label = "Cd/H/NonDeC;H_rad",
    group1 = 
"""
1 *1 C  0 {2,D} {3,S} {4,S}
2    C  0 {1,D}
3 *2 H  0 {1,S}
4    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (29800000.0, 'cm^3/(mol*s)'),
        n = 1.95,
        alpha = 0,
        E0 = (8.65, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy CBS-Q calculations. Rate expression per H atom.""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 30,
    label = "H2;C_rad/H/CtS",
    group1 = 
"""
1 *1 H 0 {2,S}
2 *2 H 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Ct 0 {1,S}
4    S  0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0469, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (22.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""
Sumathy CBS-Q calculations. Rate expression per H atom.
Sumathi, R.; Carstensen, H.-H.; Green, W.H. Jr.; J. Phys. Chem. A. 2001, 105, 8978

Table 8: Modified ArrHenius Fitted Parameters for GA Predicted Rates.

RCH=CR2 + H --> RC=CR2 + H2

Verified by Karma James
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 31,
    label = "C/H3/Cd;H_rad",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    Cd 0 {1,S}
""",
    group2 = 
"""
1 *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (433000, 'cm^3/(mol*s)'),
        n = 2.38,
        alpha = 0,
        E0 = (2.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy CBS-Q calculations. Rate expression per H atom.""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 31,
    label = "H2;C_rad/CtCsS",
    group1 = 
"""
1 *1 H 0 {2,S}
2 *2 H 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Ct 0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.192, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (23.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""
Sumathy CBS-Q calculations. Rate expression per H atom.
Sumathi, R.; Carstensen, H.-H.; Green, W.H. Jr.; J. Phys. Chem. A. 2001, 105, 8978

Table 8: Modified ArrHenius Fitted Parameters for GA Predicted Rates.

R2C=CRCH3 + H --> R2C=CRCH2 + H2

Verified by Karma James
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 32,
    label = "C/H2/OneDeC;H_rad",
    group1 = 
"""
1 *1 C                0 {2,S} {3,S} {4,S} {5,S}
2 *2 H                0 {1,S}
3    H                0 {1,S}
4    {Cd,Ct,CO,Cb,CS} 0 {1,S}
5    Cs               0 {1,S}
""",
    group2 = 
"""
1 *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (699000, 'cm^3/(mol*s)'),
        n = 2.36,
        alpha = 0,
        E0 = (1.11, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy CBS-Q calculations. Rate expression per H atom. Primary allylic hydrogen {C/Cd/C/H2}""",
    longDesc = 
u"""
Sumathy CBS-Q calculations. Rate expression per H atom.
Sumathi, R.; Carstensen, H.-H.; Green, W.H. Jr.; J. Phys. Chem. A. 2001, 105, 8978

Table 8: Modified ArrHenius Fitted Parameters for GA Predicted Rates.

RR2C=CRCH2R + H --> R2C=CRCHR + H2

Verified by Karma James
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 33,
    label = "C/H2/OneDeC;H_rad",
    group1 = 
"""
1 *1 C                0 {2,S} {3,S} {4,S} {5,S}
2 *2 H                0 {1,S}
3    H                0 {1,S}
4    {Cd,Ct,CO,Cb,CS} 0 {1,S}
5    Cs               0 {1,S}
""",
    group2 = 
"""
1 *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (77900000.0, 'cm^3/(mol*s)'),
        n = 1.78,
        alpha = 0,
        E0 = (2.11, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy CBS-Q calculations. Rate expression per H atom. Primary propergylic {C/Ct/C/H2}""",
    longDesc = 
u"""
Sumathy CBS-Q calculations. Rate expression per H atom.
Sumathi, R.; Carstensen, H.-H.; Green, W.H. Jr.; J. Phys. Chem. A. 2001, 105, 8978

Table 8: Modified ArrHenius Fitted Parameters for GA Predicted Rates.

RCCCH2R + H --> RCCCHR + H2

Verified by Karma James
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 34,
    label = "C/H/Cs2;H_rad",
    group1 = 
"""
1 *1 C                0 {2,S} {3,S} {4,S} {5,S}
2 *2 H                0 {1,S}
3    {Cd,Ct,Cb,CO,CS} 0 {1,S}
4    Cs               0 {1,S}
5    Cs               0 {1,S}
""",
    group2 = 
"""
1 *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (3020000.0, 'cm^3/(mol*s)'),
        n = 2.16,
        alpha = 0,
        E0 = (-0.45, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy CBS-Q calculations. Rate expression per H atom. Secondary allylic hydrogen {C/Cd/C2/H}""",
    longDesc = 
u"""
Sumathy CBS-Q calculations. Rate expression per H atom.
Sumathi, R.; Carstensen, H.-H.; Green, W.H. Jr.; J. Phys. Chem. A. 2001, 105, 8978

Table 8: Modified ArrHenius Fitted Parameters for GA Predicted Rates.

R2C=CRCHR2 + H --> R2C=CRCR2 + H2

Verified by Karma James
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 35,
    label = "C/H/Cs2;H_rad",
    group1 = 
"""
1 *1 C                0 {2,S} {3,S} {4,S} {5,S}
2 *2 H                0 {1,S}
3    {Cd,Ct,Cb,CO,CS} 0 {1,S}
4    Cs               0 {1,S}
5    Cs               0 {1,S}
""",
    group2 = 
"""
1 *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (121000000.0, 'cm^3/(mol*s)'),
        n = 1.72,
        alpha = 0,
        E0 = (-0.73, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy CBS-Q calculations. Rate expression per H atom. Secondary propergylic {C/Ct/C2/H}""",
    longDesc = 
u"""
Sumathy CBS-Q calculations. Rate expression per H atom.
Sumathi, R.; Carstensen, H.-H.; Green, W.H. Jr.; J. Phys. Chem. A. 2001, 105, 8978

Table 8: Modified ArrHenius Fitted Parameters for GA Predicted Rates.

RCCCHR2 + H --> RCCCR2 + H2

Verified by Karma James
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 36,
    label = "C/H2/TwoDe;H_rad",
    group1 = 
"""
1 *1 C                0 {2,S} {3,S} {4,S} {5,S}
2 *2 H                0 {1,S}
3    H                0 {1,S}
4    {Cd,Ct,CO,Cb,CS} 0 {1,S}
5    {Cd,Ct,CO,Cb,CS} 0 {1,S}
""",
    group2 = 
"""
1 *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (7090, 'cm^3/(mol*s)'),
        n = 2.85,
        alpha = 0,
        E0 = (-1.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy CBS-Q calculations. Rate expression per H atom.""",
    longDesc = 
u"""
Sumathy CBS-Q calculations. Rate expression per H atom.
Sumathi, R.; Carstensen, H.-H.; Green, W.H. Jr.; J. Phys. Chem. A. 2001, 105, 8978

Table 8: Modified ArrHenius Fitted Parameters for GA Predicted Rates.

R2C=CH-CH2-CH=CR2 + H --> R2C=CH-CH-CH=CR2 + H2

Verified by Karma James
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 37,
    label = "Cd/H/OneDe;H_rad",
    group1 = 
"""
1 *1 C                0 {2,D} {3,S} {4,S}
2    C                0 {1,D}
3 *2 H                0 {1,S}
4    {Cd,Ct,Cb,CO,CS} 0 {1,S}
""",
    group2 = 
"""
1 *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (193000000.0, 'cm^3/(mol*s)'),
        n = 1.74,
        alpha = 0,
        E0 = (10.28, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy CBS-Q calculations. Rate expression per H atom. Dienylic {Cd/Cd/H}""",
    longDesc = 
u"""
Sumathy CBS-Q calculations. Rate expression per H atom.
Sumathi, R.; Carstensen, H.-H.; Green, W.H. Jr.; J. Phys. Chem. A. 2001, 105, 8978

Table 8: Modified ArrHenius Fitted Parameters for GA Predicted Rates.

R2C=CRCH=CR2 + H --> R2C=CRC=CR2 + H2

Verified by Karma James
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 38,
    label = "Cd/H/OneDe;H_rad",
    group1 = 
"""
1 *1 C                0 {2,D} {3,S} {4,S}
2    C                0 {1,D}
3 *2 H                0 {1,S}
4    {Cd,Ct,Cb,CO,CS} 0 {1,S}
""",
    group2 = 
"""
1 *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (2180000.0, 'cm^3/(mol*s)'),
        n = 2.4,
        alpha = 0,
        E0 = (6.11, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy CBS-Q calculations. Rate expression per H atom. Eneynic {Cd/Ct/H}""",
    longDesc = 
u"""
Sumathy CBS-Q calculations. Rate expression per H atom.
Sumathi, R.; Carstensen, H.-H.; Green, W.H. Jr.; J. Phys. Chem. A. 2001, 105, 8978

Table 8: Modified ArrHenius Fitted Parameters for GA Predicted Rates.

RCC-CH=CR2 + H --> RCC-C=CR2 + H2

Verified by Karma James
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 39,
    label = "Ct_H;H_rad",
    group1 = 
"""
1 *1 C 0 {2,T} {3,S}
2    C 0 {1,T}
3 *2 H 0 {1,S}
""",
    group2 = 
"""
1 *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (165000000.0, 'cm^3/(mol*s)'),
        n = 1.85,
        alpha = 0,
        E0 = (26.52, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy CBS-Q calculations. Rate expression per H atom.""",
    longDesc = 
u"""
Sumathy CBS-Q calculations. Rate expression per H atom.
Sumathi, R.; Carstensen, H.-H.; Green, W.H. Jr.; J. Phys. Chem. A. 2001, 105, 8978

Table 8: Modified ArrHenius Fitted Parameters for GA Predicted Rates.

RCCH + H --> RCC + H2

NOTE: There was a discrepancy in the rate values. The published values were: A = 1.30E+08, n = 1.88, 

E0 = 1.34E+04

RMG values: A=1.65E+08, n=1.85, E0=	26.52.

Verified by Karma James
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 40,
    label = "C/H3/Ct;H_rad",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    Ct 0 {1,S}
""",
    group2 = 
"""
1 *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (27000000.0, 'cm^3/(mol*s)'),
        n = 1.91,
        alpha = 0,
        E0 = (5.99, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy CBS-Q calculations. Rate expression per H atom.""",
    longDesc = 
u"""
Sumathy CBS-Q calculations. Rate expression per H atom.
Sumathi, R.; Carstensen, H.-H.; Green, W.H. Jr.; J. Phys. Chem. A. 2001, 105, 8978

Table 8: Modified ArrHenius Fitted Parameters for GA Predicted Rates.

RCCCH3 + H --> RCCCH2 + H2

Verified by Karma James
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 41,
    label = "Cd/H/NonDeO;H_rad",
    group1 = 
"""
1 *1 C 0 {2,D} {3,S} {4,S}
2    C 0 {1,D}
3 *2 H 0 {1,S}
4    O 0 {1,S}
""",
    group2 = 
"""
1 *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (9670000000.0, 'cm^3/(mol*s)'),
        n = 1.23,
        alpha = 0,
        E0 = (11.69, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy CBS-Q calculations. Rate expression per H atom.""",
    longDesc = 
u"""
Sumathy CBS-Q calculations. Rate expression per H atom.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 42,
    label = "O/H/OneDe;H_rad",
    group1 = 
"""
1 *1 O                0 {2,S} {3,S}
2 *2 H                0 {1,S}
3    {Cd,Ct,Cb,CO,CS} 0 {1,S}
""",
    group2 = 
"""
1 *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (130000000000.0, 'cm^3/(mol*s)'),
        n = 0.82,
        alpha = 0,
        E0 = (7.75, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy CBS-Q calculations. Rate expression per H atom.""",
    longDesc = 
u"""
Sumathy CBS-Q calculations. Rate expression per H atom.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 43,
    label = "Cd_pri;C_methyl",
    group1 = 
"""
1 *1 C 0 {2,D} {3,S} {4,S}
2    C 0 {1,D}
3 *2 H 0 {1,S}
4    H 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (3240, 'cm^3/(mol*s)'),
        n = 2.58,
        alpha = 0,
        E0 = (14.04, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy CBS-Q calculations. Rate expression per H atom.""",
    longDesc = 
u"""
Sumathy CBS-Q calculations. Rate expression per H atom.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 44,
    label = "C/H3/Cd;C_methyl",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    Cd 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (80.4, 'cm^3/(mol*s)'),
        n = 2.92,
        alpha = 0,
        E0 = (7.16, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy CBS-Q calculations. Rate expression per H atom.""",
    longDesc = 
u"""
Sumathy CBS-Q calculations. Rate expression per H atom.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 45,
    label = "O/H/NonDeC;C_methyl",
    group1 = 
"""
1 *1 O  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (254000, 'cm^3/(mol*s)'),
        n = 1.89,
        alpha = 0,
        E0 = (8.97, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy CBS-Q calculations. Rate expression per H atom.""",
    longDesc = 
u"""
Sumathy CBS-Q calculations. Rate expression per H atom.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 46,
    label = "CO/H/NonDe;C_methyl",
    group1 = 
"""
1 *1 C        0 {2,D} {3,S} {4,S}
2    O        0 {1,D}
3 *2 H        0 {1,S}
4    {Cs,O,S} 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (29200, 'cm^3/(mol*s)'),
        n = 2.29,
        alpha = 0,
        E0 = (5.44, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy CBS-Q calculations. Rate expression per H atom.""",
    longDesc = 
u"""
Sumathy CBS-Q calculations. Rate expression per H atom.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 47,
    label = "O/H/OneDe;C_methyl",
    group1 = 
"""
1 *1 O                0 {2,S} {3,S}
2 *2 H                0 {1,S}
3    {Cd,Ct,Cb,CO,CS} 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (90700, 'cm^3/(mol*s)'),
        n = 2.04,
        alpha = 0,
        E0 = (10.85, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy CBS-Q calculations. Rate expression per H atom. Olefinic alcohol {O/Cd/H}""",
    longDesc = 
u"""
Sumathy CBS-Q calculations. Rate expression per H atom.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 48,
    label = "O/H/OneDe;H_rad",
    group1 = 
"""
1 *1 O                0 {2,S} {3,S}
2 *2 H                0 {1,S}
3    {Cd,Ct,Cb,CO,CS} 0 {1,S}
""",
    group2 = 
"""
1 *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (330000000.0, 'cm^3/(mol*s)'),
        n = 1.56,
        alpha = 0,
        E0 = (13.94, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy CBS-Q calculations. Rate expression per H atom. Acid O-H {O/CO/H}""",
    longDesc = 
u"""
Sumathy CBS-Q calculations. Rate expression per H atom.
Sumathi, R.; Carstensen, H.-H.; Green, W.H. Jr.; J. Phys. Chem. A. 2001, 105, 8978

Table 8: Modified ArrHenius Fitted Parameters for GA Predicted Rates.

RCOOOH + H --> RCOOO + H2

Verified by Karma James
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 49,
    label = "CO/H/NonDe;C_methyl",
    group1 = 
"""
1 *1 C        0 {2,D} {3,S} {4,S}
2    O        0 {1,D}
3 *2 H        0 {1,S}
4    {Cs,O,S} 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (4530, 'cm^3/(mol*s)'),
        n = 2.43,
        alpha = 0,
        E0 = (8.85, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy CBS-Q calculations. Rate expression per H atom.""",
    longDesc = 
u"""
Sumathy CBS-Q calculations. Rate expression per H atom.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 50,
    label = "C_methane;C_methyl",
    group1 = 
"""
1 *1 C 0 {2,S} {3,S} {4,S} {5,S}
2 *2 H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
5    H 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (60300000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (19, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom. 
Same reaction as #19. 

Saeys, M.; Reyniers, M.-F.; Marin, G.B.; Van Speybroeck, V.; Waroquier, M. J. Phys. Chem. A 2003, 107, 9147 - 9159.

CH3 + CH4 --> CH4 + CH3

pg 9156 Table 6: Calculated and Experimental Activation Energies(kJ/mol) at 0 K, deltaE (0 k), 

for Three Families of Radical Reactions from Various Levels of Theory.

From reference: E0 = 71.0/4.185 = 16.97, @ 0 K, from database: E0 = 19.0 @ 300 - 1500 K

Experimental values from reference @ 0 K = 55.4 kJ/mol, 60.7 kJ/mol, 61.9 kJ/mol
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 51,
    label = "C/H3/Cs;C_methyl",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (280000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (16.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 52,
    label = "C/H3/Cs;C_methyl",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (61500000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (15.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 53,
    label = "C/H3/Cs;C_methyl",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (7710000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (13.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 54,
    label = "C/H2/NonDeC;C_methyl",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (50200000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (13.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 55,
    label = "C/H/Cs3;C_methyl",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (50200000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (11.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 55,
    label = "C_methane;C_rad/H2/S",
    group1 = 
"""
1 *1 C 0 {2,S} {3,S} {4,S} {5,S}
2 *2 H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
5    H 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    S 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00452, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (15.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 56,
    label = "C/H/Cs3;C_methyl",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (44200000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (11.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 56,
    label = "C_methane;C_rad/H/CsS",
    group1 = 
"""
1 *1 C 0 {2,S} {3,S} {4,S} {5,S}
2 *2 H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
5    H 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00807, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (15.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 57,
    label = "C/H3/Cd;C_methyl",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    Cd 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (26200000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (12.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 57,
    label = "C_methane;C_rad/Cs2S",
    group1 = 
"""
1 *1 C 0 {2,S} {3,S} {4,S} {5,S}
2 *2 H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
5    H 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    S  0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00326, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (15.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 58,
    label = "C/H2/OneDeC;C_methyl",
    group1 = 
"""
1 *1 C                0 {2,S} {3,S} {4,S} {5,S}
2 *2 H                0 {1,S}
3    H                0 {1,S}
4    {Cd,Ct,CO,Cb,CS} 0 {1,S}
5    Cs               0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (27300000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (10.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 58,
    label = "C_methane;Cd_rad/NonDeS",
    group1 = 
"""
1 *1 C 0 {2,S} {3,S} {4,S} {5,S}
2 *2 H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
5    H 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,D} {3,S}
2    C 0 {1,D}
3    S 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.027, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 59,
    label = "C/H/Cs2;C_methyl",
    group1 = 
"""
1 *1 C                0 {2,S} {3,S} {4,S} {5,S}
2 *2 H                0 {1,S}
3    {Cd,Ct,Cb,CO,CS} 0 {1,S}
4    Cs               0 {1,S}
5    Cs               0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (27300000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (8.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 59,
    label = "C_methane;C_rad/H/CdS",
    group1 = 
"""
1 *1 C 0 {2,S} {3,S} {4,S} {5,S}
2 *2 H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
5    H 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cd 0 {1,S}
4    S  0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0446, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (26.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 60,
    label = "C/H2/TwoDe;C_methyl",
    group1 = 
"""
1 *1 C                0 {2,S} {3,S} {4,S} {5,S}
2 *2 H                0 {1,S}
3    H                0 {1,S}
4    {Cd,Ct,CO,Cb,CS} 0 {1,S}
5    {Cd,Ct,CO,Cb,CS} 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (75400000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (8.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 60,
    label = "C_methane;C_rad/CdCsS",
    group1 = 
"""
1 *1 C 0 {2,S} {3,S} {4,S} {5,S}
2 *2 H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
5    H 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cd 0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00564, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (26.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 61,
    label = "C/H/Cs;C_methyl",
    group1 = 
"""
1 *1 C                0 {2,S} {3,S} {4,S} {5,S}
2 *2 H                0 {1,S}
3    {Cd,Ct,Cb,CO,CS} 0 {1,S}
4    {Cd,Ct,Cb,CO,CS} 0 {1,S}
5    Cs               0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (9320000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 61,
    label = "C_methane;C_rad/H/CtS",
    group1 = 
"""
1 *1 C 0 {2,S} {3,S} {4,S} {5,S}
2 *2 H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
5    H 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Ct 0 {1,S}
4    S  0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0265, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (25.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 62,
    label = "C/H3/Cb;C_methyl",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    Cb 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (4900000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (13.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 62,
    label = "C_methane;C_rad/CtCsS",
    group1 = 
"""
1 *1 C 0 {2,S} {3,S} {4,S} {5,S}
2 *2 H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
5    H 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Ct 0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.108, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (26.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 63,
    label = "C/H2/OneDeC;C_methyl",
    group1 = 
"""
1 *1 C                0 {2,S} {3,S} {4,S} {5,S}
2 *2 H                0 {1,S}
3    H                0 {1,S}
4    {Cd,Ct,CO,Cb,CS} 0 {1,S}
5    Cs               0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (17000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (11.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 64,
    label = "C/H/Cs2;C_methyl",
    group1 = 
"""
1 *1 C                0 {2,S} {3,S} {4,S} {5,S}
2 *2 H                0 {1,S}
3    {Cd,Ct,Cb,CO,CS} 0 {1,S}
4    Cs               0 {1,S}
5    Cs               0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (11700000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (11, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 65,
    label = "C/H3/Ct;C_methyl",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    Ct 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (66000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (13.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 66,
    label = "C/H2/OneDeC;C_methyl",
    group1 = 
"""
1 *1 C                0 {2,S} {3,S} {4,S} {5,S}
2 *2 H                0 {1,S}
3    H                0 {1,S}
4    {Cd,Ct,CO,Cb,CS} 0 {1,S}
5    Cs               0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (28100000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (11, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 67,
    label = "C/H2/TwoDe;C_methyl",
    group1 = 
"""
1 *1 C                0 {2,S} {3,S} {4,S} {5,S}
2 *2 H                0 {1,S}
3    H                0 {1,S}
4    {Cd,Ct,CO,Cb,CS} 0 {1,S}
5    {Cd,Ct,CO,Cb,CS} 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (138000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (8.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 68,
    label = "C/H/Cs;C_methyl",
    group1 = 
"""
1 *1 C                0 {2,S} {3,S} {4,S} {5,S}
2 *2 H                0 {1,S}
3    {Cd,Ct,Cb,CO,CS} 0 {1,S}
4    {Cd,Ct,Cb,CO,CS} 0 {1,S}
5    Cs               0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (34300000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (7.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 69,
    label = "C/H/Cs2;C_methyl",
    group1 = 
"""
1 *1 C                0 {2,S} {3,S} {4,S} {5,S}
2 *2 H                0 {1,S}
3    {Cd,Ct,Cb,CO,CS} 0 {1,S}
4    Cs               0 {1,S}
5    Cs               0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (50300000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (9.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 70,
    label = "Cd_pri;C_methyl",
    group1 = 
"""
1 *1 C 0 {2,D} {3,S} {4,S}
2    C 0 {1,D}
3 *2 H 0 {1,S}
4    H 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (188000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (18.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 71,
    label = "Cd/H/NonDeC;C_methyl",
    group1 = 
"""
1 *1 C  0 {2,D} {3,S} {4,S}
2    C  0 {1,D}
3 *2 H  0 {1,S}
4    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (44300000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (16.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 72,
    label = "Cd/H/OneDe;C_methyl",
    group1 = 
"""
1 *1 C                0 {2,D} {3,S} {4,S}
2    C                0 {1,D}
3 *2 H                0 {1,S}
4    {Cd,Ct,Cb,CO,CS} 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (57800000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (16.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 73,
    label = "Cd/H/OneDe;C_methyl",
    group1 = 
"""
1 *1 C                0 {2,D} {3,S} {4,S}
2    C                0 {1,D}
3 *2 H                0 {1,S}
4    {Cd,Ct,Cb,CO,CS} 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (22600000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (15.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 74,
    label = "Cd/H/OneDe;C_methyl",
    group1 = 
"""
1 *1 C                0 {2,D} {3,S} {4,S}
2    C                0 {1,D}
3 *2 H                0 {1,S}
4    {Cd,Ct,Cb,CO,CS} 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (43700000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (13.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 75,
    label = "Ct_H;C_methyl",
    group1 = 
"""
1 *1 C 0 {2,T} {3,S}
2    C 0 {1,T}
3 *2 H 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (3.33e+12, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (28, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 76,
    label = "Cb_H;C_methyl",
    group1 = 
"""
1 *1 Cb       0 {2,B} {3,B} {4,S}
2    {Cb,Cbf} 0 {1,B}
3    {Cb,Cbf} 0 {1,B}
4 *2 H        0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1170000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (19.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 77,
    label = "C/H2/NonDeC;C_methyl",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (987000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (13.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 78,
    label = "C/H2/NonDeC;C_methyl",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (4510000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (12.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 79,
    label = "C/H/Cs3;C_methyl",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (24600000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (11, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 80,
    label = "C/H2/OneDeC;C_methyl",
    group1 = 
"""
1 *1 C                0 {2,S} {3,S} {4,S} {5,S}
2 *2 H                0 {1,S}
3    H                0 {1,S}
4    {Cd,Ct,CO,Cb,CS} 0 {1,S}
5    Cs               0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (59800000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (9.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 81,
    label = "C_methane;H_rad",
    group1 = 
"""
1 *1 C 0 {2,S} {3,S} {4,S} {5,S}
2 *2 H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
5    H 0 {1,S}
""",
    group2 = 
"""
1 *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (187000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (14.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 82,
    label = "C_methane;C_methyl",
    group1 = 
"""
1 *1 C 0 {2,S} {3,S} {4,S} {5,S}
2 *2 H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
5    H 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (60300000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (19, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 83,
    label = "C_methane;C_rad/H2/Cd",
    group1 = 
"""
1 *1 C 0 {2,S} {3,S} {4,S} {5,S}
2 *2 H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
5    H 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    H  0 {1,S}
4    Cd 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (153000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (30.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 84,
    label = "C_methane;Cd_pri_rad",
    group1 = 
"""
1 *1 C 0 {2,S} {3,S} {4,S} {5,S}
2 *2 H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
5    H 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,D} {3,S}
2    C 0 {1,D}
3    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (159000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (13.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 85,
    label = "C_methane;C_rad/Cs3",
    group1 = 
"""
1 *1 C 0 {2,S} {3,S} {4,S} {5,S}
2 *2 H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
5    H 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cs 0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (18600000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (20.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 86,
    label = "C/H/Cs3;H_rad",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (53100000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (5.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 86,
    label = "C/H3/Cs;C_rad/H2/S",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    S 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00681, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (13.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 87,
    label = "C/H/Cs3;C_methyl",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (50200000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (11.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 87,
    label = "C/H3/Cs;C_rad/H/CsS",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0122, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (13.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 88,
    label = "C/H/Cs3;C_rad/H2/Cd",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    H  0 {1,S}
4    Cd 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (50200000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (20.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 88,
    label = "C/H3/Cs;C_rad/Cs2S",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    S  0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00491, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (13.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 89,
    label = "C/H/Cs3;Cd_pri_rad",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,D} {3,S}
2    C 0 {1,D}
3    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (89500000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (6.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 89,
    label = "C/H3/Cs;Cd_rad/NonDeS",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,D} {3,S}
2    C 0 {1,D}
3    S 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0407, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (5.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 90,
    label = "C/H/Cs3;C_rad/Cs3",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cs 0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (543000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (11.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 90,
    label = "C/H3/Cs;C_rad/H/CdS",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cd 0 {1,S}
4    S  0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0672, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (24.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 91,
    label = "C/H/Cs3;C_rad/H2/Cs",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    H  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (3030000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (12.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 91,
    label = "C/H3/Cs;C_rad/CdCsS",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cd 0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00849, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (24.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 92,
    label = "C/H/Cs3;C_rad/H/NonDeC",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (2440000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (12.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 92,
    label = "C/H3/Cs;C_rad/H/CtS",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Ct 0 {1,S}
4    S  0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.04, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (23.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 93,
    label = "C/H/Cs3;C_rad/H/OneDeC",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C                1 {2,S} {3,S} {4,S}
2    H                0 {1,S}
3    {Cd,Ct,Cb,CO,CS} 0 {1,S}
4    Cs               0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (5460000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (21.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 93,
    label = "C/H3/Cs;C_rad/CtCsS",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Ct 0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.163, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (23.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 94,
    label = "C/H/Cs3;C_rad/Cs2",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C                1 {2,S} {3,S} {4,S}
2    {Cd,Ct,Cb,CO,CS} 0 {1,S}
3    Cs               0 {1,S}
4    Cs               0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1100000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (21.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 95,
    label = "C/H/Cs3;Cd_rad/NonDeC",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,D} {3,S}
2    C  0 {1,D}
3    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (102000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (5.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 96,
    label = "C/H/Cs3;Cd_rad/OneDe",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C                1 {2,D} {3,S}
2    C                0 {1,D}
3    {Cd,Ct,Cb,CO,CS} 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (4160000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (13.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 97,
    label = "C/H/Cs3;C_rad/H2/Ct",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    H  0 {1,S}
4    Ct 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (31400000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (17, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 98,
    label = "C/H/Cs3;C_rad/H/OneDeC",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C                1 {2,S} {3,S} {4,S}
2    H                0 {1,S}
3    {Cd,Ct,Cb,CO,CS} 0 {1,S}
4    Cs               0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (2530000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (18, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 99,
    label = "C/H/Cs3;C_rad/Cs2",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C                1 {2,S} {3,S} {4,S}
2    {Cd,Ct,Cb,CO,CS} 0 {1,S}
3    Cs               0 {1,S}
4    Cs               0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (978000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (18.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 100,
    label = "Cd_pri;H_rad",
    group1 = 
"""
1 *1 C 0 {2,D} {3,S} {4,S}
2    C 0 {1,D}
3 *2 H 0 {1,S}
4    H 0 {1,S}
""",
    group2 = 
"""
1 *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (339000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (15.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 101,
    label = "Cd_pri;C_methyl",
    group1 = 
"""
1 *1 C 0 {2,D} {3,S} {4,S}
2    C 0 {1,D}
3 *2 H 0 {1,S}
4    H 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (188000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (18.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 102,
    label = "Cd_pri;C_rad/H2/Cd",
    group1 = 
"""
1 *1 C 0 {2,D} {3,S} {4,S}
2    C 0 {1,D}
3 *2 H 0 {1,S}
4    H 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    H  0 {1,S}
4    Cd 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (53600000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (30.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 103,
    label = "Cd_pri;Cd_pri_rad",
    group1 = 
"""
1 *1 C 0 {2,D} {3,S} {4,S}
2    C 0 {1,D}
3 *2 H 0 {1,S}
4    H 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,D} {3,S}
2    C 0 {1,D}
3    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (14700000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (13.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 104,
    label = "Cd_pri;C_rad/Cs3",
    group1 = 
"""
1 *1 C 0 {2,D} {3,S} {4,S}
2    C 0 {1,D}
3 *2 H 0 {1,S}
4    H 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cs 0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (39300000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (20.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 105,
    label = "Cd_pri;C_rad/H2/Cs",
    group1 = 
"""
1 *1 C 0 {2,D} {3,S} {4,S}
2    C 0 {1,D}
3 *2 H 0 {1,S}
4    H 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    H  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (7820000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (19.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 106,
    label = "Cd_pri;C_rad/H/NonDeC",
    group1 = 
"""
1 *1 C 0 {2,D} {3,S} {4,S}
2    C 0 {1,D}
3 *2 H 0 {1,S}
4    H 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (3250000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (20.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 107,
    label = "Cd_pri;C_rad/H/OneDeC",
    group1 = 
"""
1 *1 C 0 {2,D} {3,S} {4,S}
2    C 0 {1,D}
3 *2 H 0 {1,S}
4    H 0 {1,S}
""",
    group2 = 
"""
1 *3 C                1 {2,S} {3,S} {4,S}
2    H                0 {1,S}
3    {Cd,Ct,Cb,CO,CS} 0 {1,S}
4    Cs               0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (15100000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (31.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 108,
    label = "Cd_pri;C_rad/Cs2",
    group1 = 
"""
1 *1 C 0 {2,D} {3,S} {4,S}
2    C 0 {1,D}
3 *2 H 0 {1,S}
4    H 0 {1,S}
""",
    group2 = 
"""
1 *3 C                1 {2,S} {3,S} {4,S}
2    {Cd,Ct,Cb,CO,CS} 0 {1,S}
3    Cs               0 {1,S}
4    Cs               0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (3390000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (38.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 109,
    label = "Cd_pri;Cd_rad/NonDeC",
    group1 = 
"""
1 *1 C 0 {2,D} {3,S} {4,S}
2    C 0 {1,D}
3 *2 H 0 {1,S}
4    H 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,D} {3,S}
2    C  0 {1,D}
3    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (60400000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (14, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 110,
    label = "Cd_pri;Cd_rad/OneDe",
    group1 = 
"""
1 *1 C 0 {2,D} {3,S} {4,S}
2    C 0 {1,D}
3 *2 H 0 {1,S}
4    H 0 {1,S}
""",
    group2 = 
"""
1 *3 C                1 {2,D} {3,S}
2    C                0 {1,D}
3    {Cd,Ct,Cb,CO,CS} 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (13000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (20.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 111,
    label = "Cd_pri;C_rad/H2/Ct",
    group1 = 
"""
1 *1 C 0 {2,D} {3,S} {4,S}
2    C 0 {1,D}
3 *2 H 0 {1,S}
4    H 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    H  0 {1,S}
4    Ct 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (25500000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (26.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 112,
    label = "Cd_pri;C_rad/H/OneDeC",
    group1 = 
"""
1 *1 C 0 {2,D} {3,S} {4,S}
2    C 0 {1,D}
3 *2 H 0 {1,S}
4    H 0 {1,S}
""",
    group2 = 
"""
1 *3 C                1 {2,S} {3,S} {4,S}
2    H                0 {1,S}
3    {Cd,Ct,Cb,CO,CS} 0 {1,S}
4    Cs               0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (4410000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (28.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 113,
    label = "Cd_pri;C_rad/Cs2",
    group1 = 
"""
1 *1 C 0 {2,D} {3,S} {4,S}
2    C 0 {1,D}
3 *2 H 0 {1,S}
4    H 0 {1,S}
""",
    group2 = 
"""
1 *3 C                1 {2,S} {3,S} {4,S}
2    {Cd,Ct,Cb,CO,CS} 0 {1,S}
3    Cs               0 {1,S}
4    Cs               0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (3590000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (35.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 114,
    label = "C/H3/Cd;H_rad",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    Cd 0 {1,S}
""",
    group2 = 
"""
1 *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (31300000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (7.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 115,
    label = "C/H3/Cd;C_methyl",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    Cd 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (26200000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (12.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 116,
    label = "C/H3/Cd;C_rad/H2/Cd",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    Cd 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    H  0 {1,S}
4    Cd 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (5780000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (21.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 117,
    label = "C/H2/NonDeC;C_rad/H2/S",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    S 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0156, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (11.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 117,
    label = "C/H3/Cd;Cd_pri_rad",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    Cd 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,D} {3,S}
2    C 0 {1,D}
3    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (7730000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (7.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 118,
    label = "C/H2/NonDeC;C_rad/H/CsS",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0279, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (11.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 118,
    label = "C/H3/Cd;C_rad/Cs3",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    Cd 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cs 0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (3180000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (11.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 119,
    label = "C/H2/NonDeC;C_rad/Cs2S",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    S  0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0112, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (11.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 119,
    label = "C/H3/Cd;C_rad/H2/Cs",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    Cd 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    H  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (560000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (12.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 120,
    label = "C/H2/NonDeC;Cd_rad/NonDeS",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,D} {3,S}
2    C 0 {1,D}
3    S 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0933, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (3.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 120,
    label = "C/H3/Cd;C_rad/H/NonDeC",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    Cd 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (287000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (12.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 121,
    label = "C/H2/NonDeC;C_rad/H/CdS",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cd 0 {1,S}
4    S  0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.154, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (22.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 121,
    label = "C/H3/Cd;C_rad/H/OneDeC",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    Cd 0 {1,S}
""",
    group2 = 
"""
1 *3 C                1 {2,S} {3,S} {4,S}
2    H                0 {1,S}
3    {Cd,Ct,Cb,CO,CS} 0 {1,S}
4    Cs               0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1520000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (21.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 122,
    label = "C/H2/NonDeC;C_rad/CdCsS",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cd 0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0195, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (22.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 122,
    label = "C/H3/Cd;C_rad/Cs2",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    Cd 0 {1,S}
""",
    group2 = 
"""
1 *3 C                1 {2,S} {3,S} {4,S}
2    {Cd,Ct,Cb,CO,CS} 0 {1,S}
3    Cs               0 {1,S}
4    Cs               0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (413000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (21.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 123,
    label = "C/H2/NonDeC;C_rad/H/CtS",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Ct 0 {1,S}
4    S  0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0915, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (21.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 123,
    label = "C/H3/Cd;Cd_rad/NonDeC",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    Cd 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,D} {3,S}
2    C  0 {1,D}
3    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (5520000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (7.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 124,
    label = "C/H2/NonDeC;C_rad/CtCsS",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Ct 0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.374, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (21.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 124,
    label = "C/H3/Cd;Cd_rad/OneDe",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    Cd 0 {1,S}
""",
    group2 = 
"""
1 *3 C                1 {2,D} {3,S}
2    C                0 {1,D}
3    {Cd,Ct,Cb,CO,CS} 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1950000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (14.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 125,
    label = "C/H3/Cd;C_rad/H2/Ct",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    Cd 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    H  0 {1,S}
4    Ct 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (7580000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (18.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 126,
    label = "C/H3/Cd;C_rad/H/OneDeC",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    Cd 0 {1,S}
""",
    group2 = 
"""
1 *3 C                1 {2,S} {3,S} {4,S}
2    H                0 {1,S}
3    {Cd,Ct,Cb,CO,CS} 0 {1,S}
4    Cs               0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (509000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (18.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 127,
    label = "C/H3/Cd;C_rad/Cs2",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    Cd 0 {1,S}
""",
    group2 = 
"""
1 *3 C                1 {2,S} {3,S} {4,S}
2    {Cd,Ct,Cb,CO,CS} 0 {1,S}
3    Cs               0 {1,S}
4    Cs               0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (332000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (18.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 128,
    label = "H2;H_rad",
    group1 = 
"""
1 *1 H 0 {2,S}
2 *2 H 0 {1,S}
""",
    group2 = 
"""
1 *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (23700000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (9.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 129,
    label = "H2;C_methyl",
    group1 = 
"""
1 *1 H 0 {2,S}
2 *2 H 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (2950000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (14.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 130,
    label = "H2;C_rad/H2/Cd",
    group1 = 
"""
1 *1 H 0 {2,S}
2 *2 H 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    H  0 {1,S}
4    Cd 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (2870000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (25.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 131,
    label = "H2;Cd_pri_rad",
    group1 = 
"""
1 *1 H 0 {2,S}
2 *2 H 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,D} {3,S}
2    C 0 {1,D}
3    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (4490000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (10.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 132,
    label = "H2;C_rad/Cs3",
    group1 = 
"""
1 *1 H 0 {2,S}
2 *2 H 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cs 0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (308000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (14.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 133,
    label = "H2;C_rad/H2/Cs",
    group1 = 
"""
1 *1 H 0 {2,S}
2 *2 H 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    H  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (457000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (14.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 134,
    label = "H2;C_rad/H/NonDeC",
    group1 = 
"""
1 *1 H 0 {2,S}
2 *2 H 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (304000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (15.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 135,
    label = "H2;C_rad/H/OneDeC",
    group1 = 
"""
1 *1 H 0 {2,S}
2 *2 H 0 {1,S}
""",
    group2 = 
"""
1 *3 C                1 {2,S} {3,S} {4,S}
2    H                0 {1,S}
3    {Cd,Ct,Cb,CO,CS} 0 {1,S}
4    Cs               0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1820000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (27, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 136,
    label = "H2;C_rad/Cs2",
    group1 = 
"""
1 *1 H 0 {2,S}
2 *2 H 0 {1,S}
""",
    group2 = 
"""
1 *3 C                1 {2,S} {3,S} {4,S}
2    {Cd,Ct,Cb,CO,CS} 0 {1,S}
3    Cs               0 {1,S}
4    Cs               0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (430000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (27.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 137,
    label = "H2;Cd_rad/NonDeC",
    group1 = 
"""
1 *1 H 0 {2,S}
2 *2 H 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,D} {3,S}
2    C  0 {1,D}
3    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (3010000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (10.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 138,
    label = "H2;Cd_rad/OneDe",
    group1 = 
"""
1 *1 H 0 {2,S}
2 *2 H 0 {1,S}
""",
    group2 = 
"""
1 *3 C                1 {2,D} {3,S}
2    C                0 {1,D}
3    {Cd,Ct,Cb,CO,CS} 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (2370000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (18.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 139,
    label = "H2;C_rad/H2/Ct",
    group1 = 
"""
1 *1 H 0 {2,S}
2 *2 H 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    H  0 {1,S}
4    Ct 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (2910000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (23, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 140,
    label = "H2;C_rad/H/OneDeC",
    group1 = 
"""
1 *1 H 0 {2,S}
2 *2 H 0 {1,S}
""",
    group2 = 
"""
1 *3 C                1 {2,S} {3,S} {4,S}
2    H                0 {1,S}
3    {Cd,Ct,Cb,CO,CS} 0 {1,S}
4    Cs               0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (534000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (24, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 141,
    label = "H2;C_rad/Cs2",
    group1 = 
"""
1 *1 H 0 {2,S}
2 *2 H 0 {1,S}
""",
    group2 = 
"""
1 *3 C                1 {2,S} {3,S} {4,S}
2    {Cd,Ct,Cb,CO,CS} 0 {1,S}
3    Cs               0 {1,S}
4    Cs               0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (420000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (24.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 142,
    label = "C/H3/Cs;O_pri_rad",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 O 1 {2,S}
2    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (5930000.0, 'cm^3/(mol*s)'),
        n = 1.8,
        alpha = 0,
        E0 = (1.431, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""Curran et al. [8] Rate expressions for H atom abstraction from fuels. Fixed by RWest (changed to per H)""",
    longDesc = 
u"""
[8] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 2002, 129, 253. http://dx.doi.org/10.1016/S0010-2180(01)00373-X

Rate expressions for H atom abstraction from fuels. 
pg 257 A Comprehensive Modelling Study of iso-Octane Oxidation, Table 1. Radical:OH, Site: primary (a)
Verified by Karma James

**HOWEVER** This entry should probably use the numbers for primary(d) not primary(a).
Primary(a) is for a primary on neopentane; primary(d) is for a primary on propane.
Richard West. (Updated accordingly).

These numbers reported by Curran et al. were apparently taken from
N. Cohen, *Intl. J. Chem. Kinet.* 14 (1982), p. 1339 http://dx.doi.org/10.1002/kin.550141206

Rate expression is changed to per H.(divided by 3)
Yushi Suzuki
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 143,
    label = "C/H2/NonDeC;O_pri_rad",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 O 1 {2,S}
2    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (450000, 'cm^3/(mol*s)'),
        n = 2,
        alpha = 0,
        E0 = (-1.133, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""Curran et al. [8] Rate expressions for H atom abstraction from fuels. (changed to per H)""",
    longDesc = 
u"""
[8] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 2002, 129, 253.
http://dx.doi.org/10.1016/S0010-2180(01)00373-X

Rate expressions for H atom abstraction from fuels. 
pg 257 A Comprehensive Modelling Study of iso-Octane Oxidation, Table 1. Radical:OH, Site: secondary (b)

Verified by Karma James

These numbers reported by Curran et al. were apparently taken from
N. Cohen, *Intl. J. Chem. Kinet.* 14 (1982), p. 1339 http://dx.doi.org/10.1002/kin.550141206


Rate expression is changed to per H.(divided by 2)
Yushi Suzuki
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 144,
    label = "C/H/Cs3;O_pri_rad",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 O 1 {2,S}
2    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1700000.0, 'cm^3/(mol*s)'),
        n = 1.9,
        alpha = 0,
        E0 = (-1.451, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""Curran et al. [8] Rate expressions for H atom abstraction from fuels.""",
    longDesc = 
u"""
[8] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 2002, 129, 253.
http://dx.doi.org/10.1016/S0010-2180(01)00373-X

Rate expressions for H atom abstraction from fuels.
pg 257 A Comprehensive Modelling Study of iso-Octane Oxidation, Table 1. Radical:OH, Site: tertiary (c)

Verified by Karma James

These numbers reported by Curran et al. were apparently taken from
N. Cohen, *Intl. J. Chem. Kinet.* 14 (1982), p. 1339 http://dx.doi.org/10.1002/kin.550141206
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 145,
    label = "C/H3/Cs;O_atom_triplet",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 O 2T
""",
    kinetics = ArrheniusEP(
        A = (950, 'cm^3/(mol*s)'),
        n = 3.05,
        alpha = 0,
        E0 = (3.123, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""Curran et al. [8] Rate expressions for H atom abstraction from fuels. (changed to per H)""",
    longDesc = 
u"""
[8] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 2002, 129, 253.
Rate expressions for H atom abstraction from fuels.

pg 257 A Comprehensive Modelling Study of iso-Octane Oxidation, Table 1. Radical:O, Site: primary (a)

Verified by Karma James

Rate expression is changed to per H.(divided by 9)
Yushi Suzuki
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 146,
    label = "C/H2/NonDeC;O_atom_triplet",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 O 2T
""",
    kinetics = ArrheniusEP(
        A = (23900, 'cm^3/(mol*s)'),
        n = 2.71,
        alpha = 0,
        E0 = (2.106, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""Curran et al. [8] Rate expressions for H atom abstraction from fuels. (changed to per H)""",
    longDesc = 
u"""
[8] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 2002, 129, 253.
Rate expressions for H atom abstraction from fuels.

pg 257 A Comprehensive Modelling Study of iso-Octane Oxidation, Table 1. Radical:O, Site: secondary (b)

Verified by Karma James


Rate expression is changed to per H.(divided by 2)
Yushi Suzuki
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 147,
    label = "C/H/Cs3;O_atom_triplet",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 O 2T
""",
    kinetics = ArrheniusEP(
        A = (383000, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (1.14, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""Curran et al. [8] Rate expressions for H atom abstraction from fuels.""",
    longDesc = 
u"""
[8] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 2002, 129, 253.
Rate expressions for H atom abstraction from fuels.

pg 257 A Comprehensive Modelling Study of iso-Octane Oxidation, Table 1. Radical:O, Site: tertiary (c)

Verified by Karma James


This rate parameter actually comes from following new mechanism for PRF.

https://www-pls.llnl.gov/data/docs/science_and_technology/chemistry/combustion/prf_2d_mech.txt

Yushi Suzuki
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 148,
    label = "C/H/Cs3;C_rad/H2/S",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    S 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0094, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (9.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 148,
    label = "C/H3/Cs;O_rad/NonDeO",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 O 1 {2,S}
2    O 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (2800000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (20.435, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""Curran et al. [8] Rate expressions for H atom abstraction from fuels. (changed to per H)""",
    longDesc = 
u"""
[8] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 2002, 129, 253.
Rate expressions for H atom abstraction from fuels.

pg 257 A Comprehensive Modelling Study of iso-Octane Oxidation, Table 1. Radical:HO2, Site: primary (a)
Verified by Karma James

Rate expression is changed to per H.(divided by 9)
Yushi Suzuki
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 149,
    label = "C/H/Cs3;C_rad/H/CsS",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0168, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (9.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 149,
    label = "C/H2/NonDeC;O_rad/NonDeO",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 O 1 {2,S}
2    O 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (2800000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (17.686, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""Curran et al. [8] Rate expressions for H atom abstraction from fuels. (changed to per H)""",
    longDesc = 
u"""
[8] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 2002, 129, 253.
Rate expressions for H atom abstraction from fuels.

pg 257 A Comprehensive Modelling Study of iso-Octane Oxidation, Table 1. Radical:HO2, Site: secondary (b)

Verified by Karma James

Rate expression is changed to per H.(divided by 2)
Yushi Suzuki
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 150,
    label = "C/H/Cs3;C_rad/Cs2S",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    S  0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00677, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (9.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 150,
    label = "C/H/Cs3;O_rad/NonDeO",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 O 1 {2,S}
2    O 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (2800000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (16.013, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""Curran et al. [8] Rate expressions for H atom abstraction from fuels.""",
    longDesc = 
u"""
[8] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 2002, 129, 253.
Rate expressions for H atom abstraction from fuels.

pg 257 A Comprehensive Modelling Study of iso-Octane Oxidation, Table 1. Radical:HO2, Site: tertiary (c)

Verified by Karma James
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 151,
    label = "C/H/Cs3;Cd_rad/NonDeS",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,D} {3,S}
2    C 0 {1,D}
3    S 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0562, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (1.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""
[8] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 2002, 129, 253.
Rate expressions for H atom abstraction from fuels.

pg 257 A Comprehensive Modelling Study of iso-Octane Oxidation, Table 1. Radical:CH3O, Site: primary (a)

Verified by Karma James

Rate expression is changed to per H.(divided by 9)
Yushi Suzuki
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 151,
    label = "C/H3/Cs;O_rad/NonDeC",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 O  1 {2,S}
2    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (52700000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""Curran et al. [8] Rate expressions for H atom abstraction from fuels. (changed to per H)""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 152,
    label = "C/H/Cs3;C_rad/H/CdS",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cd 0 {1,S}
4    S  0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0928, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (20.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 152,
    label = "C/H2/NonDeC;O_rad/NonDeC",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 O  1 {2,S}
2    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (55000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""Curran et al. [8] Rate expressions for H atom abstraction from fuels. (changed to per H)""",
    longDesc = 
u"""
[8] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 2002, 129, 253.
Rate expressions for H atom abstraction from fuels.

pg 257 A Comprehensive Modelling Study of iso-Octane Oxidation, Table 1. Radical:CH3O, Site: secondary (b)

Verified by Karma James

Rate expression is changed to per H.(divided by 2)
Yushi Suzuki
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 153,
    label = "C/H/Cs3;C_rad/CdCsS",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cd 0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0117, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (20.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 153,
    label = "C/H/Cs3;O_rad/NonDeC",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 O  1 {2,S}
2    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (19000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (2.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""Curran et al. [8] Rate expressions for H atom abstraction from fuels.""",
    longDesc = 
u"""
[8] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 2002, 129, 253.
Rate expressions for H atom abstraction from fuels.

pg 257 A Comprehensive Modelling Study of iso-Octane Oxidation, Table 1. Radical:CH3O, Site: tertiary (c)

Verified by Karma James
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 154,
    label = "C/H/Cs3;C_rad/H/CtS",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Ct 0 {1,S}
4    S  0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0552, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (19.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 154,
    label = "C/H3/Cs;O2b",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 O 1 {2,S}
2    O 1 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (7000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (50.76, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""Curran et al. [8] Rate expressions for H atom abstraction from fuels. (changed to per H)""",
    longDesc = 
u"""
[8] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 2002, 129, 253.
Rate expressions for H atom abstraction from fuels.

pg 257 A Comprehensive Modelling Study of iso-Octane Oxidation, Table 1. Radical:O2, Site: primary (a)

Verified by Karma James

Rate expression is changed to per H.(divided by 9)
Yushi Suzuki
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 155,
    label = "C/H/Cs3;C_rad/CtCsS",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Ct 0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.226, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (20, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 155,
    label = "C/H2/NonDeC;O2b",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 O 1 {2,S}
2    O 1 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (7000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (48.21, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""Curran et al. [8] Rate expressions for H atom abstraction from fuels. (changed to per H)""",
    longDesc = 
u"""
[8] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 2002, 129, 253.
Rate expressions for H atom abstraction from fuels.

pg 257 A Comprehensive Modelling Study of iso-Octane Oxidation, Table 1. Radical:O2, Site: secondary (b)

Verified by Karma James

Rate expression is changed to per H.(divided by 2)
Yushi Suzuki
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 156,
    label = "C/H/Cs3;O2b",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 O 1 {2,S}
2    O 1 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (7000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (46.06, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""Curran et al. [8] Rate expressions for H atom abstraction from fuels.""",
    longDesc = 
u"""
[8] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 2002, 129, 253.
Rate expressions for H atom abstraction from fuels.

pg 257 A Comprehensive Modelling Study of iso-Octane Oxidation, Table 1. Radical:O2, Site: tertiary (c)

Verified by Karma James
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 157,
    label = "H2;O2b",
    group1 = 
"""
1 *1 H 0 {2,S}
2 *2 H 0 {1,S}
""",
    group2 = 
"""
1 *3 O 1 {2,S}
2    O 1 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (72500000000000.0, 'cm^3/(mol*s)', '*|/', 5),
        n = 0,
        alpha = 0,
        E0 = (56.64, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (800, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang et al. [89] literature review.""",
    longDesc = 
u"""
[89] Tsang, W.; Hampson, R.F. J. Phys. Chem. Ref. Data 1986, 15, 1087.
H2 + O2 --> H + HO2 C.D.W divided original rate expression by 2, to get rate expression per H atom.

pg 1091, Chemical Kinetic Database For Combustion Chemistry, 2. Index of Reactions and Summary of Recommended Rate Expressions. No. 3,2.

Verified by Karma James

pg. 1109: Discussion of evaluated data

Recommended value computed using reverse rate and thermodynamics

MRH 28-Aug-2009
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 158,
    label = "H2;Cd_pri_rad",
    group1 = 
"""
1 *1 H 0 {2,S}
2 *2 H 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,D} {3,S}
2    C 0 {1,D}
3    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (4730, 'cm^3/(mol*s)'),
        n = 2.56,
        alpha = 0,
        E0 = (5.03, 'kcal/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Knyazev et al. [119] Transition state theory.""",
    longDesc = 
u"""
[119] Knyazev, V.D; Bencsura, A.; Stoliarov, S.I.; Slagle, I.R. J. Phys. Chem. 1996, 100, 11346.
H2 + C2H3 --> H + C2H4 C.D.W divided original rate expression by 2 ( from A = 9.45E+03), to get rate expression per H atom.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 159,
    label = "H2;Cd_pri_rad",
    group1 = 
"""
1 *1 H 0 {2,S}
2 *2 H 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,D} {3,S}
2    C 0 {1,D}
3    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (11100, 'cm^3/(mol*s)'),
        n = 2.48,
        alpha = 0,
        E0 = (7.13, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (3500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mebel et al. [120] Transition state theory.""",
    longDesc = 
u"""
[120] Mebel, A.M.; Morokuma, K.; Lin, M.C. J Chem. Phys. 1995, 103, 3440.
H2 + C2H3 --> H + C2H4 C.D.W divided original rate expression by 2, to get rate expression per H atom.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 160,
    label = "H2;Cd_pri_rad",
    group1 = 
"""
1 *1 H 0 {2,S}
2 *2 H 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,D} {3,S}
2    C 0 {1,D}
3    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1580000000.0, 'cm^3/(mol*s)'),
        n = 0.7,
        alpha = 0,
        E0 = (5.11, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Weissman et al. [121] Transition state theory.""",
    longDesc = 
u"""
[121] Weissman, M.A.; Benson, S.W. J. Phys. Chem. 1988, 92, 4080.
H2 + C2H3 --> H + C2H4 C.D.W divided original rate expression by 2 ( from A = 3.15E+09), to get rate expression per H atom.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 161,
    label = "H2;Ct_rad",
    group1 = 
"""
1 *1 H 0 {2,S}
2 *2 H 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,T}
2    C 0 {1,T}
""",
    kinetics = ArrheniusEP(
        A = (5400000000000.0, 'cm^3/(mol*s)', '*|/', 3.16),
        n = 0,
        alpha = 0,
        E0 = (2.17, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Baulch et al. [94] literature review.""",
    longDesc = 
u"""
[94] Baulch, D.L.; Cobos, C.J.; Cox, R.A.; Frank, P.; Hayman, G,; Just, T.; Kerr, J.A.; Murrells, T.; Pilling, M.J.; 
Troe, J.; Walker, R.W.; Warnatz, J. J. Phys. Chem. Ref. Data 1994, 23, 847.

H2 + C2H --> H + C2H2 C.D.W divided original rate expression by 2, to get rate expression per H atom.

pg 863 Evaluated Kinetic Data for Combustion Modelling Supplement 1, Table 1. Bimolecular reactions - C2H Radical Reactions.

Verified by Karma James

pg.1013-1014: Discussion on evaluated data

C2H+H2-->C2H2+H: Recommended rate coefficient is that reported by Koshi et al.  Rate

coefficient was computed for low temperatures, but extrapolation to higher temperatures
fits other reported data reasonably well.
MRH 31-Aug-2009
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 162,
    label = "H2;Cb_rad",
    group1 = 
"""
1 *1 H 0 {2,S}
2 *2 H 0 {1,S}
""",
    group2 = 
"""
1 *3 Cb       1 {2,B} {3,B}
2    {Cb,Cbf} 0 {1,B}
3    {Cb,Cbf} 0 {1,B}
""",
    kinetics = ArrheniusEP(
        A = (28600, 'cm^3/(mol*s)'),
        n = 2.43,
        alpha = 0,
        E0 = (6.28, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (5000, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mebel et al. [122] Transition state theory.""",
    longDesc = 
u"""
[122] Mebel, A.M.; Lin, M.C.; Yu, T.; Morokuma, K. J. Phys. Chem. A. 1997, 101, 3189.
H2 + phenyl --> H + benzene C.D.W divided original rate expression by 2 ( from A = 5.71E+04), to get rate expression per H atom.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 163,
    label = "H2;CO_pri_rad",
    group1 = 
"""
1 *1 H 0 {2,S}
2 *2 H 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,D} {3,S}
2    O 0 {1,D}
3    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (900000, 'cm^3/(mol*s)', '*|/', 5),
        n = 2,
        alpha = 0,
        E0 = (17.83, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang et al. [89] literature review.""",
    longDesc = 
u"""
[89] Tsang, W.; Hampson, R.F. J. Phys. Chem. Ref. Data 1986, 15, 1087.
H2 + HCO --> H + CH2O C.D.W divided original rate expression by 2, to get rate expression per H atom.

pg 1094, Chemical Kinetic Database For Combustion Chemistry, 2. Index of Reactions and Summary of Recommended Rate Expressions. No. 15,2.

Verified by Karma James

pg. 1147: Discussion of evaluated data

Recommended value computed using reverse rate and thermodynamics

MRH 28-Aug-2009
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 164,
    label = "H2;CO_rad/NonDe",
    group1 = 
"""
1 *1 H 0 {2,S}
2 *2 H 0 {1,S}
""",
    group2 = 
"""
1 *3 C        1 {2,D} {3,S}
2    O        0 {1,D}
3    {Cs,O,S} 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (2060000.0, 'cm^3/(mol*s)', '*|/', 3),
        n = 1.82,
        alpha = 0,
        E0 = (17.61, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang et al. [89] literature review.""",
    longDesc = 
u"""
[89] Tsang, W.; Hampson, R.F. J. Phys. Chem. Ref. Data 1986, 15, 1087.
H2 + CH3CO --> H + CH3CHO C.D.W divided original rate expression by 2, to get rate expression per H atom.

//WAS UNABLE TO VERIFY DATA!!! DATA NOT FOUND IN REFERENCE.

pg. 1229: Discussion on evaluated data

No experimental data for forward rxn, at the time

Reviewers noticed that k(H+HCHO=H2+HCO) / k(H+CH3CHO=H2+CH3CO) ~ 2, due to double the number of H atoms available

Used 0.5*k(H+HCHO=H2+HCO) and equilibrium constant to compute recommended rate expression

Verified by MRH on 10Aug2009
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 165,
    label = "H2;O_pri_rad",
    group1 = 
"""
1 *1 H 0 {2,S}
2 *2 H 0 {1,S}
""",
    group2 = 
"""
1 *3 O 1 {2,S}
2    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (910000000.0, 'cm^3/(mol*s)'),
        n = 1.21,
        alpha = 0,
        E0 = (4.71, 'kcal/mol'),
        Tmin = (200, 'K'),
        Tmax = (2400, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Isaacson [123] Transition state theory.""",
    longDesc = 
u"""
[123] Isaacson, A.D. J. Chem. Phys. 1997, 107, 3832.
H2 + O2 --> H + H2O C.D.W divided original rate expression by 2, to get rate expression per H atom.

166. [100] Jodkowski, J.T.; Rauez, M.-T.; Rayez, J.-C. J. Phys. Chem. A. 1999, 103, 3750.

H2 + CH3O --> H + CH3OH The calculated reverse rate constants are in good agreement with experiment. (This is -R1 in the paper)

C.D.W divided original rate expression by 2, to get rate expression per H atom.

Verified by Greg Magoon; maximum error of fitted expression from tabular data for forward rate constant, kr1 is 15% (cf. p. 3758)
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 166,
    label = "H2;O_rad/NonDeC",
    group1 = 
"""
1 *1 H 0 {2,S}
2 *2 H 0 {1,S}
""",
    group2 = 
"""
1 *3 O  1 {2,S}
2    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0632, 'cm^3/(mol*s)'),
        n = 4,
        alpha = 0,
        E0 = (4.91, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Jodkowski et al. [100] ab initio calculations.""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 167,
    label = "C_methane;O2b",
    group1 = 
"""
1 *1 C 0 {2,S} {3,S} {4,S} {5,S}
2 *2 H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
5    H 0 {1,S}
""",
    group2 = 
"""
1 *3 O 1 {2,S}
2    O 1 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (9925000000000.0, 'cm^3/(mol*s)', '*|/', 10),
        n = 0,
        alpha = 0,
        E0 = (56.83, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Baulch et al. [95] literature review.""",
    longDesc = 
u"""
[95] Baulch, D.L.; Cobos, C.J.; Cox, R.A.; Esser, C.; Frank, P.; Just, T.; Kerr, J.A.; Pilling, M.J.; 
Troe, J.; Walker, R.W.; Warnatz, J. J. Phys. Chem. Ref. Data 1992, 21, 411.

CH4 + O2 --> CH3 + HO2 C.D.W divided original rate expression by 4, to get rate expression per H atom.

pg 417 Evaluated Kinetic Data for Combustion Modelling, Table 1. Bimolecular reactions - O2 Reactions.

Verified by Karma James

pg.483: Discussion on evaluated data

O2+CH4 --> HO2+CH3: Recommended data based on experimental value for CH2O + O2 -->

HO2 + HCO.  Assumes equal A factor per C-H bond and Ea = deltaH.
MRH 31-Aug-2009
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 168,
    label = "C_methane;C_rad/H2/Cs",
    group1 = 
"""
1 *1 C 0 {2,S} {3,S} {4,S} {5,S}
2 *2 H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
5    H 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    H  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0216, 'cm^3/(mol*s)', '*|/', 2),
        n = 4.14,
        alpha = 0,
        E0 = (12.56, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang et al. [89] literature review.""",
    longDesc = 
u"""
[89] Tsang, W.; Hampson, R.F. J. Phys. Chem. Ref. Data 1986, 15, 1087.
CH4 + C2H5 --> CH3 + C2H6 C.D.W divided original rate expression by 4, to get rate expression per H atom.

//WAS UNABLE TO VERIFY DATA!!! DATA NOT FOUND IN REFERENCE.

pg. 1177: Discussion on evaluated data

No experimental data for forward rxn, at the time

Recommended data from reverse rate and equilibrium constant

Verified by MRH on 10Aug2009
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 169,
    label = "C_methane;C_rad/H/NonDeC",
    group1 = 
"""
1 *1 C 0 {2,S} {3,S} {4,S} {5,S}
2 *2 H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
5    H 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.000181, 'cm^3/(mol*s)', '*|/', 2),
        n = 4.4,
        alpha = 0,
        E0 = (10.79, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang et al. [91] literature review.""",
    longDesc = 
u"""
[91] Tsang, W. J. Phys. Chem. Ref. Data 1988, 17, 887.
CH4 + iso-C3H7 --> CH3 + C3H8 C.D.W divided original rate expression by 4, to get rate expression per H atom.

pg 894, Chemical Kinetic Database For Combustion Chemistry, Part 3. Index of Reactions and Summary of Recommended Rate Expressions. No. 42,10.

Verified by Karma James

pg. 935: Discussion on evaluated data

Entry 42,10: No data available at the time.  Author recommends rate coefficient

expression based on reverse rate and equilibrium constant.
MRH 30-Aug-2009
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 170,
    label = "C_methane;Ct_rad",
    group1 = 
"""
1 *1 C 0 {2,S} {3,S} {4,S} {5,S}
2 *2 H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
5    H 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,T}
2    C 0 {1,T}
""",
    kinetics = ArrheniusEP(
        A = (453000000000.0, 'cm^3/(mol*s)', '*|/', 10),
        n = 0,
        alpha = 0,
        E0 = (0.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang et al. [89] literature review.""",
    longDesc = 
u"""
[89] Tsang, W.; Hampson, R.F. J. Phys. Chem. Ref. Data 1986, 15, 1087.
CH4 + C2H --> CH3 + C2H2 C.D.W divided original rate expression by 4, to get rate expression per H atom.

pg 1101, Chemical Kinetic Database For Combustion Chemistry, 2. Index of Reactions and Summary of Recommended Rate Expressions. No. 21,10.

Verified by Karma James

pg. 1220: Discussion of evaluated data

Recommended data is expression given by Brown and Laufer (1981).

They computed the pre-exponential factor by the bond energy-bond order (BEBO) method

and combined that with experimental k at room temperature to yield Arrhenius expression
MRH 28-Aug-2009
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 171,
    label = "C_methane;Cb_rad",
    group1 = 
"""
1 *1 C 0 {2,S} {3,S} {4,S} {5,S}
2 *2 H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
5    H 0 {1,S}
""",
    group2 = 
"""
1 *3 Cb       1 {2,B} {3,B}
2    {Cb,Cbf} 0 {1,B}
3    {Cb,Cbf} 0 {1,B}
""",
    kinetics = ArrheniusEP(
        A = (500000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (8.6, 'kcal/mol'),
        Tmin = (560, 'K'),
        Tmax = (1410, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Heckmann et al. [124]""",
    longDesc = 
u"""
[124] Heckmann, E.; Hippler, H. Troe, J. Sypm. Int. Combust. Proc. 1996, 26, 543.
Absolute value measured directly (excitation technique: thermal, analytical technique: vis-UV absorption) CH4 + phenyl --> benzene

C.D.W divided original rate expression by 4, to get rate expression per H atom.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 172,
    label = "C_methane;CO_pri_rad",
    group1 = 
"""
1 *1 C 0 {2,S} {3,S} {4,S} {5,S}
2 *2 H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
5    H 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,D} {3,S}
2    O 0 {1,D}
3    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1820, 'cm^3/(mol*s)', '*|/', 5),
        n = 2.85,
        alpha = 0,
        E0 = (22.46, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang et al. [89] literature review.""",
    longDesc = 
u"""
[89] Tsang, W.; Hampson, R.F. J. Phys. Chem. Ref. Data 1986, 15, 1087.
CH4 + HCO --> CH3 + CH2O C.D.W divided original rate expression by 4, to get rate expression per H atom.

pg 1094, Chemical Kinetic Database For Combustion Chemistry, 2. Index of Reactions and Summary of Recommended Rate Expressions. No. 15,10.

Verified by Karma James

pg. 1150: Discussion on evaluated data

Recommended data computed using reverse rate and equilibrium constant

MRH 28-Aug-2009
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 173,
    label = "C_methane;CO_rad/NonDe",
    group1 = 
"""
1 *1 C 0 {2,S} {3,S} {4,S} {5,S}
2 *2 H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
5    H 0 {1,S}
""",
    group2 = 
"""
1 *3 C        1 {2,D} {3,S}
2    O        0 {1,D}
3    {Cs,O,S} 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (543, 'cm^3/(mol*s)', '*|/', 5),
        n = 2.88,
        alpha = 0,
        E0 = (21.46, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang et al. [89] literature review.""",
    longDesc = 
u"""
[89] Tsang, W.; Hampson, R.F. J. Phys. Chem. Ref. Data 1986, 15, 1087.
CH4 + CH3CO --> CH3 + CH3CHO C.D.W divided original rate expression by 4, to get rate expression per H atom.

pg 1102, Chemical Kinetic Database For Combustion Chemistry, 2. Index of Reactions and Summary of Recommended Rate Expressions. No. 22,10.

Verified by Karma James

pg. 1231: Discussion on evaluated data

Recommended number computed from reverse rate and equilibrium constant

MRH 28-Aug-2009
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 174,
    label = "C_methane;O_pri_rad",
    group1 = 
"""
1 *1 C 0 {2,S} {3,S} {4,S} {5,S}
2 *2 H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
5    H 0 {1,S}
""",
    group2 = 
"""
1 *3 O 1 {2,S}
2    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.385, 'cm^3/(mol*s)'),
        n = 3.95,
        alpha = 0,
        E0 = (0.55, 'kcal/mol'),
        Tmin = (223, 'K'),
        Tmax = (2400, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Melissas and Truhlar [125] Transition state theory.""",
    longDesc = 
u"""
[125] Melissas, V.S.; Truhlar, D.G. J. Chem. Phys. 1993,99,1010.
CH4 + OH --> CH3 + H2O C.D.W divided original rate expression by 4, to get rate expression per H atom.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 175,
    label = "C_methane;O_pri_rad",
    group1 = 
"""
1 *1 C 0 {2,S} {3,S} {4,S} {5,S}
2 *2 H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
5    H 0 {1,S}
""",
    group2 = 
"""
1 *3 O 1 {2,S}
2    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (3930000.0, 'cm^3/(mol*s)', '*|/', 1.41),
        n = 1.83,
        alpha = 0,
        E0 = (2.78, 'kcal/mol'),
        Tmin = (240, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Baulch et al. [95] literature review.""",
    longDesc = 
u"""
[95] Baulch, D.L.; Cobos, C.J.; Cox, R.A.; Esser, C.; Frank, P.; Just, T.; Kerr, J.A.; Pilling, M.J.; 
Troe, J.; Walker, R.W.; Warnatz, J. J. Phys. Chem. Ref. Data 1992, 21, 411.

CH4 + OH --> CH3 + H2O C.D.W divided original rate expression by 4, to get rate expression per H atom.

pg 419 Evaluated Kinetic Data for Combustion Modelling, Table 1. Bimolecular reactions - OH Radical Reactions.

Verified by Karma James

pg.571-572: Discussion on evaluated data

OH+CH4 --> H2O+CH3: "The preferred value of k is that obtained experimentally by

Madronich and Felder which predicts very precisely the data obtained between
240 and 2000K."
MRH 31-Aug-2009
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 176,
    label = "C_methane;O_pri_rad",
    group1 = 
"""
1 *1 C 0 {2,S} {3,S} {4,S} {5,S}
2 *2 H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
5    H 0 {1,S}
""",
    group2 = 
"""
1 *3 O 1 {2,S}
2    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (25500000.0, 'cm^3/(mol*s)'),
        n = 1.6,
        alpha = 0,
        E0 = (3.12, 'kcal/mol'),
        Tmin = (298, 'K'),
        Tmax = (1510, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Cohen et al. [101] Transition state theory.""",
    longDesc = 
u"""
[101] Cohen, N. Int. J. Chem. Kinet. 1991, 23, 397.
CH4 + OH --> CH3 + H2O C.D.W divided original rate expression by 4, to get rate expression per H atom.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 177,
    label = "C_methane;O_rad/NonDeC",
    group1 = 
"""
1 *1 C 0 {2,S} {3,S} {4,S} {5,S}
2 *2 H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
5    H 0 {1,S}
""",
    group2 = 
"""
1 *3 O  1 {2,S}
2    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.000155, 'cm^3/(mol*s)'),
        n = 5,
        alpha = 0,
        E0 = (5.58, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Jodkowski et al. [100] ab initio calculations.""",
    longDesc = 
u"""
[100] Jodkowski, J.T.; Rauez, M.-T.; Rayez, J.-C. J. Phys. Chem. A. 1999, 103, 3750.
CH4 + CH3O --> CH3 + CH3OH The calculated reverse rate constants are in good agreement with experiment. (Rxn. -R3 in paper)

C.D.W divided original rate expression by 4 ( from A= 1.51E+09), to get rate expression per H atom.

Verified by Greg Magoon; cf. reverse reaction, #261, below
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 178,
    label = "C_methane;O_rad/NonDeO",
    group1 = 
"""
1 *1 C 0 {2,S} {3,S} {4,S} {5,S}
2 *2 H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
5    H 0 {1,S}
""",
    group2 = 
"""
1 *3 O 1 {2,S}
2    O 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (45300000000.0, 'cm^3/(mol*s)', '*|/', 5),
        n = 0,
        alpha = 0,
        E0 = (18.58, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang et al. [89] literature review.""",
    longDesc = 
u"""
[89] Tsang, W.; Hampson, R.F. J. Phys. Chem. Ref. Data 1986, 15, 1087.
CH4 + HO2 --> CH3 + H2O2 C.D.W divided original rate expression by 4, to get rate expression per H atom.

pg 1093, Chemical Kinetic Database For Combustion Chemistry, 2. Index of Reactions and Summary of Recommended Rate Expressions. No. 10,7.

Verified by Karma James

pg. 1131: Discussion on evaluated data

Recommended data is based on expression for HO2 attach on alkanes (Walker)

MRH 28-Aug-2009
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 179,
    label = "C/H3/Cd;C_rad/H2/S",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    Cd 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    S 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0014, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (10.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 179,
    label = "C/H3/Cs;O2b",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 O 1 {2,S}
2    O 1 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (10050000000000.0, 'cm^3/(mol*s)', '*|/', 10),
        n = 0,
        alpha = 0,
        E0 = (51.87, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Baulch et al. [95] literature review.""",
    longDesc = 
u"""
[95] Baulch, D.L.; Cobos, C.J.; Cox, R.A.; Esser, C.; Frank, P.; Just, T.; Kerr, J.A.; Pilling, M.J.; 
Troe, J.; Walker, R.W.; Warnatz, J. J. Phys. Chem. Ref. Data 1992, 21, 411.

C2H6 + O2 --> C2H5 + HO2 C.D.W divided original rate expression by 6, to get rate expression per H atom.

pg 417 Evaluated Kinetic Data for Combustion Modelling  Table 1. Bimolecular reactions - O2 Reactions. (The value for E0 does not 

match the value in the reference, E0 RMG = 1.87; E0 Reference = 51.86)

Verified by Karma James

pg.484: Discussion on evaluated data

O2+C2H6 --> HO2+C2H5: "The value given in the Walker review has been modified slightly

to allow for the higher heat of formation of the C2H5 radical now recommended
and for an assumed equal A factor per C-H bond in CH2O+O2 and C2H6+O2."
*** NOTE: MRH agrees with KJ on discrepancy in RMG-stored E0.  MRH is changing the value

of E0 in RMG from 1.87 kcal/mol to 51.87 kcal/mol. ***
MRH 31-Aug-2009
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 180,
    label = "C/H3/Cd;C_rad/H/CsS",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    Cd 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0025, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (10.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""
[89] Tsang, W.; Hampson, R.F. J. Phys. Chem. Ref. Data 1986, 15, 1087.
C2H6 + C2H --> C2H5 + C2H2 C.D.W divided original rate expression by 6, to get rate expression per H atom.

pg 1101, Chemical Kinetic Database For Combustion Chemistry, 2. Index of Reactions and Summary of Recommended Rate Expressions. No. 21,11.

Verified by Karma James

pg. 1221: Discussion on evaluated data

Recommended data is based on expression given by Brown and Laufer (1981).

Brown and Laufer calculated pre-exponential factor by BEBO method and
combined calculation with experimental measurement of k at room temperature.
MRH 28-Aug-2009
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 180,
    label = "C/H3/Cs;Ct_rad",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,T}
2    C 0 {1,T}
""",
    kinetics = ArrheniusEP(
        A = (602000000000.0, 'cm^3/(mol*s)', '*|/', 3),
        n = 0,
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang et al. [89] literature review.""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 181,
    label = "C/H3/Cd;C_rad/Cs2S",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    Cd 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    S  0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00101, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (9.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 181,
    label = "C/H3/Cs;Cb_rad",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 Cb       1 {2,B} {3,B}
2    {Cb,Cbf} 0 {1,B}
3    {Cb,Cbf} 0 {1,B}
""",
    kinetics = ArrheniusEP(
        A = (34800000000.0, 'cm^3/(mol*s)', '*|/', 2.35),
        n = 0,
        alpha = 0,
        E0 = (4.44, 'kcal/mol', '+|-', 0.18),
        Tmin = (565, 'K'),
        Tmax = (1000, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Park et al. [126]""",
    longDesc = 
u"""
[126] Park, J.; Gheyas, S.; Lin, M.C. Int. J. Chem. Kinet. 2001, 33, 64.
Absolute value measured directly. Static or low flow, flash photolysis excitation, Vis-UV absoprtion analysis. 

Phenyl radicals are produced from 193 nm photolysis of C6H5COCH3. The cavity ringdown spectroscopy and/or mass spectroscopy

have been used to monitor reactant and/or products. C2H6 + phenyl --> C2H5 + benzene.

C.D.W divided original rate expression by 6 ( from A= 2.09E+11), to get rate expression per H atom. Original delta A = 2.0E+10.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 182,
    label = "C/H3/Cd;Cd_rad/NonDeS",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    Cd 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,D} {3,S}
2    C 0 {1,D}
3    S 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00835, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (2.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""
[89] Tsang, W.; Hampson, R.F. J. Phys. Chem. Ref. Data 1986, 15, 1087.
C2H6 + HCO --> C2H5 + CH2O C.D.W divided original rate expression by 6(from A = 4.69E+04), to get rate expression per H atom.

pg 1094, Chemical Kinetic Database For Combustion Chemistry, 2. Index of Reactions and Summary of Recommended Rate Expressions. No. 15,11.

Verified by Karma James

pg. 1150: Discussion on evaluated data

Recommended data computed from reverse rate and equilibrium constant

MRH 28-Aug-2009
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 182,
    label = "C/H3/Cs;CO_pri_rad",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,D} {3,S}
2    O 0 {1,D}
3    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (7820, 'cm^3/(mol*s)', '*|/', 5),
        n = 2.72,
        alpha = 0,
        E0 = (18.24, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang et al. [89] literature review.""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 183,
    label = "C/H3/Cd;C_rad/H/CdS",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    Cd 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cd 0 {1,S}
4    S  0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0138, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (21.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 183,
    label = "C/H3/Cs;CO_rad/NonDe",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C        1 {2,D} {3,S}
2    O        0 {1,D}
3    {Cs,O,S} 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (3020, 'cm^3/(mol*s)', '*|/', 5),
        n = 2.75,
        alpha = 0,
        E0 = (17.53, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang et al. [89] literature review.""",
    longDesc = 
u"""
[89] Tsang, W.; Hampson, R.F. J. Phys. Chem. Ref. Data 1986, 15, 1087.
C2H6 + CH3CO --> C2H5 + CH3CHO C.D.W divided original rate expression by 6(from A = 1.81E+04), to get rate expression per H atom.

pg 1102, Chemical Kinetic Database For Combustion Chemistry, 2. Index of Reactions and Summary of Recommended Rate Expressions. No. 22,11.

Verified by Karma James

pg. 1231: Discussion on evaluated data

Recommended data computed using rate of C2H5+CH2O divided by 2 (since only one O=C-H

hydrogen is present in CH3CHO) and equilibrium constant
MRH 28-Aug-2009
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 184,
    label = "C/H3/Cd;C_rad/CdCsS",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    Cd 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cd 0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00174, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (21.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""
[95] Baulch, D.L.; Cobos, C.J.; Cox, R.A.; Esser, C.; Frank, P.; Just, T.; Kerr, J.A.; Pilling, M.J.; 
Troe, J.; Walker, R.W.; Warnatz, J. J. Phys. Chem. Ref. Data 1992, 21, 411.

C2H6 + OH --> C2H5 + H2O C.D.W divided original rate expression by 6, to get rate expression per H atom.

pg 420 Evaluated Kinetic Data for Combustion Modelling, Table 1. Bimolecular reactions - OH Radical Reactions.

Verified by Karma James

pg.589-590: Discussion on evaluated data

OH+C2H6 --> H2O+C2H5: "The preferred value of k is almost indistinguishable from the

value obtained by Cohen from transition state calculations carried out for
temperatures between 300 and 2000K."
MRH 31-Aug-2009
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 184,
    label = "C/H3/Cs;O_pri_rad",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 O 1 {2,S}
2    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1200000.0, 'cm^3/(mol*s)', '*|/', 1.41),
        n = 2,
        alpha = 0,
        E0 = (0.86, 'kcal/mol'),
        Tmin = (250, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Baulch et al. [95] literature review.""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 185,
    label = "C/H3/CO;O_pri_rad",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    CO 0 {1,S}
""",
    group2 = 
"""
1 *3 O 1 {2,S}
2    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (517000, 'cm^3/(mol*s)'),
        n = 2.2,
        alpha = 0,
        E0 = (1, 'kcal/mol'),
        Tmin = (295, 'K'),
        Tmax = (600, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Taylor et al. [127] Transition state theory.""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 185,
    label = "C/H3/Cd;C_rad/H/CtS",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    Cd 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Ct 0 {1,S}
4    S  0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0082, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (19.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""
[127] Taylor, P.H.; Rahman, M.S.; Arif, M.; Dellinger, B.; Marshall, P. Sypm. Int. Combust. Proc. 1996, 26, 497.
CH3CHO + OH --> CH2CHO + H2O Rate constant is high pressure limit (pressure 0.13-0.97atm?) 

C.D.W divided original rate expression by 3(from A = 1.55E+06), to get rate expression per H atom.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 186,
    label = "C/H3/Cd;C_rad/CtCsS",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    Cd 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Ct 0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0335, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (20.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""
[100] Jodkowski, J.T.; Rauez, M.-T.; Rayez, J.-C. J. Phys. Chem. A. 1999, 103, 3750.
CH3OH + CH3 --> CH2OH + CH4 The calculated rate constants are in good agreement with experiment. (Rxn. R4 in paper)

C.D.W divided original rate expression by 3 ( from A= 8.43E+08), to get rate expression per H atom.

Verified by Greg Magoon
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 186,
    label = "C/H3/O;C_methyl",
    group1 = 
"""
1 *1 C 0 {2,S} {3,S} {4,S} {5,S}
2 *2 H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
5    O 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.000205, 'cm^3/(mol*s)'),
        n = 4.9,
        alpha = 0,
        E0 = (6.72, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Jodkowski et al. [100] ab initio calculations.""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 187,
    label = "C/H3/O;O_pri_rad",
    group1 = 
"""
1 *1 C 0 {2,S} {3,S} {4,S} {5,S}
2 *2 H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
5    O 0 {1,S}
""",
    group2 = 
"""
1 *3 O 1 {2,S}
2    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (8140, 'cm^3/(mol*s)'),
        n = 2.8,
        alpha = 0,
        E0 = (-0.42, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Jodkowski et al. [100] ab initio calculations.""",
    longDesc = 
u"""
[100] Jodkowski, J.T.; Rauez, M.-T.; Rayez, J.-C. J. Phys. Chem. A. 1999, 103, 3750.
CH3OH + OH --> CH2OH + H2O The calculated rate constants are in good agreement with experiment. (Rxn. R6 in paper)

C.D.W divided original rate expression by 3 ( from A= 2.11E+11), to get rate expression per H atom.

Verified by Greg Magoon
**Note that R2 from this paper appears to be missing from the RMG library, so I have added it as 1001**
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 188,
    label = "C/H2/NonDeC;O2b",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 O 1 {2,S}
2    O 1 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (19850000000000.0, 'cm^3/(mol*s)', '*|/', 10),
        n = 0,
        alpha = 0,
        E0 = (47.69, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang [91] literature review.""",
    longDesc = 
u"""
[91] Tsang, W. J. Phys. Chem. Ref. Data 1988, 17, 887.
C3H8 + O2 --> iso-C3H7 + HO2  C.D.W divided original rate expression by 2, to get rate expression per H atom.

pg 891, Chemical Kinetic Database For Combustion Chemistry, Part 3. Index of Reactions and Summary of Recommended Rate Expressions. No. 40,3.

//NOTE: For A value, Database value = 1.985E+13 and Reference value = 1.65E+13

Verified by Karma James

NOTE: MRH computed Reference A value of 1.99E+13 (11Aug2009)

pg. 899: Discussion on evaluated data

Entry 40,3 (b): No data available at the time.  The author "estimates" the rate

coefficient expressions (no indication of how).
MRH 30-Aug-2009
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 189,
    label = "C/H2/NonDeC;CH2_triplet",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C 2T {2,S} {3,S}
2    H 0  {1,S}
3    H 0  {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.755, 'cm^3/(mol*s)', '*|/', 10),
        n = 3.46,
        alpha = 0,
        E0 = (7.47, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang [91] literature review.""",
    longDesc = 
u"""
[91] Tsang, W. J. Phys. Chem. Ref. Data 1988, 17, 887.
C3H8 + CH2 --> iso-C3H7 + CH3  C.D.W divided original rate expression by 2(from A = 1.51), to get rate expression per H atom.

pg 892, Chemical Kinetic Database For Combustion Chemistry, Part 3. Index of Reactions and Summary of Recommended Rate Expressions. No. 40,26.
Verified by Karma James

pg. 910: Discussion on evaluated data

Entry 40,26 (b): No data available at the time.  Author estimates the rate coefficient

expression as that of CH3+C3H8=i-C3H7+CH4.
MRH 30-Aug-2009
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 190,
    label = "C/H2/NonDeC;O_atom_triplet",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 O 2T
""",
    kinetics = ArrheniusEP(
        A = (23900, 'cm^3/(mol*s)', '*|/', 2),
        n = 2.71,
        alpha = 0,
        E0 = (2.11, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang [91] literature review.""",
    longDesc = 
u"""
[91] Tsang, W. J. Phys. Chem. Ref. Data 1988, 17, 887.
C3H8 + O --> iso-C3H7 + OH  C.D.W divided original rate expression by 2(from A = 4.77E+04), to get rate expression per H atom.

pg 891, Chemical Kinetic Database For Combustion Chemistry, Part 3. Index of Reactions and Summary of Recommended Rate Expressions. No. 40,5.

Verified by Karma James

pg. 901: Discussion on evaluated data

Entry 40,5 (b): The author notes "considerable scatter" among the existing data.  The

author computed Arrhenius A and n parameters using a BEBO calculation and performed
a "fit" on the data reported by Herron and Huie to obtain the Arrhenius E.  This
rate coefficient expression is stated to fit 3 (of the 5) raw data reported.
MRH 30-Aug-2009
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 191,
    label = "C/H2/NonDeC;C_rad/H2/O",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    O 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (30.2, 'cm^3/(mol*s)', '*|/', 5),
        n = 2.95,
        alpha = 0,
        E0 = (11.98, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang [91] literature review.""",
    longDesc = 
u"""
[91] Tsang, W. J. Phys. Chem. Ref. Data 1988, 17, 887.
C3H8 + CH2OH --> iso-C3H7 + CH3OH  C.D.W divided original rate expression by 2(from A = 6.03E+01), to get rate expression per H atom.

//WAS UNABLE TO VERIFY DATA!!! DATA NOT FOUND IN REFERENCE.

pg. 910: Discussion on evaluated data

Entry 40,39 (b)

No experimental data, at the time

Recommended value for C3H8+CH2OH-->n-C3H7+CH3OH comes from rate for C2H6+CH2OH-->C2H5+CH3OH

No discussion on where rate for C3H8+CH2OH-->i-C3H7+CH3OH comes from:

A is ~ factor of 3 smaller (6 hydrogens vs 2 ... seems reasonable to MRH)
E is 1 kcal/mol smaller (more stable to form secondary radical than primary)
Verified by MRH on 10Aug2009

MRH 30-Aug-2009
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 192,
    label = "C/H2/NonDeC;Cd_pri_rad",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,D} {3,S}
2    C 0 {1,D}
3    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (510, 'cm^3/(mol*s)', '*|/', 10),
        n = 3.1,
        alpha = 0,
        E0 = (8.82, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang [91] literature review.""",
    longDesc = 
u"""
[91] Tsang, W. J. Phys. Chem. Ref. Data 1988, 17, 887.
C3H8 + C2H3 --> iso-C3H7 + C2H4  C.D.W divided original rate expression by 2, to get rate expression per H atom.

pg 891, Chemical Kinetic Database For Combustion Chemistry, Part 3. Index of Reactions and Summary of Recommended Rate Expressions. No. 40,19.

Verified by Karma James

pg. 906: Discussion on evaluated data

Entry 40,19 (b): No data available at the time.  The author recommends the rate coefficient

expression of C2H3+C2H6=C2H5+C2H4 for the rxn C2H3+C3H8=n-C3H7+C2H4.  The author
assumes the ratio of secondary-to-primary H-atom abstraction for the rxn CH3+C3H8
to obtain the recommended rate coefficient expression.
MRH 30-Aug-2009
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 193,
    label = "C/H2/NonDeC;Ct_rad",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,T}
2    C 0 {1,T}
""",
    kinetics = ArrheniusEP(
        A = (605000000000.0, 'cm^3/(mol*s)', '*|/', 3),
        n = 0,
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang [91] literature review.""",
    longDesc = 
u"""
[91] Tsang, W. J. Phys. Chem. Ref. Data 1988, 17, 887.
C3H8 + C2H --> iso-C3H7 + C2H2  C.D.W divided original rate expression by 2, to get rate expression per H atom.

pg 891, Chemical Kinetic Database For Combustion Chemistry, Part 3. Index of Reactions and Summary of Recommended Rate Expressions. No. 40,21.

Verified by Karma James

pg. 906-907: Discussion on evaluated data

Entry 40,21 (b): No data available at the time.  The author recommends the rate coefficient

of C2H6+C2H=C2H2+C2H5 for the rxn C3H8+C2H=C2H2+n-C3H7.  Due to the high exothermicity
of the rxn, the author assumes the H-atom abstraction rxn is limited to the number
of H-atoms available, thus recommedning a rate coefficient equal to one-third that
recommended for C3H8+C2H=C2H2+n-C3H7.
MRH 30-Aug-2009
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 194,
    label = "C/H2/NonDeC;CO_pri_rad",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,D} {3,S}
2    O 0 {1,D}
3    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (5400000.0, 'cm^3/(mol*s)', '*|/', 3),
        n = 1.9,
        alpha = 0,
        E0 = (17.01, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang [91] literature review.""",
    longDesc = 
u"""
[91] Tsang, W. J. Phys. Chem. Ref. Data 1988, 17, 887.
C3H8 + HCO --> iso-C3H7 + CH2O  C.D.W divided original rate expression by 2, to get rate expression per H atom.

pg 891, Chemical Kinetic Database For Combustion Chemistry, Part 3. Index of Reactions and Summary of Recommended Rate Expressions. No. 40,15.

Verified by Karma James

pg. 904: Discussion on evaluated data

Entry 40,15 (b): No data available at the time.  The author recommends a rate coefficient

expression based on the reverse rxn (note: the author uses the rate of the rxn
n-C3H7+CH2O=HCO+C3H8 instead of i-C3H7+CH2O=HCO+C3H8) and equilibrium constant.
MRH 30-Aug-2009
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 195,
    label = "C/H2/NonDeC;CO_rad/NonDe",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C        1 {2,D} {3,S}
2    O        0 {1,D}
3    {Cs,O,S} 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (2650000.0, 'cm^3/(mol*s)', '*|/', 3),
        n = 2,
        alpha = 0,
        E0 = (16.24, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang [91] literature review.""",
    longDesc = 
u"""
[91] Tsang, W. J. Phys. Chem. Ref. Data 1988, 17, 887.
C3H8 + CH3CO --> iso-C3H7 + CH3CHO  C.D.W divided original rate expression by 2, to get rate expression per H atom.

pg 891, Chemical Kinetic Database For Combustion Chemistry, Part 3. Index of Reactions and Summary of Recommended Rate Expressions. No. 40,22.

Verified by Karma James

pg. 907: Discussion on evaluated data

Entry 40,22 (b): No data available at the time.  The author recommends a rate coefficient

expression based on the equilibrium constant and the reverse rate (note: the author
estimates this reverse rate using the suggestions of Kerr, J.A. and Trotman-Dickenson, A.F.).
MRH 30-Aug-2009
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 196,
    label = "C/H2/NonDeC;O_pri_rad",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 O 1 {2,S}
2    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (3950000.0, 'cm^3/(mol*s)'),
        n = 1.9,
        alpha = 0,
        E0 = (0.16, 'kcal/mol'),
        Tmin = (295, 'K'),
        Tmax = (1220, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Cohen et al. [101] Transition state theory.""",
    longDesc = 
u"""
[101] Cohen, N. Int. J. Chem. Kinet. 1991, 23, 397.
C3H8 + OH --> iso-C3H7 + H20  C.D.W divided original rate expression by 2, to get rate expression per H atom.

Not yet checked
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 197,
    label = "C/H2/NonDeC;O_rad/NonDeC",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 O  1 {2,S}
2    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (72500000000.0, 'cm^3/(mol*s)', '*|/', 5),
        n = 0,
        alpha = 0,
        E0 = (4.57, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang [91] literature review.""",
    longDesc = 
u"""
[91] Tsang, W. J. Phys. Chem. Ref. Data 1988, 17, 887.
C3H8 + CH3O --> iso-C3H7 + CH3OH  C.D.W divided original rate expression by 2, to get rate expression per H atom.

pg 891, Chemical Kinetic Database For Combustion Chemistry, Part 3. Index of Reactions and Summary of Recommended Rate Expressions. No. 40,24.

Verified by Karma James

pg. 908: Discussion on evaluated data

Entry 40,24 (b): The author assumes the Arrhenius A parameter should follow:

A(C3H8+CH3O=CH3OH+n-C3H7) / A(C3H8+CH3O=CH3OH+i-C3H7) = 3
The author also demands that the recommended data fit both sets of experiments
reported.  These assumptions (plus one unwritten one, as we still have 3
unknown parameters [A1, E1, E2 ... A2=f(A1)]) produce the reported rate
coefficient expression.
MRH 30-Aug-2009
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 198,
    label = "C/H/Cs3;O2b",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 O 1 {2,S}
2    O 1 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (39700000000000.0, 'cm^3/(mol*s)', '*|/', 3),
        n = 0,
        alpha = 0,
        E0 = (43.92, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang [92] literature review.""",
    longDesc = 
u"""
[92] Tsang, W. J. Phys. Chem. Ref. Data 1990, 19, 1.
Iso-C4H10 + O2 --> tert-C4H9 + HO2

pg 5, Chemical Kinetic Database For Combustion Chemistry, Part 4 - Isobutane. 

Index of Reactions and Summary of Recommended Rate Expressions. No. 43,3.

Verified by Karma James

pg.14: Discussion on evaluated data

Entry 43,3(b): No direct measurements at the time.  A review article reported a rate

coefficient expression for iC4H10+O2-->tC4H9+HO2.  An experiment performed by
Baldwin, Drewery, and Walker reported a rate coefficient expression for O2 abstracting
a tertiary H-atom from 2,3-dimethylbutane.  The experiment's value matched well
with the review's value, so Tsang recommended the review's value.
MRH 31-Aug-2009
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 199,
    label = "C/H/Cs3;O_atom_triplet",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 O 2T
""",
    kinetics = ArrheniusEP(
        A = (157000, 'cm^3/(mol*s)', '*|/', 2),
        n = 2.5,
        alpha = 0,
        E0 = (1.11, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang [92] literature review.""",
    longDesc = 
u"""
[92] Tsang, W. J. Phys. Chem. Ref. Data 1990, 19, 1.
Iso-C4H10 + O --> tert-C4H9 + OH

pg 5, Chemical Kinetic Database For Combustion Chemistry, Part 4 - Isobutane. 

Index of Reactions and Summary of Recommended Rate Expressions. No. 43,5.

Verified by Karma James

pg.15: Discussion on evaluated data

Entry 43,5(b): Michael et al. reported the rate coefficient expression for iC4H10+O=OH+C4H9 isomer.

Tsang subtracted from this expression the contributions from iC4H10+O=OH+iC4H9 (What
rate expression was used?  The one recommended here?) to obtain an expression for
iC4H10+O=OH+tC4H9.  Tsang then adjusted the rate expression such that the A-factor's
temperature dependence was 2.5 (was this 2.5 based on the review by Cohen and Westberg?).
MRH 31-Aug-2009
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 200,
    label = "C/H/Cs3;CH2_triplet",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C 2T {2,S} {3,S}
2    H 0  {1,S}
3    H 0  {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1090000000000.0, 'cm^3/(mol*s)', '*|/', 5),
        n = 0,
        alpha = 0,
        E0 = (4.91, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang [92] literature review.""",
    longDesc = 
u"""
[92] Tsang, W. J. Phys. Chem. Ref. Data 1990, 19, 1.
Iso-C4H10 + CH2 --> tert-C4H9 + CH3

pg 6, Chemical Kinetic Database For Combustion Chemistry, Part 4 - Isobutane. 

Index of Reactions and Summary of Recommended Rate Expressions. No. 43,25.

Verified by Karma James

pg.23-24: Discussion on evaluated data

Entry 43,25(b): Tsang recommends the rate coefficient expression reported by Bohland et al.

Tsang notes that the rate for CH2_triplet abstracting a H-atom is faster than
the recommended value for CH3 abstracting a H-atom.
MRH 31-Aug-2009
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 201,
    label = "C/H/Cs3;Cd_pri_rad",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,D} {3,S}
2    C 0 {1,D}
3    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.904, 'cm^3/(mol*s)', '*|/', 5),
        n = 3.46,
        alpha = 0,
        E0 = (2.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang [92] literature review.""",
    longDesc = 
u"""
[92] Tsang, W. J. Phys. Chem. Ref. Data 1990, 19, 1.
Iso-C4H10 + C2H3 --> tert-C4H9 + C2H4

pg 5, Chemical Kinetic Database For Combustion Chemistry, Part 4 - Isobutane. 

Index of Reactions and Summary of Recommended Rate Expressions. No. 43,19.

Verified by Karma James

pg.20: Discussion on evaluated data

Entry 43,19(b): No data available at the time.  Author recommends rate coefficient expression

based on the rxn CH3+iC4H10=CH4+tC4H9: same Arrhenius A and n parameters, Ea decreased
by 8.5 kJ/mol.
MRH 31-Aug-2009
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 202,
    label = "C/H/Cs3;Ct_rad",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,T}
2    C 0 {1,T}
""",
    kinetics = ArrheniusEP(
        A = (662000000000.0, 'cm^3/(mol*s)', '*|/', 3),
        n = 0,
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang [92] literature review.""",
    longDesc = 
u"""
[92] Tsang, W. J. Phys. Chem. Ref. Data 1990, 19, 1.
Iso-C4H10 + C2H --> tert-C4H9 + C2H2

pg 5, Chemical Kinetic Database For Combustion Chemistry, Part 4 - Isobutane. 

Index of Reactions and Summary of Recommended Rate Expressions. No. 43,21.

Verified by Karma James

pg.21: Discussion on evaluated data

Entry 43,21(b): No data available at the time.  For the rxn iC4H10+C2H=C2H2+iC4H9, author

recommends 1.5x the rate of the rxn C2H6+C2H=C2H2+C2H5 (9 vs. 6 primary H-atoms).
The author then recommends a rate coefficient for iC4H10+C2H=C2H2+tC4H9 that appears
to be 1/9 the rate of iC4H10+C2H=C2H2+iC4H9 (9 vs. 1 H-atom).
MRH 31-Aug-2009
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 203,
    label = "C/H/Cs3;CO_pri_rad",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,D} {3,S}
2    O 0 {1,D}
3    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (34300, 'cm^3/(mol*s)', '*|/', 5),
        n = 2.5,
        alpha = 0,
        E0 = (13.51, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang [92] literature review.""",
    longDesc = 
u"""
[92] Tsang, W. J. Phys. Chem. Ref. Data 1990, 19, 1.
Iso-C4H10 + HCO --> tert-C4H9 + CH2O

pg 5, Chemical Kinetic Database For Combustion Chemistry, Part 4 - Isobutane. 

Index of Reactions and Summary of Recommended Rate Expressions. No. 43,15.

Verified by Karma James

pg.18: Discussion on evaluated data

Entry 43,15(b): No data available at the time.  For the rxn iC4H10+HCO=CH2O+iC4H9, author

recommends 1.5x the rate of the rxn C3H8+HCO+CH2O+nC3H7 (9 vs. 6 primary H-atoms).
The author then recommends the rate coefficient for iC4H10+HCO=CH2O+tC4H9 to be the 
rate coefficient of iC4H10+HCO=CH2O+iC4H9, with the A factor divided by 9 (9 vs. 1
H-atoms) and the Ea decreased by 20 kJ/mol.
MRH 31-Aug-2009
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 204,
    label = "C/H/Cs3;CO_rad/NonDe",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C        1 {2,D} {3,S}
2    O        0 {1,D}
3    {Cs,O,S} 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (34300, 'cm^3/(mol*s)', '*|/', 10),
        n = 2.5,
        alpha = 0,
        E0 = (13.51, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang [92] literature review.""",
    longDesc = 
u"""
[92] Tsang, W. J. Phys. Chem. Ref. Data 1990, 19, 1.
Iso-C4H10 + CH3CO --> tert-C4H9 + CH3CHO

pg 5, Chemical Kinetic Database For Combustion Chemistry, Part 4 - Isobutane. 

Index of Reactions and Summary of Recommended Rate Expressions. No. 43,22.

Verified by Karma James

pg.21: Discussion on evaluated data

Entry 43,22(b): No data available at the time.  Author recommends rate coefficient expression

based on the rxn iC4H10+HCO=CH2O+tC4H9.
MRH 31-Aug-2009
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 205,
    label = "C/H/Cs3;O_pri_rad",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 O 1 {2,S}
2    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (2570000.0, 'cm^3/(mol*s)'),
        n = 1.9,
        alpha = 0,
        E0 = (1.45, 'kcal/mol'),
        Tmin = (298, 'K'),
        Tmax = (1150, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Cohen et al. [101] Transition state theory.""",
    longDesc = 
u"""
[101] Cohen, N. Int. J. Chem. Kinet. 1991, 23, 397.
Iso-C4H10 + OH --> tert-C4H9 + H2O

Not yet checked
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 206,
    label = "C/H/Cs3;O_rad/NonDeC",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 O  1 {2,S}
2    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (22900000000.0, 'cm^3/(mol*s)', '*|/', 10),
        n = 0,
        alpha = 0,
        E0 = (2.88, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang [92] literature review.""",
    longDesc = 
u"""
[92] Tsang, W. J. Phys. Chem. Ref. Data 1990, 19, 1.
Iso-C4H10 + CH3O --> tert-C4H9 + CH3OH

pg 6, Chemical Kinetic Database For Combustion Chemistry, Part 4 - Isobutane. 

Index of Reactions and Summary of Recommended Rate Expressions. No. 43,24.

Verified by Karma James

pg.22: Discussion on evaluated data

Entry 43,24(b): A study by Berces and Trotman-Dickenson reported a rate coefficient

for the rxn iC4H10+CH3O=CH3OH+C4H9 isomer.  Tsang used the rate coefficient for
the rxn CH3O+C(CH3)4=CH3OH+H2C*-C(CH3)3 determined by Shaw and Trotman-Dickenson
as a characteristic for CH3O+primary H-atom abstraction to recommend a rate coefficient
for iC4H10+CH3O=CH3OH+iC4H9.  This rate expression was subtracted from the rate
coefficient reported by Berces and Trotman-Dickenson to yield the rate coefficient
for iC4H10+CH3O=CH3OH+tC4H9.  Lastly, the pre-exponential factor was cut in half,
due to Tsang's correcting an arithmetic error by Kerr and Parsonage (perhaps this
work was referenced in the Berces and Trotman-Dickenson study?)
MRH 31-Aug-2009
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 207,
    label = "Cd_pri;O2b",
    group1 = 
"""
1 *1 C 0 {2,D} {3,S} {4,S}
2    C 0 {1,D}
3 *2 H 0 {1,S}
4    H 0 {1,S}
""",
    group2 = 
"""
1 *3 O 1 {2,S}
2    O 1 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (17920000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (60.01, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Hua, Ruscic, and Wang 2005, transition state theory.""",
    longDesc = 
u"""
FORMER RATES
[89] Tsang, W.; Hampson, R.F. J. Phys. Chem. Ref. Data 1986, 15, 1087.
C2H4 + O2 --> C2H3 + HO2 C.D.W divided original rate expression by 4, to get rate expression per H atom.

pg 1097, Chemical Kinetic Database For Combustion Chemistry, 2. Index of Reactions and Summary of Recommended Rate Expressions. No. 18,3.

Verified by Karma James

pg. 1184: Discussion on evaluated data

Recommended data follows Walker's estimates for O2+alkane

Note: The authors note that a lower lying channel, involving addition and
rearrangement prior to decomposition, may exist.
MRH 28-Aug-2009


CURRENT RATES
Hua, H.; B. Ruscic; B. Wang.  Chemical Physics 2005, 311, 335-341.
C2H4 + O2 --> C2H3 + HO2.

Divided rate expression by 4 to get the rate expression per H atom.  See page 338.
Overall, this agrees with the earlier rate that we used.
JDM 15-Jun-2010.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 209,
    label = "Cd_pri;O_atom_triplet",
    group1 = 
"""
1 *1 C 0 {2,D} {3,S} {4,S}
2    C 0 {1,D}
3 *2 H 0 {1,S}
4    H 0 {1,S}
""",
    group2 = 
"""
1 *3 O 2T
""",
    kinetics = ArrheniusEP(
        A = (3780000.0, 'cm^3/(mol*s)'),
        n = 1.91,
        alpha = 0,
        E0 = (3.74, 'kcal/mol'),
        Tmin = (290, 'K'),
        Tmax = (1510, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mahmud et al. [128] Transition state theory""",
    longDesc = 
u"""
[128] Mahmud, K.; Marshall, P.; Fontijn, A. J Phys. Chem. 1987, 91, `568.
C2H4 + O --> C2H3 + OH C.D.W divided original rate expression by 4(from A= 1.51E+07), to get rate expression per H atom.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 210,
    label = "C/H2/CdCs;C_rad/H2/S",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Cd 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    S 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00555, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (8.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 210,
    label = "Cd_pri;C_rad/H2/Cs",
    group1 = 
"""
1 *1 C 0 {2,D} {3,S} {4,S}
2    C 0 {1,D}
3 *2 H 0 {1,S}
4    H 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    H  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (158, 'cm^3/(mol*s)', '*|/', 10),
        n = 3.13,
        alpha = 0,
        E0 = (18, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang [89] literature review.""",
    longDesc = 
u"""
[89] Tsang, W.; Hampson, R.F. J. Phys. Chem. Ref. Data 1986, 15, 1087.
C2H4 + C2H5 --> C2H3 + C2H6 C.D.W divided original rate expression by 4, to get rate expression per H atom.

pg 1098, Chemical Kinetic Database For Combustion Chemistry, 2. Index of Reactions and Summary of Recommended Rate Expressions. No. 18,17.

Verified by Karma James

pgs. 1191-1192: Discussion on evaluated data

Recommended data based on study performed by Halstead and Quinn

Tsang fit the data against BEBO calculations (to attain the Arrhenius A, n)
and manually adjusted the E.
MRH 28-Aug-2009
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 211,
    label = "C/H2/CdCs;C_rad/H/CsS",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Cd 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00991, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (8.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""
[95] Baulch, D.L.; Cobos, C.J.; Cox, R.A.; Esser, C.; Frank, P.; Just, T.; Kerr, J.A.; Pilling, M.J.; 
Troe, J.; Walker, R.W.; Warnatz, J. J. Phys. Chem. Ref. Data 1992, 21, 411.

C2H4 + OH --> C2H3 + H2O C.D.W divided original rate expression by 4(from A= 2.05E+13), to get rate expression per H atom.

pg 420 Evaluated Kinetic Data for Combustion Modelling, Table 1. Bimolecular reactions - OH Radical Reactions.

Verified by Karma James

pg.586-587: Discussion on evaluated data

OH+C2H4 --> H2O+C2H3: Recommended rate taken from expression reported by Tully (1988).

MRH 31-Aug-2009
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 211,
    label = "Cd_pri;O_pri_rad",
    group1 = 
"""
1 *1 C 0 {2,D} {3,S} {4,S}
2    C 0 {1,D}
3 *2 H 0 {1,S}
4    H 0 {1,S}
""",
    group2 = 
"""
1 *3 O 1 {2,S}
2    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (5130000000000.0, 'cm^3/(mol*s)', '*|/', 3.16),
        n = 0,
        alpha = 0,
        E0 = (5.94, 'kcal/mol'),
        Tmin = (650, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Baulch et al. [95] literature review.""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 212,
    label = "C/H2/CdCs;C_rad/Cs2S",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Cd 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    S  0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.004, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (8.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""
[93] Tsang, W. J. Phys. Chem. Ref. Data 1991, 20, 221.
CH3CH=CH2 + O --> CH3C=CH2 + OH

pg 233-234: Discussion on evaluated data

Verified by MRH on 6Aug2009

Entry 46,5(f): No measurements on H-atom abstraction rxns. Recommended rate coefficient

is computed as follows:

The rate of O + C3H6 --> OH + H2C=CH-*CH2 is computed using the expression:
[k(O+C2H6-->C2H5+HO)/k(OH+C2H6-->C2H5+H2O)] * k(OH+C3H6-->H2C=CH-*CH2+H2O).
The author uses this expression because he notes that OH and O H-atom abstraction
rxns generally follow the same trend.  The O+C2H6, OH+C2H6, and OH+C3H6
are from other Tsang review articles.
The rate of O+C3H6 --> OH+CH3C=CH2 is computed by adjusting the O+C3H6 --> OH+H2C=CH-*CH2
rate coefficient: increasing the Ea/R by 880 Kelvin and multiplying the A
by ~0.345; these values come from the relative difference between the rxns
OH+C3H6 --> H2O+H2C=CH-*CH2 and OH+C3H6 --> H2O+CH3C=CH2
MRH 31-Aug-2009
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 212,
    label = "Cd/H/NonDeC;O_atom_triplet",
    group1 = 
"""
1 *1 C  0 {2,D} {3,S} {4,S}
2    C  0 {1,D}
3 *2 H  0 {1,S}
4    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 O 2T
""",
    kinetics = ArrheniusEP(
        A = (60200000000.0, 'cm^3/(mol*s)', '*|/', 3),
        n = 0.7,
        alpha = 0,
        E0 = (7.63, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang [93] literature review.""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 213,
    label = "C/H2/CdCs;Cd_rad/NonDeS",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Cd 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,D} {3,S}
2    C 0 {1,D}
3    S 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0332, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (1.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""
[93] Tsang, W. J. Phys. Chem. Ref. Data 1991, 20, 221.
CH3CH=CH2 + H --> CH3C=CH2 + H2

pg 231: Discussion on evaluated data

Previous modified Arrhenius parameters were for RELATIVE rate (kc/ka)

Multipled kc/ka by ka to get kc (only one H to abstract, so no division necessary)

Certified by MRH on 6Aug2009

Entry 46,4(c): No data available for H-atom abstraction rxns.  The recommended rate

coefficient is based on the author's assumption that methyl substitution has the
same influence in olefins as in alkanes.
MRH 31-Aug-2009
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 213,
    label = "Cd/H/NonDeC;H_rad",
    group1 = 
"""
1 *1 C  0 {2,D} {3,S} {4,S}
2    C  0 {1,D}
3 *2 H  0 {1,S}
4    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (409000, 'cm^3/(mol*s)', '*|/', 4),
        n = 2.5,
        alpha = 0,
        E0 = (9.79, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang [93] literature review.""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 214,
    label = "C/H2/CdCs;C_rad/H/CdS",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Cd 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cd 0 {1,S}
4    S  0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0547, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (20, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""
[93] Tsang, W. J. Phys. Chem. Ref. Data 1991, 20, 221.
CH3CH=CH2 + CH3 --> CH3C=CH2 + CH4

pg 237-239

Previous modified Arrhenius parameters were for RELATIVE rate (ke/kc)

Multiplied ke/kc by kc to get ke (only one H to abstract, so no division necessary)

Certified by MRH on 6Aug2009

Entry 46,16(e): Recommended rate coefficient is based on the author's assumption

that methyl substitution has the same influence in olefins as in alkanes.
MRH 31-Aug-2009
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 214,
    label = "Cd/H/NonDeC;C_methyl",
    group1 = 
"""
1 *1 C  0 {2,D} {3,S} {4,S}
2    C  0 {1,D}
3 *2 H  0 {1,S}
4    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.842, 'cm^3/(mol*s)', '*|/', 6),
        n = 3.5,
        alpha = 0,
        E0 = (11.66, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang [93] literature review.""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 215,
    label = "C/H2/CdCs;C_rad/CdCsS",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Cd 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cd 0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00692, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (20, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 215,
    label = "Cd/H/NonDeC;Cd_pri_rad",
    group1 = 
"""
1 *1 C  0 {2,D} {3,S} {4,S}
2    C  0 {1,D}
3 *2 H  0 {1,S}
4    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,D} {3,S}
2    C 0 {1,D}
3    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.842, 'cm^3/(mol*s)', '*|/', 6),
        n = 3.5,
        alpha = 0,
        E0 = (9.67, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang [93] literature review.""",
    longDesc = 
u"""
[93] Tsang, W. J. Phys. Chem. Ref. Data 1991, 20, 221.
CH3CH=CH2 + C2H3 --> CH3C=CH2 + C2H4

pg 240-241

Previous modified Arrhenius parameters were for RELATIVE rate (kc/ka)

Multiplied kc/ka by ka to get kc (only one H to abstract, so no division necessary)

Certified by MRH on 6Aug2009

Entry 46,19(c): No data available at the time.  The recommended rate coefficient

is based on the rate expressions for CH3 abstracting a H-atom from C3H6; all of
the Ea's have been decreased by 4kJ/mol.
MRH 31-Aug-2009
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 216,
    label = "C/H2/CdCs;C_rad/H/CtS",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Cd 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Ct 0 {1,S}
4    S  0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0325, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (18.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 216,
    label = "Cd/H/NonDeC;Ct_rad",
    group1 = 
"""
1 *1 C  0 {2,D} {3,S} {4,S}
2    C  0 {1,D}
3 *2 H  0 {1,S}
4    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,T}
2    C 0 {1,T}
""",
    kinetics = ArrheniusEP(
        A = (1210000000000.0, 'cm^3/(mol*s)', '*|/', 5),
        n = 0,
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang [93] literature review.""",
    longDesc = 
u"""
[93] Tsang, W. J. Phys. Chem. Ref. Data 1991, 20, 221.
CH3CH=CH2 + C2H --> CH3C=CH2 + C2H2 

pg 241

Verified by MRH on 6Aug2009

Entry 46,21(e): No data available at the time.  Recommended rate expression is "somewhat

smaller" than the rate of rxn C3H6+C2H --> C2H2+H2C=CH-*CH2.  The rate of this rxn
is assumed to be the rate of the rxn C2H+C2H6 --> C2H2+C2H5.
MRH 31-Aug-2009
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 217,
    label = "C/H2/CdCs;C_rad/CtCsS",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Cd 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Ct 0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.133, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (19.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""
[93] Tsang, W. J. Phys. Chem. Ref. Data 1991, 20, 221.
CH3CH=CH2 + OH --> CH3C=CH2 + H2O

pg 235-236

Valid T range in reference suggested 700-2500K

Uncertainty stated in reference was *2.0

Verified by MRH on 6Aug2009

Entry 46,6(d): No direct measurements of H-atom abstraction rxns.  The recommended

H-atom abstraction rxns are based on "the results of Tully (1988) for the rxn
of OH + C2H4 and the rate constant ratio of OH + primary Hydrogens in ethane by
Tully et al. (1986) to OH + secondary Hydrogens by Droege and Tully (1986)".  The
author has also introduced a T^2 dependence in the A-factor.
MRH 31-Aug-2009
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 217,
    label = "Cd/H/NonDeC;O_pri_rad",
    group1 = 
"""
1 *1 C  0 {2,D} {3,S} {4,S}
2    C  0 {1,D}
3 *2 H  0 {1,S}
4    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 O 1 {2,S}
2    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1110000.0, 'cm^3/(mol*s)', '*|/', 2),
        n = 2,
        alpha = 0,
        E0 = (1.45, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang [93] literature review.""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 218,
    label = "Ct_H;O2b",
    group1 = 
"""
1 *1 C 0 {2,T} {3,S}
2    C 0 {1,T}
3 *2 H 0 {1,S}
""",
    group2 = 
"""
1 *3 O 1 {2,S}
2    O 1 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (6050000000000.0, 'cm^3/(mol*s)', '*|/', 10),
        n = 0,
        alpha = 0,
        E0 = (74.52, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang [89] literature review.""",
    longDesc = 
u"""
[89] Tsang, W.; Hampson, R.F. J. Phys. Chem. Ref. Data 1986, 15, 1087.
C2H2 + O2 --> C2H + HO2 C.D.W divided original rate expression by 2, to get rate expression per H atom.

pg 1100, Chemical Kinetic Database For Combustion Chemistry, 2. Index of Reactions and Summary of Recommended Rate Expressions. No. 20,3.

Verified by Karma James

pg. 1209: Discussion on evaluated data

Recommended data based on report by Walker

NOTE: Authors note that a lower-lying channel of O2 addition, rearrangement,
and decomposition may exist.
MRH 28-Aug-2009
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 220,
    label = "Ct_H;C_rad/H2/Cs",
    group1 = 
"""
1 *1 C 0 {2,T} {3,S}
2    C 0 {1,T}
3 *2 H 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    H  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (136000000000.0, 'cm^3/(mol*s)', '*|/', 5),
        n = 0,
        alpha = 0,
        E0 = (23.45, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang [89] literature review.""",
    longDesc = 
u"""
[89] Tsang, W.; Hampson, R.F. J. Phys. Chem. Ref. Data 1986, 15, 1087.
C2H2 + C2H5 --> C2H + C2H6 C.D.W divided original rate expression by 2 (from A= 2.71E+11), to get rate expression per H atom.

pg 1100, Chemical Kinetic Database For Combustion Chemistry, 2. Index of Reactions and Summary of Recommended Rate Expressions. No. 20,17.

Verified by Karma James

pg. 1215: Discussion on evaluated data

Recommended data based on reverse rate and equilibrium constant

MRH 28-Aug-2009
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 221,
    label = "Ct_H;O_pri_rad",
    group1 = 
"""
1 *1 C 0 {2,T} {3,S}
2    C 0 {1,T}
3 *2 H 0 {1,S}
""",
    group2 = 
"""
1 *3 O 1 {2,S}
2    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (7250, 'cm^3/(mol*s)', '*|/', 10),
        n = 2.68,
        alpha = 0,
        E0 = (12.04, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang [89] literature review.""",
    longDesc = 
u"""
[89] Tsang, W.; Hampson, R.F. J. Phys. Chem. Ref. Data 1986, 15, 1087.
C2H2 + OH --> C2H + H2O C.D.W divided original rate expression by 2, to get rate expression per H atom.

pg 1100, Chemical Kinetic Database For Combustion Chemistry, 2. Index of Reactions and Summary of Recommended Rate Expressions. No. 20,6.

Verified by Karma James

pg. 1213: Discussion on evaluated data

Recommended data is derived from BEBO method calculation

MRH 28-Aug-2009
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 222,
    label = "Cb_H;O2b",
    group1 = 
"""
1 *1 Cb       0 {2,B} {3,B} {4,S}
2    {Cb,Cbf} 0 {1,B}
3    {Cb,Cbf} 0 {1,B}
4 *2 H        0 {1,S}
""",
    group2 = 
"""
1 *3 O 1 {2,S}
2    O 1 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (10520000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (60.01, 'kcal/mol'),
        Tmin = (1200, 'K'),
        Tmax = (1700, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Asaba et al. [129]. Data are estimated.""",
    longDesc = 
u"""
[129] Asaba, T.; Fujii, N.; Proc. Int. Symp. Shock Tubes Waves 1971, 8, 1.
Benzene + O2 --> phenyl + HO2 C.D.W divided original rate expression by 6(from A = 6.31E+13), to get rate expression per H atom.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 223,
    label = "Cb_H;H_rad",
    group1 = 
"""
1 *1 Cb       0 {2,B} {3,B} {4,S}
2    {Cb,Cbf} 0 {1,B}
3    {Cb,Cbf} 0 {1,B}
4 *2 H        0 {1,S}
""",
    group2 = 
"""
1 *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (100000000.0, 'cm^3/(mol*s)'),
        n = 1.8,
        alpha = 0,
        E0 = (16.35, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (800, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Mebel et al. [122] RRK(M) extrapolation.""",
    longDesc = 
u"""
[122] Mebel, A.M.; Lin, M.C.; Yu, T.; Morokuma, K. J. Phys. Chem. A. 1997, 101, 3189.
Rate constant is high pressure limit. Benzene + H --> phenyl + H2

C.D.W divided original rate expression by 6(from A = 6.02E+08), to get rate expression per H atom.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 224,
    label = "Cb_H;H_rad",
    group1 = 
"""
1 *1 Cb       0 {2,B} {3,B} {4,S}
2    {Cb,Cbf} 0 {1,B}
3    {Cb,Cbf} 0 {1,B}
4 *2 H        0 {1,S}
""",
    group2 = 
"""
1 *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (502000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (8.11, 'kcal/mol'),
        Tmin = (298, 'K'),
        Tmax = (1000, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""Nicovich et al. [130]""",
    longDesc = 
u"""
[130] Nicovich, J.M.; Ravishankara, A.R. J. Phys. Chem. 1984, 88, 2534.
Pressure 0.01-0.26 atm Excitation: flash photolysis, analysis: resonance fluorescence. Benzene + H --> phenyl + H2

C.D.W divided original rate expression by 6(from A = 3.01E+12), to get rate expression per H atom.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 225,
    label = "Cb_H;C_rad/H2/Cs",
    group1 = 
"""
1 *1 Cb       0 {2,B} {3,B} {4,S}
2    {Cb,Cbf} 0 {1,B}
3    {Cb,Cbf} 0 {1,B}
4 *2 H        0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    H  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (105000000000.0, 'cm^3/(mol*s)', '*|/', 2),
        n = 0,
        alpha = 0,
        E0 = (14.86, 'kcal/mol', '+|-', 1.19),
        Tmin = (650, 'K'),
        Tmax = (770, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""Zhang et al. [131]""",
    longDesc = 
u"""
[131] Zhang, H.X.; Ahonkhai, S.I. Back, H.M. Can. J. Chem. 1989, 67, 1541.
Pressure 0.30-0.50 atm Excitation: thermal, analysis: GC. Benzene + C2H5 --> phenyl + C2H6

C.D.W divided original rate expression by 6(from A = 6.31E+11), to get rate expression per H atom.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 226,
    label = "Cb_H;O_pri_rad",
    group1 = 
"""
1 *1 Cb       0 {2,B} {3,B} {4,S}
2    {Cb,Cbf} 0 {1,B}
3    {Cb,Cbf} 0 {1,B}
4 *2 H        0 {1,S}
""",
    group2 = 
"""
1 *3 O 1 {2,S}
2    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (27200000.0, 'cm^3/(mol*s)', '*|/', 2),
        n = 1.42,
        alpha = 0,
        E0 = (1.45, 'kcal/mol'),
        Tmin = (400, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Baulch et al. [95] literature review.""",
    longDesc = 
u"""
[95] Baulch, D.L.; Cobos, C.J.; Cox, R.A.; Esser, C.; Frank, P.; Just, T.; Kerr, J.A.; Pilling, M.J.; 
Troe, J.; Walker, R.W.; Warnatz, J. J. Phys. Chem. Ref. Data 1992, 21, 411.

Benzene + OH --> phenyl + H2O  C.D.W divided original rate expression by 6(from A = 1.63E+08), to get rate expression per H atom.

pg 420 Evaluated Kinetic Data for Combustion Modelling, Table 1. Bimolecular reactions - OH Radical Reactions.

Verified by Karma James

pg.595-597: Discussion on evaluated data

OH+C6H6 --> H2O+C6H5: Authors note that this rxn should be dominant at temperatures

above 500K.  No other comment on where the recommended rate expression comes from
(although MRH believes it is a best-fit to the available data, based on graph).
MRH 31-Aug-2009
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 227,
    label = "CO_pri;O2b",
    group1 = 
"""
1 *1 C 0 {2,D} {3,S} {4,S}
2    O 0 {1,D}
3 *2 H 0 {1,S}
4    H 0 {1,S}
""",
    group2 = 
"""
1 *3 O 1 {2,S}
2    O 1 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (23400000.0, 'cm^3/(mol*s)'),
        n = 2.05,
        alpha = 0,
        E0 = (37.93, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2200, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Michael et al. [132] Transition state theory.""",
    longDesc = 
u"""
[132] Michael, J.V.; Kumaran, S.S.; Su, M.-C. J. Phys. Chem. A. 1999, 103, 5942.
CH2O + O2 --> HCO + HO2 C.D.W divided original rate expression by 2, to get rate expression per H atom.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 228,
    label = "CO_pri;O_atom_triplet",
    group1 = 
"""
1 *1 C 0 {2,D} {3,S} {4,S}
2    O 0 {1,D}
3 *2 H 0 {1,S}
4    H 0 {1,S}
""",
    group2 = 
"""
1 *3 O 2T
""",
    kinetics = ArrheniusEP(
        A = (208000000000.0, 'cm^3/(mol*s)', '*|/', 2),
        n = 0.57,
        alpha = 0,
        E0 = (2.76, 'kcal/mol'),
        Tmin = (250, 'K'),
        Tmax = (2200, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Baulch et al. [95] literature review.""",
    longDesc = 
u"""
[95] Baulch, D.L.; Cobos, C.J.; Cox, R.A.; Esser, C.; Frank, P.; Just, T.; Kerr, J.A.; Pilling, M.J.; 
Troe, J.; Walker, R.W.; Warnatz, J. J. Phys. Chem. Ref. Data 1992, 21, 411.

CH2O + O --> HCO + OH C.D.W divided original rate expression by 2, to get rate expression per H atom.

pg 416 Evaluated Kinetic Data for Combustion Modelling, Table 1. Bimolecular reactions - O Atom Reactions.

Verified by Karma James

pg.449-450: Discussion on evaluated data

O+CH2O --> OH+HCO: "The preferred values are based on the low temperature data which are

all in good agreement, and on the higher temperature value of Bowman."
MRH 31-Aug-2009
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 229,
    label = "CO_pri;CH2_triplet",
    group1 = 
"""
1 *1 C 0 {2,D} {3,S} {4,S}
2    O 0 {1,D}
3 *2 H 0 {1,S}
4    H 0 {1,S}
""",
    group2 = 
"""
1 *3 C 2T {2,S} {3,S}
2    H 0  {1,S}
3    H 0  {1,S}
""",
    kinetics = ArrheniusEP(
        A = (3020000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang [89] literature review.""",
    longDesc = 
u"""
[89] Tsang, W.; Hampson, R.F. J. Phys. Chem. Ref. Data 1986, 15, 1087.
Rate constant is an upper limit. CH2O + CH2 --> HCO + CH3

C.D.W divided original rate expression by 2 (from A= 6.03E+09), to get rate expression per H atom.

pg 1106, Chemical Kinetic Database For Combustion Chemistry, 2. Index of Reactions and Summary of Recommended Rate Expressions. No. 26,12.

Verified by Karma James

pg. 1267: Discussion on evaluated data

Recommended data based on triplet methylene's general lack of reactivity in H-atom abstractions

NOTE: Rate coefficient is an upper limit
MRH 28-Aug-2009
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 230,
    label = "CO_pri;C_methyl",
    group1 = 
"""
1 *1 C 0 {2,D} {3,S} {4,S}
2    O 0 {1,D}
3 *2 H 0 {1,S}
4    H 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (3.89e-08, 'cm^3/(mol*s)', '*|/', 1.58),
        n = 6.1,
        alpha = 0,
        E0 = (1.97, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Baulch et al. [94] literature review.""",
    longDesc = 
u"""
[94] Baulch, D.L.; Cobos, C.J.; Cox, R.A.; Frank, P.; Hayman, G,; Just, T.; Kerr, J.A.; Murrells, T.; Pilling, M.J.; 
Troe, J.; Walker, R.W.; Warnatz, J. J. Phys. Chem. Ref. Data 1994, 23, 847.

CH2O + CH3 --> HCO + CH4 C.D.W divided original rate expression by 2, to get rate expression per H atom.

pg 862 Evaluated Kinetic Data for Combustion Modelling Supplement 1, Table 1. Bimolecular reactions - CH3 Radical Reactions.

Verified by Karma James

pg.989-990: Discussion on evaluated data

CH3+HCHO --> CH4+HCO: The recommended value is a "best fit to the data of Choudhury et al.,

the reworked data from Anastasi, together with those at lower temperatures from
Refs. 4, 5, and 7."
MRH 31-Aug-2009
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 231,
    label = "CO_pri;C_rad/H2/Cs",
    group1 = 
"""
1 *1 C 0 {2,D} {3,S} {4,S}
2    O 0 {1,D}
3 *2 H 0 {1,S}
4    H 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    H  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (2750, 'cm^3/(mol*s)', '*|/', 5),
        n = 2.81,
        alpha = 0,
        E0 = (5.86, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang [89] literature review.""",
    longDesc = 
u"""
[89] Tsang, W.; Hampson, R.F. J. Phys. Chem. Ref. Data 1986, 15, 1087.
CH2O + C2H5 --> HCO + C2H6 C.D.W divided original rate expression by 2, to get rate expression per H atom.

pg 1096, Chemical Kinetic Database For Combustion Chemistry, 2. Index of Reactions and Summary of Recommended Rate Expressions. No. 17,12.

Verified by Karma James

pg. 1178: Discussion on evaluated data

Recommended data is the rate of CH2O+CH3-->HCO+CH4.

Authors note that rate coefficients for alkyl radicals w/aldehydic H-atoms are
similar (as noted by Kerr, J.A. and Trotman-Dickenson, A.F.
MRH 28-Aug-2009
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 232,
    label = "CO_pri;C_rad/H/NonDeC",
    group1 = 
"""
1 *1 C 0 {2,D} {3,S} {4,S}
2    O 0 {1,D}
3 *2 H 0 {1,S}
4    H 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (54000000000.0, 'cm^3/(mol*s)', '*|/', 2.5),
        n = 0,
        alpha = 0,
        E0 = (6.96, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang [91] literature review.""",
    longDesc = 
u"""
[91] Tsang, W. J. Phys. Chem. Ref. Data 1988, 17, 887.
CH2O + iso-C3H7 --> HCO + C3H8 C.D.W divided original rate expression by 2, to get rate expression per H atom.

pg 894, Chemical Kinetic Database For Combustion Chemistry, Part 3. Index of Reactions and Summary of Recommended Rate Expressions. No. 42,12.

Verified by Karma James

pg. 936: Discussion on evaluated data

Entry 42,12: No data available at the time.  The author recommends a rate coefficient

expression that is twice that of the rxn i-C3H7+(CH3)2CHCHO, taken from a study
by Kerr, J.A. and Trotman-Dickenson, A.F. (1959).  The author states that a correction
was made to the 1959 report, taking the recommended rate of i-C3H7 recombination
(reported by Tsang) into consideration.
MRH 30-Aug-2009
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 233,
    label = "CO_pri;C_rad/Cs3",
    group1 = 
"""
1 *1 C 0 {2,D} {3,S} {4,S}
2    O 0 {1,D}
3 *2 H 0 {1,S}
4    H 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cs 0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1630000000.0, 'cm^3/(mol*s)', '*|/', 5),
        n = 0,
        alpha = 0,
        E0 = (3.56, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang [92] literature review.""",
    longDesc = 
u"""
[92] Tsang, W. J. Phys. Chem. Ref. Data 1990, 19, 1.
CH2O + tert-C4H9 --> HCO + iso-C4H10 C.D.W divided original rate expression by 2 (from A= 3.25E+09), to get rate expression per H atom.

pg 7, Chemical Kinetic Database For Combustion Chemistry, Part 4 - Isobutane. 

Index of Reactions and Summary of Recommended Rate Expressions. No. 44,12.

Verified by Karma James

pg.35: Discussion on evaluated data

Entry 44,12: No data available at the time.  The author recommends 2x the rate coefficient

of the rxn tC4H9+tC4H9-CHO=iC4H10+tC4H9-CO (2 vs. 1 aldehydic H-atoms); this value
was reported by Birrell and Trotman-Dickenson.  The author also notes that he has
taken into account tC4H9 combination (perhaps meaning he used a geometric mean rule
to derive the final form of the expression?)
MRH 31-Aug-2009
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 234,
    label = "CO_pri;Cd_pri_rad",
    group1 = 
"""
1 *1 C 0 {2,D} {3,S} {4,S}
2    O 0 {1,D}
3 *2 H 0 {1,S}
4    H 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,D} {3,S}
2    C 0 {1,D}
3    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (2710, 'cm^3/(mol*s)', '*|/', 5),
        n = 2.81,
        alpha = 0,
        E0 = (5.86, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang [89] literature review.""",
    longDesc = 
u"""
[89] Tsang, W.; Hampson, R.F. J. Phys. Chem. Ref. Data 1986, 15, 1087.
CH2O + C2H3 --> HCO + C2H4 C.D.W divided original rate expression by 2, to get rate expression per H atom.

pg 1099, Chemical Kinetic Database For Combustion Chemistry, 2. Index of Reactions and Summary of Recommended Rate Expressions. No. 19,12.

Verified by Karma James

pg. 1197: Discussion on evaluated data

Recommended data is the rate of CH2O+CH3-->HCO+CH4.

Authors note that rate coefficients for alkyl radicals w/aldehydic H-atoms are
similar (as noted by Kerr, J.A. and Trotman-Dickenson, A.F.
MRH 28-Aug-2009
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 235,
    label = "CO_pri;CO_rad/NonDe",
    group1 = 
"""
1 *1 C 0 {2,D} {3,S} {4,S}
2    O 0 {1,D}
3 *2 H 0 {1,S}
4    H 0 {1,S}
""",
    group2 = 
"""
1 *3 C        1 {2,D} {3,S}
2    O        0 {1,D}
3    {Cs,O,S} 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (90500000000.0, 'cm^3/(mol*s)', '*|/', 10),
        n = 0,
        alpha = 0,
        E0 = (12.92, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang [89] literature review.""",
    longDesc = 
u"""
[89] Tsang, W.; Hampson, R.F. J. Phys. Chem. Ref. Data 1986, 15, 1087.
CH2O + CH3CO --> HCO + CH3CHO C.D.W divided original rate expression by 2, to get rate expression per H atom.

pg 1102, Chemical Kinetic Database For Combustion Chemistry, 2. Index of Reactions and Summary of Recommended Rate Expressions. No. 22,12.

Verified by Karma James

pg. 1231: Discussion on evaluated data

Recommended data based on "analogous systems"

MRH 28-Aug-2009
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 236,
    label = "CO_pri;O_pri_rad",
    group1 = 
"""
1 *1 C 0 {2,D} {3,S} {4,S}
2    O 0 {1,D}
3 *2 H 0 {1,S}
4    H 0 {1,S}
""",
    group2 = 
"""
1 *3 O 1 {2,S}
2    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1720000000.0, 'cm^3/(mol*s)', '*|/', 5),
        n = 1.18,
        alpha = 0,
        E0 = (-0.45, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (3000, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Baulch et al. [95] literature review.""",
    longDesc = 
u"""
[95] Baulch, D.L.; Cobos, C.J.; Cox, R.A.; Esser, C.; Frank, P.; Just, T.; Kerr, J.A.; Pilling, M.J.; 
Troe, J.; Walker, R.W.; Warnatz, J. J. Phys. Chem. Ref. Data 1992, 21, 411.

CH2O + OH --> HCO + H2O C.D.W divided original rate expression by 2 (from A= 3.43E+09), to get rate expression per H atom.

pg 419 Evaluated Kinetic Data for Combustion Modelling, Table 1. Bimolecular reactions - OH Radical Reactions.

Verified by Karma James

pg.575-576: Discussion on evaluated data

OH+CH2O --> H2O+HCO: The recommended rate coefficient is the value reported by Tsang

and Hampson.
MRH 31-Aug-2009
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 237,
    label = "CO_pri;O_rad/NonDeC",
    group1 = 
"""
1 *1 C 0 {2,D} {3,S} {4,S}
2    O 0 {1,D}
3 *2 H 0 {1,S}
4    H 0 {1,S}
""",
    group2 = 
"""
1 *3 O  1 {2,S}
2    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (51000000000.0, 'cm^3/(mol*s)', '*|/', 3),
        n = 0,
        alpha = 0,
        E0 = (2.98, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang [89] literature review.""",
    longDesc = 
u"""
[89] Tsang, W.; Hampson, R.F. J. Phys. Chem. Ref. Data 1986, 15, 1087.
CH2O + CH3O --> HCO + CH3OH C.D.W divided original rate expression by 2, to get rate expression per H atom.

pg 1104, Chemical Kinetic Database For Combustion Chemistry, 2. Index of Reactions and Summary of Recommended Rate Expressions. No. 24,12.

Verified by Karma James

pg. 1245: Discussion on evaluated data

Recommended data based on review by Gray, based on experiments performed by Hoare and Wellington.

Authors note that experimental conditions were such that rxn of interest was
in competition with the disproportionation of two CH3O radicals (CH3O+CH3O-->CH3OH+CH2O)
MRH 28-Aug-2009
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 238,
    label = "CO_pri;O_rad/NonDeO",
    group1 = 
"""
1 *1 C 0 {2,D} {3,S} {4,S}
2    O 0 {1,D}
3 *2 H 0 {1,S}
4    H 0 {1,S}
""",
    group2 = 
"""
1 *3 O 1 {2,S}
2    O 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (20600, 'cm^3/(mol*s)'),
        n = 2.5,
        alpha = 0,
        E0 = (10.21, 'kcal/mol'),
        Tmin = (641, 'K'),
        Tmax = (1600, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Eiteneer et al. [133] literature review.""",
    longDesc = 
u"""
[133] Eiteneer, B.; Yu, C.-L.; Goldenberg, M.; Frenklach, M. J. Phys. Chem. A. 1998, 102, 5196.
CH2O + HO2 --> HCO + H2O2 C.D.W divided original rate expression by 2 (from A= 4.11E+04), to get rate expression per H atom.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 239,
    label = "CO/H/NonDe;O2b",
    group1 = 
"""
1 *1 C        0 {2,D} {3,S} {4,S}
2    O        0 {1,D}
3 *2 H        0 {1,S}
4    {Cs,O,S} 0 {1,S}
""",
    group2 = 
"""
1 *3 O 1 {2,S}
2    O 1 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (30100000000000.0, 'cm^3/(mol*s)', '*|/', 10),
        n = 0,
        alpha = 0,
        E0 = (39.15, 'kcal/mol'),
        Tmin = (600, 'K'),
        Tmax = (1100, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Baulch et al. [95] literature review.""",
    longDesc = 
u"""
[95] Baulch, D.L.; Cobos, C.J.; Cox, R.A.; Esser, C.; Frank, P.; Just, T.; Kerr, J.A.; Pilling, M.J.; 
Troe, J.; Walker, R.W.; Warnatz, J. J. Phys. Chem. Ref. Data 1992, 21, 411.

CH3CHO + O2 --> CH3CO + HO2

pg 417 Evaluated Kinetic Data for Combustion Modelling, Table 1. Bimolecular reactions - O2 Reactions.

Verified by Karma James

pg.485: Discussion on evaluated data

O2+CH3CHO --> HO2+CH3CO: "For this evaluation we prefer the approach of Walker and

the recommended value is based on the best current deltaH298 value (=163.8 kJ/mol
using deltaHf(CH3CO)=11.0 kJ/mol and deltaHf(HO2)=14.6 kJ/mol) and A=5.0x10^-11
cm3/molecule/s."
MRH 31-Aug-2009
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 240,
    label = "CO/H/NonDe;O_atom_triplet",
    group1 = 
"""
1 *1 C        0 {2,D} {3,S} {4,S}
2    O        0 {1,D}
3 *2 H        0 {1,S}
4    {Cs,O,S} 0 {1,S}
""",
    group2 = 
"""
1 *3 O 2T
""",
    kinetics = ArrheniusEP(
        A = (5000000000000.0, 'cm^3/(mol*s)', '*|/', 2),
        n = 0,
        alpha = 0,
        E0 = (1.79, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Warnatz [134] literature review""",
    longDesc = 
u"""
[134] Warnatz, J. Rate coefficeints in the C/H/O system. In Combustion Chemistry, 1984; pp 197.
CH3CHO + O --> CH3CO + OH
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 241,
    label = "C/H/Cs2Cd;C_rad/H2/S",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Cd 0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    S 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00597, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (7.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""
[134] Warnatz, J. Rate coefficeints in the C/H/O system. In Combustion Chemistry, 1984; pp 197.
CH3CHO + H --> CH3CO + H2
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 241,
    label = "CO/H/NonDe;H_rad",
    group1 = 
"""
1 *1 C        0 {2,D} {3,S} {4,S}
2    O        0 {1,D}
3 *2 H        0 {1,S}
4    {Cs,O,S} 0 {1,S}
""",
    group2 = 
"""
1 *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (40000000000000.0, 'cm^3/(mol*s)', '*|/', 2),
        n = 0,
        alpha = 0,
        E0 = (4.21, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Warnatz [134] literature review""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 242,
    label = "C/H/Cs2Cd;C_rad/H/CsS",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Cd 0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0107, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (7.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 242,
    label = "CO/H/NonDe;C_methyl",
    group1 = 
"""
1 *1 C        0 {2,D} {3,S} {4,S}
2    O        0 {1,D}
3 *2 H        0 {1,S}
4    {Cs,O,S} 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.99e-06, 'cm^3/(mol*s)', '*|/', 2),
        n = 5.64,
        alpha = 0,
        E0 = (2.46, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1250, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Baulch et al. [95] literature review.""",
    longDesc = 
u"""
[95] Baulch, D.L.; Cobos, C.J.; Cox, R.A.; Esser, C.; Frank, P.; Just, T.; Kerr, J.A.; Pilling, M.J.; 
Troe, J.; Walker, R.W.; Warnatz, J. J. Phys. Chem. Ref. Data 1992, 21, 411.

CH3CHO + CH3 --> CH3CO + CH4

pg 423 Evaluated Kinetic Data for Combustion Modelling, Table 1. Bimolecular reactions - CH3 Radical Reactions.

Verified by Karma James

pg.671: Discussion on evaluated data

CH3+CH3CHO --> CH4+CH3CO: "There are no direct studies of the kinetics of this reaction

and all of the k values are relative to methyl recombination ... The preferred values
are based on a line constructed through the mean of the low temperature data and the
data of Liu and Laidler and Colket et al."
MRH 31-Aug-2009
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 243,
    label = "C/H/Cs2Cd;C_rad/Cs2S",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Cd 0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    S  0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0043, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (7.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 243,
    label = "CO/H/NonDe;C_rad/H2/Cd",
    group1 = 
"""
1 *1 C        0 {2,D} {3,S} {4,S}
2    O        0 {1,D}
3 *2 H        0 {1,S}
4    {Cs,O,S} 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    H  0 {1,S}
4    Cd 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (380000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (7.21, 'kcal/mol'),
        Tmin = (790, 'K'),
        Tmax = (810, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""Loser et al. [135] bond strength-bond length method.""",
    longDesc = 
u"""
[135] Loser, U.; Scherzer, K.; Weber, K. Z. Phys. Chem. (Leipzig) 1989, 270, 237.
CH3CHO + CH2CH=CH2 --> CH3CO + CH3CH=CH2
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 244,
    label = "C/H/Cs2Cd;Cd_rad/NonDeS",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Cd 0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,D} {3,S}
2    C 0 {1,D}
3    S 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0357, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (-0.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 244,
    label = "CO/H/NonDe;Cd_pri_rad",
    group1 = 
"""
1 *1 C        0 {2,D} {3,S} {4,S}
2    O        0 {1,D}
3 *2 H        0 {1,S}
4    {Cs,O,S} 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,D} {3,S}
2    C 0 {1,D}
3    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (81300000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (3.68, 'kcal/mol'),
        Tmin = (480, 'K'),
        Tmax = (520, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""Scherzer et al. [136] bond energy-bond order method.""",
    longDesc = 
u"""
[136] Scherzer, K.; Loser, U.; Stiller, W. Z. Phys. Chem. 1987, 27, 300.
CH3CHO + C2H3 --> CH3CO + C2H4
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 245,
    label = "C/H/Cs2Cd;C_rad/H/CdS",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Cd 0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cd 0 {1,S}
4    S  0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0589, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (18.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""
[127] Taylor, P.H.; Rahman, M.S.; Arif, M.; Dellinger, B.; Marshall, P. Sypm. Int. Combust. Proc. 1996, 26, 497.
CH3CHO + OH --> CH3CO + H2O Pressure 0.13-0.97 atm. Rate constant is high pressure limit.

pg 501, Table 1, k2 = 2.00x10^6 T^1.8 exp(1300/RT)

Previous modified Arrhenius parameters had E=1.3 kcal/mol; it should be E=-1.3 kcal/mol

Certified by MRH on 6Aug2009
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 245,
    label = "CO/H/NonDe;O_pri_rad",
    group1 = 
"""
1 *1 C        0 {2,D} {3,S} {4,S}
2    O        0 {1,D}
3 *2 H        0 {1,S}
4    {Cs,O,S} 0 {1,S}
""",
    group2 = 
"""
1 *3 O 1 {2,S}
2    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (2000000.0, 'cm^3/(mol*s)'),
        n = 1.8,
        alpha = 0,
        E0 = (-1.3, 'kcal/mol'),
        Tmin = (295, 'K'),
        Tmax = (600, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Taylor et al. [127] Transition state theory.""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 246,
    label = "C/H/Cs2Cd;C_rad/CdCsS",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Cd 0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cd 0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00745, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (18.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""
[134] Warnatz, J. Rate coefficeints in the C/H/O system. In Combustion Chemistry, 1984; pp 197.
CH3CHO + OH --> CH3CO + H2O
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 246,
    label = "CO/H/NonDe;O_pri_rad",
    group1 = 
"""
1 *1 C        0 {2,D} {3,S} {4,S}
2    O        0 {1,D}
3 *2 H        0 {1,S}
4    {Cs,O,S} 0 {1,S}
""",
    group2 = 
"""
1 *3 O 1 {2,S}
2    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (10000000000000.0, 'cm^3/(mol*s)', '*|/', 2.51),
        n = 0,
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Warnatz [134] literature review""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 247,
    label = "C/H/Cs2Cd;C_rad/H/CtS",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Cd 0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Ct 0 {1,S}
4    S  0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.035, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (17.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""
[95] Baulch, D.L.; Cobos, C.J.; Cox, R.A.; Esser, C.; Frank, P.; Just, T.; Kerr, J.A.; Pilling, M.J.; 
Troe, J.; Walker, R.W.; Warnatz, J. J. Phys. Chem. Ref. Data 1992, 21, 411.

CH3CHO + HO2 --> CH3CO + H2O2

pg 421 Evaluated Kinetic Data for Combustion Modelling, Table 1. Bimolecular reactions - HO2 Radical Reactions.

Verified by Karma James

pg.614-615: Discussion on evaluated data

HO2+CH3CHO --> CH3CO+H2O2: "The preferred expression is based on a value of 1.7x10^-14

cm3/molecule/s at 1050K from a study performed by Colket et al. and an assumed A
factor of 5.0x10^-12 cm3/molecule/s."
MRH 31-Aug-2009
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 247,
    label = "CO/H/NonDe;O_rad/NonDeO",
    group1 = 
"""
1 *1 C        0 {2,D} {3,S} {4,S}
2    O        0 {1,D}
3 *2 H        0 {1,S}
4    {Cs,O,S} 0 {1,S}
""",
    group2 = 
"""
1 *3 O 1 {2,S}
2    O 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (3010000000000.0, 'cm^3/(mol*s)', '*|/', 5),
        n = 0,
        alpha = 0,
        E0 = (11.92, 'kcal/mol'),
        Tmin = (900, 'K'),
        Tmax = (1200, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Baulch et al. [95] literature review.""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 248,
    label = "C/H/Cs2Cd;C_rad/CtCsS",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Cd 0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Ct 0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.143, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (18.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""
[137] Mayer, S.W.; Schieler, L. J. Phys. Chem. 1968, 72, 2628.
http://dx.doi.org/10.1021/j100853a066

H2O + O2 --> OH + HO2. 
C.D.W divided original rate expression by 2, to get rate expression per H atom.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 248,
    label = "O_pri;O2b",
    group1 = 
"""
1 *1 O 0 {2,S} {3,S}
2 *2 H 0 {1,S}
3    H 0 {1,S}
""",
    group2 = 
"""
1 *3 O 1 {2,S}
2    O 1 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (2325000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (74.12, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1000, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""Mayer et al. [137] Bond energy-bond order.""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 249,
    label = "O_pri;O_atom_triplet",
    group1 = 
"""
1 *1 O 0 {2,S} {3,S}
2 *2 H 0 {1,S}
3    H 0 {1,S}
""",
    group2 = 
"""
1 *3 O 2T
""",
    kinetics = ArrheniusEP(
        A = (2630000000.0, 'cm^3/(mol*s)'),
        n = 1.2,
        alpha = 0,
        E0 = (17.83, 'kcal/mol'),
        Tmin = (298, 'K'),
        Tmax = (1000, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Karach et al. [138] Transition state theory.""",
    longDesc = 
u"""
[138] Karach, S.P.; Oscherov, V.I. J. Phys. Chem. 1999, 110, 11918.
H2O + O --> OH + OH. C.D.W divided original rate expression by 2 (from A= 2.95E+39), to get rate expression per H atom.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 250,
    label = "O_pri;O_atom_triplet",
    group1 = 
"""
1 *1 O 0 {2,S} {3,S}
2 *2 H 0 {1,S}
3    H 0 {1,S}
""",
    group2 = 
"""
1 *3 O 2T
""",
    kinetics = ArrheniusEP(
        A = (74000, 'cm^3/(mol*s)'),
        n = 2.6,
        alpha = 0,
        E0 = (15.18, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Harding et al. [139] Transition state theory.""",
    longDesc = 
u"""
[139] Harding, L.B.; Wagner, A.F. Symp. Int. Combust. proc. 1989, 22, 983.
H2O + O --> OH + OH. C.D.W divided original rate expression by 2 (from A= 1.48E+05), to get rate expression per H atom.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 251,
    label = "O_pri;H_rad",
    group1 = 
"""
1 *1 O 0 {2,S} {3,S}
2 *2 H 0 {1,S}
3    H 0 {1,S}
""",
    group2 = 
"""
1 *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (226000000.0, 'cm^3/(mol*s)', '*|/', 1.6),
        n = 1.6,
        alpha = 0,
        E0 = (19.32, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Baulch et al. [95] literature review.""",
    longDesc = 
u"""
[95] Baulch, D.L.; Cobos, C.J.; Cox, R.A.; Esser, C.; Frank, P.; Just, T.; Kerr, J.A.; Pilling, M.J.; 
Troe, J.; Walker, R.W.; Warnatz, J. J. Phys. Chem. Ref. Data 1992, 21, 411.

H2O + H --> OH + H2. C.D.W divided original rate expression by 2, to get rate expression per H atom.

pg 418 Evaluated Kinetic Data for Combustion Modelling, Table 1. Bimolecular reactions - H Atom Reactions.

NOTE: E0 Rference = 18.4, E0 RMG database = 19.32

Verified by Karma James

pg.504: Discussion on evaluated data

H+H2O --> OH+H2: "The recommended rate coefficient is based on the spare high temperature

measurements and rate data of the reverse rxn combined with the equilibrium constant."
MRH agrees with Karma.  However, the discrepancy is small and NIST's online database Webbook

has an E = 19.32 kcal/mol.
MRH 31-Aug-2009
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 252,
    label = "O_pri;C_methyl",
    group1 = 
"""
1 *1 O 0 {2,S} {3,S}
2 *2 H 0 {1,S}
3    H 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (3.2, 'cm^3/(mol*s)'),
        n = 3.31,
        alpha = 0,
        E0 = (12.56, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Ma et al. [140] Transition state theory.""",
    longDesc = 
u"""
[140] Ma, S.; Liu, R.; Sci. China Ser. S: 1996, 39, 37.
H2O + CH3 --> OH + CH4. C.D.W divided original rate expression by 2 (from A= 6.39), to get rate expression per H atom.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 253,
    label = "O_pri;C_methyl",
    group1 = 
"""
1 *1 O 0 {2,S} {3,S}
2 *2 H 0 {1,S}
3    H 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (242, 'cm^3/(mol*s)', '*|/', 1.6),
        n = 2.9,
        alpha = 0,
        E0 = (14.86, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang [89] literature review.""",
    longDesc = 
u"""
[89] Tsang, W.; Hampson, R.F. J. Phys. Chem. Ref. Data 1986, 15, 1087.
H2O + CH3 --> OH + CH4. C.D.W divided original rate expression by 2 (from A= 4.83E+02), to get rate expression per H atom.

pg 1095, Chemical Kinetic Database For Combustion Chemistry, 2. Index of Reactions and Summary of Recommended Rate Expressions. No. 16,9.

Verified by Karma James

pg. 1163: Discussion on evaluated data

Recommended data based on reverse rate and equilibrium constant

MRH 28-Aug-2009
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 254,
    label = "O_pri;C_rad/H2/Cs",
    group1 = 
"""
1 *1 O 0 {2,S} {3,S}
2 *2 H 0 {1,S}
3    H 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    H  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1700000.0, 'cm^3/(mol*s)', '*|/', 2),
        n = 1.44,
        alpha = 0,
        E0 = (20.27, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang [89] literature review.""",
    longDesc = 
u"""
[89] Tsang, W.; Hampson, R.F. J. Phys. Chem. Ref. Data 1986, 15, 1087.
H2O + C2H5 --> OH + C2H6. C.D.W divided original rate expression by 2 (from A= 3.39E+06), to get rate expression per H atom.

pg 1096, Chemical Kinetic Database For Combustion Chemistry, 2. Index of Reactions and Summary of Recommended Rate Expressions. No. 17,9.

Verified by Karma James

pg. 1177: Discussion on evaluated data

Recommended data based on reverse rate and equilibrium constant

MRH 28-Aug-2009
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 255,
    label = "O_pri;Cd_pri_rad",
    group1 = 
"""
1 *1 O 0 {2,S} {3,S}
2 *2 H 0 {1,S}
3    H 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,D} {3,S}
2    C 0 {1,D}
3    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (242, 'cm^3/(mol*s)', '*|/', 5),
        n = 2.9,
        alpha = 0,
        E0 = (14.86, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang [89] literature review.""",
    longDesc = 
u"""
[89] Tsang, W.; Hampson, R.F. J. Phys. Chem. Ref. Data 1986, 15, 1087.
H2O + C2H3 --> OH + C2H4. C.D.W divided original rate expression by 2 (from A= 4.83E+02), to get rate expression per H atom.

pg 1098, Chemical Kinetic Database For Combustion Chemistry, 2. Index of Reactions and Summary of Recommended Rate Expressions. No. 19,9.

Verified by Karma James

pg. 1196: Discussion on evaluated data

Recommended data based on expression for CH3+H2O=CH4+OH

MRH 28-Aug-2009
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 256,
    label = "O_pri;CO_pri_rad",
    group1 = 
"""
1 *1 O 0 {2,S} {3,S}
2 *2 H 0 {1,S}
3    H 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,D} {3,S}
2    O 0 {1,D}
3    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (118000000.0, 'cm^3/(mol*s)', '*|/', 5),
        n = 1.35,
        alpha = 0,
        E0 = (26.03, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang [89] literature review.""",
    longDesc = 
u"""
[89] Tsang, W.; Hampson, R.F. J. Phys. Chem. Ref. Data 1986, 15, 1087.
H2O + HCO --> OH + CH2O. C.D.W divided original rate expression by 2 (from A= 2.35E+08), to get rate expression per H atom.

pg 1094, Chemical Kinetic Database For Combustion Chemistry, 2. Index of Reactions and Summary of Recommended Rate Expressions. No. 15,9.

Verified by Karma James

pg. 1150: Discussion on evaluated data

Recommended data based on reverse rate and equilibrium constant

MRH 28-Aug-2009
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 257,
    label = "O_pri;O_pri_rad",
    group1 = 
"""
1 *1 O 0 {2,S} {3,S}
2 *2 H 0 {1,S}
3    H 0 {1,S}
""",
    group2 = 
"""
1 *3 O 1 {2,S}
2    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (2.417e-07, 'cm^3/(mol*s)'),
        n = 5.48,
        alpha = 0,
        E0 = (0.274, 'kcal/mol'),
        Tmin = (200, 'K'),
        Tmax = (700, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Masgrau et al. [141] Transition state theory.""",
    longDesc = 
u"""
[141] Masgrau, L.; Gonzalez-Lafont, A.; Lluch, J.M. J. Phys. Chem. A. 1999, 103, 1044.
H2O + OH --> OH + H2O . C.D.W refitted their k(T) to get A, n, and Ea, and divided original rate expression by 2, to get rate expression per H atom.

pg 1050, Table 4, Section: HO + HOH = HOH + OH(1), Column k_ab_CVT/SCT

MRH computed modified Arrhenius parameters using least-squares regression: ln(k) = ln(A) + n*ln(T) - (E/R)*(1/T)

E: Multiplied (E/R) expression by 1.987e-3

A: exp(ln(A)), multiplied by 6.02e23 (to convert /molecule to /mol) and divided by 2 (to get rate per H atom)

Certified by MRH on 7Aug2009
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 258,
    label = "O_pri;O_rad/NonDeC",
    group1 = 
"""
1 *1 O 0 {2,S} {3,S}
2 *2 H 0 {1,S}
3    H 0 {1,S}
""",
    group2 = 
"""
1 *3 O  1 {2,S}
2    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.174, 'cm^3/(mol*s)'),
        n = 3.8,
        alpha = 0,
        E0 = (11.49, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Jodkowski et al. [100] ab initio calculations.""",
    longDesc = 
u"""
[100] Jodkowski, J.T.; Rauez, M.-T.; Rayez, J.-C. J. Phys. Chem. A. 1999, 103, 3750.
H2O + CH3O --> OH + CH3OH C.D.W divided original rate expression by 2 (from A= 9.03E+08), to get rate expression per H atom.; This is Rxn. -R5 from mpaper

Verified by Greg Magoon: note that this reaction is endothermic; the reverse (R5), appears as #267, below
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 259,
    label = "O/H/NonDeC;O_atom_triplet",
    group1 = 
"""
1 *1 O  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 O 2T
""",
    kinetics = ArrheniusEP(
        A = (10000000000000.0, 'cm^3/(mol*s)', '*|/', 2.51),
        n = 0,
        alpha = 0,
        E0 = (4.69, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1000, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Warnatz [134] literature review""",
    longDesc = 
u"""
[134] Warnatz, J. Rate coefficeints in the C/H/O system. In Combustion Chemistry, 1984; pp 197.
CH3OH + O --> CH3O + OH
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 260,
    label = "O/H/NonDeC;CH2_triplet",
    group1 = 
"""
1 *1 O  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C 2T {2,S} {3,S}
2    H 0  {1,S}
3    H 0  {1,S}
""",
    kinetics = ArrheniusEP(
        A = (14.4, 'cm^3/(mol*s)', '*|/', 3),
        n = 3.1,
        alpha = 0,
        E0 = (6.94, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang [90] literature review.""",
    longDesc = 
u"""
[90] Tsang, W. J. Phys. Chem. Ref. Data 1987, 16, 471.
CH3OH + CH2 --> CH3O + CH3

pg 475, Chemical Kinetic Database For Combustion Chemistry, Part 2 - Methanol. 

//Index of Reactions and Summary of Recommended Rate Expressions. No. 38,25.

Verified by Karma James

Data for Rate Expression 38,26 (pg. 493)

Stated uncertainty factor is 3

Verified by MRH on 11Aug2009

Entry 38,26 (b): No data available at the time.  Author suggests the rate coefficient

expression for CH3+CH3OH=CH4+CH3O
MRH 30-Aug-2009
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 261,
    label = "O/H/NonDeC;C_methyl",
    group1 = 
"""
1 *1 O  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00037, 'cm^3/(mol*s)'),
        n = 4.7,
        alpha = 0,
        E0 = (5.78, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Jodkowski et al. [100] ab initio calculations.""",
    longDesc = 
u"""
[100] Jodkowski, J.T.; Rauez, M.-T.; Rayez, J.-C. J. Phys. Chem. A. 1999, 103, 3750.
The calculated rate constants are in good agreement with experiment. CH3OH + CH3 --> CH3O + CH4 (Rxn. R3 from paper)

Verified by Greg Magoon: I changed upper temperature to 2000 K (was 2500) in line with other reactions from same paper; note that according to the paper, this reaction is very slightly endothermic; the exothermic reverse (-R3) is included above as #177
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 262,
    label = "O/H/NonDeC;C_rad/H2/Cs",
    group1 = 
"""
1 *1 O  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    H  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (14.4, 'cm^3/(mol*s)', '*|/', 3),
        n = 3.1,
        alpha = 0,
        E0 = (8.94, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang [90] literature review.""",
    longDesc = 
u"""
[90] Tsang, W. J. Phys. Chem. Ref. Data 1987, 16, 471.
CH3OH + C2H5 --> CH3O + C2H6

pg 475, Chemical Kinetic Database For Combustion Chemistry, Part 2 - Methanol. 

Index of Reactions and Summary of Recommended Rate Expressions. No. 38,17.

Verified by Karma James

pg. 489: Discussion on evaluated data

Entry 38,17 (b): No data available at the time.  Author notes ethyl radicals are known

to be considerably less reactive than methyl.  Author recommends the rate coefficient
expression of CH3+CH3OH=CH4+CH3O, with a slight adjustment (based on the observed
trends in methyl vs. ethyl radical reactivity with hydrocarbons).
MRH 30-Aug-2009

//263: [90] Tsang, W. J. Phys. Chem. Ref. Data 1987, 16, 471.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 263,
    label = "O/H/NonDeC;C_rad/H/NonDeC",
    group1 = 
"""
1 *1 O  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (14.5, 'cm^3/(mol*s)', '*|/', 5),
        n = 3.1,
        alpha = 0,
        E0 = (10.33, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang [91] literature review.""",
    longDesc = 
u"""
[91] Tsang, W. J. Phys. Chem. Ref. Data 1988, 17, 887.
CH3OH + iso-C3H7 --> CH3O + C3H8

//WAS UNABLE TO VERIFY DATA!!! DATA NOT FOUND IN REFERENCE.

Ref[90] was incorrect; rate matches that reported in Ref[91].

pg. 944: Discussion on evaluated data

Entry 42,38 (b)

No experimental data, at the time

Recommended rate is based on C2H5+CH3OH=C2H6+CH3O

Verified by MRH on 10Aug2009

MRH 30-Aug-2009

//264: [90] Tsang, W. J. Phys. Chem. Ref. Data 1987, 16, 471.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 264,
    label = "O/H/NonDeC;C_rad/Cs3",
    group1 = 
"""
1 *1 O  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cs 0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1510, 'cm^3/(mol*s)', '*|/', 10),
        n = 1.8,
        alpha = 0,
        E0 = (9.36, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang [92] literature review.""",
    longDesc = 
u"""
[92] Tsang, W. J. Phys. Chem. Ref. Data 1990, 19, 1.
CH3OH + tert-C4H9 --> CH3O + iso-C4H10

//WAS UNABLE TO VERIFY DATA!!! DATA NOT FOUND IN REFERENCE.

Ref[90] was incorrect; rate matches that reported in Ref[92].

pg.44: Discussion on evaluated data

Entry 44,38(b)

Reference reports reaction as: t-C4H9+CH3OH=t-C4H10+CH3O

This is a typo: no t-C4H10 molecule exists (should be i-C4H10)
No experimental data, at the time

Recommended rate is based on reverse rxn and equilibrium constant

Verified by MRH on 10Aug2009
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 265,
    label = "O/H/NonDeC;Cd_pri_rad",
    group1 = 
"""
1 *1 O  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,D} {3,S}
2    C 0 {1,D}
3    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (14.4, 'cm^3/(mol*s)', '*|/', 10),
        n = 3.1,
        alpha = 0,
        E0 = (6.94, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang [90] literature review.""",
    longDesc = 
u"""
[90] Tsang, W. J. Phys. Chem. Ref. Data 1987, 16, 471.
CH3OH + C2H3 --> CH3O + C2H4

pg 475, Chemical Kinetic Database For Combustion Chemistry, Part 2 - Methanol. 

Index of Reactions and Summary of Recommended Rate Expressions. No. 38,19.

Verified by Karma James

pg. 489: Discussion on evaluated data

Entry 38,19 (b): No data available at the time.  Author recommends the rate coefficient

expression for CH3+CH3OH=CH4+CH3O.
MRH 30-Aug-2009
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 266,
    label = "O/H/NonDeC;Ct_rad",
    group1 = 
"""
1 *1 O  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,T}
2    C 0 {1,T}
""",
    kinetics = ArrheniusEP(
        A = (1210000000000.0, 'cm^3/(mol*s)', '*|/', 5),
        n = 0,
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang [90] literature review.""",
    longDesc = 
u"""
[90] Tsang, W. J. Phys. Chem. Ref. Data 1987, 16, 471.
CH3OH + C2H --> CH3O + C2H2

pg 475, Chemical Kinetic Database For Combustion Chemistry, Part 2 - Methanol. 

Index of Reactions and Summary of Recommended Rate Expressions. No. 38,21.

Verified by Karma James

pg. 490: Discussion on evaluated data

Entry 38,21 (b): No data available at the time.  Author recommends a rate coefficient

expression based on measurements of C2H+CH4 and C2H+C2H6 rxns
MRH 30-Aug-2009
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 267,
    label = "O/H/NonDeC;O_pri_rad",
    group1 = 
"""
1 *1 O  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 O 1 {2,S}
2    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (17.3, 'cm^3/(mol*s)'),
        n = 3.4,
        alpha = 0,
        E0 = (-1.14, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Jodkowski et al. [100] ab initio calculations.""",
    longDesc = 
u"""
[100] Jodkowski, J.T.; Rauez, M.-T.; Rayez, J.-C. J. Phys. Chem. A. 1999, 103, 3750.
The calculated rate constants are in good agreement with experiment. CH3OH + OH --> CH3O + H2O (Rxn. R5 from paper)

Verified by Greg Magoon (cf. reverse, #258, above)
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 268,
    label = "O/H/NonDeC;O_pri_rad",
    group1 = 
"""
1 *1 O  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 O 1 {2,S}
2    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (10000000000000.0, 'cm^3/(mol*s)', '*|/', 3.16),
        n = 0,
        alpha = 0,
        E0 = (1.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Warnatz [134] literature review""",
    longDesc = 
u"""
[134] Warnatz, J. Rate coefficeints in the C/H/O system. In Combustion Chemistry, 1984; pp 197.
CH3OH + OH --> CH3O + H2O
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 272,
    label = "C/H2/CdCd;C_rad/H2/S",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Cd 0 {1,S}
5    Cd 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    S 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00754, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (7.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 273,
    label = "C/H2/CdCd;C_rad/H/CsS",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Cd 0 {1,S}
5    Cd 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0135, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (7.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 274,
    label = "C/H2/CdCd;C_rad/Cs2S",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Cd 0 {1,S}
5    Cd 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    S  0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00543, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 275,
    label = "C/H2/CdCd;Cd_rad/NonDeS",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Cd 0 {1,S}
5    Cd 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,D} {3,S}
2    C 0 {1,D}
3    S 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.045, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (-0.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 276,
    label = "C/H2/CdCd;C_rad/H/CdS",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Cd 0 {1,S}
5    Cd 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cd 0 {1,S}
4    S  0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0744, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (18.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 277,
    label = "C/H2/CdCd;C_rad/CdCsS",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Cd 0 {1,S}
5    Cd 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cd 0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0094, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (18.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 278,
    label = "C/H2/CdCd;C_rad/H/CtS",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Cd 0 {1,S}
5    Cd 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Ct 0 {1,S}
4    S  0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0442, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (16.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 279,
    label = "C/H2/CdCd;C_rad/CtCsS",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Cd 0 {1,S}
5    Cd 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Ct 0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.181, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (17.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 301,
    label = "H2O2;InChI=1/C4H9O/c1-2-3-4-5/h5H,1-4H2",
    group1 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 0 {1,S} {4,S}
3 *2 H 0 {1,S}
4    H 0 {2,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {6,S} {7,S}
2     C 0 {1,S} {3,S} {8,S} {9,S}
3     C 0 {2,S} {4,S} {10,S} {11,S}
4     C 0 {3,S} {5,S} {12,S} {13,S}
5     O 0 {4,S} {14,S}
6     H 0 {1,S}
7     H 0 {1,S}
8     H 0 {2,S}
9     H 0 {2,S}
10    H 0 {3,S}
11    H 0 {3,S}
12    H 0 {4,S}
13    H 0 {4,S}
14    H 0 {5,S}
""",
    kinetics = ArrheniusEP(
        A = (2.88, 'cm^3/(mol*s)'),
        n = 3.16,
        alpha = 0,
        E0 = (0.75, 'kcal/mol'),
        Tmin = (600, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""MRH CBS-QB3 calculations w/o HR corrections""",
    longDesc = 
u"""
MRH CBS-QB3 calculations w/o HR corrections
H2O2 + *CH2CH2CH2CH2OH = nButanol + HO2

CBS-QB3 method was used to calculate electronic energy of reactants, products, and TS; frequencies were
calculated using B3LYP/CBSB7 method.  Arrhenius expression was computed using CanTherm: an asymmetric Eckart
tunneling correction was employed and the frequencies were scaled by 0.99 (as suggested by Montgomery et al.
J.Chem.Phys. 110 (1999) 2822-2827).  The external symmetry number for H2O2 was 2; the external symmetry number
for the remaining species and TS were set to 1.  The rate coefficient was computed at 600-2000K (in 200 K increments).
The computed pre-exponential factor was divided by 2 and this is the reported value.

For nButanol+HO2=H2O2+*CH2CH2CH2CH2OH:
Moc et al. (AIP Conference Proceedings (2009) 1148 161-164 "The Unimolecular Decomposition
and H Abstraction Reactions by HO and HO2 from n-Butanol") report reaction barriers and
enthalpies(0 K); our CBS-QB3 calculations are shown in comparison (all units are kcal/mol).
				G3		CCSD(T)/cc-pVTZ		CBS-QB3
Barrier:		18.8		19.62			17.57
Enthalpy:		14.25		14.66			13.70
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 302,
    label = "H2O2;InChI=1/C4H9O/c1-2-3-4-5/h2,5H,3-4H2,1H3",
    group1 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 0 {1,S} {4,S}
3 *2 H 0 {1,S}
4    H 0 {2,S}
""",
    group2 = 
"""
1     C 0 {2,S} {6,S} {7,S} {8,S}
2  *3 C 1 {1,S} {3,S} {9,S}
3     C 0 {2,S} {4,S} {10,S} {11,S}
4     C 0 {3,S} {5,S} {12,S} {13,S}
5     O 0 {4,S} {14,S}
6     H 0 {1,S}
7     H 0 {1,S}
8     H 0 {1,S}
9     H 0 {2,S}
10    H 0 {3,S}
11    H 0 {3,S}
12    H 0 {4,S}
13    H 0 {4,S}
14    H 0 {5,S}
""",
    kinetics = ArrheniusEP(
        A = (0.675, 'cm^3/(mol*s)'),
        n = 3.42,
        alpha = 0,
        E0 = (1.43, 'kcal/mol'),
        Tmin = (600, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""MRH CBS-QB3 calculations w/o HR corrections""",
    longDesc = 
u"""
MRH CBS-QB3 calculations w/o HR corrections
H2O2 + CH3*CHCH2CH2OH = nButanol + HO2

CBS-QB3 method was used to calculate electronic energy of reactants, products, and TS; frequencies were
calculated using B3LYP/CBSB7 method.  Arrhenius expression was computed using CanTherm: an asymmetric Eckart
tunneling correction was employed and the frequencies were scaled by 0.99 (as suggested by Montgomery et al.
J.Chem.Phys. 110 (1999) 2822-2827).  The external symmetry number for H2O2 was 2; the external symmetry number
for the remaining species and TS were set to 1.  The rate coefficient was computed at 600-2000K (in 200 K increments).
The computed pre-exponential factor was divided by 2 and this is the reported value.

For nButanol+HO2=H2O2+CH3*CHCH2CH2OH:
Moc et al. (AIP Conference Proceedings (2009) 1148 161-164 "The Unimolecular Decomposition
and H Abstraction Reactions by HO and HO2 from n-Butanol") report reaction barriers and
enthalpies(0 K); our CBS-QB3 calculations are shown in comparison (all units are kcal/mol).
				G3		CCSD(T)/cc-pVTZ		CBS-QB3
Barrier:		14.64		15.47			14.72
Enthalpy:		11.05		12.41			10.11
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 303,
    label = "C/H/CdCd;C_rad/H2/S",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Cd 0 {1,S}
4    Cd 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    S 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00607, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (6.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 303,
    label = "H2O2;InChI=1/C4H9O/c1-2-3-4-5/h3,5H,2,4H2,1H3",
    group1 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 0 {1,S} {4,S}
3 *2 H 0 {1,S}
4    H 0 {2,S}
""",
    group2 = 
"""
1     C 0 {2,S} {6,S} {7,S} {8,S}
2     C 0 {1,S} {3,S} {9,S} {10,S}
3  *3 C 1 {2,S} {4,S} {11,S}
4     C 0 {3,S} {5,S} {12,S} {13,S}
5     O 0 {4,S} {14,S}
6     H 0 {1,S}
7     H 0 {1,S}
8     H 0 {1,S}
9     H 0 {2,S}
10    H 0 {2,S}
11    H 0 {3,S}
12    H 0 {4,S}
13    H 0 {4,S}
14    H 0 {5,S}
""",
    kinetics = ArrheniusEP(
        A = (0.3145, 'cm^3/(mol*s)'),
        n = 3.52,
        alpha = 0,
        E0 = (1.61, 'kcal/mol'),
        Tmin = (600, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""MRH CBS-QB3 calculations w/o HR corrections""",
    longDesc = 
u"""
MRH CBS-QB3 calculations w/o HR corrections
H2O2 + CH3CH2*CHCH2OH = nButanol + HO2

CBS-QB3 method was used to calculate electronic energy of reactants, products, and TS; frequencies were
calculated using B3LYP/CBSB7 method.  Arrhenius expression was computed using CanTherm: an asymmetric Eckart
tunneling correction was employed and the frequencies were scaled by 0.99 (as suggested by Montgomery et al.
J.Chem.Phys. 110 (1999) 2822-2827).  The external symmetry number for H2O2 was 2; the external symmetry number
for the remaining species and TS were set to 1.  The rate coefficient was computed at 600-2000K (in 200 K increments).
The computed pre-exponential factor was divided by 2 and this is the reported value.

For nButanol+HO2=H2O2+CH3CH2*CHCH2OH:
Moc et al. (AIP Conference Proceedings (2009) 1148 161-164 "The Unimolecular Decomposition
and H Abstraction Reactions by HO and HO2 from n-Butanol") report reaction barriers and
enthalpies(0 K); our CBS-QB3 calculations are shown in comparison (all units are kcal/mol).
				G3		CCSD(T)/cc-pVTZ		CBS-QB3
Barrier:		15.43		16.37			16.33
Enthalpy:		13.53		14.02			11.48
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 304,
    label = "C/H/CdCd;C_rad/H/CsS",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Cd 0 {1,S}
4    Cd 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0108, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (6.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 304,
    label = "H2O2;InChI=1/C4H9O/c1-2-3-4-5/h4-5H,2-3H2,1H3",
    group1 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 0 {1,S} {4,S}
3 *2 H 0 {1,S}
4    H 0 {2,S}
""",
    group2 = 
"""
1     C 0 {2,S} {6,S} {7,S} {8,S}
2     C 0 {1,S} {3,S} {9,S} {10,S}
3     C 0 {2,S} {4,S} {11,S} {12,S}
4  *3 C 1 {3,S} {5,S} {13,S}
5     O 0 {4,S} {14,S}
6     H 0 {1,S}
7     H 0 {1,S}
8     H 0 {1,S}
9     H 0 {2,S}
10    H 0 {2,S}
11    H 0 {3,S}
12    H 0 {3,S}
13    H 0 {4,S}
14    H 0 {5,S}
""",
    kinetics = ArrheniusEP(
        A = (1.485, 'cm^3/(mol*s)'),
        n = 3.39,
        alpha = 0,
        E0 = (1.4, 'kcal/mol'),
        Tmin = (600, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""MRH CBS-QB3 calculations w/o HR corrections""",
    longDesc = 
u"""
MRH CBS-QB3 calculations w/o HR corrections
H2O2 + CH3CH2CH2*CHOH = nButanol + HO2

CBS-QB3 method was used to calculate electronic energy of reactants, products, and TS; frequencies were
calculated using B3LYP/CBSB7 method.  Arrhenius expression was computed using CanTherm: an asymmetric Eckart
tunneling correction was employed and the frequencies were scaled by 0.99 (as suggested by Montgomery et al.
J.Chem.Phys. 110 (1999) 2822-2827).  The external symmetry number for H2O2 was 2; the external symmetry number
for the remaining species and TS were set to 1.  The rate coefficient was computed at 600-2000K (in 200 K increments).
The computed pre-exponential factor was divided by 2 and this is the reported value.

For nButanol+HO2=H2O2+CH3CH2CH2*CHOH:
Moc et al. (AIP Conference Proceedings (2009) 1148 161-164 "The Unimolecular Decomposition
and H Abstraction Reactions by HO and HO2 from n-Butanol") report reaction barriers and
enthalpies(0 K); our CBS-QB3 calculations are shown in comparison (all units are kcal/mol).
				G3		CCSD(T)/cc-pVTZ		CBS-QB3
Barrier:		12.62		13.23			11.74
Enthalpy:		 8.35		 8.63			 7.17
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 305,
    label = "C/H/CdCd;C_rad/Cs2S",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Cd 0 {1,S}
4    Cd 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    S  0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00437, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (5.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""
MRH CBS-QB3 calculations w/o HR corrections
H2O2 + *CH2CH2CH[OH]CH3 = 2-Butanol + HO2

CBS-QB3 method was used to calculate electronic energy of reactants, products, and TS; frequencies were
calculated using B3LYP/CBSB7 method.  Arrhenius expression was computed using CanTherm: an asymmetric Eckart
tunneling correction was employed and the frequencies were scaled by 0.99 (as suggested by Montgomery et al.
J.Chem.Phys. 110 (1999) 2822-2827).  The external symmetry number for H2O2 was 2; the external symmetry number
for the remaining species and TS were set to 1.  The rate coefficient was computed at 600-2000K (in 200 K increments).
The computed pre-exponential factor was divided by 2 and this is the reported value.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 305,
    label = "H2O2;InChI=1/C4H9O/c1-3-4(2)5/h4-5H,1,3H2,2H3",
    group1 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 0 {1,S} {4,S}
3 *2 H 0 {1,S}
4    H 0 {2,S}
""",
    group2 = 
"""
1  *3 C 1 {3,S} {6,S} {7,S}
2     C 0 {4,S} {8,S} {9,S} {10,S}
3     C 0 {1,S} {4,S} {11,S} {12,S}
4     C 0 {2,S} {3,S} {5,S} {13,S}
5     O 0 {4,S} {14,S}
6     H 0 {1,S}
7     H 0 {1,S}
8     H 0 {2,S}
9     H 0 {2,S}
10    H 0 {2,S}
11    H 0 {3,S}
12    H 0 {3,S}
13    H 0 {4,S}
14    H 0 {5,S}
""",
    kinetics = ArrheniusEP(
        A = (5.75, 'cm^3/(mol*s)'),
        n = 2.94,
        alpha = 0,
        E0 = (0.46, 'kcal/mol'),
        Tmin = (600, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""MRH CBS-QB3 calculations w/o HR corrections""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 306,
    label = "C/H/CdCd;Cd_rad/NonDeS",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Cd 0 {1,S}
4    Cd 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,D} {3,S}
2    C 0 {1,D}
3    S 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0363, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (-1.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 306,
    label = "H2O2;InChI=1/C4H9O/c1-3-4(2)5/h3-5H,1-2H3",
    group1 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 0 {1,S} {4,S}
3 *2 H 0 {1,S}
4    H 0 {2,S}
""",
    group2 = 
"""
1     C 0 {3,S} {6,S} {7,S} {8,S}
2     C 0 {4,S} {9,S} {10,S} {11,S}
3  *3 C 1 {1,S} {4,S} {12,S}
4     C 0 {2,S} {3,S} {5,S} {13,S}
5     O 0 {4,S} {14,S}
6     H 0 {1,S}
7     H 0 {1,S}
8     H 0 {1,S}
9     H 0 {2,S}
10    H 0 {2,S}
11    H 0 {2,S}
12    H 0 {3,S}
13    H 0 {4,S}
14    H 0 {5,S}
""",
    kinetics = ArrheniusEP(
        A = (0.875, 'cm^3/(mol*s)'),
        n = 2.91,
        alpha = 0,
        E0 = (-0.41, 'kcal/mol'),
        Tmin = (600, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""MRH CBS-QB3 calculations w/o HR corrections""",
    longDesc = 
u"""
MRH CBS-QB3 calculations w/o HR corrections
H2O2 + CH3*CHCH[OH]CH3 = 2-Butanol + HO2

CBS-QB3 method was used to calculate electronic energy of reactants, products, and TS; frequencies were
calculated using B3LYP/CBSB7 method.  Arrhenius expression was computed using CanTherm: an asymmetric Eckart
tunneling correction was employed and the frequencies were scaled by 0.99 (as suggested by Montgomery et al.
J.Chem.Phys. 110 (1999) 2822-2827).  The external symmetry number for H2O2 was 2; the external symmetry number
for the remaining species and TS were set to 1.  The rate coefficient was computed at 600-2000K (in 200 K increments).
The computed pre-exponential factor was divided by 2 and this is the reported value.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 307,
    label = "C/H/CdCd;C_rad/H/CdS",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Cd 0 {1,S}
4    Cd 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cd 0 {1,S}
4    S  0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0598, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (17.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""
MRH CBS-QB3 calculations w/o HR corrections
H2O2 + CH3CH2*C[OH]CH3 = 2-Butanol + HO2

CBS-QB3 method was used to calculate electronic energy of reactants, products, and TS; frequencies were
calculated using B3LYP/CBSB7 method.  Arrhenius expression was computed using CanTherm: an asymmetric Eckart
tunneling correction was employed and the frequencies were scaled by 0.99 (as suggested by Montgomery et al.
J.Chem.Phys. 110 (1999) 2822-2827).  The external symmetry number for H2O2 was 2; the external symmetry number
for the remaining species and TS were set to 1.  The rate coefficient was computed at 600-2000K (in 200 K increments).
The computed pre-exponential factor was divided by 2 and this is the reported value.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 307,
    label = "H2O2;InChI=1/C4H9O/c1-3-4(2)5/h5H,3H2,1-2H3",
    group1 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 0 {1,S} {4,S}
3 *2 H 0 {1,S}
4    H 0 {2,S}
""",
    group2 = 
"""
1     C 0 {3,S} {6,S} {7,S} {8,S}
2     C 0 {4,S} {9,S} {10,S} {11,S}
3     C 0 {1,S} {4,S} {12,S} {13,S}
4  *3 C 1 {2,S} {3,S} {5,S}
5     O 0 {4,S} {14,S}
6     H 0 {1,S}
7     H 0 {1,S}
8     H 0 {1,S}
9     H 0 {2,S}
10    H 0 {2,S}
11    H 0 {2,S}
12    H 0 {3,S}
13    H 0 {3,S}
14    H 0 {5,S}
""",
    kinetics = ArrheniusEP(
        A = (17.3, 'cm^3/(mol*s)'),
        n = 3.05,
        alpha = 0,
        E0 = (1.02, 'kcal/mol'),
        Tmin = (600, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""MRH CBS-QB3 calculations w/o HR corrections""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 308,
    label = "C/H/CdCd;C_rad/CdCsS",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Cd 0 {1,S}
4    Cd 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cd 0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00756, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (17.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 308,
    label = "H2O2;InChI=1/C4H9O/c1-3-4(2)5/h4-5H,2-3H2,1H3",
    group1 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 0 {1,S} {4,S}
3 *2 H 0 {1,S}
4    H 0 {2,S}
""",
    group2 = 
"""
1     C 0 {3,S} {6,S} {7,S} {8,S}
2  *3 C 1 {4,S} {9,S} {10,S}
3     C 0 {1,S} {4,S} {11,S} {12,S}
4     C 0 {2,S} {3,S} {5,S} {13,S}
5     O 0 {4,S} {14,S}
6     H 0 {1,S}
7     H 0 {1,S}
8     H 0 {1,S}
9     H 0 {2,S}
10    H 0 {2,S}
11    H 0 {3,S}
12    H 0 {3,S}
13    H 0 {4,S}
14    H 0 {5,S}
""",
    kinetics = ArrheniusEP(
        A = (0.3055, 'cm^3/(mol*s)'),
        n = 3.53,
        alpha = 0,
        E0 = (1.52, 'kcal/mol'),
        Tmin = (600, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""MRH CBS-QB3 calculations w/o HR corrections""",
    longDesc = 
u"""
MRH CBS-QB3 calculations w/o HR corrections
H2O2 + CH3CH2CH[OH]*CH2 = 2-Butanol + HO2

CBS-QB3 method was used to calculate electronic energy of reactants, products, and TS; frequencies were
calculated using B3LYP/CBSB7 method.  Arrhenius expression was computed using CanTherm: an asymmetric Eckart
tunneling correction was employed and the frequencies were scaled by 0.99 (as suggested by Montgomery et al.
J.Chem.Phys. 110 (1999) 2822-2827).  The external symmetry number for H2O2 was 2; the external symmetry number
for the remaining species and TS were set to 1.  The rate coefficient was computed at 600-2000K (in 200 K increments).
The computed pre-exponential factor was divided by 2 and this is the reported value.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 309,
    label = "C/H/CdCd;C_rad/H/CtS",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Cd 0 {1,S}
4    Cd 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Ct 0 {1,S}
4    S  0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0356, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (15.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""
MRH CBS-QB3 calculations w/o HR corrections
H2O2 + HOC[*CH2][CH3][CH3] = tert-Butanol + HO2

CBS-QB3 method was used to calculate electronic energy of reactants, products, and TS; frequencies were
calculated using B3LYP/CBSB7 method.  Arrhenius expression was computed using CanTherm: an asymmetric Eckart
tunneling correction was employed and the frequencies were scaled by 0.99 (as suggested by Montgomery et al.
J.Chem.Phys. 110 (1999) 2822-2827).  The external symmetry number for H2O2 was 2; the external symmetry number
for the remaining species and TS were set to 1.  The rate coefficient was computed at 600-2000K (in 200 K increments).
The computed pre-exponential factor was divided by 2 and this is the reported value.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 309,
    label = "H2O2;InChI=1/C4H9O/c1-4(2,3)5/h5H,1H2,2-3H3",
    group1 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 0 {1,S} {4,S}
3 *2 H 0 {1,S}
4    H 0 {2,S}
""",
    group2 = 
"""
1  *3 C 1 {4,S} {6,S} {7,S}
2     C 0 {4,S} {8,S} {9,S} {10,S}
3     C 0 {4,S} {11,S} {12,S} {13,S}
4     C 0 {1,S} {2,S} {3,S} {5,S}
5     O 0 {4,S} {14,S}
6     H 0 {1,S}
7     H 0 {1,S}
8     H 0 {2,S}
9     H 0 {2,S}
10    H 0 {2,S}
11    H 0 {3,S}
12    H 0 {3,S}
13    H 0 {3,S}
14    H 0 {5,S}
""",
    kinetics = ArrheniusEP(
        A = (0.21, 'cm^3/(mol*s)'),
        n = 3.53,
        alpha = 0,
        E0 = (1.56, 'kcal/mol'),
        Tmin = (600, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""MRH CBS-QB3 calculations w/o HR corrections""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 310,
    label = "C/H/CdCd;C_rad/CtCsS",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Cd 0 {1,S}
4    Cd 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Ct 0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.145, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (16.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""
JDM increased the activation energy for the abstraction of a vinyl-H hydrogen by O2.  August 2010.
Using the Evans-Polanyi principle with alpha = 1, the activation energy was increased by delta(vinyl radical - alkyl radical) = 9.6 kcal/mol.
Reaction rate 154 was the basis for this.

Previously, rates had been calculated by an averaging-of-averages technique, which resulted in the abstraction of vinyl-H's being orders of magnitude faster than the abstraction of alkyl-H's.

These rates have been calculated based on rates of primary- and secondary-alkyl H-abstractions by O2. 
The A-factors have remained the same.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 334,
    label = "C/H3/Ct;C_rad/H2/S",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    Ct 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    S 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00388, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (10.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 335,
    label = "C/H3/Ct;C_rad/H/CsS",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    Ct 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00693, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (10.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 336,
    label = "C/H3/Ct;C_rad/Cs2S",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    Ct 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    S  0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00279, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (10.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 337,
    label = "C/H3/Ct;Cd_rad/NonDeS",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    Ct 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,D} {3,S}
2    C 0 {1,D}
3    S 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0232, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (2.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 338,
    label = "C/H3/Ct;C_rad/H/CdS",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    Ct 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cd 0 {1,S}
4    S  0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0383, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (21.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 339,
    label = "C/H3/Ct;C_rad/CdCsS",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    Ct 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cd 0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00483, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (21.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 340,
    label = "C/H3/Ct;C_rad/H/CtS",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    Ct 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Ct 0 {1,S}
4    S  0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0227, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (20.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 341,
    label = "C/H3/Ct;C_rad/CtCsS",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    Ct 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Ct 0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.093, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (21.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 365,
    label = "C/H2/CtCs;C_rad/H2/S",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Ct 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    S 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0053, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (9.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 366,
    label = "C/H2/CtCs;C_rad/H/CsS",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Ct 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00946, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (9.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 367,
    label = "C/H2/CtCs;C_rad/Cs2S",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Ct 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    S  0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00382, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 368,
    label = "C/H2/CtCs;Cd_rad/NonDeS",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Ct 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,D} {3,S}
2    C 0 {1,D}
3    S 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0317, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (1.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 369,
    label = "C/H2/CtCs;C_rad/H/CdS",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Ct 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cd 0 {1,S}
4    S  0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0523, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (20.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 370,
    label = "C/H2/CtCs;C_rad/CdCsS",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Ct 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cd 0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0066, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (20.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 371,
    label = "C/H2/CtCs;C_rad/H/CtS",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Ct 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Ct 0 {1,S}
4    S  0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0311, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (18.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 372,
    label = "C/H2/CtCs;C_rad/CtCsS",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Ct 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Ct 0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.127, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (19.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 396,
    label = "C/H/Cs2Ct;C_rad/H2/S",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Ct 0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    S 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00947, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (7.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 397,
    label = "C/H/Cs2Ct;C_rad/H/CsS",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Ct 0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0169, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (7.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 398,
    label = "C/H/Cs2Ct;C_rad/Cs2S",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Ct 0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    S  0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00682, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (7.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 399,
    label = "C/H/Cs2Ct;Cd_rad/NonDeS",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Ct 0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,D} {3,S}
2    C 0 {1,D}
3    S 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0566, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 400,
    label = "C/H/Cs2Ct;C_rad/H/CdS",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Ct 0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cd 0 {1,S}
4    S  0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0934, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (18.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 401,
    label = "C/H/Cs2Ct;C_rad/CdCsS",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Ct 0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cd 0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0118, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (18.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 402,
    label = "C/H/Cs2Ct;C_rad/H/CtS",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Ct 0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Ct 0 {1,S}
4    S  0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0555, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (17.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 403,
    label = "C/H/Cs2Ct;C_rad/CtCsS",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Ct 0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Ct 0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.227, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (18.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 427,
    label = "C/H2/CtCt;C_rad/H2/S",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Ct 0 {1,S}
5    Ct 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    S 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00674, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (7.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 428,
    label = "C/H2/CtCt;C_rad/H/CsS",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Ct 0 {1,S}
5    Ct 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.012, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (7.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 429,
    label = "C/H2/CtCt;C_rad/Cs2S",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Ct 0 {1,S}
5    Ct 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    S  0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00486, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (7.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 430,
    label = "C/H2/CtCt;Cd_rad/NonDeS",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Ct 0 {1,S}
5    Ct 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,D} {3,S}
2    C 0 {1,D}
3    S 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0403, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (-0.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 431,
    label = "C/H2/CtCt;C_rad/H/CdS",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Ct 0 {1,S}
5    Ct 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cd 0 {1,S}
4    S  0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0665, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (18.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 432,
    label = "C/H2/CtCt;C_rad/CdCsS",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Ct 0 {1,S}
5    Ct 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cd 0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0084, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (18.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 433,
    label = "C/H2/CtCt;C_rad/H/CtS",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Ct 0 {1,S}
5    Ct 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Ct 0 {1,S}
4    S  0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0395, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (17, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 434,
    label = "C/H2/CtCt;C_rad/CtCsS",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Ct 0 {1,S}
5    Ct 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Ct 0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.162, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (17.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 458,
    label = "C/H/CtCt;C_rad/H2/S",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Ct 0 {1,S}
4    Ct 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    S 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00743, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (6.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 459,
    label = "C/H/CtCt;C_rad/H/CsS",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Ct 0 {1,S}
4    Ct 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0133, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (6.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 460,
    label = "C/H/CtCt;C_rad/Cs2S",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Ct 0 {1,S}
4    Ct 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    S  0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00535, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 461,
    label = "C/H/CtCt;Cd_rad/NonDeS",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Ct 0 {1,S}
4    Ct 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,D} {3,S}
2    C 0 {1,D}
3    S 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0444, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (-1.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 462,
    label = "C/H/CtCt;C_rad/H/CdS",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Ct 0 {1,S}
4    Ct 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cd 0 {1,S}
4    S  0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0733, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (17.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 463,
    label = "C/H/CtCt;C_rad/CdCsS",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Ct 0 {1,S}
4    Ct 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cd 0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00926, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (17.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 464,
    label = "C/H/CtCt;C_rad/H/CtS",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Ct 0 {1,S}
4    Ct 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Ct 0 {1,S}
4    S  0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0436, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (15.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 465,
    label = "C/H/CtCt;C_rad/CtCsS",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Ct 0 {1,S}
4    Ct 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Ct 0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.178, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (16.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 486,
    label = "Orad_O_H;O_rad/NonDeO",
    group1 = 
"""
1 *1 O 0 {2,S} {3,S}
2 *2 H 0 {1,S}
3    O 1 {1,S}
""",
    group2 = 
"""
1 *3 O 1 {2,S}
2    O 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (17500000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (-3.275, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""[8] Curran's estimation in reaction type 13, RO2 + HO2 --> RO2H + O2""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 487,
    label = "C/H2/NonDeC;O2b",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 O 1 {2,S}
2    O 1 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (316000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (43.3, 'kcal/mol'),
        Tmin = (378, 'K'),
        Tmax = (433, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""ET Denisov, LN Denisova. Int J Chem Kinet 8:123-130, 1975 for BuCH2(CH-H)Me in benzene""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 489,
    label = "C/H3/Cb;C_rad/H2/S",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    Cb 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    S 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00125, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (12, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 490,
    label = "C/H3/Cb;C_rad/H/CsS",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    Cb 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00223, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (12, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 491,
    label = "C/H3/Cb;C_rad/Cs2S",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    Cb 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    S  0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.000898, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (11.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 492,
    label = "C/H3/Cb;Cd_rad/NonDeS",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    Cb 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,D} {3,S}
2    C 0 {1,D}
3    S 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00745, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (4.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 493,
    label = "C/H3/Cb;C_rad/H/CdS",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    Cb 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cd 0 {1,S}
4    S  0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0123, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (23.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 494,
    label = "C/H3/Cb;C_rad/CdCsS",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    Cb 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cd 0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00155, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (23.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 495,
    label = "C/H3/Cb;C_rad/H/CtS",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    Cb 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Ct 0 {1,S}
4    S  0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00731, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (21.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 496,
    label = "C/H3/Cb;C_rad/CtCsS",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    Cb 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Ct 0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0299, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (22.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 500,
    label = "CO_pri;InChI=1/C4H7/c1-4(2)3/h1-2H2,3H3",
    group1 = 
"""
1 *1 C 0 {2,D} {3,S} {4,S}
2    O 0 {1,D}
3 *2 H 0 {1,S}
4    H 0 {1,S}
""",
    group2 = 
"""
1     C 0 {2,D} {5,S} {6,S}
2     C 0 {1,D} {3,S} {4,S}
3  *3 C 1 {2,S} {7,S} {8,S}
4     C 0 {2,S} {9,S} {10,S} {11,S}
5     H 0 {1,S}
6     H 0 {1,S}
7     H 0 {3,S}
8     H 0 {3,S}
9     H 0 {4,S}
10    H 0 {4,S}
11    H 0 {4,S}
""",
    kinetics = ArrheniusEP(
        A = (0.03065, 'cm^3/(mol*s)'),
        n = 3.95,
        alpha = 0,
        E0 = (12.22, 'kcal/mol'),
        Tmin = (600, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""MRH CBS-QB3 calculations w/o HR corrections""",
    longDesc = 
u"""
MRH CBS-QB3 calculations w/o HR corrections
CH2O + H2C=C[*CH2][CH3] = HCO + H2C=C[CH3]2

Geometries and energies of reactants, products, and TS were computed using the CBS-QB3 methodology; frequencies
were calculated at B3LYP/CBSB7.  Arrhenius expression was computed using CanTherm; an asymmetric Eckart tunneling
correction was employed and the frequencies were scaled by 0.99 (as suggested by Montgomergy et al.; J. Chem. Phys.
110 (1999) 2822-2827).  The Arrhenius fit was based on k(T) at T=600, 800, 1000, 1200, 1400, 1600, 1800, and 2000K.
The external symmetry number for CH2O and iso-butene was 2; the external symmetry for all others was 1.  The
electronic spin multiplicity was 1 for CH2O and iso-butene; the electronic spin multiplicity for all others was 2.
The computed pre-exponential factor was divided by 2 (symmetry of CH2O), from 6.13e-02 to 3.065e-02.

There are no rate coefficients for this reaction in the literature (based on MRH's limited search).
   Tsang {J. Phys. Chem. Ref. Data 20 (1991) 221-273} recommends the following for the reaction of 
   CH2O + H2C=CH-*CH2 = HCO + H2C=CH-CH3: k(T) = 1.26e+08 * T^1.9 * exp(-18.184 kcal/mol / RT) cm3 mol-1 s-1.
   This rate coefficient is 25-85x faster than MRH's calculation over the range 600-2000K.
   
   The previous estimate by RMG for this reaction was: k(T) = 5.500e+03 * T^2.81 * exp(-5.86 kcal/mol / RT) cm3 mol-1 s-1.
   This rate coefficient is 80-13,000x faster than MRH's calculation over the range 600-2000K.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 501,
    label = "InChI=1/C3H8/c1-3-2/h3H2,1-2H3;InChI=1/C4H9O/c1-4(2)3-5/h5H,3H2,1-2H3",
    group1 = 
"""
1     C 0 {2,S} {4,S} {5,S} {6,S}
2  *1 C 0 {1,S} {3,S} {7,S} {8,S}
3     C 0 {2,S} {9,S} {10,S} {11,S}
4     H 0 {1,S}
5     H 0 {1,S}
6     H 0 {1,S}
7  *2 H 0 {2,S}
8     H 0 {2,S}
9     H 0 {3,S}
10    H 0 {3,S}
11    H 0 {3,S}
""",
    group2 = 
"""
1     C 0 {2,S} {6,S} {7,S} {8,S}
2  *3 C 1 {1,S} {3,S} {5,S}
3     C 0 {2,S} {4,S} {9,S} {10,S}
4     O 0 {3,S} {11,S}
5     C 0 {2,S} {12,S} {13,S} {14,S}
6     H 0 {1,S}
7     H 0 {1,S}
8     H 0 {1,S}
9     H 0 {3,S}
10    H 0 {3,S}
11    H 0 {4,S}
12    H 0 {5,S}
13    H 0 {5,S}
14    H 0 {5,S}
""",
    kinetics = ArrheniusEP(
        A = (9.11e-07, 'cm^3/(mol*s)'),
        n = 5.11,
        alpha = 0,
        E0 = (5.69, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""MRH CBS-QB3 calculations w/o HR corrections""",
    longDesc = 
u"""
MRH CBS-QB3 calculations w/RRHO [MRHCBSQB3RRHO]_.  Pre-exponential was divided by 2 to get per-H value.

InChI=1/C3H8/c1-3-2/h3H2,1-2H3 (external symmetry number = 2, spin multiplicity = 1)
 +
InChI=1/C4H9O/c1-4(2)3-5/h5H,3H2,1-2H3 (external symmetry number = 1, spin multiplicity = 2)
 <=> (TS: external symmetry number = 1, spin multiplicity = 2)
InChI=1/C3H7/c1-3-2/h3H,1-2H3 (external symmetry number = 1, spin multiplicity = 2)
 +
InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3 (external symmetry number = 1, spin multiplicity = 1)
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 502,
    label = "InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3/alpha;InChI=1/C3H7/c1-3-2/h3H,1-2H3",
    group1 = 
"""
1     C 0 {2,S} {6,S} {7,S} {8,S}
2     C 0 {1,S} {3,S} {5,S} {9,S}
3  *1 C 0 {2,S} {4,S} {10,S} {11,S}
4     O 0 {3,S} {12,S}
5     C 0 {2,S} {13,S} {14,S} {15,S}
6     H 0 {1,S}
7     H 0 {1,S}
8     H 0 {1,S}
9     H 0 {2,S}
10 *2 H 0 {3,S}
11    H 0 {3,S}
12    H 0 {4,S}
13    H 0 {5,S}
14    H 0 {5,S}
15    H 0 {5,S}
""",
    group2 = 
"""
1     C 0 {2,S} {4,S} {5,S} {6,S}
2  *3 C 1 {1,S} {3,S} {7,S}
3     C 0 {2,S} {8,S} {9,S} {10,S}
4     H 0 {1,S}
5     H 0 {1,S}
6     H 0 {1,S}
7     H 0 {2,S}
8     H 0 {3,S}
9     H 0 {3,S}
10    H 0 {3,S}
""",
    kinetics = ArrheniusEP(
        A = (1.06e-06, 'cm^3/(mol*s)'),
        n = 5.06,
        alpha = 0,
        E0 = (4.89, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""MRH CBS-QB3 calculations w/o HR corrections""",
    longDesc = 
u"""
MRH CBS-QB3 calculations w/RRHO [MRHCBSQB3RRHO]_.  Pre-exponential was divided by 2 to get per-H value.

InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3 (external symmetry number = 1, spin multiplicity = 1)
 +
InChI=1/C3H7/c1-3-2/h3H,1-2H3 (external symmetry number = 1, spin multiplicity = 2)
 <=> (TS: external symmetry number = 1, spin multiplicity = 2)
InChI=1/C4H9O/c1-4(2)3-5/h3-5H,1-2H3 (external symmetry number = 1, spin multiplicity = 2)
 +
InChI=1/C3H8/c1-3-2/h3H2,1-2H3 (external symmetry number = 2, spin multiplicity = 1)
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 503,
    label = "InChI=1/C4H8/c1-4(2)3/h1H2,2-3H3;InChI=1/C4H9O/c1-4(2)3-5/h4-5H,1,3H2,2H3",
    group1 = 
"""
1     C 0 {2,D} {5,S} {6,S}
2     C 0 {1,D} {3,S} {4,S}
3  *1 C 0 {2,S} {7,S} {8,S} {9,S}
4     C 0 {2,S} {10,S} {11,S} {12,S}
5     H 0 {1,S}
6     H 0 {1,S}
7  *2 H 0 {3,S}
8     H 0 {3,S}
9     H 0 {3,S}
10    H 0 {4,S}
11    H 0 {4,S}
12    H 0 {4,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {6,S} {7,S}
2     C 0 {1,S} {3,S} {5,S} {8,S}
3     C 0 {2,S} {4,S} {9,S} {10,S}
4     O 0 {3,S} {11,S}
5     C 0 {2,S} {12,S} {13,S} {14,S}
6     H 0 {1,S}
7     H 0 {1,S}
8     H 0 {2,S}
9     H 0 {3,S}
10    H 0 {3,S}
11    H 0 {4,S}
12    H 0 {5,S}
13    H 0 {5,S}
14    H 0 {5,S}
""",
    kinetics = ArrheniusEP(
        A = (8.39e-06, 'cm^3/(mol*s)'),
        n = 4.89,
        alpha = 0,
        E0 = (4.32, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""MRH CBS-QB3 calculations w/o HR corrections""",
    longDesc = 
u"""
MRH CBS-QB3 calculations w/RRHO [MRHCBSQB3RRHO]_.  Pre-exponential was divided by 6 to get per-H value.

InChI=1/C4H8/c1-4(2)3/h1H2,2-3H3 (external symmetry number = 2, spin multiplicity = 1)
 +
InChI=1/C4H9O/c1-4(2)3-5/h4-5H,1,3H2,2H3 (external symmetry number = 1, spin multiplicity = 2)
 <=> (TS: external symmetry number = 1, spin multiplicity = 2)
InChI=1/C4H7/c1-4(2)3/h1-2H2,3H3 (external symmetry number = 1, spin multiplicity = 2)
 +
InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3 (external symmetry number = 1, spin multiplicity = 1)
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 504,
    label = "InChI=1/C4H8/c1-4(2)3/h1H2,2-3H3;InChI=1/C4H9O/c1-4(2)3-5/h5H,3H2,1-2H3",
    group1 = 
"""
1     C 0 {2,D} {5,S} {6,S}
2     C 0 {1,D} {3,S} {4,S}
3  *1 C 0 {2,S} {7,S} {8,S} {9,S}
4     C 0 {2,S} {10,S} {11,S} {12,S}
5     H 0 {1,S}
6     H 0 {1,S}
7  *2 H 0 {3,S}
8     H 0 {3,S}
9     H 0 {3,S}
10    H 0 {4,S}
11    H 0 {4,S}
12    H 0 {4,S}
""",
    group2 = 
"""
1     C 0 {2,S} {6,S} {7,S} {8,S}
2  *3 C 1 {1,S} {3,S} {5,S}
3     C 0 {2,S} {4,S} {9,S} {10,S}
4     O 0 {3,S} {11,S}
5     C 0 {2,S} {12,S} {13,S} {14,S}
6     H 0 {1,S}
7     H 0 {1,S}
8     H 0 {1,S}
9     H 0 {3,S}
10    H 0 {3,S}
11    H 0 {4,S}
12    H 0 {5,S}
13    H 0 {5,S}
14    H 0 {5,S}
""",
    kinetics = ArrheniusEP(
        A = (1.44e-05, 'cm^3/(mol*s)'),
        n = 4.52,
        alpha = 0,
        E0 = (1.46, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""MRH CBS-QB3 calculations w/o HR corrections""",
    longDesc = 
u"""
MRH CBS-QB3 calculations w/RRHO [MRHCBSQB3RRHO]_.  Pre-exponential was divided by 6 to get per-H value.

InChI=1/C4H8/c1-4(2)3/h1H2,2-3H3 (external symmetry number = 2, spin multiplicity = 1)
 +
InChI=1/C4H9O/c1-4(2)3-5/h5H,3H2,1-2H3 (external symmetry number = 1, spin multiplicity = 2)
 <=> (TS: external symmetry number = 1, spin multiplicity = 2)
InChI=1/C4H7/c1-4(2)3/h1-2H2,3H3 (external symmetry number = 1, spin multiplicity = 2)
 +
InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3 (external symmetry number = 1, spin multiplicity = 1)
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 505,
    label = "InChI=1/C4H8/c1-4(2)3/h1H2,2-3H3;InChI=1/C4H9O/c1-4(2)3-5/h3-5H,1-2H3",
    group1 = 
"""
1     C 0 {2,D} {5,S} {6,S}
2     C 0 {1,D} {3,S} {4,S}
3  *1 C 0 {2,S} {7,S} {8,S} {9,S}
4     C 0 {2,S} {10,S} {11,S} {12,S}
5     H 0 {1,S}
6     H 0 {1,S}
7  *2 H 0 {3,S}
8     H 0 {3,S}
9     H 0 {3,S}
10    H 0 {4,S}
11    H 0 {4,S}
12    H 0 {4,S}
""",
    group2 = 
"""
1     C 0 {2,S} {6,S} {7,S} {8,S}
2     C 0 {1,S} {3,S} {5,S} {9,S}
3  *3 C 1 {2,S} {4,S} {10,S}
4     O 0 {3,S} {11,S}
5     C 0 {2,S} {12,S} {13,S} {14,S}
6     H 0 {1,S}
7     H 0 {1,S}
8     H 0 {1,S}
9     H 0 {2,S}
10    H 0 {3,S}
11    H 0 {4,S}
12    H 0 {5,S}
13    H 0 {5,S}
14    H 0 {5,S}
""",
    kinetics = ArrheniusEP(
        A = (4.91e-06, 'cm^3/(mol*s)'),
        n = 5.07,
        alpha = 0,
        E0 = (3.66, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""MRH CBS-QB3 calculations w/o HR corrections""",
    longDesc = 
u"""
MRH CBS-QB3 calculations w/RRHO [MRHCBSQB3RRHO]_.  Pre-exponential was divided by 6 to get per-H value.

InChI=1/C4H8/c1-4(2)3/h1H2,2-3H3 (external symmetry number = 2, spin multiplicity = 1)
 +
InChI=1/C4H9O/c1-4(2)3-5/h3-5H,1-2H3 (external symmetry number = 1, spin multiplicity = 2)
 <=> (TS: external symmetry number = 1, spin multiplicity = 2)
InChI=1/C4H7/c1-4(2)3/h1-2H2,3H3 (external symmetry number = 1, spin multiplicity = 2)
 +
InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3 (external symmetry number = 1, spin multiplicity = 1)
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 506,
    label = "InChI=1/C4H8/c1-4(2)3/h1H2,2-3H3;InChI=1/C4H9O/c1-4(2)3-5/h4H,3H2,1-2H3",
    group1 = 
"""
1     C 0 {2,D} {5,S} {6,S}
2     C 0 {1,D} {3,S} {4,S}
3  *1 C 0 {2,S} {7,S} {8,S} {9,S}
4     C 0 {2,S} {10,S} {11,S} {12,S}
5     H 0 {1,S}
6     H 0 {1,S}
7  *2 H 0 {3,S}
8     H 0 {3,S}
9     H 0 {3,S}
10    H 0 {4,S}
11    H 0 {4,S}
12    H 0 {4,S}
""",
    group2 = 
"""
1     C 0 {2,S} {6,S} {7,S} {8,S}
2     C 0 {1,S} {3,S} {5,S} {9,S}
3     C 0 {2,S} {4,S} {10,S} {11,S}
4  *3 O 1 {3,S}
5     C 0 {2,S} {12,S} {13,S} {14,S}
6     H 0 {1,S}
7     H 0 {1,S}
8     H 0 {1,S}
9     H 0 {2,S}
10    H 0 {3,S}
11    H 0 {3,S}
12    H 0 {5,S}
13    H 0 {5,S}
14    H 0 {5,S}
""",
    kinetics = ArrheniusEP(
        A = (0.583, 'cm^3/(mol*s)'),
        n = 3.74,
        alpha = 0,
        E0 = (1.45, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""MRH CBS-QB3 calculations w/o HR corrections""",
    longDesc = 
u"""
MRH CBS-QB3 calculations w/RRHO [MRHCBSQB3RRHO]_.  Pre-exponential was divided by 6 to get per-H value.

InChI=1/C4H8/c1-4(2)3/h1H2,2-3H3 (external symmetry number = 2, spin multiplicity = 1)
 +
InChI=1/C4H9O/c1-4(2)3-5/h4H,3H2,1-2H3 (external symmetry number = 1, spin multiplicity = 2)
 <=> (TS: external symmetry number = 1, spin multiplicity = 2)
InChI=1/C4H7/c1-4(2)3/h1-2H2,3H3 (external symmetry number = 1, spin multiplicity = 2)
 +
InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3 (external symmetry number = 1, spin multiplicity = 1)
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 507,
    label = "InChI=1/C3H6/c1-3-2/h3H,1H2,2H3;InChI=1/C4H9O/c1-4(2)3-5/h4-5H,1,3H2,2H3",
    group1 = 
"""
1 *1 C 0 {2,S} {4,S} {5,S} {6,S}
2    C 0 {1,S} {3,D} {7,S}
3    C 0 {2,D} {8,S} {9,S}
4 *2 H 0 {1,S}
5    H 0 {1,S}
6    H 0 {1,S}
7    H 0 {2,S}
8    H 0 {3,S}
9    H 0 {3,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {6,S} {7,S}
2     C 0 {1,S} {3,S} {5,S} {8,S}
3     C 0 {2,S} {4,S} {9,S} {10,S}
4     O 0 {3,S} {11,S}
5     C 0 {2,S} {12,S} {13,S} {14,S}
6     H 0 {1,S}
7     H 0 {1,S}
8     H 0 {2,S}
9     H 0 {3,S}
10    H 0 {3,S}
11    H 0 {4,S}
12    H 0 {5,S}
13    H 0 {5,S}
14    H 0 {5,S}
""",
    kinetics = ArrheniusEP(
        A = (3.36e-05, 'cm^3/(mol*s)'),
        n = 4.75,
        alpha = 0,
        E0 = (4.13, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""MRH CBS-QB3 calculations w/o HR corrections""",
    longDesc = 
u"""
MRH CBS-QB3 calculations w/RRHO [MRHCBSQB3RRHO]_.  Pre-exponential was divided by 3 to get per-H value.

InChI=1/C3H6/c1-3-2/h3H,1H2,2H3 (external symmetry number = 1, spin multiplicity = 1)
 +
InChI=1/C4H9O/c1-4(2)3-5/h4-5H,1,3H2,2H3 (external symmetry number = 1, spin multiplicity = 2)
 <=> (TS: external symmetry number = 1, spin multiplicity = 2)
InChI=1/C3H5/c1-3-2/h3H,1-2H2 (external symmetry number = 2, spin multiplicity = 2)
 +
InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3 (external symmetry number = 1, spin multiplicity = 1)

Tsang [Tsang1991]_ recommends k(T) = 2.23e+00 * (T/K)^3.5 * exp(-6.64 kcal/mol /RT) cm3 mol-1 s-1
for the reaction C3H6 + iso-C4H9 = iso-C4H10 + C3H5.  The new rate coefficient expression is
in good agreement with this expression (within 10% over most of the valid temperature range).
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 508,
    label = "InChI=1/C3H6/c1-3-2/h3H,1H2,2H3;InChI=1/C4H9O/c1-4(2)3-5/h5H,3H2,1-2H3",
    group1 = 
"""
1 *1 C 0 {2,S} {4,S} {5,S} {6,S}
2    C 0 {1,S} {3,D} {7,S}
3    C 0 {2,D} {8,S} {9,S}
4 *2 H 0 {1,S}
5    H 0 {1,S}
6    H 0 {1,S}
7    H 0 {2,S}
8    H 0 {3,S}
9    H 0 {3,S}
""",
    group2 = 
"""
1     C 0 {2,S} {6,S} {7,S} {8,S}
2  *3 C 1 {1,S} {3,S} {5,S}
3     C 0 {2,S} {4,S} {9,S} {10,S}
4     O 0 {3,S} {11,S}
5     C 0 {2,S} {12,S} {13,S} {14,S}
6     H 0 {1,S}
7     H 0 {1,S}
8     H 0 {1,S}
9     H 0 {3,S}
10    H 0 {3,S}
11    H 0 {4,S}
12    H 0 {5,S}
13    H 0 {5,S}
14    H 0 {5,S}
""",
    kinetics = ArrheniusEP(
        A = (1.64e-06, 'cm^3/(mol*s)'),
        n = 4.98,
        alpha = 0,
        E0 = (3.18, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""MRH CBS-QB3 calculations w/o HR corrections""",
    longDesc = 
u"""
MRH CBS-QB3 calculations w/RRHO [MRHCBSQB3RRHO]_.  Pre-exponential was divided by 3 to get per-H value.

InChI=1/C3H6/c1-3-2/h3H,1H2,2H3 (external symmetry number = 1, spin multiplicity = 1)
 +
InChI=1/C4H9O/c1-4(2)3-5/h5H,3H2,1-2H3 (external symmetry number = 1, spin multiplicity = 2)
 <=> (TS: external symmetry number = 1, spin multiplicity = 2)
InChI=1/C3H5/c1-3-2/h3H,1-2H2 (external symmetry number = 2, spin multiplicity = 2)
 +
InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3 (external symmetry number = 1, spin multiplicity = 1)

Tsang [Tsang1991]_ recommends k(T) = 3.01e-05 * (T/K)^4.9 * exp(-7.95 kcal/mol /RT) cm3 mol-1 s-1
for the reaction C3H6 + tert-C4H9 = iso-C4H10 + C3H5.  The new rate coefficient expression is faster
by as much as 10x over of the valid temperature range.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 509,
    label = "InChI=1/C3H6/c1-3-2/h3H,1H2,2H3;InChI=1/C4H9O/c1-4(2)3-5/h3-5H,1-2H3",
    group1 = 
"""
1 *1 C 0 {2,S} {4,S} {5,S} {6,S}
2    C 0 {1,S} {3,D} {7,S}
3    C 0 {2,D} {8,S} {9,S}
4 *2 H 0 {1,S}
5    H 0 {1,S}
6    H 0 {1,S}
7    H 0 {2,S}
8    H 0 {3,S}
9    H 0 {3,S}
""",
    group2 = 
"""
1     C 0 {2,S} {6,S} {7,S} {8,S}
2     C 0 {1,S} {3,S} {5,S} {9,S}
3  *3 C 1 {2,S} {4,S} {10,S}
4     O 0 {3,S} {11,S}
5     C 0 {2,S} {12,S} {13,S} {14,S}
6     H 0 {1,S}
7     H 0 {1,S}
8     H 0 {1,S}
9     H 0 {2,S}
10    H 0 {3,S}
11    H 0 {4,S}
12    H 0 {5,S}
13    H 0 {5,S}
14    H 0 {5,S}
""",
    kinetics = ArrheniusEP(
        A = (3.11e-06, 'cm^3/(mol*s)'),
        n = 4.97,
        alpha = 0,
        E0 = (3.64, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""MRH CBS-QB3 calculations w/o HR corrections""",
    longDesc = 
u"""
MRH CBS-QB3 calculations w/RRHO [MRHCBSQB3RRHO]_.  Pre-exponential was divided by 3 to get per-H value.

InChI=1/C3H6/c1-3-2/h3H,1H2,2H3 (external symmetry number = 1, spin multiplicity = 1)
 +
InChI=1/C4H9O/c1-4(2)3-5/h3-5H,1-2H3 (external symmetry number = 1, spin multiplicity = 2)
 <=> (TS: external symmetry number = 1, spin multiplicity = 2)
InChI=1/C3H5/c1-3-2/h3H,1-2H2 (external symmetry number = 2, spin multiplicity = 2)
 +
InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3 (external symmetry number = 1, spin multiplicity = 1)
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 510,
    label = "InChI=1/C3H6/c1-3-2/h3H,1H2,2H3;InChI=1/C4H9O/c1-4(2)3-5/h4H,3H2,1-2H3",
    group1 = 
"""
1 *1 C 0 {2,S} {4,S} {5,S} {6,S}
2    C 0 {1,S} {3,D} {7,S}
3    C 0 {2,D} {8,S} {9,S}
4 *2 H 0 {1,S}
5    H 0 {1,S}
6    H 0 {1,S}
7    H 0 {2,S}
8    H 0 {3,S}
9    H 0 {3,S}
""",
    group2 = 
"""
1     C 0 {2,S} {6,S} {7,S} {8,S}
2     C 0 {1,S} {3,S} {5,S} {9,S}
3     C 0 {2,S} {4,S} {10,S} {11,S}
4  *3 O 1 {3,S}
5     C 0 {2,S} {12,S} {13,S} {14,S}
6     H 0 {1,S}
7     H 0 {1,S}
8     H 0 {1,S}
9     H 0 {2,S}
10    H 0 {3,S}
11    H 0 {3,S}
12    H 0 {5,S}
13    H 0 {5,S}
14    H 0 {5,S}
""",
    kinetics = ArrheniusEP(
        A = (0.119, 'cm^3/(mol*s)'),
        n = 3.9,
        alpha = 0,
        E0 = (1.81, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""MRH CBS-QB3 calculations w/o HR corrections""",
    longDesc = 
u"""
MRH CBS-QB3 calculations w/RRHO [MRHCBSQB3RRHO]_.  Pre-exponential was divided by 3 to get per-H value.

InChI=1/C3H6/c1-3-2/h3H,1H2,2H3 (external symmetry number = 1, spin multiplicity = 1)
 +
InChI=1/C4H9O/c1-4(2)3-5/h4H,3H2,1-2H3 (external symmetry number = 1, spin multiplicity = 2)
 <=> (TS: external symmetry number = 1, spin multiplicity = 2)
InChI=1/C3H5/c1-3-2/h3H,1-2H2 (external symmetry number = 2, spin multiplicity = 2)
 +
InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3 (external symmetry number = 1, spin multiplicity = 1)
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 511,
    label = "InChI=1/C2H6/c1-2/h1-2H3;InChI=1/C4H9O/c1-4(2)3-5/h4-5H,1,3H2,2H3",
    group1 = 
"""
1 *1 C 0 {2,S} {3,S} {4,S} {5,S}
2    C 0 {1,S} {6,S} {7,S} {8,S}
3 *2 H 0 {1,S}
4    H 0 {1,S}
5    H 0 {1,S}
6    H 0 {2,S}
7    H 0 {2,S}
8    H 0 {2,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {6,S} {7,S}
2     C 0 {1,S} {3,S} {5,S} {8,S}
3     C 0 {2,S} {4,S} {9,S} {10,S}
4     O 0 {3,S} {11,S}
5     C 0 {2,S} {12,S} {13,S} {14,S}
6     H 0 {1,S}
7     H 0 {1,S}
8     H 0 {2,S}
9     H 0 {3,S}
10    H 0 {3,S}
11    H 0 {4,S}
12    H 0 {5,S}
13    H 0 {5,S}
14    H 0 {5,S}
""",
    kinetics = ArrheniusEP(
        A = (3.21e-06, 'cm^3/(mol*s)'),
        n = 5.28,
        alpha = 0,
        E0 = (7.78, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""MRH CBS-QB3 calculations w/o HR corrections""",
    longDesc = 
u"""
MRH CBS-QB3 calculations w/RRHO [MRHCBSQB3RRHO]_.  Pre-exponential was divided by 6 to get per-H value.

InChI=1/C2H6/c1-2/h1-2H3 (external symmetry number = 6, spin multiplicity = 1)
 +
InChI=1/C4H9O/c1-4(2)3-5/h4-5H,1,3H2,2H3 (external symmetry number = 1, spin multiplicity = 2)
 <=> (TS: external symmetry number = 1, spin multiplicity = 2)
InChI=1/C2H5/c1-2/h1H2,2H3 (external symmetry number = 1, spin multiplicity = 2)
 +
InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3 (external symmetry number = 1, spin multiplicity = 1)

Tsang [Tsang1990]_ recommends k(T) = 2.894e-01 * (T/K)^3.7 * exp(-9.78 kcal/mol /RT) cm3 mol-1 s-1
for the reaction C2H6 + iso-C4H9 = iso-C4H10 + C2H5.  The new rate coefficient expression is faster
by 10-100x over of the valid temperature range.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 512,
    label = "InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3/beta;InChI=1/C2H5/c1-2/h1H2,2H3",
    group1 = 
"""
1     C 0 {2,S} {6,S} {7,S} {8,S}
2  *1 C 0 {1,S} {3,S} {5,S} {9,S}
3     C 0 {2,S} {4,S} {10,S} {11,S}
4     O 0 {3,S} {12,S}
5     C 0 {2,S} {13,S} {14,S} {15,S}
6     H 0 {1,S}
7     H 0 {1,S}
8     H 0 {1,S}
9  *2 H 0 {2,S}
10    H 0 {3,S}
11    H 0 {3,S}
12    H 0 {4,S}
13    H 0 {5,S}
14    H 0 {5,S}
15    H 0 {5,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    C 0 {1,S} {5,S} {6,S} {7,S}
3    H 0 {1,S}
4    H 0 {1,S}
5    H 0 {2,S}
6    H 0 {2,S}
7    H 0 {2,S}
""",
    kinetics = ArrheniusEP(
        A = (1.41e-05, 'cm^3/(mol*s)'),
        n = 4.83,
        alpha = 0,
        E0 = (4.37, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""MRH CBS-QB3 calculations w/o HR corrections""",
    longDesc = 
u"""
MRH CBS-QB3 calculations w/RRHO [MRHCBSQB3RRHO]_.

InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3 (external symmetry number = 1, spin multiplicity = 1)
 +
InChI=1/C2H5/c1-2/h1H2,2H3 (external symmetry number = 1, spin multiplicity = 2)
 <=> (TS: external symmetry number = 1, spin multiplicity = 2)
InChI=1/C4H9O/c1-4(2)3-5/h5H,3H2,1-2H3 (external symmetry number = 1, spin multiplicity = 2)
 +
InChI=1/C2H6/c1-2/h1-2H3 (external symmetry number = 6, spin multiplicity = 1)

Tsang [Tsang1990]_ recommends k(T) = 5.41e-01 * (T/K)^3.46 * exp(-5.96 kcal/mol /RT) cm3 mol-1 s-1
for the reaction iso-C4H10 + C2H5 = C2H6 + tert-C4H9.  The new rate coefficient expression is
in good agreement with this expression (within a factor of 1.6 over the valid temperature range).
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 513,
    label = "InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3/alpha;InChI=1/C2H5/c1-2/h1H2,2H3",
    group1 = 
"""
1     C 0 {2,S} {6,S} {7,S} {8,S}
2     C 0 {1,S} {3,S} {5,S} {9,S}
3  *1 C 0 {2,S} {4,S} {10,S} {11,S}
4     O 0 {3,S} {12,S}
5     C 0 {2,S} {13,S} {14,S} {15,S}
6     H 0 {1,S}
7     H 0 {1,S}
8     H 0 {1,S}
9     H 0 {2,S}
10 *2 H 0 {3,S}
11    H 0 {3,S}
12    H 0 {4,S}
13    H 0 {5,S}
14    H 0 {5,S}
15    H 0 {5,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    C 0 {1,S} {5,S} {6,S} {7,S}
3    H 0 {1,S}
4    H 0 {1,S}
5    H 0 {2,S}
6    H 0 {2,S}
7    H 0 {2,S}
""",
    kinetics = ArrheniusEP(
        A = (4.25e-06, 'cm^3/(mol*s)'),
        n = 5.01,
        alpha = 0,
        E0 = (5.01, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""MRH CBS-QB3 calculations w/o HR corrections""",
    longDesc = 
u"""
MRH CBS-QB3 calculations w/RRHO [MRHCBSQB3RRHO]_.  Pre-exponential was divided by 2 to get per-H value.

InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3 (external symmetry number = 1, spin multiplicity = 1)
 +
InChI=1/C2H5/c1-2/h1H2,2H3 (external symmetry number = 1, spin multiplicity = 2)
 <=> (TS: external symmetry number = 1, spin multiplicity = 2)
InChI=1/C4H9O/c1-4(2)3-5/h3-5H,1-2H3 (external symmetry number = 1, spin multiplicity = 2)
 +
InChI=1/C2H6/c1-2/h1-2H3 (external symmetry number = 6, spin multiplicity = 1)
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 514,
    label = "InChI=1/C2H6/c1-2/h1-2H3;InChI=1/C4H9O/c1-4(2)3-5/h4H,3H2,1-2H3",
    group1 = 
"""
1 *1 C 0 {2,S} {3,S} {4,S} {5,S}
2    C 0 {1,S} {6,S} {7,S} {8,S}
3 *2 H 0 {1,S}
4    H 0 {1,S}
5    H 0 {1,S}
6    H 0 {2,S}
7    H 0 {2,S}
8    H 0 {2,S}
""",
    group2 = 
"""
1     C 0 {2,S} {6,S} {7,S} {8,S}
2     C 0 {1,S} {3,S} {5,S} {9,S}
3     C 0 {2,S} {4,S} {10,S} {11,S}
4  *3 O 1 {3,S}
5     C 0 {2,S} {12,S} {13,S} {14,S}
6     H 0 {1,S}
7     H 0 {1,S}
8     H 0 {1,S}
9     H 0 {2,S}
10    H 0 {3,S}
11    H 0 {3,S}
12    H 0 {5,S}
13    H 0 {5,S}
14    H 0 {5,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00507, 'cm^3/(mol*s)'),
        n = 4.52,
        alpha = 0,
        E0 = (2.34, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""MRH CBS-QB3 calculations w/o HR corrections""",
    longDesc = 
u"""
MRH CBS-QB3 calculations w/RRHO [MRHCBSQB3RRHO]_.  Pre-exponential was divided by 6 to get per-H value.

InChI=1/C2H6/c1-2/h1-2H3 (external symmetry number = 6, spin multiplicity = 1)
 +
InChI=1/C4H9O/c1-4(2)3-5/h4H,3H2,1-2H3 (external symmetry number = 1, spin multiplicity = 2)
 <=> (TS: external symmetry number = 1, spin multiplicity = 2)
InChI=1/C2H5/c1-2/h1H2,2H3 (external symmetry number = 1, spin multiplicity = 2)
 +
InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3 (external symmetry number = 1, spin multiplicity = 1)
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 515,
    label = "InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3/beta;InChI=1/C2H3/c1-2/h1H,2H2",
    group1 = 
"""
1     C 0 {2,S} {6,S} {7,S} {8,S}
2  *1 C 0 {1,S} {3,S} {5,S} {9,S}
3     C 0 {2,S} {4,S} {10,S} {11,S}
4     O 0 {3,S} {12,S}
5     C 0 {2,S} {13,S} {14,S} {15,S}
6     H 0 {1,S}
7     H 0 {1,S}
8     H 0 {1,S}
9  *2 H 0 {2,S}
10    H 0 {3,S}
11    H 0 {3,S}
12    H 0 {4,S}
13    H 0 {5,S}
14    H 0 {5,S}
15    H 0 {5,S}
""",
    group2 = 
"""
1 *3 C 1 {2,D} {3,S}
2    C 0 {1,D} {4,S} {5,S}
3    H 0 {1,S}
4    H 0 {2,S}
5    H 0 {2,S}
""",
    kinetics = ArrheniusEP(
        A = (5.49, 'cm^3/(mol*s)'),
        n = 3.33,
        alpha = 0,
        E0 = (0.63, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""MRH CBS-QB3 calculations w/o HR corrections""",
    longDesc = 
u"""
MRH CBS-QB3 calculations w/RRHO [MRHCBSQB3RRHO]_.

InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3 (external symmetry number = 1, spin multiplicity = 1)
 +
InChI=1/C2H3/c1-2/h1H,2H2 (external symmetry number = 1, spin multiplicity = 2)
 <=> (TS: external symmetry number = 1, spin multiplicity = 2)
InChI=1/C4H9O/c1-4(2)3-5/h5H,3H2,1-2H3 (external symmetry number = 1, spin multiplicity = 2)
 +
InChI=1/C2H4/c1-2/h1-2H2 (external symmetry number = 4, spin multiplicity = 1)

Tsang [Tsang1990]_ recommends k(T) = 9.04e-01 * (T/K)^3.46 * exp(-2.60 kcal/mol /RT) cm3 mol-1 s-1
for the reaction iso-C4H10 + C2H3 = C2H4 + tert-C4H9.  The new rate coefficient is faster by 4-10x
over the valid temperature range.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 516,
    label = "InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3/gamma;InChI=1/C3H5/c1-3-2/h1H2,2H3",
    group1 = 
"""
1  *1 C 0 {2,S} {6,S} {7,S} {8,S}
2     C 0 {1,S} {3,S} {5,S} {9,S}
3     C 0 {2,S} {4,S} {10,S} {11,S}
4     O 0 {3,S} {12,S}
5     C 0 {2,S} {13,S} {14,S} {15,S}
6  *2 H 0 {1,S}
7     H 0 {1,S}
8     H 0 {1,S}
9     H 0 {2,S}
10    H 0 {3,S}
11    H 0 {3,S}
12    H 0 {4,S}
13    H 0 {5,S}
14    H 0 {5,S}
15    H 0 {5,S}
""",
    group2 = 
"""
1    C 0 {2,D} {4,S} {5,S}
2 *3 C 1 {1,D} {3,S}
3    C 0 {2,S} {6,S} {7,S} {8,S}
4    H 0 {1,S}
5    H 0 {1,S}
6    H 0 {3,S}
7    H 0 {3,S}
8    H 0 {3,S}
""",
    kinetics = ArrheniusEP(
        A = (3.11e-05, 'cm^3/(mol*s)'),
        n = 4.87,
        alpha = 0,
        E0 = (3.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""MRH CBS-QB3 calculations w/o HR corrections""",
    longDesc = 
u"""
MRH CBS-QB3 calculations w/RRHO [MRHCBSQB3RRHO]_.  Pre-exponential was divided by 6 to get per-H value.

InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3 (external symmetry number = 1, spin multiplicity = 1)
 +
InChI=1/C3H5/c1-3-2/h1H2,2H3 (external symmetry number = 1, spin multiplicity = 2)
 <=> (TS: external symmetry number = 1, spin multiplicity = 2)
InChI=1/C4H9O/c1-4(2)3-5/h4-5H,1,3H2,2H3 (external symmetry number = 1, spin multiplicity = 2)
 +
InChI=1/C3H6/c1-3-2/h3H,1H2,2H3 (external symmetry number = 1, spin multiplicity = 1)
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 517,
    label = "InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3/alpha;InChI=1/C3H5/c1-3-2/h1H2,2H3",
    group1 = 
"""
1     C 0 {2,S} {6,S} {7,S} {8,S}
2     C 0 {1,S} {3,S} {5,S} {9,S}
3  *1 C 0 {2,S} {4,S} {10,S} {11,S}
4     O 0 {3,S} {12,S}
5     C 0 {2,S} {13,S} {14,S} {15,S}
6     H 0 {1,S}
7     H 0 {1,S}
8     H 0 {1,S}
9     H 0 {2,S}
10 *2 H 0 {3,S}
11    H 0 {3,S}
12    H 0 {4,S}
13    H 0 {5,S}
14    H 0 {5,S}
15    H 0 {5,S}
""",
    group2 = 
"""
1    C 0 {2,D} {4,S} {5,S}
2 *3 C 1 {1,D} {3,S}
3    C 0 {2,S} {6,S} {7,S} {8,S}
4    H 0 {1,S}
5    H 0 {1,S}
6    H 0 {3,S}
7    H 0 {3,S}
8    H 0 {3,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0128, 'cm^3/(mol*s)'),
        n = 4.09,
        alpha = 0,
        E0 = (1.31, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""MRH CBS-QB3 calculations w/o HR corrections""",
    longDesc = 
u"""
MRH CBS-QB3 calculations w/RRHO [MRHCBSQB3RRHO]_.  Pre-exponential was divided by 2 to get per-H value.

InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3 (external symmetry number = 1, spin multiplicity = 1)
 +
InChI=1/C3H5/c1-3-2/h1H2,2H3 (external symmetry number = 1, spin multiplicity = 2)
 <=> (TS: external symmetry number = 1, spin multiplicity = 2)
InChI=1/C4H9O/c1-4(2)3-5/h3-5H,1-2H3 (external symmetry number = 1, spin multiplicity = 2)
 +
InChI=1/C3H6/c1-3-2/h3H,1H2,2H3 (external symmetry number = 1, spin multiplicity = 1)
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 518,
    label = "InChI=1/C3H6O/c1-2-3-4/h3H,2H2,1H3/beta;InChI=1/C4H9O/c1-4(2)3-5/h4-5H,1,3H2,2H3",
    group1 = 
"""
1     C 0 {2,S} {5,S} {6,S} {7,S}
2  *1 C 0 {1,S} {3,S} {8,S} {9,S}
3     C 0 {2,S} {4,D} {10,S}
4     O 0 {3,D}
5     H 0 {1,S}
6     H 0 {1,S}
7     H 0 {1,S}
8  *2 H 0 {2,S}
9     H 0 {2,S}
10    H 0 {3,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {6,S} {7,S}
2     C 0 {1,S} {3,S} {5,S} {8,S}
3     C 0 {2,S} {4,S} {9,S} {10,S}
4     O 0 {3,S} {11,S}
5     C 0 {2,S} {12,S} {13,S} {14,S}
6     H 0 {1,S}
7     H 0 {1,S}
8     H 0 {2,S}
9     H 0 {3,S}
10    H 0 {3,S}
11    H 0 {4,S}
12    H 0 {5,S}
13    H 0 {5,S}
14    H 0 {5,S}
""",
    kinetics = ArrheniusEP(
        A = (0.000156, 'cm^3/(mol*s)'),
        n = 4.31,
        alpha = 0,
        E0 = (3.39, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""MRH CBS-QB3 calculations w/o HR corrections""",
    longDesc = 
u"""
MRH CBS-QB3 calculations w/RRHO [MRHCBSQB3RRHO]_.  Pre-exponential was divided by 2 to get per-H value.

InChI=1/C3H6O/c1-2-3-4/h3H,2H2,1H3 (external symmetry number = 1, spin multiplicity = 1)
 +
InChI=1/C4H9O/c1-4(2)3-5/h4-5H,1,3H2,2H3 (external symmetry number = 1, spin multiplicity = 2)
 <=> (TS: external symmetry number = 1, spin multiplicity = 2)
InChI=1/C3H5O/c1-2-3-4/h2-3H,1H3 (external symmetry number = 1, spin multiplicity = 2)
 +
InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3 (external symmetry number = 1, spin multiplicity = 1)
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 519,
    label = "InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3/beta;InChI=1/C3H5O/c1-2-3-4/h2-3H,1H3/c",
    group1 = 
"""
1     C 0 {2,S} {6,S} {7,S} {8,S}
2  *1 C 0 {1,S} {3,S} {5,S} {9,S}
3     C 0 {2,S} {4,S} {10,S} {11,S}
4     O 0 {3,S} {12,S}
5     C 0 {2,S} {13,S} {14,S} {15,S}
6     H 0 {1,S}
7     H 0 {1,S}
8     H 0 {1,S}
9  *2 H 0 {2,S}
10    H 0 {3,S}
11    H 0 {3,S}
12    H 0 {4,S}
13    H 0 {5,S}
14    H 0 {5,S}
15    H 0 {5,S}
""",
    group2 = 
"""
1    C 0 {2,S} {5,S} {6,S} {7,S}
2 *3 C 1 {1,S} {3,S} {8,S}
3    C 0 {2,S} {4,D} {9,S}
4    O 0 {3,D}
5    H 0 {1,S}
6    H 0 {1,S}
7    H 0 {1,S}
8    H 0 {2,S}
9    H 0 {3,S}
""",
    kinetics = ArrheniusEP(
        A = (0.000485, 'cm^3/(mol*s)'),
        n = 4.37,
        alpha = 0,
        E0 = (9.66, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""MRH CBS-QB3 calculations w/o HR corrections""",
    longDesc = 
u"""
MRH CBS-QB3 calculations w/RRHO [MRHCBSQB3RRHO]_.

InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3 (external symmetry number = 1, spin multiplicity = 1)
 +
InChI=1/C3H5O/c1-2-3-4/h2-3H,1H3 (external symmetry number = 1, spin multiplicity = 2)
 <=> (TS: external symmetry number = 1, spin multiplicity = 2)
InChI=1/C4H9O/c1-4(2)3-5/h5H,3H2,1-2H3 (external symmetry number = 1, spin multiplicity = 2)
 +
InChI=1/C3H6O/c1-2-3-4/h3H,2H2,1H3 (external symmetry number = 1, spin multiplicity = 1)
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 520,
    label = "C/H2/CbCs;C_rad/H2/S",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Cb 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    S 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00184, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (10.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 520,
    label = "InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3/alpha;InChI=1/C3H5O/c1-2-3-4/h2-3H,1H3/c",
    group1 = 
"""
1     C 0 {2,S} {6,S} {7,S} {8,S}
2     C 0 {1,S} {3,S} {5,S} {9,S}
3  *1 C 0 {2,S} {4,S} {10,S} {11,S}
4     O 0 {3,S} {12,S}
5     C 0 {2,S} {13,S} {14,S} {15,S}
6     H 0 {1,S}
7     H 0 {1,S}
8     H 0 {1,S}
9     H 0 {2,S}
10 *2 H 0 {3,S}
11    H 0 {3,S}
12    H 0 {4,S}
13    H 0 {5,S}
14    H 0 {5,S}
15    H 0 {5,S}
""",
    group2 = 
"""
1    C 0 {2,S} {5,S} {6,S} {7,S}
2 *3 C 1 {1,S} {3,S} {8,S}
3    C 0 {2,S} {4,D} {9,S}
4    O 0 {3,D}
5    H 0 {1,S}
6    H 0 {1,S}
7    H 0 {1,S}
8    H 0 {2,S}
9    H 0 {3,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00184, 'cm^3/(mol*s)'),
        n = 4.02,
        alpha = 0,
        E0 = (7.92, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""MRH CBS-QB3 calculations w/o HR corrections""",
    longDesc = 
u"""
MRH CBS-QB3 calculations w/RRHO [MRHCBSQB3RRHO]_.  Pre-exponential was divided by 2 to get per-H value.

InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3 (external symmetry number = 1, spin multiplicity = 1)
 +
InChI=1/C3H5O/c1-2-3-4/h2-3H,1H3 (external symmetry number = 1, spin multiplicity = 2)
 <=> (TS: external symmetry number = 1, spin multiplicity = 2)
InChI=1/C4H9O/c1-4(2)3-5/h3-5H,1-2H3 (external symmetry number = 1, spin multiplicity = 2)
 +
InChI=1/C3H6O/c1-2-3-4/h3H,2H2,1H3 (external symmetry number = 1, spin multiplicity = 1)
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 521,
    label = "C/H2/CbCs;C_rad/H/CsS",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Cb 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00329, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (10.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 521,
    label = "InChI=1/C4H8O/c1-4(2)3-5/h3-4H,1-2H3;H_rad",
    group1 = 
"""
1     C 0 {2,S} {6,S} {7,S} {8,S}
2  *1 C 0 {1,S} {3,S} {5,S} {9,S}
3     C 0 {2,S} {4,D} {10,S}
4     O 0 {3,D}
5     C 0 {2,S} {11,S} {12,S} {13,S}
6     H 0 {1,S}
7     H 0 {1,S}
8     H 0 {1,S}
9  *2 H 0 {2,S}
10    H 0 {3,S}
11    H 0 {5,S}
12    H 0 {5,S}
13    H 0 {5,S}
""",
    group2 = 
"""
1 *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (20800000.0, 'cm^3/(mol*s)'),
        n = 1.84,
        alpha = 0,
        E0 = (3.03, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""MRH CBS-QB3 calculations w/o HR corrections""",
    longDesc = 
u"""
MRH CBS-QB3 calculations w/RRHO [MRHCBSQB3RRHO]_.

InChI=1/C4H8O/c1-4(2)3-5/h3-4H,1-2H3 (external symmetry number = 1, spin multiplicity = 1)
 +
InChI=1/H (external symmetry number = 1, spin multiplicity = 2)
 <=> (TS: external symmetry number = 1, spin multiplicity = 2)
InChI=1/C4H7O/c1-4(2)3-5/h3H,1-2H3 (external symmetry number = 1, spin multiplicity = 2)
 +
InChI=1/H2/h1H (external symmetry number = 2, spin multiplicity = 1)
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 522,
    label = "C/H2/CbCs;C_rad/Cs2S",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Cb 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    S  0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00133, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (10, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""
MRH CBS-QB3 calculations w/RRHO [MRHCBSQB3RRHO]_.  Pre-exponential was divided by 6 to get per-H value.

InChI=1/C4H8/c1-4(2)3/h1H2,2-3H3 (external symmetry number = 2, spin multiplicity = 1)
 +
InChI=1/C3H5O/c1-2-3-4/h2-3H,1H3 (external symmetry number = 1, spin multiplicity = 2)
 <=> (TS: external symmetry number = 1, spin multiplicity = 2)
InChI=1/C4H7/c1-4(2)3/h1-2H2,3H3 (external symmetry number = 1, spin multiplicity = 2)
 +
InChI=1/C3H6O/c1-2-3-4/h2-4H,1H3/ (external symmetry number = 1, spin multiplicity = 1)
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 522,
    label = "InChI=1/C4H8/c1-4(2)3/h1H2,2-3H3;InChI=1/C3H5O/c1-2-3-4/h2-3H,1H3/o",
    group1 = 
"""
1     C 0 {2,D} {5,S} {6,S}
2     C 0 {1,D} {3,S} {4,S}
3  *1 C 0 {2,S} {7,S} {8,S} {9,S}
4     C 0 {2,S} {10,S} {11,S} {12,S}
5     H 0 {1,S}
6     H 0 {1,S}
7  *2 H 0 {3,S}
8     H 0 {3,S}
9     H 0 {3,S}
10    H 0 {4,S}
11    H 0 {4,S}
12    H 0 {4,S}
""",
    group2 = 
"""
1    C 0 {2,S} {5,S} {6,S} {7,S}
2    C 0 {1,S} {3,D} {8,S}
3    C 0 {2,D} {4,S} {9,S}
4 *3 O 1 {3,S}
5    H 0 {1,S}
6    H 0 {1,S}
7    H 0 {1,S}
8    H 0 {2,S}
9    H 0 {3,S}
""",
    kinetics = ArrheniusEP(
        A = (7.52e-08, 'cm^3/(mol*s)'),
        n = 5.77,
        alpha = 0,
        E0 = (12.04, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""MRH CBS-QB3 calculations w/o HR corrections""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 523,
    label = "C/H2/CbCs;Cd_rad/NonDeS",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Cb 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,D} {3,S}
2    C 0 {1,D}
3    S 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.011, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (2.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""
ROH + .OO. --> HOO. + RO.

This rate coefficient is an estimate from W.H. Green (personal communication).  The pre-exponential factor has been
 divided by 2 (from 1e11 to 5e10), to account for the symmetry of .OO.  The temperature range is estimated as 300-2000 K
 and the rank is assigned 1, so that this rate coefficient estimate will be used in all instances.
This is simply an estimate; JDM and/or MRH will refine this value in the near future.
See also rate 532 for X_H + .OO. --> HOO. + X.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 523,
    label = "O/H/NonDeC;O2b",
    group1 = 
"""
1 *1 O  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 O 1 {2,S}
2    O 1 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (50000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 1,
        E0 = (0, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 1,
    shortDesc = u"""Estimate [W.H. Green]""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 524,
    label = "C/H2/CbCs;C_rad/H/CdS",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Cb 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cd 0 {1,S}
4    S  0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0182, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (21.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 524,
    label = "C/H3/Cd;O_rad/NonDeO",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    Cd 0 {1,S}
""",
    group2 = 
"""
1 *3 O 1 {2,S}
2    O 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00057833, 'cm^3/(mol*s)'),
        n = 4.65,
        alpha = 0,
        E0 = (9.78, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""SSM due to lack of better value ref rate rule 525""",
    longDesc = 
u"""
This rate rules matches C=C-CH3 + HO-O* <=> C=C-CH2* + H2O2

Due to lack of better estimate SSM has given this node the value obtained from 2-Butene + HO2 calculations (Rate rule 525)
The rate was calculated using CBS-QB3 w/o hindered rotors and is valid in a range of temperature from 300 -2000 K.
The Wigner tunneling currection that was used to account for tunneling.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 525,
    label = "C/H2/CbCs;C_rad/CdCsS",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Cb 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cd 0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00229, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (21.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""
SSM CBS-QB3 calculations w/RRHO .  Pre-exponential was divided by 6 to get per-H value.

InChI=1/C4H8/c1-3-4-2/h3-4H,1-2H3/b4-3+ (external symmetry number = 2, spin multiplicity = 1)
 +
HO2 (external symmetry number = 1, spin multiplicity = 2)
 <=> (TS: external symmetry number = 1, spin multiplicity = 2)
InChI=1/C4H7/c1-3-4-2/h3-4H,1H2,2H3  (external symmetry number = 1, spin multiplicity = 2)
 +
H2O2 (external symmetry number = 2, spin multiplicity = 1)
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 525,
    label = "InChI=1/C4H8/c1-3-4-2/h3-4H,1-2H3/b4-3+;O_rad/NonDeO",
    group1 = 
"""
1  *1 C 0 {2,S} {5,S} {6,S} {7,S}
2     C 0 {1,S} {3,D} {8,S}
3     C 0 {2,D} {4,S} {9,S}
4     C 0 {3,S} {10,S} {11,S} {12,S}
5     H 0 {1,S}
6     H 0 {1,S}
7  *2 H 0 {1,S}
8     H 0 {2,S}
9     H 0 {3,S}
10    H 0 {4,S}
11    H 0 {4,S}
12    H 0 {4,S}
""",
    group2 = 
"""
1 *3 O 1 {2,S}
2    O 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00057833, 'cm^3/(mol*s)'),
        n = 4.65,
        alpha = 0,
        E0 = (9.78, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""SSM CBS-QB3 calculations w/o HR corrections""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 526,
    label = "C/H2/CbCs;C_rad/H/CtS",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Cb 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Ct 0 {1,S}
4    S  0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0108, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (19.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""
This rate rules matches C=C*-C + H2O2 <=> C=C-C + HO-O*

Due to lack of better estimate SSM has given this node the value obtained from 2-Butene + HO2 calculations (Rate rule 527)
The rate was calculated using CBS-QB3 w/o hindered rotors and is valid in a range of temperature from 300 -2000 K.
The Wigner tunneling currection that was used to account for tunneling.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 526,
    label = "H2O2;Cd_rad/NonDeC",
    group1 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 0 {1,S} {4,S}
3 *2 H 0 {1,S}
4    H 0 {2,S}
""",
    group2 = 
"""
1 *3 C  1 {2,D} {3,S}
2    C  0 {1,D}
3    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.4375, 'cm^3/(mol*s)'),
        n = 3.59,
        alpha = 0,
        E0 = (-4.03, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""SSM due to lack of better value ref rate rule 527""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 527,
    label = "C/H2/CbCs;C_rad/CtCsS",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Cb 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Ct 0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0441, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (20.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 527,
    label = "H2O2;InChI=1/C4H7/c1-3-4-2/h3H,1-2H3",
    group1 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 0 {1,S} {4,S}
3 *2 H 0 {1,S}
4    H 0 {2,S}
""",
    group2 = 
"""
1     C 0 {2,S} {5,S} {6,S} {7,S}
2  *3 C 1 {1,S} {3,D}
3     C 0 {2,D} {4,S} {8,S}
4     C 0 {3,S} {9,S} {10,S} {11,S}
5     H 0 {1,S}
6     H 0 {1,S}
7     H 0 {1,S}
8     H 0 {3,S}
9     H 0 {4,S}
10    H 0 {4,S}
11    H 0 {4,S}
""",
    kinetics = ArrheniusEP(
        A = (0.4375, 'cm^3/(mol*s)'),
        n = 3.59,
        alpha = 0,
        E0 = (-4.03, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""SSM CBS-QB3 calculations w/o HR corrections""",
    longDesc = 
u"""
SSM CBS-QB3 calculations w/RRHO .  Pre-exponential was divided by 2 to account for summetry of H2O2
The rate rule is valid in a range of temperature from 300 -2000 K.
The Wigner tunneling currection that was used to account for tunneling.

InChI=1/C4H7/c1-3-4-2/h3H,1-2H3 (external symmetry number = 1, spin multiplicity = 2)
 +
H2O2 (external symmetry number = 2, spin multiplicity = 1)
 <=> (TS: external symmetry number = 1, spin multiplicity = 2)
InChI=1/C4H8/c1-3-4-2/h3-4H,1-2H3/b4-3+  (external symmetry number = 2, spin multiplicity = 1)
 +
HO2 (external symmetry number = 1, spin multiplicity = 2)
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 528,
    label = "C/H2/OneDeC;O_rad/NonDeO",
    group1 = 
"""
1 *1 C                0 {2,S} {3,S} {4,S} {5,S}
2 *2 H                0 {1,S}
3    H                0 {1,S}
4    {Cd,Ct,CO,Cb,CS} 0 {1,S}
5    Cs               0 {1,S}
""",
    group2 = 
"""
1 *3 O 1 {2,S}
2    O 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.000254, 'cm^3/(mol*s)'),
        n = 4.59,
        alpha = 0,
        E0 = (7.16, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""SSM due to lack of better value ref rate rule 529""",
    longDesc = 
u"""
This rate rules matches Cs-CH2-C=C + HO-O* <=> Cs-CH*-C=C + H2O2

Due to lack of better estimate SSM has given this node the value obtained from 1-Butene + HO2 calculations (Rate rule 529)
The rate was calculated using CBS-QB3 w/o hindered rotors and is valid in a range of temperature from 300 -2000 K.
The Wigner tunneling currection that was used to account for tunneling.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 529,
    label = "InChI=1/C4H8/c1-3-4-2/h3H,1,4H2,2H3;O_rad/NonDeO",
    group1 = 
"""
1     C 0 {2,S} {5,S} {6,S} {7,S}
2  *1 C 0 {1,S} {3,S} {8,S} {9,S}
3     C 0 {2,S} {4,D} {10,S}
4     C 0 {3,D} {11,S} {12,S}
5     H 0 {1,S}
6     H 0 {1,S}
7     H 0 {1,S}
8  *2 H 0 {2,S}
9     H 0 {2,S}
10    H 0 {3,S}
11    H 0 {4,S}
12    H 0 {4,S}
""",
    group2 = 
"""
1 *3 O 1 {2,S}
2    O 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.000254, 'cm^3/(mol*s)'),
        n = 4.59,
        alpha = 0,
        E0 = (7.16, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""SSM CBS-QB3 calculations w/o HR corrections""",
    longDesc = 
u"""
SSM CBS-QB3 calculations w/RRHO .  Pre-exponential was divided by 2 to get per-H value.
The rate rule is valid in a range of temperature from 300 -2000 K.
The Wigner tunneling currection that was used to account for tunneling.

InChI=1/C4H8/c1-3-4-2/h3H,1,4H2,2H3 (external symmetry number = 1, spin multiplicity = 1)
 +
HO2 (external symmetry number = 1, spin multiplicity = 2)
 <=> (TS: external symmetry number = 1, spin multiplicity = 2)
InChI=1/C4H7/c1-3-4-2/h3-4H,1H2,2H3   (external symmetry number = 1, spin multiplicity = 2)
 +
H2O2 (external symmetry number = 2, spin multiplicity = 1)
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 530,
    label = "H2O2;Cd_pri_rad",
    group1 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 0 {1,S} {4,S}
3 *2 H 0 {1,S}
4    H 0 {2,S}
""",
    group2 = 
"""
1 *3 C 1 {2,D} {3,S}
2    C 0 {1,D}
3    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1, 'cm^3/(mol*s)'),
        n = 3.52,
        alpha = 0,
        E0 = (-7.48, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""SSM due to lack of better value ref rate rule 531""",
    longDesc = 
u"""
This rate rules matches C-HC=CH* + H2O2 <=> C-HC=CH2 + HO=O*

Due to lack of better estimate SSM has given this node the value obtained from 1-Butene + HO2 calculations (Rate rule 531)
The rate was calculated using CBS-QB3 w/o hindered rotors and is valid in a range of temperature from 300 -2000 K.
The Wigner tunneling currection that was used to account for tunneling.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 531,
    label = "H2O2;InChI=1/C4H7/c1-3-4-2/h1,3H,4H2,2H3",
    group1 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 0 {1,S} {4,S}
3 *2 H 0 {1,S}
4    H 0 {2,S}
""",
    group2 = 
"""
1     C 0 {2,S} {5,S} {6,S} {7,S}
2     C 0 {1,S} {3,S} {8,S} {9,S}
3     C 0 {2,S} {4,D} {10,S}
4  *3 C 1 {3,D} {11,S}
5     H 0 {1,S}
6     H 0 {1,S}
7     H 0 {1,S}
8     H 0 {2,S}
9     H 0 {2,S}
10    H 0 {3,S}
11    H 0 {4,S}
""",
    kinetics = ArrheniusEP(
        A = (1, 'cm^3/(mol*s)'),
        n = 3.52,
        alpha = 0,
        E0 = (-7.48, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""SSM CBS-QB3 calculations w/o HR corrections""",
    longDesc = 
u"""
SSM CBS-QB3 calculations w/RRHO .  Pre-exponential was divided by 2 to account for summetry of H2O2
The rate rule is valid in a range of temperature from 300 -2000 K.
The Wigner tunneling currection that was used to account for tunneling.

InChI=1/C4H7/c1-3-4-2/h1,3H,4H2,2H3  (external symmetry number = 1, spin multiplicity = 2)
 +
H2O2 (external symmetry number = 2, spin multiplicity = 1)
 <=> (TS: external symmetry number = 1, spin multiplicity = 2)
InChI=1/C4H8/c1-3-4-2/h3H,1,4H2,2H3  (external symmetry number = 1, spin multiplicity = 1)
 +
HO2 (external symmetry number = 1, spin multiplicity = 2)
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 532,
    label = "X_H;O2b",
    group1 = 
"""
1 *1 R 0 {2,S}
2 *2 H 0 {1,S}
""",
    group2 = 
"""
1 *3 O 1 {2,S}
2    O 1 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (50000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 1,
        E0 = (0, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 1,
    shortDesc = u"""Estimate [W.H. Green]""",
    longDesc = 
u"""
X_H + .OO. --> HOO. + X.

I have taken the estimated rate from 523, which assumes A=1e11 with Ea=enthothermicity,
and assigned it to the top level X_H node so that whenever .OO. is abstracting from 
something without a proper rate, this value is used instead of the lengthy average.
See notes to 523 for further details.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 533,
    label = "C_methane;C2b",
    group1 = 
"""
1 *1 C 0 {2,S} {3,S} {4,S} {5,S}
2 *2 H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
5    H 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,T}
2    C 1 {1,T}
""",
    kinetics = ArrheniusEP(
        A = (7500000000000.0, 'cm^3/(mol*s)', '+|-', 1600000000000.0),
        n = 0,
        alpha = 0,
        E0 = (1.05, 'kcal/mol', '+|-', 0.12),
        Tmin = (294, 'K'),
        Tmax = (376, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Matsugi et al 10.1021/jp1012494""",
    longDesc = 
u"""
For CH4 + C2 = CH3 + C2H

J. Phys. Chem. A 2010, 114, 4580-4585
http://dx.doi.org/10.1021/jp1012494

Rate Constants and Kinetic Isotope Effects on the Reaction of C2($X^1\Sigma_g^+$) with CH4 and CD4.
Akira Matsugi, Kohsuke Suma, and Akira Miyoshi

It was measured at pretty low temperatures (294-376), but also calculated ab initio. The calculated
rates are plotted but the expression is not reported.

    k = (10.0 +- 2.1)E-11 exp[-(4.4+-0.5 kJ mol)/RT] cm3 molecule-1 s-1
which gives 
    A = 6e13+-1.3e13 cm3/mole/s
    n = 0
    Ea = 1.05+-0.12  kcal/mol
The degeneracy of this reaction is 8 though, so per-site A is:
    A = 7.5e12+-1.6e12
    
(See also  doi:10.1063/1.3480395  for reactions of C2, but that may be the wrong electronic state.)
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 534,
    label = "H2O2;InChI=1/C4H7O/c1-2-3-4-5/h3-4H,2H2,1H3",
    group1 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 0 {1,S} {4,S}
3 *2 H 0 {1,S}
4    H 0 {2,S}
""",
    group2 = 
"""
1    C 0 {2,S}
2    C 0 {1,S} {3,S}
3    C 0 {2,S} {4,D}
4    C 0 {3,D} {5,S}
5 *3 O 1 {4,S}
""",
    kinetics = ArrheniusEP(
        A = (0.03495, 'cm^3/(mol*s)', '*|/', 3),
        n = 3.75,
        alpha = 0,
        E0 = (10.89, 'kcal/mol', '+|-', 2),
        Tmin = (600, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""MHS CBS-QB3 w/1dHR calculations""",
    longDesc = 
u"""
Exact reaction: HOOH + *O-CH=CH-C2H5 <=> HO-CH=CH-C2H5 + HOO*
Rxn family nodes: H2O2 + InChI=1/C4H7O/c1-2-3-4-5/h3-4H,2H2,1H3

MHS computed rate coefficient using CBS-QB3 method, see _[MRHCBSQB3RRHO] for general algorithm
employed.  Two differences::
	1) the k(T) was calculated from 600 to 2000 K, in 200 K increments.
	2) Low-frequency torsional modes were treated as 1-d separable hindered rotors.  The scans
		were performed at the B3LYP/6-31G(d) level.

MHS computed the fitted Arrhenius expression to be: k(T) = 6.99e-2 (T/1K)^3.75 exp(-10.89 kcal mol-1 / RT) cm3 mol-1 s-1.
The pre-exponential was divided by 2 to get the per-H event.  The uncertainty in the E0
was estimated to be 2 kcal mol-1 (general accuracy of CBS-QB3 calculations) and the uncertainty
in the A parameter was MRH guess.

RMG previously estimated the kinetics of the titled reaction to be ~10^3 times faster
than calculations of MHS.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 535,
    label = "H2O2;O_rad/OneDe",
    group1 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 0 {1,S} {4,S}
3 *2 H 0 {1,S}
4    H 0 {2,S}
""",
    group2 = 
"""
1 *3 O                1 {2,S}
2    {Cd,Ct,Cb,CO,CS} 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.03495, 'cm^3/(mol*s)', '*|/', 3),
        n = 3.75,
        alpha = 0,
        E0 = (10.89, 'kcal/mol', '+|-', 2),
        Tmin = (600, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""MHS CBS-QB3 w/1dHR calculations, see node 534.""",
    longDesc = 
u"""
Rxn family nodes: H2O2 + O_rad/OneDe

The rate coefficient for this node was taken from node 534 (H2O2 + InChI=1/C4H7O/c1-2-3-4-5/h3-4H,2H2,1H3)
by analogy: HOOH + *O-C=R.  Discussed with MRH.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 536,
    label = "H2O2;OOCH3",
    group1 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 0 {1,S} {4,S}
3 *2 H 0 {1,S}
4    H 0 {2,S}
""",
    group2 = 
"""
1 *3 O 1 {2,S}
2    O 0 {1,S} {3,S}
3    C 0 {2,S}
""",
    kinetics = ArrheniusEP(
        A = (0.092, 'cm^3/(mol*s)', '*|/', 3),
        n = 3.96,
        alpha = 0,
        E0 = (6.63, 'kcal/mol', '+|-', 2),
        Tmin = (600, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""MHS CBS-QB3 w/1dHR calculations""",
    longDesc = 
u"""
Exact reaction: HOOH + *O-O-CH3 <=> HO-O-CH3 + HOO*
Rxn family nodes: H2O2 + OOCH3

MHS computed rate coefficient using CBS-QB3 method, see _[MRHCBSQB3RRHO] for general algorithm
employed.  Two differences::
	1) the k(T) was calculated from 600 to 2000 K, in 200 K increments.
	2) Low-frequency torsional modes were treated as 1-d separable hindered rotors.  The scans
		were performed at the B3LYP/6-31G(d) level.

MHS computed the fitted Arrhenius expression to be: k(T) = 1.84e-1 (T/1K)^3.96 exp(-6.63 kcal mol-1 / RT) cm3 mol-1 s-1.
The pre-exponential was divided by 2 to get the per-H event.  The uncertainty in the E0
was estimated to be 2 kcal mol-1 (general accuracy of CBS-QB3 calculations) and the uncertainty
in the A parameter was MRH guess.

RMG previously estimated the kinetics of the titled reaction to be 1-3 orders of magnitude faster
than calculations of MHS.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 537,
    label = "H2O2;O_rad/NonDeO",
    group1 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 0 {1,S} {4,S}
3 *2 H 0 {1,S}
4    H 0 {2,S}
""",
    group2 = 
"""
1 *3 O 1 {2,S}
2    O 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.092, 'cm^3/(mol*s)', '*|/', 3),
        n = 3.96,
        alpha = 0,
        E0 = (6.63, 'kcal/mol', '+|-', 2),
        Tmin = (600, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""MHS CBS-QB3 w/1dHR calculations, see node 536.""",
    longDesc = 
u"""
Rxn family nodes: H2O2 + O_rad/NonDeO

The rate coefficient for this node was taken from node 536 (H2O2 + OOCH3)
by analogy: HOOH + *O-O-R.  Discussed with MRH.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 538,
    label = "InChI=1/C4H8/c1-3-4-2/h3H,1,4H2,2H3;OOCH3",
    group1 = 
"""
1     C 0 {2,S} {5,S} {6,S} {7,S}
2  *1 C 0 {1,S} {3,S} {8,S} {9,S}
3     C 0 {2,S} {4,D} {10,S}
4     C 0 {3,D} {11,S} {12,S}
5     H 0 {1,S}
6     H 0 {1,S}
7     H 0 {1,S}
8  *2 H 0 {2,S}
9     H 0 {2,S}
10    H 0 {3,S}
11    H 0 {4,S}
12    H 0 {4,S}
""",
    group2 = 
"""
1 *3 O 1 {2,S}
2    O 0 {1,S} {3,S}
3    C 0 {2,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00741, 'cm^3/(mol*s)', '*|/', 3),
        n = 4.313,
        alpha = 0,
        E0 = (8.016, 'kcal/mol', '+|-', 2),
        Tmin = (600, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""MRH CBS-QB3 calculations, w/1dHR corrections""",
    longDesc = 
u"""
MRH CBS-QB3 calculations w/1d hindered rotor corrections
Exact reaction: CH3CH2CH=CH2 + OOCH3 = HOOCH3 + CH3CHCH=CH2

This reaction was of interest to MRH/MHS because the butanol model was sensitive to its kinetics
(in particular, the C4H8-1 predicted concentration for 10-atm JSR simulations between 800-1000 K).
The original mechanism had an estimate that was much faster than these new calculations (the RMG old
k(T) was 50-100x faster than these calculations between 800-1000 K).

MRH computed these kinetics using the CBS-QB3 method.  Hindered rotor corrections were accounted for in all species:
	CH3CH2CH=CH2: -CH3 and -CH2CH3 rotor
	OOCH3: -CH3 rotor
	TS: -CH3 and -CH=CH2 rotor of react1, -CH3 and -OCH3 of react2, and -OOCH3 between react1 and react2
	HOOCH3: -CH3 and -OCH3 rotor
	CH3CHCH=CH2: -CH3 and -CH=CH2 rotor
External symmetry number of all speces was 1.  k(T) was computed from 600 - 2000 K, in 200 K intervals.  An
asymmetric Eckart tunneling correction was used.

The computed k(T) was 1.482e-02 * (T/1K)^4.313 * exp(-8.016 kcal/mol / RT) cm3 mol-1 s-1.
MRH divided the pre-exponential by 2 to account for the reaction path degeneracy.

NOTE: Running PopulateReactions before and after this number produced results that differed by less than a factor
of three.  New numbers in the RMG database thus lead to an improvement in the RMG estimate (RMG works!).  Also,
this computed rate coefficient is a factor of 10 faster than Tsang's recommendation for C3H6 + OOCH3 = HOOCH3 + allyl;
his stated uncertainty is a factor of ten.  However, one would expect abstraction from the secondary carbon of
1-butane to be faster than the primary carbon of propene, because the C-H bond strength should be weaker.  So,
this calculation is in reasonable agreement with the literature.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 539,
    label = "H2O2;InChI=1/C3H5/c1-3-2/h3H,1-2H2",
    group1 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 0 {1,S} {4,S}
3 *2 H 0 {1,S}
4    H 0 {2,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {4,S} {5,S}
2    C 0 {1,S} {3,D} {6,S}
3    C 0 {2,D}
4    H 0 {1,S}
5    H 0 {1,S}
6    H 0 {2,S}
""",
    kinetics = ArrheniusEP(
        A = (0.01755, 'cm^3/(mol*s)', '*|/', 3),
        n = 4.22,
        alpha = 0,
        E0 = (9.86, 'kcal/mol', '+|-', 2),
        Tmin = (600, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""MHS CBS-QB3 w/1dHR calculations""",
    longDesc = 
u"""
MHS CBS-QB3 calculations w/1d hindered rotor corrections
Exact reaction: *CH2-CH=CH2 + H2O2 = CH3-CH=CH2 + HO2

MHS computed rate coefficient using CBS-QB3 method, see _[MRHCBSQB3RRHO] for general algorithm
employed.  Two differences::
	1) the k(T) was calculated from 600 to 2000 K, in 200 K increments.
	2) Low-frequency torsional modes were treated as 1-d separable hindered rotors.  The scans
		were performed at the B3LYP/6-31G(d) level.

MHS computed the fitted Arrhenius expression to be: k(T) = 3.51e-2 (T/1K)^4.22 exp(-9.86 kcal mol-1 / RT) cm3 mol-1 s-1.
The pre-exponential was divided by 2 to get the per-H event.  The uncertainty in the E0
was estimated to be 2 kcal mol-1 (general accuracy of CBS-QB3 calculations) and the uncertainty
in the A parameter was MRH guess.

RMG previously estimated the kinetics of the titled reaction to be ~2 orders of magnitude faster
than calculations of MHS.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 540,
    label = "InChI=1/C4H8O/c1-2-3-4-5/h4H,2-3H2,1H3;O_rad/NonDeO",
    group1 = 
"""
1  *1 C 0 {2,D} {3,S} {6,S}
2     O 0 {1,D}
3     C 0 {1,S} {4,S} {7,S} {8,S}
4     C 0 {3,S} {5,S} {9,S} {10,S}
5     C 0 {4,S} {11,S} {12,S} {13,S}
6  *2 H 0 {1,S}
7     H 0 {3,S}
8     H 0 {3,S}
9     H 0 {4,S}
10    H 0 {4,S}
11    H 0 {5,S}
12    H 0 {5,S}
13    H 0 {5,S}
""",
    group2 = 
"""
1 *3 O 1 {2,S}
2    O 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.000191, 'cm^3/(mol*s)', '*|/', 3),
        n = 4.25,
        alpha = 0,
        E0 = (0.81, 'kcal/mol', '+|-', 2),
        Tmin = (600, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""MHS CBS-QB3 w/o 1dHR calculations""",
    longDesc = 
u"""
MHS CBS-QB3 calculations without 1d hindered rotor correction (due to presence of hydrogen bond interactions)
Exact reaction: HO2 + CH3-CH2-CH2-CH=O = H2O2 + CH3-CH2-CH2-C*=O

MHS computed rate coefficient using CBS-QB3 method, see _[MRHCBSQB3RRHO] for general algorithm
employed.  With the difference that the k(T) was calculated from 600 to 2000 K, in 200 K increments.

MHS computed the fitted Arrhenius expression to be: k(T) = 1.91e-4 (T/1K)^4.25 exp(-0.81 kcal mol-1 / RT) cm3 mol-1 s-1.
The uncertainty in the E0 was estimated to be 2 kcal mol-1 (general accuracy of CBS-QB3 calculations) and the uncertainty
in the A parameter was MRH guess.
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 541,
    label = "C/H3/Cb;O_pri_rad",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    Cb 0 {1,S}
""",
    group2 = 
"""
1 *3 O 1 {2,S}
2    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (4200000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (2.59, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (1000, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 1,
    shortDesc = u"""Tully et al. experimental data (changed to per H)""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 542,
    label = "C/H2/Cb;O_pri_rad",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    C  0 {1,S}
5    Cb 0 {1,S}
""",
    group2 = 
"""
1 *3 O 1 {2,S}
2    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (4200000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (2.59, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (1000, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 1,
    shortDesc = u"""Tully et al. experimental data (changed to per H)""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 543,
    label = "C/H/Cb;O_pri_rad",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    C  0 {1,S}
4    C  0 {1,S}
5    Cb 0 {1,S}
""",
    group2 = 
"""
1 *3 O 1 {2,S}
2    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (4200000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (2.59, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (1000, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 1,
    shortDesc = u"""Tully et al. experimental data (changed to per H)""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 544,
    label = "C/H3/Cb;O_rad/NonDeO",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    Cb 0 {1,S}
""",
    group2 = 
"""
1 *3 O 1 {2,S}
2    O 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (132000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (14.08, 'kcal/mol'),
        Tmin = (600, 'K'),
        Tmax = (1000, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 1,
    shortDesc = u"""Baulch et al. literature review (value for HO2 + toluene) (changed to per H)""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 545,
    label = "C/H2/Cb;O_rad/NonDeO",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    C  0 {1,S}
5    Cb 0 {1,S}
""",
    group2 = 
"""
1 *3 O 1 {2,S}
2    O 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (133000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (11.3, 'kcal/mol'),
        Tmin = (600, 'K'),
        Tmax = (1000, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 1,
    shortDesc = u"""Baulch et al. literature review (value for HO2 + ethylbenzene) (changed to per H)""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 546,
    label = "C/H/Cb;O_rad/NonDeO",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    C  0 {1,S}
4    C  0 {1,S}
5    Cb 0 {1,S}
""",
    group2 = 
"""
1 *3 O 1 {2,S}
2    O 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (133000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (11.3, 'kcal/mol'),
        Tmin = (600, 'K'),
        Tmax = (1000, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 1,
    shortDesc = u"""Baulch et al. literature review (value for HO2 + ethylbenzene) (changed to per H)""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 547,
    label = "C/H3/Cb;O2b",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    Cb 0 {1,S}
""",
    group2 = 
"""
1 *3 O 1 {2,S}
2    O 1 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (600000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (39.71, 'kcal/mol'),
        Tmin = (700, 'K'),
        Tmax = (1200, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 1,
    shortDesc = u"""Baulch et al. literature review (value for HO2 + toluene entered here) (changed to per H)""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 548,
    label = "C/H2/Cb;O2b",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    C  0 {1,S}
5    Cb 0 {1,S}
""",
    group2 = 
"""
1 *3 O 1 {2,S}
2    O 1 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (600000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (39.71, 'kcal/mol'),
        Tmin = (700, 'K'),
        Tmax = (1200, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 1,
    shortDesc = u"""Baulch et al. literature review (value for HO2 + toluene entered here) (changed to per H)""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 549,
    label = "C/H/Cb;O2b",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    C  0 {1,S}
4    C  0 {1,S}
5    Cb 0 {1,S}
""",
    group2 = 
"""
1 *3 O 1 {2,S}
2    O 1 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (600000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (39.71, 'kcal/mol'),
        Tmin = (700, 'K'),
        Tmax = (1200, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 1,
    shortDesc = u"""Baulch et al. literature review (value for HO2 + toluene entered here) (changed to per H)""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 550,
    label = "ROOH_pri;C_rad/H/NonDeC",
    group1 = 
"""
1 *1 O  0 {2,S} {7,S}
2    O  0 {1,S} {3,S}
3    C  0 {2,S} {4,S} {5,S} {6,S}
4    Cs 0 {3,S}
5    H  0 {3,S}
6    H  0 {3,S}
7 *2 H  0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (2.51e-11, 'cm^3/(mol*s)'),
        n = 6.77,
        alpha = 0,
        E0 = (-8.6, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (1000, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 1,
    shortDesc = u"""[AJ]Assumed to be same as for ROOH_sec""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 551,
    label = "C/H/Cs2Cb;C_rad/H2/S",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Cb 0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    S 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00127, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (9.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 551,
    label = "ROOH_sec;C_rad/H/NonDeC",
    group1 = 
"""
1 *1 O  0 {2,S} {7,S}
2    O  0 {1,S} {3,S}
3    C  0 {2,S} {4,S} {5,S} {6,S}
4    Cs 0 {3,S}
5    Cs 0 {3,S}
6    H  0 {3,S}
7 *2 H  0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (2.51e-11, 'cm^3/(mol*s)'),
        n = 6.77,
        alpha = 0,
        E0 = (-8.6, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (1000, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 1,
    shortDesc = u"""[AJ]CBS-QB3 calculations with 1DHR corrections, reverse rates computed using DFT_QCI_thermo""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 552,
    label = "C/H/Cs2Cb;C_rad/H/CsS",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Cb 0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00228, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (9.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 552,
    label = "ROOH_pri;C_rad/H2/Cs",
    group1 = 
"""
1 *1 O  0 {2,S} {7,S}
2    O  0 {1,S} {3,S}
3    C  0 {2,S} {4,S} {5,S} {6,S}
4    Cs 0 {3,S}
5    H  0 {3,S}
6    H  0 {3,S}
7 *2 H  0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    H  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (2.51e-11, 'cm^3/(mol*s)'),
        n = 6.77,
        alpha = 0,
        E0 = (-8.6, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (1000, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 1,
    shortDesc = u"""[AJ]Assumed to be same as for C_rad/H/NonDeC""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 553,
    label = "C/H/Cs2Cb;C_rad/Cs2S",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Cb 0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    S  0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.000918, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (8.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 553,
    label = "ROOH_sec;C_rad/H2/Cs",
    group1 = 
"""
1 *1 O  0 {2,S} {7,S}
2    O  0 {1,S} {3,S}
3    C  0 {2,S} {4,S} {5,S} {6,S}
4    Cs 0 {3,S}
5    Cs 0 {3,S}
6    H  0 {3,S}
7 *2 H  0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    H  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (2.51e-11, 'cm^3/(mol*s)'),
        n = 6.77,
        alpha = 0,
        E0 = (-8.6, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (1000, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 1,
    shortDesc = u"""[AJ]Assumed to be same as for C_rad/H/NonDeC""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 554,
    label = "C/H/Cs2Cb;Cd_rad/NonDeS",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Cb 0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,D} {3,S}
2    C 0 {1,D}
3    S 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00762, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (1.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 554,
    label = "ROOH_pri;C_rad/OOH/Cs/Cs",
    group1 = 
"""
1 *1 O  0 {2,S} {7,S}
2    O  0 {1,S} {3,S}
3    C  0 {2,S} {4,S} {5,S} {6,S}
4    Cs 0 {3,S}
5    H  0 {3,S}
6    H  0 {3,S}
7 *2 H  0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    O  0 {1,S} {5,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
5    O  0 {2,S}
""",
    kinetics = ArrheniusEP(
        A = (5.066e-14, 'cm^3/(mol*s)'),
        n = 7.18,
        alpha = 0,
        E0 = (-5.27, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (1000, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 1,
    shortDesc = u"""[AJ] Assumed to be same as for ROOH_sec""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 555,
    label = "C/H/Cs2Cb;C_rad/H/CdS",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Cb 0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cd 0 {1,S}
4    S  0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0126, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (20.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 555,
    label = "ROOH_sec;C_rad/OOH/Cs/Cs",
    group1 = 
"""
1 *1 O  0 {2,S} {7,S}
2    O  0 {1,S} {3,S}
3    C  0 {2,S} {4,S} {5,S} {6,S}
4    Cs 0 {3,S}
5    Cs 0 {3,S}
6    H  0 {3,S}
7 *2 H  0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    O  0 {1,S} {5,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
5    O  0 {2,S}
""",
    kinetics = ArrheniusEP(
        A = (5.066e-14, 'cm^3/(mol*s)'),
        n = 7.18,
        alpha = 0,
        E0 = (-5.27, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (1000, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 1,
    shortDesc = u"""[AJ] CBS-QB3 calculations with 1DHR corrections""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 556,
    label = "C/H/Cs2Cb;C_rad/CdCsS",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Cb 0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cd 0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00159, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (20.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 556,
    label = "ROOH_pri;CO_rad/NonDe",
    group1 = 
"""
1 *1 O  0 {2,S} {7,S}
2    O  0 {1,S} {3,S}
3    C  0 {2,S} {4,S} {5,S} {6,S}
4    Cs 0 {3,S}
5    H  0 {3,S}
6    H  0 {3,S}
7 *2 H  0 {1,S}
""",
    group2 = 
"""
1 *3 C        1 {2,D} {3,S}
2    O        0 {1,D}
3    {Cs,O,S} 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0009569, 'cm^3/(mol*s)'),
        n = 4.45,
        alpha = 0,
        E0 = (0.54, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (1000, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 1,
    shortDesc = u"""[AJ] Assumed to be same as for ROOH_sec""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 557,
    label = "C/H/Cs2Cb;C_rad/H/CtS",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Cb 0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Ct 0 {1,S}
4    S  0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00748, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (18.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 557,
    label = "ROOH_sec;CO_rad/NonDe",
    group1 = 
"""
1 *1 O  0 {2,S} {7,S}
2    O  0 {1,S} {3,S}
3    C  0 {2,S} {4,S} {5,S} {6,S}
4    Cs 0 {3,S}
5    Cs 0 {3,S}
6    H  0 {3,S}
7 *2 H  0 {1,S}
""",
    group2 = 
"""
1 *3 C        1 {2,D} {3,S}
2    O        0 {1,D}
3    {Cs,O,S} 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0009569, 'cm^3/(mol*s)'),
        n = 4.45,
        alpha = 0,
        E0 = (0.54, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (1000, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 1,
    shortDesc = u"""[AJ] CBS-QB3 calculations with 1DHR corrections""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 558,
    label = "C/H/Cs2Cb;C_rad/CtCsS",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Cb 0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Ct 0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0306, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (19.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 558,
    label = "ROOH_pri;C_rad/H/CO/Cs",
    group1 = 
"""
1 *1 O  0 {2,S} {7,S}
2    O  0 {1,S} {3,S}
3    C  0 {2,S} {4,S} {5,S} {6,S}
4    Cs 0 {3,S}
5    H  0 {3,S}
6    H  0 {3,S}
7 *2 H  0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cs 0 {1,S}
4    CO 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.73e-10, 'cm^3/(mol*s)'),
        n = 6.3,
        alpha = 0,
        E0 = (-2.14, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (1000, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 1,
    shortDesc = u"""[AJ] Assumed to be same as for ROOH_sec""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 559,
    label = "ROOH_sec;C_rad/H/CO/Cs",
    group1 = 
"""
1 *1 O  0 {2,S} {7,S}
2    O  0 {1,S} {3,S}
3    C  0 {2,S} {4,S} {5,S} {6,S}
4    Cs 0 {3,S}
5    Cs 0 {3,S}
6    H  0 {3,S}
7 *2 H  0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cs 0 {1,S}
4    CO 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.73e-10, 'cm^3/(mol*s)'),
        n = 6.3,
        alpha = 0,
        E0 = (-2.14, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (1000, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 1,
    shortDesc = u"""[AJ] Assumed to be same as for C_rad/H2/CO""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 560,
    label = "ROOH_pri;C_rad/H2/CO",
    group1 = 
"""
1 *1 O  0 {2,S} {7,S}
2    O  0 {1,S} {3,S}
3    C  0 {2,S} {4,S} {5,S} {6,S}
4    Cs 0 {3,S}
5    H  0 {3,S}
6    H  0 {3,S}
7 *2 H  0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    H  0 {1,S}
4    CO 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.73e-10, 'cm^3/(mol*s)'),
        n = 6.3,
        alpha = 0,
        E0 = (-2.14, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (1000, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 1,
    shortDesc = u"""[AJ] Assumed to be same as for ROOH_sec""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 561,
    label = "ROOH_sec;C_rad/H2/CO",
    group1 = 
"""
1 *1 O  0 {2,S} {7,S}
2    O  0 {1,S} {3,S}
3    C  0 {2,S} {4,S} {5,S} {6,S}
4    Cs 0 {3,S}
5    Cs 0 {3,S}
6    H  0 {3,S}
7 *2 H  0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    H  0 {1,S}
4    CO 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.73e-10, 'cm^3/(mol*s)'),
        n = 6.3,
        alpha = 0,
        E0 = (-2.14, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (1000, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 1,
    shortDesc = u"""[AJ] CBS-QB3 calculations with 1DHR corrections""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 562,
    label = "CS/H/NonDeC;C_rad/H/CsS",
    group1 = 
"""
1 *1 C  0 {2,D} {3,S} {4,S}
2    S  0 {1,D}
3 *2 H  0 {1,S}
4    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (4.36e-10, 'cm^3/(mol*s)'),
        n = 4.56,
        alpha = 0,
        E0 = (4.77, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""CAC CBS-QB3 calc, 1dhr""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 563,
    label = "CS/H/NonDeC;C_rad/H2/Cs",
    group1 = 
"""
1 *1 C  0 {2,D} {3,S} {4,S}
2    S  0 {1,D}
3 *2 H  0 {1,S}
4    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    H  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.377, 'cm^3/(mol*s)'),
        n = 3.63,
        alpha = 0,
        E0 = (3.98, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""CAC CBS-QB3 calc, 1dhr""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 582,
    label = "Cd_pri;C_rad/H2/S",
    group1 = 
"""
1 *1 C 0 {2,D} {3,S} {4,S}
2    C 0 {1,D}
3 *2 H 0 {1,S}
4    H 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    S 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00655, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (16.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 583,
    label = "Cd_pri;C_rad/H/CsS",
    group1 = 
"""
1 *1 C 0 {2,D} {3,S} {4,S}
2    C 0 {1,D}
3 *2 H 0 {1,S}
4    H 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0117, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (16.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 584,
    label = "Cd_pri;C_rad/Cs2S",
    group1 = 
"""
1 *1 C 0 {2,D} {3,S} {4,S}
2    C 0 {1,D}
3 *2 H 0 {1,S}
4    H 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    S  0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00472, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (16, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 585,
    label = "Cd_pri;Cd_rad/NonDeS",
    group1 = 
"""
1 *1 C 0 {2,D} {3,S} {4,S}
2    C 0 {1,D}
3 *2 H 0 {1,S}
4    H 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,D} {3,S}
2    C 0 {1,D}
3    S 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0391, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (8.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 586,
    label = "Cd_pri;C_rad/H/CdS",
    group1 = 
"""
1 *1 C 0 {2,D} {3,S} {4,S}
2    C 0 {1,D}
3 *2 H 0 {1,S}
4    H 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cd 0 {1,S}
4    S  0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0646, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (27.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 587,
    label = "Cd_pri;C_rad/CdCsS",
    group1 = 
"""
1 *1 C 0 {2,D} {3,S} {4,S}
2    C 0 {1,D}
3 *2 H 0 {1,S}
4    H 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cd 0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00817, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (27.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 588,
    label = "Cd_pri;C_rad/H/CtS",
    group1 = 
"""
1 *1 C 0 {2,D} {3,S} {4,S}
2    C 0 {1,D}
3 *2 H 0 {1,S}
4    H 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Ct 0 {1,S}
4    S  0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0384, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (25.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 589,
    label = "Cd_pri;C_rad/CtCsS",
    group1 = 
"""
1 *1 C 0 {2,D} {3,S} {4,S}
2    C 0 {1,D}
3 *2 H 0 {1,S}
4    H 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Ct 0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.157, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (26.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 613,
    label = "Cd/H/NonDeC;C_rad/H2/S",
    group1 = 
"""
1 *1 C  0 {2,D} {3,S} {4,S}
2    C  0 {1,D}
3 *2 H  0 {1,S}
4    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    S 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0101, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (13.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 614,
    label = "Cd/H/NonDeC;C_rad/H/CsS",
    group1 = 
"""
1 *1 C  0 {2,D} {3,S} {4,S}
2    C  0 {1,D}
3 *2 H  0 {1,S}
4    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.018, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (13.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 615,
    label = "Cd/H/NonDeC;C_rad/Cs2S",
    group1 = 
"""
1 *1 C  0 {2,D} {3,S} {4,S}
2    C  0 {1,D}
3 *2 H  0 {1,S}
4    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    S  0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00725, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (13.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 616,
    label = "Cd/H/NonDeC;Cd_rad/NonDeS",
    group1 = 
"""
1 *1 C  0 {2,D} {3,S} {4,S}
2    C  0 {1,D}
3 *2 H  0 {1,S}
4    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,D} {3,S}
2    C 0 {1,D}
3    S 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0601, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (6.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 617,
    label = "Cd/H/NonDeC;C_rad/H/CdS",
    group1 = 
"""
1 *1 C  0 {2,D} {3,S} {4,S}
2    C  0 {1,D}
3 *2 H  0 {1,S}
4    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cd 0 {1,S}
4    S  0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0993, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (25.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 618,
    label = "Cd/H/NonDeC;C_rad/CdCsS",
    group1 = 
"""
1 *1 C  0 {2,D} {3,S} {4,S}
2    C  0 {1,D}
3 *2 H  0 {1,S}
4    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cd 0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0125, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (25.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 619,
    label = "Cd/H/NonDeC;C_rad/H/CtS",
    group1 = 
"""
1 *1 C  0 {2,D} {3,S} {4,S}
2    C  0 {1,D}
3 *2 H  0 {1,S}
4    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Ct 0 {1,S}
4    S  0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.059, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (23.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 620,
    label = "Cd/H/NonDeC;C_rad/CtCsS",
    group1 = 
"""
1 *1 C  0 {2,D} {3,S} {4,S}
2    C  0 {1,D}
3 *2 H  0 {1,S}
4    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Ct 0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.241, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (24.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 644,
    label = "Cd/H/Cd;C_rad/H2/S",
    group1 = 
"""
1 *1 C  0 {2,D} {3,S} {4,S}
2    C  0 {1,D}
3 *2 H  0 {1,S}
4    Cd 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    S 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00675, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (13.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 645,
    label = "Cd/H/Cd;C_rad/H/CsS",
    group1 = 
"""
1 *1 C  0 {2,D} {3,S} {4,S}
2    C  0 {1,D}
3 *2 H  0 {1,S}
4    Cd 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0121, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (13.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 646,
    label = "Cd/H/Cd;C_rad/Cs2S",
    group1 = 
"""
1 *1 C  0 {2,D} {3,S} {4,S}
2    C  0 {1,D}
3 *2 H  0 {1,S}
4    Cd 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    S  0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00486, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (13.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 647,
    label = "Cd/H/Cd;Cd_rad/NonDeS",
    group1 = 
"""
1 *1 C  0 {2,D} {3,S} {4,S}
2    C  0 {1,D}
3 *2 H  0 {1,S}
4    Cd 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,D} {3,S}
2    C 0 {1,D}
3    S 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0404, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 648,
    label = "Cd/H/Cd;C_rad/H/CdS",
    group1 = 
"""
1 *1 C  0 {2,D} {3,S} {4,S}
2    C  0 {1,D}
3 *2 H  0 {1,S}
4    Cd 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cd 0 {1,S}
4    S  0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0666, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (24.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 649,
    label = "Cd/H/Cd;C_rad/CdCsS",
    group1 = 
"""
1 *1 C  0 {2,D} {3,S} {4,S}
2    C  0 {1,D}
3 *2 H  0 {1,S}
4    Cd 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cd 0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00842, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (24.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 650,
    label = "Cd/H/Cd;C_rad/H/CtS",
    group1 = 
"""
1 *1 C  0 {2,D} {3,S} {4,S}
2    C  0 {1,D}
3 *2 H  0 {1,S}
4    Cd 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Ct 0 {1,S}
4    S  0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0396, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (23.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 651,
    label = "Cd/H/Cd;C_rad/CtCsS",
    group1 = 
"""
1 *1 C  0 {2,D} {3,S} {4,S}
2    C  0 {1,D}
3 *2 H  0 {1,S}
4    Cd 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Ct 0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.162, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (24.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 675,
    label = "Cb_H;C_rad/H2/S",
    group1 = 
"""
1 *1 Cb       0 {2,B} {3,B} {4,S}
2    {Cb,Cbf} 0 {1,B}
3    {Cb,Cbf} 0 {1,B}
4 *2 H        0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    S 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00747, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (18.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 676,
    label = "Cb_H;C_rad/H/CsS",
    group1 = 
"""
1 *1 Cb       0 {2,B} {3,B} {4,S}
2    {Cb,Cbf} 0 {1,B}
3    {Cb,Cbf} 0 {1,B}
4 *2 H        0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0133, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (18.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 677,
    label = "Cb_H;C_rad/Cs2S",
    group1 = 
"""
1 *1 Cb       0 {2,B} {3,B} {4,S}
2    {Cb,Cbf} 0 {1,B}
3    {Cb,Cbf} 0 {1,B}
4 *2 H        0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    S  0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00538, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (17.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 678,
    label = "Cb_H;Cd_rad/NonDeS",
    group1 = 
"""
1 *1 Cb       0 {2,B} {3,B} {4,S}
2    {Cb,Cbf} 0 {1,B}
3    {Cb,Cbf} 0 {1,B}
4 *2 H        0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,D} {3,S}
2    C 0 {1,D}
3    S 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0446, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (10.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 679,
    label = "Cb_H;C_rad/H/CdS",
    group1 = 
"""
1 *1 Cb       0 {2,B} {3,B} {4,S}
2    {Cb,Cbf} 0 {1,B}
3    {Cb,Cbf} 0 {1,B}
4 *2 H        0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cd 0 {1,S}
4    S  0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0737, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (29.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 680,
    label = "Cb_H;C_rad/CdCsS",
    group1 = 
"""
1 *1 Cb       0 {2,B} {3,B} {4,S}
2    {Cb,Cbf} 0 {1,B}
3    {Cb,Cbf} 0 {1,B}
4 *2 H        0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cd 0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00931, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (29.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 681,
    label = "Cb_H;C_rad/H/CtS",
    group1 = 
"""
1 *1 Cb       0 {2,B} {3,B} {4,S}
2    {Cb,Cbf} 0 {1,B}
3    {Cb,Cbf} 0 {1,B}
4 *2 H        0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Ct 0 {1,S}
4    S  0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0438, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (27.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 682,
    label = "Cb_H;C_rad/CtCsS",
    group1 = 
"""
1 *1 Cb       0 {2,B} {3,B} {4,S}
2    {Cb,Cbf} 0 {1,B}
3    {Cb,Cbf} 0 {1,B}
4 *2 H        0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Ct 0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.179, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (28.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 706,
    label = "Cd/H/Ct;C_rad/H2/S",
    group1 = 
"""
1 *1 C  0 {2,D} {3,S} {4,S}
2    C  0 {1,D}
3 *2 H  0 {1,S}
4    Ct 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    S 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00498, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (11.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 707,
    label = "Cd/H/Ct;C_rad/H/CsS",
    group1 = 
"""
1 *1 C  0 {2,D} {3,S} {4,S}
2    C  0 {1,D}
3 *2 H  0 {1,S}
4    Ct 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00889, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (11.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 708,
    label = "Cd/H/Ct;C_rad/Cs2S",
    group1 = 
"""
1 *1 C  0 {2,D} {3,S} {4,S}
2    C  0 {1,D}
3 *2 H  0 {1,S}
4    Ct 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    S  0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00359, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (11.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 709,
    label = "Cd/H/Ct;Cd_rad/NonDeS",
    group1 = 
"""
1 *1 C  0 {2,D} {3,S} {4,S}
2    C  0 {1,D}
3 *2 H  0 {1,S}
4    Ct 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,D} {3,S}
2    C 0 {1,D}
3    S 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0298, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (3.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 710,
    label = "Cd/H/Ct;C_rad/H/CdS",
    group1 = 
"""
1 *1 C  0 {2,D} {3,S} {4,S}
2    C  0 {1,D}
3 *2 H  0 {1,S}
4    Ct 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cd 0 {1,S}
4    S  0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0491, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (22.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 711,
    label = "Cd/H/Ct;C_rad/CdCsS",
    group1 = 
"""
1 *1 C  0 {2,D} {3,S} {4,S}
2    C  0 {1,D}
3 *2 H  0 {1,S}
4    Ct 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cd 0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00621, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (22.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 712,
    label = "Cd/H/Ct;C_rad/H/CtS",
    group1 = 
"""
1 *1 C  0 {2,D} {3,S} {4,S}
2    C  0 {1,D}
3 *2 H  0 {1,S}
4    Ct 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Ct 0 {1,S}
4    S  0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0292, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (21.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 713,
    label = "Cd/H/Ct;C_rad/CtCsS",
    group1 = 
"""
1 *1 C  0 {2,D} {3,S} {4,S}
2    C  0 {1,D}
3 *2 H  0 {1,S}
4    Ct 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Ct 0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.119, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (21.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 714,
    label = "C/H3/S;H_rad",
    group1 = 
"""
1 *1 C 0 {2,S} {3,S} {4,S} {5,S}
2 *2 H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
5    S 0 {1,S}
""",
    group2 = 
"""
1 *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (0.177, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (3.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 715,
    label = "C/H3/S;C_methyl",
    group1 = 
"""
1 *1 C 0 {2,S} {3,S} {4,S} {5,S}
2 *2 H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
5    S 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00511, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (5.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 716,
    label = "C/H3/S;C_rad/H2/Cs",
    group1 = 
"""
1 *1 C 0 {2,S} {3,S} {4,S} {5,S}
2 *2 H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
5    S 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    H  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00104, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (7.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 717,
    label = "C/H3/S;C_rad/H/NonDeC",
    group1 = 
"""
1 *1 C 0 {2,S} {3,S} {4,S} {5,S}
2 *2 H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
5    S 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00275, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (8.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 718,
    label = "C/H3/S;C_rad/Cs3",
    group1 = 
"""
1 *1 C 0 {2,S} {3,S} {4,S} {5,S}
2 *2 H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
5    S 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cs 0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00144, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (8.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 719,
    label = "C/H3/S;C_rad/H2/Cd",
    group1 = 
"""
1 *1 C 0 {2,S} {3,S} {4,S} {5,S}
2 *2 H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
5    S 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    H  0 {1,S}
4    Cd 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0107, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (18.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 720,
    label = "C/H3/S;C_rad/H/CdCs",
    group1 = 
"""
1 *1 C 0 {2,S} {3,S} {4,S} {5,S}
2 *2 H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
5    S 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cd 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00846, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (20.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 721,
    label = "C/H3/S;C_rad/CdCs2",
    group1 = 
"""
1 *1 C 0 {2,S} {3,S} {4,S} {5,S}
2 *2 H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
5    S 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cd 0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00231, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (20.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 722,
    label = "C/H3/S;C_rad/H/CdCd",
    group1 = 
"""
1 *1 C 0 {2,S} {3,S} {4,S} {5,S}
2 *2 H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
5    S 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cd 0 {1,S}
4    Cd 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0341, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (28.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 723,
    label = "C/H3/S;C_rad/CdCdCs",
    group1 = 
"""
1 *1 C 0 {2,S} {3,S} {4,S} {5,S}
2 *2 H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
5    S 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cd 0 {1,S}
3    Cd 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00302, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (29.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 724,
    label = "C/H3/S;C_rad/H2/Ct",
    group1 = 
"""
1 *1 C 0 {2,S} {3,S} {4,S} {5,S}
2 *2 H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
5    S 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    H  0 {1,S}
4    Ct 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00488, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (14.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 725,
    label = "C/H3/S;C_rad/H/CtCs",
    group1 = 
"""
1 *1 C 0 {2,S} {3,S} {4,S} {5,S}
2 *2 H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
5    S 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Ct 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00203, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (16.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 726,
    label = "C/H3/S;C_rad/CtCs2",
    group1 = 
"""
1 *1 C 0 {2,S} {3,S} {4,S} {5,S}
2 *2 H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
5    S 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Ct 0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00144, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (17.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 727,
    label = "C/H3/S;C_rad/H/CtCt",
    group1 = 
"""
1 *1 C 0 {2,S} {3,S} {4,S} {5,S}
2 *2 H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
5    S 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Ct 0 {1,S}
4    Ct 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0103, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (22.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 728,
    label = "C/H3/S;C_rad/CtCtCs",
    group1 = 
"""
1 *1 C 0 {2,S} {3,S} {4,S} {5,S}
2 *2 H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
5    S 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Ct 0 {1,S}
3    Ct 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.000508, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (24, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 729,
    label = "C/H3/S;C_rad/H2/Cb",
    group1 = 
"""
1 *1 C 0 {2,S} {3,S} {4,S} {5,S}
2 *2 H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
5    S 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    H  0 {1,S}
4    Cb 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0105, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (16.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 730,
    label = "C/H3/S;C_rad/H/CbCs",
    group1 = 
"""
1 *1 C 0 {2,S} {3,S} {4,S} {5,S}
2 *2 H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
5    S 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cb 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00538, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (17.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 731,
    label = "C/H3/S;C_rad/CbCs2",
    group1 = 
"""
1 *1 C 0 {2,S} {3,S} {4,S} {5,S}
2 *2 H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
5    S 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cb 0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.000256, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (17, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 732,
    label = "C/H3/S;Cd_pri_rad",
    group1 = 
"""
1 *1 C 0 {2,S} {3,S} {4,S} {5,S}
2 *2 H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
5    S 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,D} {3,S}
2    C 0 {1,D}
3    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00481, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (1.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 733,
    label = "C/H3/S;Cd_rad/NonDeC",
    group1 = 
"""
1 *1 C 0 {2,S} {3,S} {4,S} {5,S}
2 *2 H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
5    S 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,D} {3,S}
2    C  0 {1,D}
3    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00476, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (2.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 734,
    label = "C/H3/S;Cd_rad/Cd",
    group1 = 
"""
1 *1 C 0 {2,S} {3,S} {4,S} {5,S}
2 *2 H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
5    S 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,D} {3,S}
2    C  0 {1,D}
3    Cd 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00227, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 735,
    label = "C/H3/S;Cb_rad",
    group1 = 
"""
1 *1 C 0 {2,S} {3,S} {4,S} {5,S}
2 *2 H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
5    S 0 {1,S}
""",
    group2 = 
"""
1 *3 Cb       1 {2,B} {3,B}
2    {Cb,Cbf} 0 {1,B}
3    {Cb,Cbf} 0 {1,B}
""",
    kinetics = ArrheniusEP(
        A = (0.00572, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (-1.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 736,
    label = "C/H3/S;Cd_rad/Ct",
    group1 = 
"""
1 *1 C 0 {2,S} {3,S} {4,S} {5,S}
2 *2 H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
5    S 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,D} {3,S}
2    C  0 {1,D}
3    Ct 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.000487, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (6.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 737,
    label = "C/H3/S;C_rad/H2/S",
    group1 = 
"""
1 *1 C 0 {2,S} {3,S} {4,S} {5,S}
2 *2 H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
5    S 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    S 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00165, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (11.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 738,
    label = "C/H3/S;C_rad/H/CsS",
    group1 = 
"""
1 *1 C 0 {2,S} {3,S} {4,S} {5,S}
2 *2 H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
5    S 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00294, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (11.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 739,
    label = "C/H3/S;C_rad/Cs2S",
    group1 = 
"""
1 *1 C 0 {2,S} {3,S} {4,S} {5,S}
2 *2 H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
5    S 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    S  0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00119, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (11, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 740,
    label = "C/H3/S;Cd_rad/NonDeS",
    group1 = 
"""
1 *1 C 0 {2,S} {3,S} {4,S} {5,S}
2 *2 H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
5    S 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,D} {3,S}
2    C 0 {1,D}
3    S 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00986, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (3.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 741,
    label = "C/H3/S;C_rad/H/CdS",
    group1 = 
"""
1 *1 C 0 {2,S} {3,S} {4,S} {5,S}
2 *2 H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
5    S 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cd 0 {1,S}
4    S  0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0163, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (22.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 742,
    label = "C/H3/S;C_rad/CdCsS",
    group1 = 
"""
1 *1 C 0 {2,S} {3,S} {4,S} {5,S}
2 *2 H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
5    S 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cd 0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00206, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (22.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 743,
    label = "C/H3/S;C_rad/H/CtS",
    group1 = 
"""
1 *1 C 0 {2,S} {3,S} {4,S} {5,S}
2 *2 H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
5    S 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Ct 0 {1,S}
4    S  0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00967, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (20.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 744,
    label = "C/H3/S;C_rad/CtCsS",
    group1 = 
"""
1 *1 C 0 {2,S} {3,S} {4,S} {5,S}
2 *2 H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
5    S 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Ct 0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0395, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (21.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 745,
    label = "C/H2/CsS;H_rad",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    S  0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (0.487, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (2.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 746,
    label = "C/H2/CsS;C_methyl",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    S  0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0141, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (4.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 747,
    label = "C/H2/CsS;C_rad/H2/Cs",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    S  0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    H  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00287, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (5.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 748,
    label = "C/H2/CsS;C_rad/H/NonDeC",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    S  0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00759, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (6.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 749,
    label = "C/H2/CsS;C_rad/Cs3",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    S  0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cs 0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00398, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (6.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 750,
    label = "C/H2/CsS;C_rad/H2/Cd",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    S  0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    H  0 {1,S}
4    Cd 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0296, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (17.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 751,
    label = "C/H2/CsS;C_rad/H/CdCs",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    S  0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cd 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0233, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (19, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 752,
    label = "C/H2/CsS;C_rad/CdCs2",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    S  0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cd 0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00638, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (19.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 753,
    label = "C/H2/CsS;C_rad/H/CdCd",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    S  0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cd 0 {1,S}
4    Cd 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0939, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (27.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 754,
    label = "C/H2/CsS;C_rad/CdCdCs",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    S  0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cd 0 {1,S}
3    Cd 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00834, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (27.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 755,
    label = "C/H2/CsS;C_rad/H2/Ct",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    S  0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    H  0 {1,S}
4    Ct 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0135, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (13.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 756,
    label = "C/H2/CsS;C_rad/H/CtCs",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    S  0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Ct 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0056, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (15, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 757,
    label = "C/H2/CsS;C_rad/CtCs2",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    S  0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Ct 0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00397, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (15.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 758,
    label = "C/H2/CsS;C_rad/H/CtCt",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    S  0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Ct 0 {1,S}
4    Ct 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0285, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (21.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 759,
    label = "C/H2/CsS;C_rad/CtCtCs",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    S  0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Ct 0 {1,S}
3    Ct 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0014, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (22.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 760,
    label = "C/H2/CsS;C_rad/H2/Cb",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    S  0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    H  0 {1,S}
4    Cb 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0289, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (15.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 761,
    label = "C/H2/CsS;C_rad/H/CbCs",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    S  0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cb 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0148, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (15.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 762,
    label = "C/H2/CsS;C_rad/CbCs2",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    S  0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cb 0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.000707, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (15.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 763,
    label = "C/H2/CsS;Cd_pri_rad",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    S  0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,D} {3,S}
2    C 0 {1,D}
3    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0133, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (-0.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 764,
    label = "C/H2/CsS;Cd_rad/NonDeC",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    S  0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,D} {3,S}
2    C  0 {1,D}
3    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0131, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (0.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 765,
    label = "C/H2/CsS;Cd_rad/Cd",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    S  0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,D} {3,S}
2    C  0 {1,D}
3    Cd 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00626, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (7.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 766,
    label = "C/H2/CsS;Cb_rad",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    S  0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 Cb       1 {2,B} {3,B}
2    {Cb,Cbf} 0 {1,B}
3    {Cb,Cbf} 0 {1,B}
""",
    kinetics = ArrheniusEP(
        A = (0.0158, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (-2.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 767,
    label = "C/H2/CsS;Cd_rad/Ct",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    S  0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,D} {3,S}
2    C  0 {1,D}
3    Ct 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00134, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (4.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 768,
    label = "C/H2/CsS;C_rad/H2/S",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    S  0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    S 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00455, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (9.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 769,
    label = "C/H2/CsS;C_rad/H/CsS",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    S  0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00812, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (9.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 770,
    label = "C/H2/CsS;C_rad/Cs2S",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    S  0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    S  0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00328, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (9.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 771,
    label = "C/H2/CsS;Cd_rad/NonDeS",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    S  0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,D} {3,S}
2    C 0 {1,D}
3    S 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0272, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 772,
    label = "C/H2/CsS;C_rad/H/CdS",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    S  0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cd 0 {1,S}
4    S  0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0449, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (20.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 773,
    label = "C/H2/CsS;C_rad/CdCsS",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    S  0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cd 0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00567, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (20.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 774,
    label = "C/H2/CsS;C_rad/H/CtS",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    S  0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Ct 0 {1,S}
4    S  0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0267, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (19.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 775,
    label = "C/H2/CsS;C_rad/CtCsS",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    S  0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Ct 0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.109, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (20.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 776,
    label = "C/H/Cs2S;H_rad",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (0.595, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (0.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 777,
    label = "C/H/Cs2S;C_methyl",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0172, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (2.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 778,
    label = "C/H/Cs2S;C_rad/H2/Cs",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    H  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00351, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (4.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 779,
    label = "C/H/Cs2S;C_rad/H/NonDeC",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00926, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (5.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 780,
    label = "C/H/Cs2S;C_rad/Cs3",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cs 0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00487, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (5.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 781,
    label = "C/H/Cs2S;C_rad/H2/Cd",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    H  0 {1,S}
4    Cd 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0362, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (15.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 782,
    label = "C/H/Cs2S;C_rad/H/CdCs",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cd 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0285, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (17.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 783,
    label = "C/H/Cs2S;C_rad/CdCs2",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cd 0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00779, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (17.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 784,
    label = "C/H/Cs2S;C_rad/H/CdCd",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cd 0 {1,S}
4    Cd 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.115, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (25.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 785,
    label = "C/H/Cs2S;C_rad/CdCdCs",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cd 0 {1,S}
3    Cd 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0102, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (26.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 786,
    label = "C/H/Cs2S;C_rad/H2/Ct",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    H  0 {1,S}
4    Ct 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0164, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (11.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 787,
    label = "C/H/Cs2S;C_rad/H/CtCs",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Ct 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00684, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (13.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 788,
    label = "C/H/Cs2S;C_rad/CtCs2",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Ct 0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00485, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (14.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 789,
    label = "C/H/Cs2S;C_rad/H/CtCt",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Ct 0 {1,S}
4    Ct 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0348, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (20, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 790,
    label = "C/H/Cs2S;C_rad/CtCtCs",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Ct 0 {1,S}
3    Ct 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00171, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (21, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 791,
    label = "C/H/Cs2S;C_rad/H2/Cb",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    H  0 {1,S}
4    Cb 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0353, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (13.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 792,
    label = "C/H/Cs2S;C_rad/H/CbCs",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cb 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0181, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (14.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 793,
    label = "C/H/Cs2S;C_rad/CbCs2",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cb 0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.000864, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (14, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 794,
    label = "C/H/Cs2S;Cd_pri_rad",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,D} {3,S}
2    C 0 {1,D}
3    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0162, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (-1.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 795,
    label = "C/H/Cs2S;Cd_rad/NonDeC",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,D} {3,S}
2    C  0 {1,D}
3    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.016, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (-0.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 796,
    label = "C/H/Cs2S;Cd_rad/Cd",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,D} {3,S}
2    C  0 {1,D}
3    Cd 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00765, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 797,
    label = "C/H/Cs2S;Cb_rad",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 Cb       1 {2,B} {3,B}
2    {Cb,Cbf} 0 {1,B}
3    {Cb,Cbf} 0 {1,B}
""",
    kinetics = ArrheniusEP(
        A = (0.0193, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (-4.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 798,
    label = "C/H/Cs2S;Cd_rad/Ct",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,D} {3,S}
2    C  0 {1,D}
3    Ct 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00164, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (3.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 799,
    label = "C/H/Cs2S;C_rad/H2/S",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    S 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00555, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (8.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 800,
    label = "C/H/Cs2S;C_rad/H/CsS",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00992, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (8.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 801,
    label = "C/H/Cs2S;C_rad/Cs2S",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    S  0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.004, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 802,
    label = "C/H/Cs2S;Cd_rad/NonDeS",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,D} {3,S}
2    C 0 {1,D}
3    S 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0332, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (0.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 803,
    label = "C/H/Cs2S;C_rad/H/CdS",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cd 0 {1,S}
4    S  0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0548, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (19.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 804,
    label = "C/H/Cs2S;C_rad/CdCsS",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cd 0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00692, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (19.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 805,
    label = "C/H/Cs2S;C_rad/H/CtS",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Ct 0 {1,S}
4    S  0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0326, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (17.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 806,
    label = "C/H/Cs2S;C_rad/CtCsS",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Ct 0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.133, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (18.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 807,
    label = "Cd/H/CS;H_rad",
    group1 = 
"""
1 *1 C  0 {2,D} {3,S} {4,S}
2    C  0 {1,D}
3 *2 H  0 {1,S}
4    Cd 0 {1,S} {5,D}
5    S  0 {4,D}
""",
    group2 = 
"""
1 *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (1.24, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (4.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 808,
    label = "Cd/H/CS;C_methyl",
    group1 = 
"""
1 *1 C  0 {2,D} {3,S} {4,S}
2    C  0 {1,D}
3 *2 H  0 {1,S}
4    Cd 0 {1,S} {5,D}
5    S  0 {4,D}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.036, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (6.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 809,
    label = "Cd/H/CS;C_rad/H2/Cs",
    group1 = 
"""
1 *1 C  0 {2,D} {3,S} {4,S}
2    C  0 {1,D}
3 *2 H  0 {1,S}
4    Cd 0 {1,S} {5,D}
5    S  0 {4,D}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    H  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00733, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (8.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 810,
    label = "Cd/H/CS;C_rad/H/NonDeC",
    group1 = 
"""
1 *1 C  0 {2,D} {3,S} {4,S}
2    C  0 {1,D}
3 *2 H  0 {1,S}
4    Cd 0 {1,S} {5,D}
5    S  0 {4,D}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0194, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (9.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 811,
    label = "Cd/H/CS;C_rad/Cs3",
    group1 = 
"""
1 *1 C  0 {2,D} {3,S} {4,S}
2    C  0 {1,D}
3 *2 H  0 {1,S}
4    Cd 0 {1,S} {5,D}
5    S  0 {4,D}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cs 0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0102, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (9.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 812,
    label = "Cd/H/CS;C_rad/H2/Cd",
    group1 = 
"""
1 *1 C  0 {2,D} {3,S} {4,S}
2    C  0 {1,D}
3 *2 H  0 {1,S}
4    Cd 0 {1,S} {5,D}
5    S  0 {4,D}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    H  0 {1,S}
4    Cd 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0756, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (19.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 813,
    label = "Cd/H/CS;C_rad/H/CdCs",
    group1 = 
"""
1 *1 C  0 {2,D} {3,S} {4,S}
2    C  0 {1,D}
3 *2 H  0 {1,S}
4    Cd 0 {1,S} {5,D}
5    S  0 {4,D}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cd 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0596, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (21.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 814,
    label = "Cd/H/CS;C_rad/CdCs2",
    group1 = 
"""
1 *1 C  0 {2,D} {3,S} {4,S}
2    C  0 {1,D}
3 *2 H  0 {1,S}
4    Cd 0 {1,S} {5,D}
5    S  0 {4,D}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cd 0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0163, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (21.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 815,
    label = "Cd/H/CS;C_rad/H/CdCd",
    group1 = 
"""
1 *1 C  0 {2,D} {3,S} {4,S}
2    C  0 {1,D}
3 *2 H  0 {1,S}
4    Cd 0 {1,S} {5,D}
5    S  0 {4,D}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cd 0 {1,S}
4    Cd 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.24, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (29.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 816,
    label = "Cd/H/CS;C_rad/CdCdCs",
    group1 = 
"""
1 *1 C  0 {2,D} {3,S} {4,S}
2    C  0 {1,D}
3 *2 H  0 {1,S}
4    Cd 0 {1,S} {5,D}
5    S  0 {4,D}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cd 0 {1,S}
3    Cd 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0213, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (30.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 817,
    label = "Cd/H/CS;C_rad/H2/Ct",
    group1 = 
"""
1 *1 C  0 {2,D} {3,S} {4,S}
2    C  0 {1,D}
3 *2 H  0 {1,S}
4    Cd 0 {1,S} {5,D}
5    S  0 {4,D}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    H  0 {1,S}
4    Ct 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0344, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (15.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 818,
    label = "Cd/H/CS;C_rad/H/CtCs",
    group1 = 
"""
1 *1 C  0 {2,D} {3,S} {4,S}
2    C  0 {1,D}
3 *2 H  0 {1,S}
4    Cd 0 {1,S} {5,D}
5    S  0 {4,D}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Ct 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0143, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (17.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 819,
    label = "Cd/H/CS;C_rad/CtCs2",
    group1 = 
"""
1 *1 C  0 {2,D} {3,S} {4,S}
2    C  0 {1,D}
3 *2 H  0 {1,S}
4    Cd 0 {1,S} {5,D}
5    S  0 {4,D}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Ct 0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0101, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (18.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 820,
    label = "Cd/H/CS;C_rad/H/CtCt",
    group1 = 
"""
1 *1 C  0 {2,D} {3,S} {4,S}
2    C  0 {1,D}
3 *2 H  0 {1,S}
4    Cd 0 {1,S} {5,D}
5    S  0 {4,D}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Ct 0 {1,S}
4    Ct 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0728, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (23.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 821,
    label = "Cd/H/CS;C_rad/CtCtCs",
    group1 = 
"""
1 *1 C  0 {2,D} {3,S} {4,S}
2    C  0 {1,D}
3 *2 H  0 {1,S}
4    Cd 0 {1,S} {5,D}
5    S  0 {4,D}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Ct 0 {1,S}
3    Ct 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00358, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (25, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 822,
    label = "Cd/H/CS;C_rad/H2/Cb",
    group1 = 
"""
1 *1 C  0 {2,D} {3,S} {4,S}
2    C  0 {1,D}
3 *2 H  0 {1,S}
4    Cd 0 {1,S} {5,D}
5    S  0 {4,D}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    H  0 {1,S}
4    Cb 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0738, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (17.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 823,
    label = "Cd/H/CS;C_rad/H/CbCs",
    group1 = 
"""
1 *1 C  0 {2,D} {3,S} {4,S}
2    C  0 {1,D}
3 *2 H  0 {1,S}
4    Cd 0 {1,S} {5,D}
5    S  0 {4,D}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cb 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0379, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (18.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 824,
    label = "Cd/H/CS;C_rad/CbCs2",
    group1 = 
"""
1 *1 C  0 {2,D} {3,S} {4,S}
2    C  0 {1,D}
3 *2 H  0 {1,S}
4    Cd 0 {1,S} {5,D}
5    S  0 {4,D}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cb 0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00181, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (17.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 825,
    label = "Cd/H/CS;Cd_pri_rad",
    group1 = 
"""
1 *1 C  0 {2,D} {3,S} {4,S}
2    C  0 {1,D}
3 *2 H  0 {1,S}
4    Cd 0 {1,S} {5,D}
5    S  0 {4,D}
""",
    group2 = 
"""
1 *3 C 1 {2,D} {3,S}
2    C 0 {1,D}
3    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0339, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (2.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 826,
    label = "Cd/H/CS;Cd_rad/NonDeC",
    group1 = 
"""
1 *1 C  0 {2,D} {3,S} {4,S}
2    C  0 {1,D}
3 *2 H  0 {1,S}
4    Cd 0 {1,S} {5,D}
5    S  0 {4,D}
""",
    group2 = 
"""
1 *3 C  1 {2,D} {3,S}
2    C  0 {1,D}
3    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0335, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (3.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 827,
    label = "Cd/H/CS;Cd_rad/Cd",
    group1 = 
"""
1 *1 C  0 {2,D} {3,S} {4,S}
2    C  0 {1,D}
3 *2 H  0 {1,S}
4    Cd 0 {1,S} {5,D}
5    S  0 {4,D}
""",
    group2 = 
"""
1 *3 C  1 {2,D} {3,S}
2    C  0 {1,D}
3    Cd 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.016, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (9.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 828,
    label = "Cd/H/CS;Cb_rad",
    group1 = 
"""
1 *1 C  0 {2,D} {3,S} {4,S}
2    C  0 {1,D}
3 *2 H  0 {1,S}
4    Cd 0 {1,S} {5,D}
5    S  0 {4,D}
""",
    group2 = 
"""
1 *3 Cb       1 {2,B} {3,B}
2    {Cb,Cbf} 0 {1,B}
3    {Cb,Cbf} 0 {1,B}
""",
    kinetics = ArrheniusEP(
        A = (0.0403, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (-0.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 829,
    label = "Cd/H/CS;Cd_rad/Ct",
    group1 = 
"""
1 *1 C  0 {2,D} {3,S} {4,S}
2    C  0 {1,D}
3 *2 H  0 {1,S}
4    Cd 0 {1,S} {5,D}
5    S  0 {4,D}
""",
    group2 = 
"""
1 *3 C  1 {2,D} {3,S}
2    C  0 {1,D}
3    Ct 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00343, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (7.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 830,
    label = "Cd/H/CS;C_rad/H2/S",
    group1 = 
"""
1 *1 C  0 {2,D} {3,S} {4,S}
2    C  0 {1,D}
3 *2 H  0 {1,S}
4    Cd 0 {1,S} {5,D}
5    S  0 {4,D}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    S 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0116, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (12.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 831,
    label = "Cd/H/CS;C_rad/H/CsS",
    group1 = 
"""
1 *1 C  0 {2,D} {3,S} {4,S}
2    C  0 {1,D}
3 *2 H  0 {1,S}
4    Cd 0 {1,S} {5,D}
5    S  0 {4,D}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0207, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (12.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 832,
    label = "Cd/H/CS;C_rad/Cs2S",
    group1 = 
"""
1 *1 C  0 {2,D} {3,S} {4,S}
2    C  0 {1,D}
3 *2 H  0 {1,S}
4    Cd 0 {1,S} {5,D}
5    S  0 {4,D}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    S  0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00837, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (11.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 833,
    label = "Cd/H/CS;Cd_rad/NonDeS",
    group1 = 
"""
1 *1 C  0 {2,D} {3,S} {4,S}
2    C  0 {1,D}
3 *2 H  0 {1,S}
4    Cd 0 {1,S} {5,D}
5    S  0 {4,D}
""",
    group2 = 
"""
1 *3 C 1 {2,D} {3,S}
2    C 0 {1,D}
3    S 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0694, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (4.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 834,
    label = "Cd/H/CS;C_rad/H/CdS",
    group1 = 
"""
1 *1 C  0 {2,D} {3,S} {4,S}
2    C  0 {1,D}
3 *2 H  0 {1,S}
4    Cd 0 {1,S} {5,D}
5    S  0 {4,D}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cd 0 {1,S}
4    S  0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.115, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (23.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 835,
    label = "Cd/H/CS;C_rad/CdCsS",
    group1 = 
"""
1 *1 C  0 {2,D} {3,S} {4,S}
2    C  0 {1,D}
3 *2 H  0 {1,S}
4    Cd 0 {1,S} {5,D}
5    S  0 {4,D}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cd 0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0145, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (23.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 836,
    label = "Cd/H/CS;C_rad/H/CtS",
    group1 = 
"""
1 *1 C  0 {2,D} {3,S} {4,S}
2    C  0 {1,D}
3 *2 H  0 {1,S}
4    Cd 0 {1,S} {5,D}
5    S  0 {4,D}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Ct 0 {1,S}
4    S  0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0681, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (21.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 837,
    label = "Cd/H/CS;C_rad/CtCsS",
    group1 = 
"""
1 *1 C  0 {2,D} {3,S} {4,S}
2    C  0 {1,D}
3 *2 H  0 {1,S}
4    Cd 0 {1,S} {5,D}
5    S  0 {4,D}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Ct 0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.279, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (22.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 838,
    label = "C/H2/CdS;H_rad",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Cd 0 {1,S}
5    S  0 {1,S}
""",
    group2 = 
"""
1 *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (0.893, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (1.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 839,
    label = "C/H2/CdS;C_methyl",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Cd 0 {1,S}
5    S  0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0258, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (3.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 840,
    label = "C/H2/CdS;C_rad/H2/Cs",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Cd 0 {1,S}
5    S  0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    H  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00526, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (4.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 841,
    label = "C/H2/CdS;C_rad/H/NonDeC",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Cd 0 {1,S}
5    S  0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0139, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (5.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 842,
    label = "C/H2/CdS;C_rad/Cs3",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Cd 0 {1,S}
5    S  0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cs 0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0073, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (5.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 843,
    label = "C/H2/CdS;C_rad/H2/Cd",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Cd 0 {1,S}
5    S  0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    H  0 {1,S}
4    Cd 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0543, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (16.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 844,
    label = "C/H2/CdS;C_rad/H/CdCs",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Cd 0 {1,S}
5    S  0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cd 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0428, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (18, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 845,
    label = "C/H2/CdS;C_rad/CdCs2",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Cd 0 {1,S}
5    S  0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cd 0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0117, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (18.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 846,
    label = "C/H2/CdS;C_rad/H/CdCd",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Cd 0 {1,S}
5    S  0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cd 0 {1,S}
4    Cd 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.172, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (26.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 847,
    label = "C/H2/CdS;C_rad/CdCdCs",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Cd 0 {1,S}
5    S  0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cd 0 {1,S}
3    Cd 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0153, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (26.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 848,
    label = "C/H2/CdS;C_rad/H2/Ct",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Cd 0 {1,S}
5    S  0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    H  0 {1,S}
4    Ct 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0247, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (12.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 849,
    label = "C/H2/CdS;C_rad/H/CtCs",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Cd 0 {1,S}
5    S  0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Ct 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0103, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (14, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 850,
    label = "C/H2/CdS;C_rad/CtCs2",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Cd 0 {1,S}
5    S  0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Ct 0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00728, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (14.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 851,
    label = "C/H2/CdS;C_rad/H/CtCt",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Cd 0 {1,S}
5    S  0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Ct 0 {1,S}
4    Ct 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0523, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (20.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 852,
    label = "C/H2/CdS;C_rad/CtCtCs",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Cd 0 {1,S}
5    S  0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Ct 0 {1,S}
3    Ct 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00257, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (21.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 853,
    label = "C/H2/CdS;C_rad/H2/Cb",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Cd 0 {1,S}
5    S  0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    H  0 {1,S}
4    Cb 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0529, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (14.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 854,
    label = "C/H2/CdS;C_rad/H/CbCs",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Cd 0 {1,S}
5    S  0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cb 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0272, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (14.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 855,
    label = "C/H2/CdS;C_rad/CbCs2",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Cd 0 {1,S}
5    S  0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cb 0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0013, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (14.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 856,
    label = "C/H2/CdS;Cd_pri_rad",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Cd 0 {1,S}
5    S  0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,D} {3,S}
2    C 0 {1,D}
3    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0243, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (-1.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 857,
    label = "C/H2/CdS;Cd_rad/NonDeC",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Cd 0 {1,S}
5    S  0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,D} {3,S}
2    C  0 {1,D}
3    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.024, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (-0.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 858,
    label = "C/H2/CdS;Cd_rad/Cd",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Cd 0 {1,S}
5    S  0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,D} {3,S}
2    C  0 {1,D}
3    Cd 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0115, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (6.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 859,
    label = "C/H2/CdS;Cb_rad",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Cd 0 {1,S}
5    S  0 {1,S}
""",
    group2 = 
"""
1 *3 Cb       1 {2,B} {3,B}
2    {Cb,Cbf} 0 {1,B}
3    {Cb,Cbf} 0 {1,B}
""",
    kinetics = ArrheniusEP(
        A = (0.0289, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (-3.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 860,
    label = "C/H2/CdS;Cd_rad/Ct",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Cd 0 {1,S}
5    S  0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,D} {3,S}
2    C  0 {1,D}
3    Ct 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00246, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (3.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 861,
    label = "C/H2/CdS;C_rad/H2/S",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Cd 0 {1,S}
5    S  0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    S 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00834, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (8.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 862,
    label = "C/H2/CdS;C_rad/H/CsS",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Cd 0 {1,S}
5    S  0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0149, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (8.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 863,
    label = "C/H2/CdS;C_rad/Cs2S",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Cd 0 {1,S}
5    S  0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    S  0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.006, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (8.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 864,
    label = "C/H2/CdS;Cd_rad/NonDeS",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Cd 0 {1,S}
5    S  0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,D} {3,S}
2    C 0 {1,D}
3    S 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0498, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 865,
    label = "C/H2/CdS;C_rad/H/CdS",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Cd 0 {1,S}
5    S  0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cd 0 {1,S}
4    S  0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0823, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (19.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 866,
    label = "C/H2/CdS;C_rad/CdCsS",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Cd 0 {1,S}
5    S  0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cd 0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0104, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (19.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 867,
    label = "C/H2/CdS;C_rad/H/CtS",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Cd 0 {1,S}
5    S  0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Ct 0 {1,S}
4    S  0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0489, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (18.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 868,
    label = "C/H2/CdS;C_rad/CtCsS",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Cd 0 {1,S}
5    S  0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Ct 0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.2, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (19.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 869,
    label = "C/H/CdCsS;H_rad",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Cd 0 {1,S}
4    S  0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (0.481, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 870,
    label = "C/H/CdCsS;C_methyl",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Cd 0 {1,S}
4    S  0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0139, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (2.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 871,
    label = "C/H/CdCsS;C_rad/H2/Cs",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Cd 0 {1,S}
4    S  0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    H  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00283, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (3.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 872,
    label = "C/H/CdCsS;C_rad/H/NonDeC",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Cd 0 {1,S}
4    S  0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00749, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (4.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 873,
    label = "C/H/CdCsS;C_rad/Cs3",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Cd 0 {1,S}
4    S  0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cs 0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00393, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (4.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 874,
    label = "C/H/CdCsS;C_rad/H2/Cd",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Cd 0 {1,S}
4    S  0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    H  0 {1,S}
4    Cd 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0292, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (14.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 875,
    label = "C/H/CdCsS;C_rad/H/CdCs",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Cd 0 {1,S}
4    S  0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cd 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.023, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (16.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 876,
    label = "C/H/CdCsS;C_rad/CdCs2",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Cd 0 {1,S}
4    S  0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cd 0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0063, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (17.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 877,
    label = "C/H/CdCsS;C_rad/H/CdCd",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Cd 0 {1,S}
4    S  0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cd 0 {1,S}
4    Cd 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0927, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (25, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 878,
    label = "C/H/CdCsS;C_rad/CdCdCs",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Cd 0 {1,S}
4    S  0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cd 0 {1,S}
3    Cd 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00823, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (25.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 879,
    label = "C/H/CdCsS;C_rad/H2/Ct",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Cd 0 {1,S}
4    S  0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    H  0 {1,S}
4    Ct 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0133, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (11.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 880,
    label = "C/H/CdCsS;C_rad/H/CtCs",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Cd 0 {1,S}
4    S  0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Ct 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00553, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (12.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 881,
    label = "C/H/CdCsS;C_rad/CtCs2",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Cd 0 {1,S}
4    S  0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Ct 0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00392, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (13.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 882,
    label = "C/H/CdCsS;C_rad/H/CtCt",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Cd 0 {1,S}
4    S  0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Ct 0 {1,S}
4    Ct 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0282, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (19.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 883,
    label = "C/H/CdCsS;C_rad/CtCtCs",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Cd 0 {1,S}
4    S  0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Ct 0 {1,S}
3    Ct 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00138, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (20.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 884,
    label = "C/H/CdCsS;C_rad/H2/Cb",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Cd 0 {1,S}
4    S  0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    H  0 {1,S}
4    Cb 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0285, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (12.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 885,
    label = "C/H/CdCsS;C_rad/H/CbCs",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Cd 0 {1,S}
4    S  0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cb 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0147, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (13.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 886,
    label = "C/H/CdCsS;C_rad/CbCs2",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Cd 0 {1,S}
4    S  0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cb 0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.000698, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (13.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 887,
    label = "C/H/CdCsS;Cd_pri_rad",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Cd 0 {1,S}
4    S  0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,D} {3,S}
2    C 0 {1,D}
3    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0131, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (-2.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 888,
    label = "C/H/CdCsS;Cd_rad/NonDeC",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Cd 0 {1,S}
4    S  0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,D} {3,S}
2    C  0 {1,D}
3    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.013, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (-1.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 889,
    label = "C/H/CdCsS;Cd_rad/Cd",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Cd 0 {1,S}
4    S  0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,D} {3,S}
2    C  0 {1,D}
3    Cd 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00618, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (5.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 890,
    label = "C/H/CdCsS;Cb_rad",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Cd 0 {1,S}
4    S  0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 Cb       1 {2,B} {3,B}
2    {Cb,Cbf} 0 {1,B}
3    {Cb,Cbf} 0 {1,B}
""",
    kinetics = ArrheniusEP(
        A = (0.0156, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (-5.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 891,
    label = "C/H/CdCsS;Cd_rad/Ct",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Cd 0 {1,S}
4    S  0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,D} {3,S}
2    C  0 {1,D}
3    Ct 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00133, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (2.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 892,
    label = "C/H/CdCsS;C_rad/H2/S",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Cd 0 {1,S}
4    S  0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    S 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00449, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (7.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 893,
    label = "C/H/CdCsS;C_rad/H/CsS",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Cd 0 {1,S}
4    S  0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00802, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (7.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 894,
    label = "C/H/CdCsS;C_rad/Cs2S",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Cd 0 {1,S}
4    S  0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    S  0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00323, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (7.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 895,
    label = "C/H/CdCsS;Cd_rad/NonDeS",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Cd 0 {1,S}
4    S  0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,D} {3,S}
2    C 0 {1,D}
3    S 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0268, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (-0.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 896,
    label = "C/H/CdCsS;C_rad/H/CdS",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Cd 0 {1,S}
4    S  0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cd 0 {1,S}
4    S  0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0443, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (18.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 897,
    label = "C/H/CdCsS;C_rad/CdCsS",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Cd 0 {1,S}
4    S  0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cd 0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0056, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (18.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 898,
    label = "C/H/CdCsS;C_rad/H/CtS",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Cd 0 {1,S}
4    S  0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Ct 0 {1,S}
4    S  0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0263, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (17.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 899,
    label = "C/H/CdCsS;C_rad/CtCsS",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Cd 0 {1,S}
4    S  0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Ct 0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.108, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (17.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 900,
    label = "C/H2/CtS;H_rad",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Ct 0 {1,S}
5    S  0 {1,S}
""",
    group2 = 
"""
1 *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (0.732, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (0.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 901,
    label = "C/H2/CtS;C_methyl",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Ct 0 {1,S}
5    S  0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0212, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 902,
    label = "C/H2/CtS;C_rad/H2/Cs",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Ct 0 {1,S}
5    S  0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    H  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00431, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (4.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 903,
    label = "C/H2/CtS;C_rad/H/NonDeC",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Ct 0 {1,S}
5    S  0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0114, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (5.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 904,
    label = "C/H2/CtS;C_rad/Cs3",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Ct 0 {1,S}
5    S  0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cs 0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00598, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (5.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 905,
    label = "C/H2/CtS;C_rad/H2/Cd",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Ct 0 {1,S}
5    S  0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    H  0 {1,S}
4    Cd 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0445, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (15.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 906,
    label = "C/H2/CtS;C_rad/H/CdCs",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Ct 0 {1,S}
5    S  0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cd 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0351, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (17.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 907,
    label = "C/H2/CtS;C_rad/CdCs2",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Ct 0 {1,S}
5    S  0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cd 0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00958, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (18, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 908,
    label = "C/H2/CtS;C_rad/H/CdCd",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Ct 0 {1,S}
5    S  0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cd 0 {1,S}
4    Cd 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.141, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (25.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 909,
    label = "C/H2/CtS;C_rad/CdCdCs",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Ct 0 {1,S}
5    S  0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cd 0 {1,S}
3    Cd 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0125, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (26.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 910,
    label = "C/H2/CtS;C_rad/H2/Ct",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Ct 0 {1,S}
5    S  0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    H  0 {1,S}
4    Ct 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0202, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (12, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 911,
    label = "C/H2/CtS;C_rad/H/CtCs",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Ct 0 {1,S}
5    S  0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Ct 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00841, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (13.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 912,
    label = "C/H2/CtS;C_rad/CtCs2",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Ct 0 {1,S}
5    S  0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Ct 0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00597, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (14.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 913,
    label = "C/H2/CtS;C_rad/H/CtCt",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Ct 0 {1,S}
5    S  0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Ct 0 {1,S}
4    Ct 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0428, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (20.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 914,
    label = "C/H2/CtS;C_rad/CtCtCs",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Ct 0 {1,S}
5    S  0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Ct 0 {1,S}
3    Ct 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00211, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (21.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 915,
    label = "C/H2/CtS;C_rad/H2/Cb",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Ct 0 {1,S}
5    S  0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    H  0 {1,S}
4    Cb 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0434, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (13.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 916,
    label = "C/H2/CtS;C_rad/H/CbCs",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Ct 0 {1,S}
5    S  0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cb 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0223, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (14.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 917,
    label = "C/H2/CtS;C_rad/CbCs2",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Ct 0 {1,S}
5    S  0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cb 0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00106, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (14.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 918,
    label = "C/H2/CtS;Cd_pri_rad",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Ct 0 {1,S}
5    S  0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,D} {3,S}
2    C 0 {1,D}
3    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0199, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (-1.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 919,
    label = "C/H2/CtS;Cd_rad/NonDeC",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Ct 0 {1,S}
5    S  0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,D} {3,S}
2    C  0 {1,D}
3    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0197, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (-0.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 920,
    label = "C/H2/CtS;Cd_rad/Cd",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Ct 0 {1,S}
5    S  0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,D} {3,S}
2    C  0 {1,D}
3    Cd 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0094, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (6.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 921,
    label = "C/H2/CtS;Cb_rad",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Ct 0 {1,S}
5    S  0 {1,S}
""",
    group2 = 
"""
1 *3 Cb       1 {2,B} {3,B}
2    {Cb,Cbf} 0 {1,B}
3    {Cb,Cbf} 0 {1,B}
""",
    kinetics = ArrheniusEP(
        A = (0.0237, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (-4.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 922,
    label = "C/H2/CtS;Cd_rad/Ct",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Ct 0 {1,S}
5    S  0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,D} {3,S}
2    C  0 {1,D}
3    Ct 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00202, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (3.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 923,
    label = "C/H2/CtS;C_rad/H2/S",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Ct 0 {1,S}
5    S  0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    S 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00683, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (8.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 924,
    label = "C/H2/CtS;C_rad/H/CsS",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Ct 0 {1,S}
5    S  0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0122, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (8.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 925,
    label = "C/H2/CtS;C_rad/Cs2S",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Ct 0 {1,S}
5    S  0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    S  0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00492, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (8.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 926,
    label = "C/H2/CtS;Cd_rad/NonDeS",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Ct 0 {1,S}
5    S  0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,D} {3,S}
2    C 0 {1,D}
3    S 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0408, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (0.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 927,
    label = "C/H2/CtS;C_rad/H/CdS",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Ct 0 {1,S}
5    S  0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cd 0 {1,S}
4    S  0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0674, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (19.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 928,
    label = "C/H2/CtS;C_rad/CdCsS",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Ct 0 {1,S}
5    S  0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cd 0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00851, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (19.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 929,
    label = "C/H2/CtS;C_rad/H/CtS",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Ct 0 {1,S}
5    S  0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Ct 0 {1,S}
4    S  0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0401, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (18, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 930,
    label = "C/H2/CtS;C_rad/CtCsS",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Ct 0 {1,S}
5    S  0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Ct 0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.164, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (18.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 931,
    label = "C/H/CtCsS;H_rad",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Ct 0 {1,S}
4    S  0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (0.739, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (-0.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 932,
    label = "C/H/CtCsS;C_methyl",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Ct 0 {1,S}
4    S  0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0214, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (1.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 933,
    label = "C/H/CtCsS;C_rad/H2/Cs",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Ct 0 {1,S}
4    S  0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    H  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00435, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (2.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 934,
    label = "C/H/CtCsS;C_rad/H/NonDeC",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Ct 0 {1,S}
4    S  0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0115, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (3.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 935,
    label = "C/H/CtCsS;C_rad/Cs3",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Ct 0 {1,S}
4    S  0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cs 0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00604, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (3.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 936,
    label = "C/H/CtCsS;C_rad/H2/Cd",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Ct 0 {1,S}
4    S  0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    H  0 {1,S}
4    Cd 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0449, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (14.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 937,
    label = "C/H/CtCsS;C_rad/H/CdCs",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Ct 0 {1,S}
4    S  0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cd 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0354, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (16.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 938,
    label = "C/H/CtCsS;C_rad/CdCs2",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Ct 0 {1,S}
4    S  0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cd 0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00967, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (16.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 939,
    label = "C/H/CtCsS;C_rad/H/CdCd",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Ct 0 {1,S}
4    S  0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cd 0 {1,S}
4    Cd 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.142, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (24.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 940,
    label = "C/H/CtCsS;C_rad/CdCdCs",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Ct 0 {1,S}
4    S  0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cd 0 {1,S}
3    Cd 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0126, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (24.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 941,
    label = "C/H/CtCsS;C_rad/H2/Ct",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Ct 0 {1,S}
4    S  0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    H  0 {1,S}
4    Ct 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0204, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (10.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 942,
    label = "C/H/CtCsS;C_rad/H/CtCs",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Ct 0 {1,S}
4    S  0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Ct 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00849, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (12.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 943,
    label = "C/H/CtCsS;C_rad/CtCs2",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Ct 0 {1,S}
4    S  0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Ct 0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00602, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (12.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 944,
    label = "C/H/CtCsS;C_rad/H/CtCt",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Ct 0 {1,S}
4    S  0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Ct 0 {1,S}
4    Ct 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0432, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (18.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 945,
    label = "C/H/CtCsS;C_rad/CtCtCs",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Ct 0 {1,S}
4    S  0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Ct 0 {1,S}
3    Ct 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00213, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (19.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 946,
    label = "C/H/CtCsS;C_rad/H2/Cb",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Ct 0 {1,S}
4    S  0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    H  0 {1,S}
4    Cb 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0438, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (12.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 947,
    label = "C/H/CtCsS;C_rad/H/CbCs",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Ct 0 {1,S}
4    S  0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cb 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0225, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (13, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 948,
    label = "C/H/CtCsS;C_rad/CbCs2",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Ct 0 {1,S}
4    S  0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cb 0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00107, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (12.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 949,
    label = "C/H/CtCsS;Cd_pri_rad",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Ct 0 {1,S}
4    S  0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,D} {3,S}
2    C 0 {1,D}
3    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0201, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (-3.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 950,
    label = "C/H/CtCsS;Cd_rad/NonDeC",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Ct 0 {1,S}
4    S  0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,D} {3,S}
2    C  0 {1,D}
3    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0199, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (-2.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 951,
    label = "C/H/CtCsS;Cd_rad/Cd",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Ct 0 {1,S}
4    S  0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,D} {3,S}
2    C  0 {1,D}
3    Cd 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00949, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (4.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 952,
    label = "C/H/CtCsS;Cb_rad",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Ct 0 {1,S}
4    S  0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 Cb       1 {2,B} {3,B}
2    {Cb,Cbf} 0 {1,B}
3    {Cb,Cbf} 0 {1,B}
""",
    kinetics = ArrheniusEP(
        A = (0.0239, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (-5.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 953,
    label = "C/H/CtCsS;Cd_rad/Ct",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Ct 0 {1,S}
4    S  0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,D} {3,S}
2    C  0 {1,D}
3    Ct 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00204, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (1.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 954,
    label = "C/H/CtCsS;C_rad/H2/S",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Ct 0 {1,S}
4    S  0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    S 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00689, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (6.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 955,
    label = "C/H/CtCsS;C_rad/H/CsS",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Ct 0 {1,S}
4    S  0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0123, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (6.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 956,
    label = "C/H/CtCsS;C_rad/Cs2S",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Ct 0 {1,S}
4    S  0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    S  0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00497, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (6.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 957,
    label = "C/H/CtCsS;Cd_rad/NonDeS",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Ct 0 {1,S}
4    S  0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,D} {3,S}
2    C 0 {1,D}
3    S 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0412, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (-0.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 958,
    label = "C/H/CtCsS;C_rad/H/CdS",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Ct 0 {1,S}
4    S  0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cd 0 {1,S}
4    S  0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.068, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (18, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 959,
    label = "C/H/CtCsS;C_rad/CdCsS",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Ct 0 {1,S}
4    S  0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cd 0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00859, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (18, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 960,
    label = "C/H/CtCsS;C_rad/CtCsS",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Ct 0 {1,S}
4    S  0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Ct 0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0404, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (16.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 961,
    label = "C/H/CtCsS;C_rad/CtCsS",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Ct 0 {1,S}
4    S  0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Ct 0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.165, 'cm^3/(mol*s)'),
        n = 4.24,
        alpha = 0,
        E0 = (17.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 962,
    label = "S_pri;H_rad",
    group1 = 
"""
1 *1 S 0 {2,S} {3,S}
2 *2 H 0 {1,S}
3    H 0 {1,S}
""",
    group2 = 
"""
1 *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (11600, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (-0.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 963,
    label = "S_pri;C_methyl",
    group1 = 
"""
1 *1 S 0 {2,S} {3,S}
2 *2 H 0 {1,S}
3    H 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (208, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (0.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 964,
    label = "S_pri;C_rad/H2/Cs",
    group1 = 
"""
1 *1 S 0 {2,S} {3,S}
2 *2 H 0 {1,S}
3    H 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    H  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (32.2, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (-0.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 965,
    label = "S_pri;C_rad/H/NonDeC",
    group1 = 
"""
1 *1 S 0 {2,S} {3,S}
2 *2 H 0 {1,S}
3    H 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (39.2, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (-1.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 966,
    label = "S_pri;C_rad/Cs3",
    group1 = 
"""
1 *1 S 0 {2,S} {3,S}
2 *2 H 0 {1,S}
3    H 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cs 0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (87.4, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (-2.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 967,
    label = "S_pri;Cd_pri_rad",
    group1 = 
"""
1 *1 S 0 {2,S} {3,S}
2 *2 H 0 {1,S}
3    H 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,D} {3,S}
2    C 0 {1,D}
3    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (550, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (-1.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 968,
    label = "S_pri;Cd_rad/NonDeC",
    group1 = 
"""
1 *1 S 0 {2,S} {3,S}
2 *2 H 0 {1,S}
3    H 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,D} {3,S}
2    C  0 {1,D}
3    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (291, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (-2.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 969,
    label = "S_pri;Cd_rad/Cd",
    group1 = 
"""
1 *1 S 0 {2,S} {3,S}
2 *2 H 0 {1,S}
3    H 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,D} {3,S}
2    C  0 {1,D}
3    Cd 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (195, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (2.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 970,
    label = "S_pri;Cd_rad/Ct",
    group1 = 
"""
1 *1 S 0 {2,S} {3,S}
2 *2 H 0 {1,S}
3    H 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,D} {3,S}
2    C  0 {1,D}
3    Ct 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (30.8, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (-0.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 971,
    label = "S_pri;C_rad/H2/Cd",
    group1 = 
"""
1 *1 S 0 {2,S} {3,S}
2 *2 H 0 {1,S}
3    H 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    H  0 {1,S}
4    Cd 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (143, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 972,
    label = "S_pri;C_rad/H/CdCs",
    group1 = 
"""
1 *1 S 0 {2,S} {3,S}
2 *2 H 0 {1,S}
3    H 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cd 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (114, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (6.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 973,
    label = "S_pri;C_rad/CdCs2",
    group1 = 
"""
1 *1 S 0 {2,S} {3,S}
2 *2 H 0 {1,S}
3    H 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cd 0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (21, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (5.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 974,
    label = "S_pri;C_rad/H/CdCd",
    group1 = 
"""
1 *1 S 0 {2,S} {3,S}
2 *2 H 0 {1,S}
3    H 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cd 0 {1,S}
4    Cd 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (235, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (13, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 975,
    label = "S_pri;C_rad/CdCdCs",
    group1 = 
"""
1 *1 S 0 {2,S} {3,S}
2 *2 H 0 {1,S}
3    H 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cd 0 {1,S}
3    Cd 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (12.5, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (13.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 976,
    label = "S_pri;C_rad/H2/Ct",
    group1 = 
"""
1 *1 S 0 {2,S} {3,S}
2 *2 H 0 {1,S}
3    H 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    H  0 {1,S}
4    Ct 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (124, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (4.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 977,
    label = "S_pri;C_rad/H/CtCs",
    group1 = 
"""
1 *1 S 0 {2,S} {3,S}
2 *2 H 0 {1,S}
3    H 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Ct 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (39.3, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (4.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 978,
    label = "S_pri;C_rad/CtCs2",
    group1 = 
"""
1 *1 S 0 {2,S} {3,S}
2 *2 H 0 {1,S}
3    H 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Ct 0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (13.7, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (3.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 979,
    label = "S_pri;C_rad/H/CtCt",
    group1 = 
"""
1 *1 S 0 {2,S} {3,S}
2 *2 H 0 {1,S}
3    H 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Ct 0 {1,S}
4    Ct 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (98.6, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (9.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 980,
    label = "S_pri;C_rad/CtCtCs",
    group1 = 
"""
1 *1 S 0 {2,S} {3,S}
2 *2 H 0 {1,S}
3    H 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Ct 0 {1,S}
3    Ct 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (2.75, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (9.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 981,
    label = "S_pri;Cb_rad",
    group1 = 
"""
1 *1 S 0 {2,S} {3,S}
2 *2 H 0 {1,S}
3    H 0 {1,S}
""",
    group2 = 
"""
1 *3 Cb       1 {2,B} {3,B}
2    {Cb,Cbf} 0 {1,B}
3    {Cb,Cbf} 0 {1,B}
""",
    kinetics = ArrheniusEP(
        A = (383, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (-3.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 982,
    label = "S_pri;C_rad/H2/Cb",
    group1 = 
"""
1 *1 S 0 {2,S} {3,S}
2 *2 H 0 {1,S}
3    H 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    H  0 {1,S}
4    Cb 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (89.1, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (3.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 983,
    label = "S_pri;C_rad/H/CbCs",
    group1 = 
"""
1 *1 S 0 {2,S} {3,S}
2 *2 H 0 {1,S}
3    H 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cb 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (33.5, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (2.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 984,
    label = "S_pri;C_rad/CbCs2",
    group1 = 
"""
1 *1 S 0 {2,S} {3,S}
2 *2 H 0 {1,S}
3    H 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cb 0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (2.33, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (1.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 985,
    label = "S_pri;C_rad/H2/S",
    group1 = 
"""
1 *1 S 0 {2,S} {3,S}
2 *2 H 0 {1,S}
3    H 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    S 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (28.3, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 986,
    label = "S_pri;C_rad/H/CsS",
    group1 = 
"""
1 *1 S 0 {2,S} {3,S}
2 *2 H 0 {1,S}
3    H 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (66.7, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (-0.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 987,
    label = "S_pri;C_rad/Cs2S",
    group1 = 
"""
1 *1 S 0 {2,S} {3,S}
2 *2 H 0 {1,S}
3    H 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    S  0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (16.3, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (-1.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 988,
    label = "S_pri;Cd_rad/NonDeS",
    group1 = 
"""
1 *1 S 0 {2,S} {3,S}
2 *2 H 0 {1,S}
3    H 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,D} {3,S}
2    C 0 {1,D}
3    S 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (7760, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (-1.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 989,
    label = "S_pri;C_rad/H/CdS",
    group1 = 
"""
1 *1 S 0 {2,S} {3,S}
2 *2 H 0 {1,S}
3    H 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cd 0 {1,S}
4    S  0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (124, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 990,
    label = "S_pri;C_rad/CdCsS",
    group1 = 
"""
1 *1 S 0 {2,S} {3,S}
2 *2 H 0 {1,S}
3    H 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cd 0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (22.6, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (7.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 991,
    label = "S_pri;C_rad/H/CtS",
    group1 = 
"""
1 *1 S 0 {2,S} {3,S}
2 *2 H 0 {1,S}
3    H 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Ct 0 {1,S}
4    S  0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (80.9, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (7.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 992,
    label = "S_pri;C_rad/CtCsS",
    group1 = 
"""
1 *1 S 0 {2,S} {3,S}
2 *2 H 0 {1,S}
3    H 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Ct 0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (381, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (7.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 993,
    label = "S/H/NonDeC;H_rad",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (32200, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (-0.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 994,
    label = "S/H/NonDeC;C_methyl",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (579, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (0.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 995,
    label = "S/H/NonDeC;C_rad/H2/Cs",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    H  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (89.9, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (-0.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 996,
    label = "S/H/NonDeC;C_rad/H/NonDeC",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (109, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (-1.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 997,
    label = "S/H/NonDeC;C_rad/Cs3",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cs 0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (244, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (-3.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 998,
    label = "S/H/NonDeC;Cd_pri_rad",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,D} {3,S}
2    C 0 {1,D}
3    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1530, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (-2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 999,
    label = "S/H/NonDeC;Cd_rad/NonDeC",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,D} {3,S}
2    C  0 {1,D}
3    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (810, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (-3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1000,
    label = "S/H/NonDeC;Cd_rad/Cd",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,D} {3,S}
2    C  0 {1,D}
3    Cd 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (545, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (2.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1001,
    label = "C/H3/O;H_rad",
    group1 = 
"""
1 *1 C 0 {2,S} {3,S} {4,S} {5,S}
2 *2 H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
5    O 0 {1,S}
""",
    group2 = 
"""
1 *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (451, 'cm^3/(mol*s)'),
        n = 3.2,
        alpha = 0,
        E0 = (3.49, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Jodkowski et al. [100] ab initio calculations. added by Greg Magoon 08/25/09""",
    longDesc = 
u"""
[100] Jodkowski, J.T.; Rauez, M.-T.; Rayez, J.-C. J. Phys. Chem. A. 1999, 103, 3750.

CH3OH + H --> CH2OH + H2 (Rxn. R2 in paper)

divided original rate expression by 3 to get rate expression per H atom.

Created by Greg Magoon; maximum error of fitted expression from tabular data for kr2 is 20% (cf. p. 3758); rank of 2 assigned based on rank for other values reported in the paper in the rateLibrary (also 2)
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1001,
    label = "S/H/NonDeC;Cd_rad/Ct",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,D} {3,S}
2    C  0 {1,D}
3    Ct 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (86, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (-0.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1002,
    label = "InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3/beta;InChI=1/C3H7/c1-3-2/h3H,1-2H3",
    group1 = 
"""
1     C 0 {2,S} {6,S} {7,S} {8,S}
2  *1 C 0 {1,S} {3,S} {5,S} {9,S}
3     C 0 {2,S} {4,S} {10,S} {11,S}
4     O 0 {3,S} {12,S}
5     C 0 {2,S} {13,S} {14,S} {15,S}
6     H 0 {1,S}
7     H 0 {1,S}
8     H 0 {1,S}
9  *2 H 0 {2,S}
10    H 0 {3,S}
11    H 0 {3,S}
12    H 0 {4,S}
13    H 0 {5,S}
14    H 0 {5,S}
15    H 0 {5,S}
""",
    group2 = 
"""
1     C 0 {2,S} {4,S} {5,S} {6,S}
2  *3 C 1 {1,S} {3,S} {7,S}
3     C 0 {2,S} {8,S} {9,S} {10,S}
4     H 0 {1,S}
5     H 0 {1,S}
6     H 0 {1,S}
7     H 0 {2,S}
8     H 0 {3,S}
9     H 0 {3,S}
10    H 0 {3,S}
""",
    kinetics = ArrheniusEP(
        A = (2.35e-06, 'cm^3/(mol*s)'),
        n = 4.84,
        alpha = 0,
        E0 = (4.27, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""MRH CBS-QB3 calculations w/o HR corrections""",
    longDesc = 
u"""
MRH CBS-QB3 calculations w/RRHO [MRHCBSQB3RRHO]_.

InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3 (external symmetry number = 1, spin multiplicity = 1)
 +
InChI=1/C3H7/c1-3-2/h3H,1-2H3 (external symmetry number = 1, spin multiplicity = 2)
 <=> (TS: external symmetry number = 1, spin multiplicity = 2)
InChI=1/C4H9O/c1-4(2)3-5/h5H,3H2,1-2H3 (external symmetry number = 1, spin multiplicity = 2)
 +
InChI=1/C3H8/c1-3-2/h3H2,1-2H3 (external symmetry number = 2, spin multiplicity = 1)

Tsang [Tsang1990]_ recommends k(T) = 1.51e-03 * (T/K)^4.2 * exp(-5.96 kcal/mol /RT) cm3 mol-1 s-1
for the reaction iso-C4H10 + iso-C3H7 = C3H8 + tert-C4H9.  The new rate coefficient expression is
in good agreement with this expression (within a factor of 3.5 over the valid temperature range).
""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1002,
    label = "S/H/NonDeC;C_rad/H2/Cd",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    H  0 {1,S}
4    Cd 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (400, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (5.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1003,
    label = "S/H/NonDeC;C_rad/H/CdCs",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cd 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (317, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (5.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1004,
    label = "S/H/NonDeC;C_rad/CdCs2",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cd 0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (58.6, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (5.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1005,
    label = "S/H/NonDeC;C_rad/H/CdCd",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cd 0 {1,S}
4    Cd 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (655, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (12.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1006,
    label = "S/H/NonDeC;C_rad/CdCdCs",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cd 0 {1,S}
3    Cd 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (34.8, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (12.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1007,
    label = "S/H/NonDeC;C_rad/H2/Ct",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    H  0 {1,S}
4    Ct 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (346, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (4.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1008,
    label = "S/H/NonDeC;C_rad/H/CtCs",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Ct 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (110, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (3.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1009,
    label = "S/H/NonDeC;C_rad/CtCs2",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Ct 0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (38.1, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (3.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1010,
    label = "S/H/NonDeC;C_rad/H/CtCt",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Ct 0 {1,S}
4    Ct 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (275, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (9.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1011,
    label = "S/H/NonDeC;C_rad/CtCtCs",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Ct 0 {1,S}
3    Ct 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (7.66, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (9.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1012,
    label = "S/H/NonDeC;Cb_rad",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 Cb       1 {2,B} {3,B}
2    {Cb,Cbf} 0 {1,B}
3    {Cb,Cbf} 0 {1,B}
""",
    kinetics = ArrheniusEP(
        A = (1070, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (-3.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1013,
    label = "S/H/NonDeC;C_rad/H2/Cb",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    H  0 {1,S}
4    Cb 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (249, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (2.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1014,
    label = "S/H/NonDeC;C_rad/H/CbCs",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cb 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (93.5, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (2.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1015,
    label = "S/H/NonDeC;C_rad/CbCs2",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cb 0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (6.51, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (1.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1016,
    label = "S/H/NonDeC;C_rad/H2/S",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    S 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (79, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (0.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1017,
    label = "S/H/NonDeC;C_rad/H/CsS",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (186, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (-0.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1018,
    label = "S/H/NonDeC;C_rad/Cs2S",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    S  0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (45.6, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (-1.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1019,
    label = "S/H/NonDeC;Cd_rad/NonDeS",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,D} {3,S}
2    C 0 {1,D}
3    S 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (21600, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (-1.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1020,
    label = "S/H/NonDeC;C_rad/H/CdS",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cd 0 {1,S}
4    S  0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (344, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (7.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1021,
    label = "S/H/NonDeC;C_rad/CdCsS",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cd 0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (63, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (7.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1022,
    label = "S/H/NonDeC;C_rad/H/CtS",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Ct 0 {1,S}
4    S  0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (226, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (6.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1023,
    label = "S/H/NonDeC;C_rad/CtCsS",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Ct 0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1060, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1024,
    label = "S/H/Cd;H_rad",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cd 0 {1,S}
""",
    group2 = 
"""
1 *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (44200, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (-1.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1025,
    label = "S/H/Cd;C_methyl",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cd 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (795, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (-0.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1026,
    label = "S/H/Cd;C_rad/H2/Cs",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cd 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    H  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (123, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (-1.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1027,
    label = "S/H/Cd;C_rad/H/NonDeC",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cd 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (150, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (-2.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1028,
    label = "S/H/Cd;C_rad/Cs3",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cd 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cs 0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (334, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (-3.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1029,
    label = "S/H/Cd;Cd_pri_rad",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cd 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,D} {3,S}
2    C 0 {1,D}
3    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (2100, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (-2.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1030,
    label = "S/H/Cd;Cd_rad/NonDeC",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cd 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,D} {3,S}
2    C  0 {1,D}
3    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1110, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (-3.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1031,
    label = "S/H/Cd;Cd_rad/Cd",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cd 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,D} {3,S}
2    C  0 {1,D}
3    Cd 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (747, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (1.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1032,
    label = "S/H/Cd;Cd_rad/Ct",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cd 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,D} {3,S}
2    C  0 {1,D}
3    Ct 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (118, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (-1.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1033,
    label = "S/H/Cd;C_rad/H2/Cd",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cd 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    H  0 {1,S}
4    Cd 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (549, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (5.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1034,
    label = "S/H/Cd;C_rad/H/CdCs",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cd 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cd 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (435, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (5.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1035,
    label = "S/H/Cd;C_rad/CdCs2",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cd 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cd 0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (80.4, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (4.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1036,
    label = "S/H/Cd;C_rad/H/CdCd",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cd 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cd 0 {1,S}
4    Cd 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (898, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (12.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1037,
    label = "S/H/Cd;C_rad/CdCdCs",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cd 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cd 0 {1,S}
3    Cd 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (47.7, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (12.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1038,
    label = "S/H/Cd;C_rad/H2/Ct",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cd 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    H  0 {1,S}
4    Ct 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (475, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (3.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1039,
    label = "S/H/Cd;C_rad/H/CtCs",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cd 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Ct 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (150, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (3.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1040,
    label = "S/H/Cd;C_rad/CtCs2",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cd 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Ct 0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (52.2, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (2.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1041,
    label = "S/H/Cd;C_rad/H/CtCt",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cd 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Ct 0 {1,S}
4    Ct 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (377, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (8.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1042,
    label = "S/H/Cd;C_rad/CtCtCs",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cd 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Ct 0 {1,S}
3    Ct 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (10.5, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (8.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1043,
    label = "S/H/Cd;Cb_rad",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cd 0 {1,S}
""",
    group2 = 
"""
1 *3 Cb       1 {2,B} {3,B}
2    {Cb,Cbf} 0 {1,B}
3    {Cb,Cbf} 0 {1,B}
""",
    kinetics = ArrheniusEP(
        A = (1460, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (-4.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1044,
    label = "S/H/Cd;C_rad/H2/Cb",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cd 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    H  0 {1,S}
4    Cb 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (341, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (2.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1045,
    label = "S/H/Cd;C_rad/H/CbCs",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cd 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cb 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (128, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (1.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1046,
    label = "S/H/Cd;C_rad/CbCs2",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cd 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cb 0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (8.93, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1047,
    label = "S/H/Cd;C_rad/H2/S",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cd 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    S 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (108, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1048,
    label = "S/H/Cd;C_rad/H/CsS",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cd 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (255, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (-1.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1049,
    label = "S/H/Cd;C_rad/Cs2S",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cd 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    S  0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (62.5, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (-2.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1050,
    label = "S/H/Cd;Cd_rad/NonDeS",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cd 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,D} {3,S}
2    C 0 {1,D}
3    S 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (29700, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (-2.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1051,
    label = "S/H/Cd;C_rad/H/CdS",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cd 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cd 0 {1,S}
4    S  0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (472, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (7.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1052,
    label = "S/H/Cd;C_rad/CdCsS",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cd 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cd 0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (86.4, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (6.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1053,
    label = "S/H/Cd;C_rad/H/CtS",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cd 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Ct 0 {1,S}
4    S  0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (309, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (6.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1054,
    label = "S/H/Cd;C_rad/CtCsS",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cd 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Ct 0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1460, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (6.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1055,
    label = "S/H/Ct;H_rad",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Ct 0 {1,S}
""",
    group2 = 
"""
1 *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (44800, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (-2.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1056,
    label = "S/H/Ct;C_methyl",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Ct 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (806, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (-1.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1057,
    label = "S/H/Ct;C_rad/H2/Cs",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Ct 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    H  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (125, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (-2.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1058,
    label = "S/H/Ct;C_rad/H/NonDeC",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Ct 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (152, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (-3.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1059,
    label = "S/H/Ct;C_rad/Cs3",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Ct 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cs 0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (339, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (-5.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1060,
    label = "S/H/Ct;Cd_pri_rad",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Ct 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,D} {3,S}
2    C 0 {1,D}
3    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (2130, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (-4.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1061,
    label = "S/H/Ct;Cd_rad/NonDeC",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Ct 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,D} {3,S}
2    C  0 {1,D}
3    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1130, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (-5.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1062,
    label = "S/H/Ct;Cd_rad/Cd",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Ct 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,D} {3,S}
2    C  0 {1,D}
3    Cd 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (758, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1063,
    label = "S/H/Ct;Cd_rad/Ct",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Ct 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,D} {3,S}
2    C  0 {1,D}
3    Ct 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (120, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (-2.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1064,
    label = "S/H/Ct;C_rad/H2/Cd",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Ct 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    H  0 {1,S}
4    Cd 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (557, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (3.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1065,
    label = "S/H/Ct;C_rad/H/CdCs",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Ct 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cd 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (441, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (3.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1066,
    label = "S/H/Ct;C_rad/CdCs2",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Ct 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cd 0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (81.5, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (3.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1067,
    label = "S/H/Ct;C_rad/H/CdCd",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Ct 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cd 0 {1,S}
4    Cd 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (911, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (10.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1068,
    label = "S/H/Ct;C_rad/CdCdCs",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Ct 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cd 0 {1,S}
3    Cd 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (48.4, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (10.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1069,
    label = "S/H/Ct;C_rad/H2/Ct",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Ct 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    H  0 {1,S}
4    Ct 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (482, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1070,
    label = "S/H/Ct;C_rad/H/CtCs",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Ct 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Ct 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (153, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (1.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1071,
    label = "S/H/Ct;C_rad/CtCs2",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Ct 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Ct 0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (53, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (1.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1072,
    label = "S/H/Ct;C_rad/H/CtCt",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Ct 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Ct 0 {1,S}
4    Ct 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (382, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (7.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1073,
    label = "S/H/Ct;C_rad/CtCtCs",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Ct 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Ct 0 {1,S}
3    Ct 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (10.7, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (7.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1074,
    label = "S/H/Ct;Cb_rad",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Ct 0 {1,S}
""",
    group2 = 
"""
1 *3 Cb       1 {2,B} {3,B}
2    {Cb,Cbf} 0 {1,B}
3    {Cb,Cbf} 0 {1,B}
""",
    kinetics = ArrheniusEP(
        A = (1490, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (-5.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1075,
    label = "S/H/Ct;C_rad/H2/Cb",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Ct 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    H  0 {1,S}
4    Cb 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (346, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (0.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1076,
    label = "S/H/Ct;C_rad/H/CbCs",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Ct 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cb 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (130, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (0.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1077,
    label = "S/H/Ct;C_rad/CbCs2",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Ct 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cb 0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (9.05, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (-0.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1078,
    label = "S/H/Ct;C_rad/H2/S",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Ct 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    S 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (110, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (-1.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1079,
    label = "S/H/Ct;C_rad/H/CsS",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Ct 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (259, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (-2.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1080,
    label = "S/H/Ct;C_rad/Cs2S",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Ct 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    S  0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (63.4, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (-3.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1081,
    label = "S/H/Ct;Cd_rad/NonDeS",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Ct 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,D} {3,S}
2    C 0 {1,D}
3    S 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (30100, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (-3.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1082,
    label = "S/H/Ct;C_rad/H/CdS",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Ct 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cd 0 {1,S}
4    S  0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (479, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (5.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1083,
    label = "S/H/Ct;C_rad/CdCsS",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Ct 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cd 0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (87.6, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (5.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1084,
    label = "S/H/Ct;C_rad/H/CtS",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Ct 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Ct 0 {1,S}
4    S  0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (314, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (4.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1085,
    label = "S/H/Ct;C_rad/CtCsS",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Ct 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Ct 0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1480, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (4.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1086,
    label = "S/H/Cb;H_rad",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cb 0 {1,S}
""",
    group2 = 
"""
1 *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (3640, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (-1.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1087,
    label = "S/H/Cb;C_methyl",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cb 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (65.4, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (-0.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1088,
    label = "S/H/Cb;C_rad/H2/Cs",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cb 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    H  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (10.1, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (-1.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1089,
    label = "S/H/Cb;C_rad/H/NonDeC",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cb 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (12.4, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (-2.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1090,
    label = "S/H/Cb;C_rad/Cs3",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cb 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cs 0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (27.5, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (-4.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1091,
    label = "S/H/Cb;Cd_pri_rad",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cb 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,D} {3,S}
2    C 0 {1,D}
3    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (173, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (-3.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1092,
    label = "S/H/Cb;Cd_rad/NonDeC",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cb 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,D} {3,S}
2    C  0 {1,D}
3    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (91.5, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (-4.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1093,
    label = "S/H/Cb;Cd_rad/Cd",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cb 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,D} {3,S}
2    C  0 {1,D}
3    Cd 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (61.5, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1094,
    label = "S/H/Cb;Cd_rad/Ct",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cb 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,D} {3,S}
2    C  0 {1,D}
3    Ct 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (9.71, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (-1.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1095,
    label = "S/H/Cb;C_rad/H2/Cd",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cb 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    H  0 {1,S}
4    Cd 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (45.2, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (4.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1096,
    label = "S/H/Cb;C_rad/H/CdCs",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cb 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cd 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (35.8, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (4.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1097,
    label = "S/H/Cb;C_rad/CdCs2",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cb 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cd 0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (6.62, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (4.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1098,
    label = "S/H/Cb;C_rad/H/CdCd",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cb 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cd 0 {1,S}
4    Cd 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (74, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (11.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1099,
    label = "S/H/Cb;C_rad/CdCdCs",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cb 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cd 0 {1,S}
3    Cd 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (3.93, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (11.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1100,
    label = "S/H/Cb;C_rad/H2/Ct",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cb 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    H  0 {1,S}
4    Ct 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (39.1, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1101,
    label = "S/H/Cb;C_rad/H/CtCs",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cb 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Ct 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (12.4, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (2.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1102,
    label = "S/H/Cb;C_rad/CtCs2",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cb 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Ct 0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (4.3, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (2.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1103,
    label = "S/H/Cb;C_rad/H/CtCt",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cb 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Ct 0 {1,S}
4    Ct 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (31, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (8.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1104,
    label = "S/H/Cb;C_rad/CtCtCs",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cb 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Ct 0 {1,S}
3    Ct 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.865, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (8.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1105,
    label = "S/H/Cb;Cb_rad",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cb 0 {1,S}
""",
    group2 = 
"""
1 *3 Cb       1 {2,B} {3,B}
2    {Cb,Cbf} 0 {1,B}
3    {Cb,Cbf} 0 {1,B}
""",
    kinetics = ArrheniusEP(
        A = (121, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (-4.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1106,
    label = "S/H/Cb;C_rad/H2/Cb",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cb 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    H  0 {1,S}
4    Cb 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (28.1, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (1.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1107,
    label = "S/H/Cb;C_rad/H/CbCs",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cb 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cb 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (10.6, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (1.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1108,
    label = "S/H/Cb;C_rad/CbCs2",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cb 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cb 0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.735, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (0.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1109,
    label = "S/H/Cb;C_rad/H2/S",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cb 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    S 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (8.92, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (-0.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1110,
    label = "S/H/Cb;C_rad/H/CsS",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cb 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (21, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (-1.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1111,
    label = "S/H/Cb;C_rad/Cs2S",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cb 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    S  0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (5.15, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (-2.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1112,
    label = "S/H/Cb;Cd_rad/NonDeS",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cb 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,D} {3,S}
2    C 0 {1,D}
3    S 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (2440, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (-2.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1113,
    label = "S/H/Cb;C_rad/H/CdS",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cb 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cd 0 {1,S}
4    S  0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (38.9, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (6.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1114,
    label = "S/H/Cb;C_rad/CdCsS",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cb 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cd 0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (7.11, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (6.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1115,
    label = "S/H/Cb;C_rad/H/CtS",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cb 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Ct 0 {1,S}
4    S  0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (25.5, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (5.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1116,
    label = "S/H/Cb;C_rad/CtCsS",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cb 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Ct 0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (120, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (5.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1117,
    label = "S/H/NonDeS;H_rad",
    group1 = 
"""
1 *1 S 0 {2,S} {3,S}
2 *2 H 0 {1,S}
3    S 0 {1,S}
""",
    group2 = 
"""
1 *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (48300, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (-2.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1118,
    label = "S/H/NonDeS;C_methyl",
    group1 = 
"""
1 *1 S 0 {2,S} {3,S}
2 *2 H 0 {1,S}
3    S 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (869, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (-1.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1119,
    label = "S/H/NonDeS;C_rad/H2/Cs",
    group1 = 
"""
1 *1 S 0 {2,S} {3,S}
2 *2 H 0 {1,S}
3    S 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    H  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (135, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (-2.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1120,
    label = "S/H/NonDeS;C_rad/H/NonDeC",
    group1 = 
"""
1 *1 S 0 {2,S} {3,S}
2 *2 H 0 {1,S}
3    S 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (164, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (-3.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1121,
    label = "S/H/NonDeS;C_rad/Cs3",
    group1 = 
"""
1 *1 S 0 {2,S} {3,S}
2 *2 H 0 {1,S}
3    S 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cs 0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (365, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (-5.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1122,
    label = "S/H/NonDeS;Cd_pri_rad",
    group1 = 
"""
1 *1 S 0 {2,S} {3,S}
2 *2 H 0 {1,S}
3    S 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,D} {3,S}
2    C 0 {1,D}
3    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (2300, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (-4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1123,
    label = "S/H/NonDeS;Cd_rad/NonDeC",
    group1 = 
"""
1 *1 S 0 {2,S} {3,S}
2 *2 H 0 {1,S}
3    S 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,D} {3,S}
2    C  0 {1,D}
3    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1210, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (-5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1124,
    label = "S/H/NonDeS;Cd_rad/Cd",
    group1 = 
"""
1 *1 S 0 {2,S} {3,S}
2 *2 H 0 {1,S}
3    S 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,D} {3,S}
2    C  0 {1,D}
3    Cd 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (817, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (0.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1125,
    label = "S/H/NonDeS;Cd_rad/Ct",
    group1 = 
"""
1 *1 S 0 {2,S} {3,S}
2 *2 H 0 {1,S}
3    S 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,D} {3,S}
2    C  0 {1,D}
3    Ct 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (129, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (-2.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1126,
    label = "S/H/NonDeS;C_rad/H2/Cd",
    group1 = 
"""
1 *1 S 0 {2,S} {3,S}
2 *2 H 0 {1,S}
3    S 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    H  0 {1,S}
4    Cd 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (600, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (3.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1127,
    label = "S/H/NonDeS;C_rad/H/CdCs",
    group1 = 
"""
1 *1 S 0 {2,S} {3,S}
2 *2 H 0 {1,S}
3    S 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cd 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (475, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (3.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1128,
    label = "S/H/NonDeS;C_rad/CdCs2",
    group1 = 
"""
1 *1 S 0 {2,S} {3,S}
2 *2 H 0 {1,S}
3    S 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cd 0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (87.9, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (3.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1129,
    label = "S/H/NonDeS;C_rad/H/CdCd",
    group1 = 
"""
1 *1 S 0 {2,S} {3,S}
2 *2 H 0 {1,S}
3    S 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cd 0 {1,S}
4    Cd 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (982, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (10.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1130,
    label = "S/H/NonDeS;C_rad/CdCdCs",
    group1 = 
"""
1 *1 S 0 {2,S} {3,S}
2 *2 H 0 {1,S}
3    S 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cd 0 {1,S}
3    Cd 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (52.2, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (10.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1131,
    label = "S/H/NonDeS;C_rad/H2/Ct",
    group1 = 
"""
1 *1 S 0 {2,S} {3,S}
2 *2 H 0 {1,S}
3    S 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    H  0 {1,S}
4    Ct 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (519, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (2.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1132,
    label = "S/H/NonDeS;C_rad/H/CtCs",
    group1 = 
"""
1 *1 S 0 {2,S} {3,S}
2 *2 H 0 {1,S}
3    S 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Ct 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (164, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (1.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1133,
    label = "S/H/NonDeS;C_rad/CtCs2",
    group1 = 
"""
1 *1 S 0 {2,S} {3,S}
2 *2 H 0 {1,S}
3    S 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Ct 0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (57.1, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (1.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1134,
    label = "S/H/NonDeS;C_rad/H/CtCt",
    group1 = 
"""
1 *1 S 0 {2,S} {3,S}
2 *2 H 0 {1,S}
3    S 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Ct 0 {1,S}
4    Ct 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (412, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (7.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1135,
    label = "S/H/NonDeS;C_rad/CtCtCs",
    group1 = 
"""
1 *1 S 0 {2,S} {3,S}
2 *2 H 0 {1,S}
3    S 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Ct 0 {1,S}
3    Ct 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (11.5, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (7.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1136,
    label = "S/H/NonDeS;Cb_rad",
    group1 = 
"""
1 *1 S 0 {2,S} {3,S}
2 *2 H 0 {1,S}
3    S 0 {1,S}
""",
    group2 = 
"""
1 *3 Cb       1 {2,B} {3,B}
2    {Cb,Cbf} 0 {1,B}
3    {Cb,Cbf} 0 {1,B}
""",
    kinetics = ArrheniusEP(
        A = (1600, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (-5.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1137,
    label = "S/H/NonDeS;C_rad/H2/Cb",
    group1 = 
"""
1 *1 S 0 {2,S} {3,S}
2 *2 H 0 {1,S}
3    S 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    H  0 {1,S}
4    Cb 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (373, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (0.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1138,
    label = "S/H/NonDeS;C_rad/H/CbCs",
    group1 = 
"""
1 *1 S 0 {2,S} {3,S}
2 *2 H 0 {1,S}
3    S 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cb 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (140, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (0.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1139,
    label = "S/H/NonDeS;C_rad/CbCs2",
    group1 = 
"""
1 *1 S 0 {2,S} {3,S}
2 *2 H 0 {1,S}
3    S 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cb 0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (9.76, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (-0.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1140,
    label = "S/H/NonDeS;C_rad/H2/S",
    group1 = 
"""
1 *1 S 0 {2,S} {3,S}
2 *2 H 0 {1,S}
3    S 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    S 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (118, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (-1.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1141,
    label = "S/H/NonDeS;C_rad/H/CsS",
    group1 = 
"""
1 *1 S 0 {2,S} {3,S}
2 *2 H 0 {1,S}
3    S 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (279, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (-2.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1142,
    label = "S/H/NonDeS;C_rad/Cs2S",
    group1 = 
"""
1 *1 S 0 {2,S} {3,S}
2 *2 H 0 {1,S}
3    S 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    S  0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (68.3, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (-3.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1143,
    label = "S/H/NonDeS;Cd_rad/NonDeS",
    group1 = 
"""
1 *1 S 0 {2,S} {3,S}
2 *2 H 0 {1,S}
3    S 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,D} {3,S}
2    C 0 {1,D}
3    S 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (32400, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (-3.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1144,
    label = "S/H/NonDeS;C_rad/H/CdS",
    group1 = 
"""
1 *1 S 0 {2,S} {3,S}
2 *2 H 0 {1,S}
3    S 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cd 0 {1,S}
4    S  0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (517, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (5.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1145,
    label = "S/H/NonDeS;C_rad/CdCsS",
    group1 = 
"""
1 *1 S 0 {2,S} {3,S}
2 *2 H 0 {1,S}
3    S 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cd 0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (94.4, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (5.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1146,
    label = "S/H/NonDeS;C_rad/H/CtS",
    group1 = 
"""
1 *1 S 0 {2,S} {3,S}
2 *2 H 0 {1,S}
3    S 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Ct 0 {1,S}
4    S  0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (338, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (4.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1147,
    label = "S/H/NonDeS;C_rad/CtCsS",
    group1 = 
"""
1 *1 S 0 {2,S} {3,S}
2 *2 H 0 {1,S}
3    S 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Ct 0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1590, 'cm^3/(mol*s)'),
        n = 2.98,
        alpha = 0,
        E0 = (5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1148,
    label = "S_pri;S_pri_rad",
    group1 = 
"""
1 *1 S 0 {2,S} {3,S}
2 *2 H 0 {1,S}
3    H 0 {1,S}
""",
    group2 = 
"""
1 *3 S 1 {2,S}
2    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1530, 'cm^3/(mol*s)'),
        n = 3.17,
        alpha = 0,
        E0 = (2.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1149,
    label = "S_pri;S_rad/NonDeC",
    group1 = 
"""
1 *1 S 0 {2,S} {3,S}
2 *2 H 0 {1,S}
3    H 0 {1,S}
""",
    group2 = 
"""
1 *3 S  1 {2,S}
2    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (790, 'cm^3/(mol*s)'),
        n = 3.17,
        alpha = 0,
        E0 = (4.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1150,
    label = "S_pri;S_rad/Cd",
    group1 = 
"""
1 *1 S 0 {2,S} {3,S}
2 *2 H 0 {1,S}
3    H 0 {1,S}
""",
    group2 = 
"""
1 *3 S  1 {2,S}
2    Cd 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (312, 'cm^3/(mol*s)'),
        n = 3.17,
        alpha = 0,
        E0 = (0.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1151,
    label = "S_pri;S_rad/Ct",
    group1 = 
"""
1 *1 S 0 {2,S} {3,S}
2 *2 H 0 {1,S}
3    H 0 {1,S}
""",
    group2 = 
"""
1 *3 S  1 {2,S}
2    Ct 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (901, 'cm^3/(mol*s)'),
        n = 3.17,
        alpha = 0,
        E0 = (12.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1152,
    label = "S_pri;S_rad/Cb",
    group1 = 
"""
1 *1 S 0 {2,S} {3,S}
2 *2 H 0 {1,S}
3    H 0 {1,S}
""",
    group2 = 
"""
1 *3 S  1 {2,S}
2    Cb 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (227, 'cm^3/(mol*s)'),
        n = 3.17,
        alpha = 0,
        E0 = (2.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1153,
    label = "S_pri;S_rad/NonDeS",
    group1 = 
"""
1 *1 S 0 {2,S} {3,S}
2 *2 H 0 {1,S}
3    H 0 {1,S}
""",
    group2 = 
"""
1 *3 S 1 {2,S}
2    S 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (164, 'cm^3/(mol*s)'),
        n = 3.17,
        alpha = 0,
        E0 = (3.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1154,
    label = "S/H/NonDeC;S_pri_rad",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 S 1 {2,S}
2    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1490, 'cm^3/(mol*s)'),
        n = 3.17,
        alpha = 0,
        E0 = (-0.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1155,
    label = "S/H/NonDeC;S_rad/NonDeC",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 S  1 {2,S}
2    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (768, 'cm^3/(mol*s)'),
        n = 3.17,
        alpha = 0,
        E0 = (1.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1156,
    label = "S/H/NonDeC;S_rad/Cd",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 S  1 {2,S}
2    Cd 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (304, 'cm^3/(mol*s)'),
        n = 3.17,
        alpha = 0,
        E0 = (-2.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1157,
    label = "S/H/NonDeC;S_rad/Ct",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 S  1 {2,S}
2    Ct 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (876, 'cm^3/(mol*s)'),
        n = 3.17,
        alpha = 0,
        E0 = (9.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1158,
    label = "S/H/NonDeC;S_rad/Cb",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 S  1 {2,S}
2    Cb 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (220, 'cm^3/(mol*s)'),
        n = 3.17,
        alpha = 0,
        E0 = (-0.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1159,
    label = "S/H/NonDeC;S_rad/NonDeS",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 S 1 {2,S}
2    S 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (159, 'cm^3/(mol*s)'),
        n = 3.17,
        alpha = 0,
        E0 = (0.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1160,
    label = "S/H/Cd;S_pri_rad",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cd 0 {1,S}
""",
    group2 = 
"""
1 *3 S 1 {2,S}
2    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1560, 'cm^3/(mol*s)'),
        n = 3.17,
        alpha = 0,
        E0 = (-3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1161,
    label = "S/H/Cd;S_rad/NonDeC",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cd 0 {1,S}
""",
    group2 = 
"""
1 *3 S  1 {2,S}
2    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (801, 'cm^3/(mol*s)'),
        n = 3.17,
        alpha = 0,
        E0 = (-0.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1162,
    label = "S/H/Cd;S_rad/Cd",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cd 0 {1,S}
""",
    group2 = 
"""
1 *3 S  1 {2,S}
2    Cd 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (317, 'cm^3/(mol*s)'),
        n = 3.17,
        alpha = 0,
        E0 = (-4.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1163,
    label = "S/H/Cd;S_rad/Ct",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cd 0 {1,S}
""",
    group2 = 
"""
1 *3 S  1 {2,S}
2    Ct 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (914, 'cm^3/(mol*s)'),
        n = 3.17,
        alpha = 0,
        E0 = (7.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1164,
    label = "S/H/Cd;S_rad/Cb",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cd 0 {1,S}
""",
    group2 = 
"""
1 *3 S  1 {2,S}
2    Cb 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (230, 'cm^3/(mol*s)'),
        n = 3.17,
        alpha = 0,
        E0 = (-2.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1165,
    label = "S/H/Cd;S_rad/NonDeS",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cd 0 {1,S}
""",
    group2 = 
"""
1 *3 S 1 {2,S}
2    S 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (166, 'cm^3/(mol*s)'),
        n = 3.17,
        alpha = 0,
        E0 = (-1.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1166,
    label = "S/H/Ct;S_pri_rad",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Ct 0 {1,S}
""",
    group2 = 
"""
1 *3 S 1 {2,S}
2    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (595, 'cm^3/(mol*s)'),
        n = 3.17,
        alpha = 0,
        E0 = (-3.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1167,
    label = "S/H/Ct;S_rad/NonDeC",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Ct 0 {1,S}
""",
    group2 = 
"""
1 *3 S  1 {2,S}
2    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (306, 'cm^3/(mol*s)'),
        n = 3.17,
        alpha = 0,
        E0 = (-0.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1168,
    label = "S/H/Ct;S_rad/Cd",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Ct 0 {1,S}
""",
    group2 = 
"""
1 *3 S  1 {2,S}
2    Cd 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (121, 'cm^3/(mol*s)'),
        n = 3.17,
        alpha = 0,
        E0 = (-5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1169,
    label = "S/H/Ct;S_rad/Ct",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Ct 0 {1,S}
""",
    group2 = 
"""
1 *3 S  1 {2,S}
2    Ct 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (349, 'cm^3/(mol*s)'),
        n = 3.17,
        alpha = 0,
        E0 = (7.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1170,
    label = "S/H/Ct;S_rad/Cb",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Ct 0 {1,S}
""",
    group2 = 
"""
1 *3 S  1 {2,S}
2    Cb 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (87.8, 'cm^3/(mol*s)'),
        n = 3.17,
        alpha = 0,
        E0 = (-2.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1171,
    label = "S/H/Ct;S_rad/NonDeS",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Ct 0 {1,S}
""",
    group2 = 
"""
1 *3 S 1 {2,S}
2    S 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (63.5, 'cm^3/(mol*s)'),
        n = 3.17,
        alpha = 0,
        E0 = (-2.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1172,
    label = "S/H/Cb;S_pri_rad",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cb 0 {1,S}
""",
    group2 = 
"""
1 *3 S 1 {2,S}
2    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (428, 'cm^3/(mol*s)'),
        n = 3.17,
        alpha = 0,
        E0 = (-2.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1173,
    label = "S/H/Cb;S_rad/NonDeC",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cb 0 {1,S}
""",
    group2 = 
"""
1 *3 S  1 {2,S}
2    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (220, 'cm^3/(mol*s)'),
        n = 3.17,
        alpha = 0,
        E0 = (-0.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1174,
    label = "S/H/Cb;S_rad/Cd",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cb 0 {1,S}
""",
    group2 = 
"""
1 *3 S  1 {2,S}
2    Cd 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (87.2, 'cm^3/(mol*s)'),
        n = 3.17,
        alpha = 0,
        E0 = (-4.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1175,
    label = "S/H/Cb;S_rad/Ct",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cb 0 {1,S}
""",
    group2 = 
"""
1 *3 S  1 {2,S}
2    Ct 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (251, 'cm^3/(mol*s)'),
        n = 3.17,
        alpha = 0,
        E0 = (7.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1176,
    label = "S/H/Cb;S_rad/Cb",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cb 0 {1,S}
""",
    group2 = 
"""
1 *3 S  1 {2,S}
2    Cb 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (63.2, 'cm^3/(mol*s)'),
        n = 3.17,
        alpha = 0,
        E0 = (-2.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1177,
    label = "S/H/Cb;S_rad/NonDeS",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cb 0 {1,S}
""",
    group2 = 
"""
1 *3 S 1 {2,S}
2    S 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (45.7, 'cm^3/(mol*s)'),
        n = 3.17,
        alpha = 0,
        E0 = (-1.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1178,
    label = "S/H/NonDeS;S_pri_rad",
    group1 = 
"""
1 *1 S 0 {2,S} {3,S}
2 *2 H 0 {1,S}
3    S 0 {1,S}
""",
    group2 = 
"""
1 *3 S 1 {2,S}
2    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (309, 'cm^3/(mol*s)'),
        n = 3.17,
        alpha = 0,
        E0 = (-1.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1179,
    label = "S/H/NonDeS;S_rad/NonDeC",
    group1 = 
"""
1 *1 S 0 {2,S} {3,S}
2 *2 H 0 {1,S}
3    S 0 {1,S}
""",
    group2 = 
"""
1 *3 S  1 {2,S}
2    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (159, 'cm^3/(mol*s)'),
        n = 3.17,
        alpha = 0,
        E0 = (0.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1180,
    label = "S/H/NonDeS;S_rad/Cd",
    group1 = 
"""
1 *1 S 0 {2,S} {3,S}
2 *2 H 0 {1,S}
3    S 0 {1,S}
""",
    group2 = 
"""
1 *3 S  1 {2,S}
2    Cd 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (63, 'cm^3/(mol*s)'),
        n = 3.17,
        alpha = 0,
        E0 = (-3.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1181,
    label = "S/H/NonDeS;S_rad/Ct",
    group1 = 
"""
1 *1 S 0 {2,S} {3,S}
2 *2 H 0 {1,S}
3    S 0 {1,S}
""",
    group2 = 
"""
1 *3 S  1 {2,S}
2    Ct 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (182, 'cm^3/(mol*s)'),
        n = 3.17,
        alpha = 0,
        E0 = (8.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1182,
    label = "S/H/NonDeS;S_rad/Cb",
    group1 = 
"""
1 *1 S 0 {2,S} {3,S}
2 *2 H 0 {1,S}
3    S 0 {1,S}
""",
    group2 = 
"""
1 *3 S  1 {2,S}
2    Cb 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (45.7, 'cm^3/(mol*s)'),
        n = 3.17,
        alpha = 0,
        E0 = (-1.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1183,
    label = "S/H/NonDeS;S_rad/NonDeS",
    group1 = 
"""
1 *1 S 0 {2,S} {3,S}
2 *2 H 0 {1,S}
3    S 0 {1,S}
""",
    group2 = 
"""
1 *3 S 1 {2,S}
2    S 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (33, 'cm^3/(mol*s)'),
        n = 3.17,
        alpha = 0,
        E0 = (-0.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1184,
    label = "S/H/NonDeC;CS_pri_rad",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,D} {3,S}
2    S 0 {1,D}
3    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (395, 'cm^3/(mol*s)'),
        n = 3.17,
        alpha = 0,
        E0 = (0.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1185,
    label = "CS_pri;C_methyl",
    group1 = 
"""
1 *1 C 0 {2,D} {3,S} {4,S}
2    S 0 {1,D}
3 *2 H 0 {1,S}
4    H 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (83200, 'cm^3/(mol*s)'),
        n = 2.3,
        alpha = 0,
        E0 = (-0.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1192,
    label = "S_pri;O_pri_rad",
    group1 = 
"""
1 *1 S 0 {2,S} {3,S}
2 *2 H 0 {1,S}
3    H 0 {1,S}
""",
    group2 = 
"""
1 *3 O 1 {2,S}
2    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (23300, 'cm^3/(mol*s)'),
        n = 2.61,
        alpha = 0,
        E0 = (11.35, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""CAC calculation CBS-QB3 1dhr""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1193,
    label = "S/H/NonDeC;O_pri_rad",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 O 1 {2,S}
2    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (3490, 'cm^3/(mol*s)'),
        n = 3.13,
        alpha = 0,
        E0 = (-1.73, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""CAC calculation CBS-QB3 1dhr""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1194,
    label = "S/H/NonDeC;O_rad/NonDeC",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 O  1 {2,S}
2    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (28400, 'cm^3/(mol*s)'),
        n = 2.79,
        alpha = 0,
        E0 = (2.64, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""CAC calculation CBS-QB3 1dhr""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1195,
    label = "S_pri;O_rad/OneDe",
    group1 = 
"""
1 *1 S 0 {2,S} {3,S}
2 *2 H 0 {1,S}
3    H 0 {1,S}
""",
    group2 = 
"""
1 *3 O                1 {2,S}
2    {Cd,Ct,Cb,CO,CS} 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (641, 'cm^3/(mol*s)'),
        n = 2.6,
        alpha = 0,
        E0 = (-8.23, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""CAC calculation CBS-QB3 *HO approx*""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1196,
    label = "C/H2/CsS;CO_rad/NonDe",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    S  0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C        1 {2,D} {3,S}
2    O        0 {1,D}
3    {Cs,O,S} 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (14.1, 'cm^3/(mol*s)'),
        n = 3.53,
        alpha = 0,
        E0 = (13.23, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""CAC calculation CBS-QB3 1dhr""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1197,
    label = "C/H/CsOS;Cs_rad",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    O  0 {1,S}
4    S  0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    R 0 {1,S}
3    R 0 {1,S}
4    R 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00668, 'cm^3/(mol*s)'),
        n = 4.12,
        alpha = 0,
        E0 = (2.94, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""CAC calculation CBS-QB3 1dhr""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1198,
    label = "S/H/CO;Cs_rad",
    group1 = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    CO 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    R 0 {1,S}
3    R 0 {1,S}
4    R 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (58300, 'cm^3/(mol*s)'),
        n = 1.97,
        alpha = 0,
        E0 = (-0.83, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""CAC calculation CBS-QB3 1dhr""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1199,
    label = "C/H/CsOS;S_pri_rad",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    O  0 {1,S}
4    S  0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 S 1 {2,S}
2    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (2890, 'cm^3/(mol*s)'),
        n = 2.95,
        alpha = 0,
        E0 = (0.04, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""CAC calculation CBS-QB3 1dhr (py)""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jan  9 11:01:40 2013","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 2000,
    label = "C_pri;N3s_rad/H2",
    group1 = 
"""
1 *1 C   0 {2,S} {3,S} {4,S} {5,S}
2 *2 H   0 {1,S}
3    H   0 {1,S}
4    H   0 {1,S}
5    R!H 0 {1,S}
""",
    group2 = 
"""
1 *3 N3s 1 {2,S} {3,S}
2    H   0 {1,S}
3    H   0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (920000, 'cm^3/(mol*s)'),
        n = 1.94,
        alpha = 0.23,
        E0 = (8.920, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli",
    longDesc = 
u"""

""",
    history = [
        (""),
    ],
)

entry(
    index = 2001,
    label = "C_sec;N3s_rad/H2",
    group1 = 
"""
1 *1 C   0 {2,S} {3,S} {4,S} {5,S}
2 *2 H   0 {1,S}
3    H   0 {1,S}
4    R!H 0 {1,S}
5    R!H 0 {1,S}
""",
    group2 = 
"""
1 *3 N3s 1 {2,S} {3,S}
2    H   0 {1,S}
3    H   0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (920000, 'cm^3/(mol*s)'),
        n = 1.94,
        alpha = 0.23,
        E0 = (8.920, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"Dean and Bozzelli chapter 2, estimation same as C_pri;N3s_rad/H2",
    longDesc = 
u"""

""",
    history = [
        (""),
    ],
)

entry(
    index = 2002,
    label = "C_ter;N3s_rad/H2",
    group1 = 
"""
1 *1 C   0 {2,S} {3,S} {4,S} {5,S}
2 *2 H   0 {1,S}
3    R!H 0 {1,S}
4    R!H 0 {1,S}
5    R!H 0 {1,S}
""",
    group2 = 
"""
1 *3 N3s 1 {2,S} {3,S}
2    H   0 {1,S}
3    H   0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (920000, 'cm^3/(mol*s)'),
        n = 1.94,
        alpha = 0.23,
        E0 = (8.920, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"Dean and Bozzelli chapter 2, estimation same as C_pri;N3s_rad/H2",
    longDesc = 
u"""

""",
    history = [
        (""),
    ],
)

entry(
    index = 2003,
    label = "N3s_H;H_rad",
    group1 = 
"""
1 *1 N3s 0 {2,S} {3,S} {4,S}
2 *2 H   0 {1,S}
3    R   0 {1,S}
4    R   0 {1,S}
""",
    group2 = 
"""
1 *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (240000000, 'cm^3/(mol*s)'),
        n = 1.5,
        alpha = 0.21,
        E0 = (10.402, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli",
    longDesc = 
u"""

""",
    history = [
        (""),
    ],
)

entry(
    index = 2004,
    label = "N3s_H;O_atom_triplet",
    group1 = 
"""
1 *1 N3s 0 {2,S} {3,S} {4,S}
2 *2 H   0 {1,S}
3    R   0 {1,S}
4    R   0 {1,S}
""",
    group2 = 
"""
1 *3 O 2T
""",
    kinetics = ArrheniusEP(
        A = (170000000, 'cm^3/(mol*s)'),
        n = 1.5,
        alpha = 0.15,
        E0 = (6.544, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli",
    longDesc = 
u"""

""",
    history = [
        (""),
    ],
)

entry(
    index = 2005,
    label = "N3s_H;O_pri_rad",
    group1 = 
"""
1 *1 N3s 0 {2,S} {3,S} {4,S}
2 *2 H   0 {1,S}
3    R   0 {1,S}
4    R   0 {1,S}
""",
    group2 = 
"""
1 *3 O 1 {2,S}
2    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1200000, 'cm^3/(mol*s)'),
        n = 2.0,
        alpha = 0.05,
        E0 = (1.329, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli",
    longDesc = 
u"""

""",
    history = [
        (""),
    ],
)

entry(
    index = 2006,
    label = "N3s_H;C_methyl",
    group1 = 
"""
1 *1 N3s 0 {2,S} {3,S} {4,S}
2 *2 H   0 {1,S}
3    R   0 {1,S}
4    R   0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (810000, 'cm^3/(mol*s)'),
        n = 1.87,
        alpha = 0.15,
        E0 = (9.420, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli",
    longDesc = 
u"""

""",
    history = [
        (""),
    ],
)

entry(
    index = 2007,
    label = "C/H3/Cs;InChI=1S/NO3/c2-1(3)4",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 Os  1 {2,S}
2    N4d 0 {1,S} {3,D} {4,S}
3    Od  0 {2,D}
4    Os  0 {2,S}
""",
    kinetics = ArrheniusEP(
        A = (2.03e-12, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (8.31, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 1,
    shortDesc = u"Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli",
    longDesc = 
u"""

""",
    history = [
        (""),
    ],
)

entry(
    index = 2008,
    label = "CsXX;InChI=1S/NO3/c2-1(3)4",
    group1 = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    Ct 0 {1,S}
""",
    group2 = 
"""
1 *3 Os  1 {2,S}
2    N4d 0 {1,S} {3,D} {4,S}
3    Od  0 {2,D}
4    Os  0 {2,S}
""",
    kinetics = ArrheniusEP(
        A = (810000, 'cm^3/(mol*s)'),
        n = 1.87,
        alpha = 0.15,
        E0 = (9.420, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 1,
    shortDesc = u"Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli",
    longDesc = 
u"""

""",
    history = [
        (""),
    ],
)




