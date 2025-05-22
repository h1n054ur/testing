COUNTRY_DATA = {
    'US': {
        'name': 'United States',
        'number_types': {
            'local': 1.15,
            'mobile': 1.15,
            'tollfree': 2.15,
        },
        'tollfree_prefixes': [800, 833, 844, 855, 866, 877, 888],
        'regions': {
            "Alabama": {"code": "AL", "area_codes": [205, 251, 256, 334, 938]},
            "Alaska": {"code": "AK", "area_codes": [907]},
            "Arizona": {"code": "AZ", "area_codes": [480, 520, 602, 623, 928]},
            "Arkansas": {"code": "AR", "area_codes": [479, 501, 870]},
            "California": {"code": "CA", "area_codes": [209, 213, 310, 415, 510, 530, 559, 619, 626, 650, 661, 707, 714, 805, 818, 858, 909, 916, 925, 949]},
            "Colorado": {"code": "CO", "area_codes": [303, 719, 720, 970]},
            "Connecticut": {"code": "CT", "area_codes": [203, 475, 860, 959]},
            "Delaware": {"code": "DE", "area_codes": [302]},
            "Florida": {"code": "FL", "area_codes": [305, 321, 352, 386, 407, 561, 727, 754, 772, 786, 813, 850, 863, 904, 941, 954]},
            "Georgia": {"code": "GA", "area_codes": [229, 404, 470, 478, 678, 706, 762, 770, 912]},
            "Hawaii": {"code": "HI", "area_codes": [808]},
            "Idaho": {"code": "ID", "area_codes": [208, 986]},
            "Illinois": {"code": "IL", "area_codes": [217, 224, 309, 312, 331, 618, 630, 708, 773, 779, 815, 847]},
            "Indiana": {"code": "IN", "area_codes": [219, 260, 317, 463, 574, 765, 812, 930]},
            "Iowa": {"code": "IA", "area_codes": [319, 515, 563, 641, 712]},
            "Kansas": {"code": "KS", "area_codes": [316, 620, 785, 913]},
            "Kentucky": {"code": "KY", "area_codes": [270, 364, 502, 606, 859]},
            "Louisiana": {"code": "LA", "area_codes": [225, 318, 337, 504, 985]},
            "Maine": {"code": "ME", "area_codes": [207]},
            "Maryland": {"code": "MD", "area_codes": [240, 301, 410, 443, 667]},
            "Massachusetts": {"code": "MA", "area_codes": [339, 351, 413, 508, 617, 774, 781, 857, 978]},
            "Michigan": {"code": "MI", "area_codes": [231, 248, 269, 313, 517, 586, 616, 734, 810, 906, 947, 989]},
            "Minnesota": {"code": "MN", "area_codes": [218, 320, 507, 612, 651, 763, 952]},
            "Mississippi": {"code": "MS", "area_codes": [228, 601, 662, 769]},
            "Missouri": {"code": "MO", "area_codes": [314, 417, 573, 636, 660, 816, 975]},
            "Montana": {"code": "MT", "area_codes": [406]},
            "Nebraska": {"code": "NE", "area_codes": [308, 402, 531]},
            "Nevada": {"code": "NV", "area_codes": [702, 725, 775]},
            "New Hampshire": {"code": "NH", "area_codes": [603]},
            "New Jersey": {"code": "NJ", "area_codes": [201, 551, 609, 732, 848, 856, 862, 908, 973]},
            "New Mexico": {"code": "NM", "area_codes": [505, 575]},
            "New York": {"code": "NY", "area_codes": [212, 315, 332, 347, 516, 518, 585, 607, 631, 646, 680, 716, 718, 838, 845, 914, 917, 929]},
            "North Carolina": {"code": "NC", "area_codes": [252, 336, 704, 743, 828, 910, 919, 980, 984]},
            "North Dakota": {"code": "ND", "area_codes": [701]},
            "Ohio": {"code": "OH", "area_codes": [216, 220, 234, 283, 330, 380, 419, 440, 513, 567, 614, 740, 937]},
            "Oklahoma": {"code": "OK", "area_codes": [405, 539, 580, 918]},
            "Oregon": {"code": "OR", "area_codes": [458, 503, 541, 971]},
            "Pennsylvania": {"code": "PA", "area_codes": [215, 223, 267, 272, 412, 445, 484, 570, 582, 610, 717, 724, 814, 878]},
            "Rhode Island": {"code": "RI", "area_codes": [401]},
            "South Carolina": {"code": "SC", "area_codes": [803, 839, 843, 854, 864]},
            "South Dakota": {"code": "SD", "area_codes": [605]},
            "Tennessee": {"code": "TN", "area_codes": [423, 615, 629, 731, 865, 901, 931]},
            "Texas": {"code": "TX", "area_codes": [210, 214, 254, 281, 325, 346, 361, 409, 430, 432, 469, 512, 682, 713, 737, 806, 817, 830, 832, 903, 915, 936, 940, 956, 972, 979]},
            "Utah": {"code": "UT", "area_codes": [385, 435, 801]},
            "Vermont": {"code": "VT", "area_codes": [802]},
            "Virginia": {"code": "VA", "area_codes": [276, 434, 540, 571, 703, 757, 804]},
            "Washington": {"code": "WA", "area_codes": [206, 253, 360, 425, 509]},
            "West Virginia": {"code": "WV", "area_codes": [304, 681]},
            "Wisconsin": {"code": "WI", "area_codes": [262, 274, 414, 534, 608, 715, 920]},
            "Wyoming": {"code": "WY", "area_codes": [307]},
            "Washington DC": {"code": "DC", "area_codes": [202]},
            "Any region (Country-wide)": {"code": None, "area_codes": []}
        }
    },
    'CA': {
        'name': 'Canada',
        'number_types': {
            'local': 1.15,
            'tollfree': 2.15,
        },
        'tollfree_prefixes': [800, 833, 844, 855, 866, 877, 888],
        'regions': {
            "British Columbia": {"code": "BC", "area_codes": [236, 250, 604, 672, 778]},
            "Alberta": {"code": "AB", "area_codes": [403, 587, 780, 825, 368]},
            "Ontario": {"code": "ON", "area_codes": [226, 289, 343, 416, 519, 613, 647, 705, 807, 905]},
            "Quebec": {"code": "QC", "area_codes": [367, 418, 438, 450, 514, 579, 581, 819, 873]},
            "Yukon": {"code": "YT", "area_codes": [867]},
            "Any region (Country-wide)": {"code": None, "area_codes": []}
        }
    },
    'GB': {
        'name': 'United Kingdom',
        'number_types': {
            'local': 1.15,
            'mobile': 1.15,
            'tollfree': 2.15,
        },
        'tollfree_prefixes': [800, 808],
        'regions': {
            "England": {
                "code": "ENG",
                "area_codes": [
                    20, 23, 24, 113, 114, 115, 116, 117, 118, 121, 151, 161, 191,
                    (1200, 1299), (1300, 1399), (1400, 1499), (1500, 1599), (1600, 1699),
                    (1700, 1799), (1800, 1899), (1900, 1999)
                ]
            },
            "Scotland": {
                "code": "SCT",
                "area_codes": [
                    131, 141, 1224, 1382, 1463, 1506, 1556, 1653, 1738, 1786
                ]
            },
            "Wales": {
                "code": "WLS",
                "area_codes": [
                    29, 1745, 1248, 1559, 1970, 1654, 1570, 1437, 1492, 1554,
                    1600, 1656, 1686, 1691, 1689, 1832, 1833, 1837, 1974, 1978, 1992
                ]
            },
            "Northern Ireland": {
                "code": "NIR",
                "area_codes": [
                    28
                ]
            },
            "Any region (nation‑wide)": {"code": None, "area_codes": []}
        }
    },
    'AU': {
        'name': 'Australia',
        'number_types': {
            'local': 3.00,
            'mobile': 6.50,
            'tollfree': 16.00,
        },
        'tollfree_prefixes': [1800],
        'regions': {
            "New South Wales": {"code": "New South Wales", "area_codes": [612]},
            "Victoria": {"code": "Victoria", "area_codes": [613]},
            "Queensland": {"code": "Queensland", "area_codes": [617]},
            "South Australia": {"code": "South Australia", "area_codes": [618]},
            "Western Australia": {"code": "Western Australia", "area_codes": [618]},
            "Tasmania": {"code": "Tasmania", "area_codes": [613]},
            "Australian Capital Territory": {"code": "New South Wales", "area_codes": [612]},
            "Northern Territory": {"code": "South Australia", "area_codes": [618]},
            "Any region (Country-wide)": {"code": None, "area_codes": []}
        }
    },
    
    'AR': {
        'name': 'Argentina',
        'number_types': {
            'local': 8.0,
            'tollfree': 25.0,
            'mobile': None,
            'national': None,
        },
        'tollfree_prefixes': [800],
        'regions': {
        "Buenos Aires": {"code": None, "area_codes": [11]},
        "Córdoba": {"code": None, "area_codes": [351]},
        "San Juan": {"code": None, "area_codes": [264]},
        "San Luis": {"code": None, "area_codes": [266]},
        "Santa Fe": {"code": None, "area_codes": [342]},
        "Any region (Country-wide)": {"code": None, "area_codes": []}
    }
},
'AT': {
    'name': 'Austria',
    'number_types': {
        'local': 1.0,
        'mobile': 6.0,
        'national': 1.0,
        'tollfree': 25.0,
    },
    'tollfree_prefixes': [800],
    'regions': {
        "Burgenland": {"code": None, "area_codes": [2682]},
        "Carinthia": {"code": None, "area_codes": [463]},
        "Lower Austria": {"code": None, "area_codes": [2742]},
        "Salzburg": {"code": None, "area_codes": [662]},
        "Styria": {"code": None, "area_codes": [316]},
        "Tyrol": {"code": None, "area_codes": [512]},
        "Upper Austria": {"code": None, "area_codes": [732]},
        "Vorarlberg": {"code": None, "area_codes": [5574]},
        "Any region (Country-wide)": {"code": None, "area_codes": []}
    }
},
'BE': {
    'name': 'Belgium',
    'number_types': {
        'local': None,
        'mobile': None,
        'national': None,
        'tollfree': 25.0,
    },
    'tollfree_prefixes': [800],
    'regions': {
        "Wallonia": {"code": None, "area_codes": [4, 71, 81, 82, 83, 85, 86, 87, 89]},
        "Any region (Country-wide)": {"code": None, "area_codes": []}
    }
},
'BR': {
    'name': 'Brazil',
    'number_types': {
        'local': 4.25,
        'mobile': None,
        'national': None,
        'tollfree': None,
    },
    'tollfree_prefixes': [800],
    'regions': {
        "Espirito Santo": {"code": None, "area_codes": [27]},
        "Federal District": {"code": None, "area_codes": [61]},
        "Goias": {"code": None, "area_codes": [62]},
        "Minas Gerais": {"code": None, "area_codes": [31, 32, 33, 34, 35, 37, 38]},
        "Parana": {"code": None, "area_codes": [41, 42, 43, 44, 45, 46]},
        "Rio Grande do Sul": {"code": None, "area_codes": [51, 53, 54, 55]},
        "Santa Catarina": {"code": None, "area_codes": [47, 48, 49]},
        "Sao Paulo": {"code": None, "area_codes": [11, 12, 13, 14, 15, 16, 17, 18, 19]},
        "Sergipe": {"code": None, "area_codes": [79]},
        "Tocantins": {"code": None, "area_codes": [63]},
        "Any region (Country-wide)": {"code": None, "area_codes": []}
    }
},
'CL': {
    'name': 'Chile',
    'number_types': {
        'local': 7.0,
        'mobile': None,
        'national': None,
        'tollfree': None,
    },
    'tollfree_prefixes': [800],
    'regions': {
        "Santiago Metropolitan": {"code": None, "area_codes": [2]},
        "Any region (Country-wide)": {"code": None, "area_codes": []}
    }
},
'CO': {
    'name': 'Colombia',
    'number_types': {
        'local': 14.0,
        'mobile': None,
        'national': None,
        'tollfree': 25.0,
    },
    'tollfree_prefixes': [800],
    'regions': {
        "Antioquia": {"code": None, "area_codes": [4]},
        "Bolivar": {"code": None, "area_codes": [5]},
        "Santander": {"code": None, "area_codes": [7]},
        "Tolima": {"code": None, "area_codes": [8]},
        "Valle del Cauca": {"code": None, "area_codes": [2]},
        "Any region (Country-wide)": {"code": None, "area_codes": []}
    }
},
'CZ': {
    'name': 'Czech Republic',
    'number_types': {
        'local': 1.5,
        'mobile': 12.0,
        'national': 1.5,
        'tollfree': 35.0,
    },
    'tollfree_prefixes': [800],
    'regions': {
        "Czech Republic Proper": {"code": None, "area_codes": [2]},
        "Region Pardubicky": {"code": None, "area_codes": [46]},
        "South Moravian": {"code": None, "area_codes": [5]},
        "Any region (Country-wide)": {"code": None, "area_codes": []}
    }
},
'DE': {
    'name': 'Germany',
    'number_types': {
        'local': 1.15,
        'mobile': None,
        'national': None,
        'tollfree': None,
    },
    'tollfree_prefixes': [800],
    'regions': {
        "Baden-Wuerttemberg": {"code": None, "area_codes": [711, 721, 731]},
        "Bavaria": {"code": None, "area_codes": [89, 911, 941]},
        "Brandenburg": {"code": None, "area_codes": [331, 355]},
        "Hesse": {"code": None, "area_codes": [69, 611, 6151]},
        "Lower Saxony": {"code": None, "area_codes": [511, 531]},
        "Mecklenburg-Vorpommern": {"code": None, "area_codes": [381, 385]},
        "Minden Westf": {"code": None, "area_codes": [571]},
        "North Rhine-Westphalia": {"code": None, "area_codes": [211, 221, 231]},
        "Nurnberg": {"code": None, "area_codes": [911]},
        "Oberstenfeld": {"code": None, "area_codes": [7062]},
        "Ottenbach": {"code": None, "area_codes": [7165]},
        "Rheinland-Pfalz": {"code": None, "area_codes": [261, 621]},
        "Saarland": {"code": None, "area_codes": [681]},
        "Saxony": {"code": None, "area_codes": [351, 371]},
        "Saxony-Anhalt": {"code": None, "area_codes": [391, 345]},
        "Sinzheim": {"code": None, "area_codes": [7221]},
        "Sulzfeld Baden": {"code": None, "area_codes": [7269]},
        "Wang": {"code": None, "area_codes": [8772]},
        "Wesseling Rheinl": {"code": None, "area_codes": [2236]},
        "Woltersdorf": {"code": None, "area_codes": [3362]},
        "Any region (Country-wide)": {"code": None, "area_codes": []}
    }
},
    'GR': {
        'name': 'Greece',
        'number_types': {
            'local': 1.0,
            'mobile': None,
            'national': None,
            'tollfree': None,
        },
        'tollfree_prefixes': [800],
        'regions': {
            "Attica": {"code": None, "area_codes": [21]},
            "Any region (Country-wide)": {"code": None, "area_codes": []}
        }
    },
    'HK': {
        'name': 'Hong Kong',
        'number_types': {
            'local': None,
            'mobile': 15.0,
            'national': 6.0,
            'tollfree': 25.0,
        },
        'tollfree_prefixes': [800],
        'regions': {
            "Central and Western": {"code": None, "area_codes": [2]},
            "Any region (Country-wide)": {"code": None, "area_codes": []}
        }
    },
'HR': {
    'name': 'Croatia',
    'number_types': {
        'local': 5.0,
        'tollfree': 19.0,
        'mobile': None,
        'national': None,
    },
    'tollfree_prefixes': [800],
    'regions': {
        "Bjelovarsko-Bilogorska": {"code": None, "area_codes": [43]},
        "City of Zagreb": {"code": None, "area_codes": [1]},
        "Dubrovacko-Neretvanska": {"code": None, "area_codes": [20]},
        "Istarska": {"code": None, "area_codes": [52]},
        "Karlovacka": {"code": None, "area_codes": [47]},
        "Koprivnicko-Krizevacka": {"code": None, "area_codes": [48]},
        "Krapinsko-Zagorska": {"code": None, "area_codes": [49]},
        "Licko-Senjska": {"code": None, "area_codes": [53]},
        "Osjecko-Baranjska": {"code": None, "area_codes": [31]},
        "Slavonski Brod-Posavina": {"code": None, "area_codes": [35]},
        "Splitsko-Dalmatinska": {"code": None, "area_codes": [21]},
        "Varazdinska": {"code": None, "area_codes": [42]},
        "Virovitick-Podravska": {"code": None, "area_codes": [33]},
        "Zadarska": {"code": None, "area_codes": [23]},
        "Any region (Country-wide)": {"code": None, "area_codes": []}
    }
},
'ID': {
    'name': 'Indonesia',
    'number_types': {
        'local': 23.0,
        'tollfree': 25.0,
        'mobile': None,
        'national': None,
    },
    'tollfree_prefixes': [800],
    'regions': {
        "Jakarta": {"code": None, "area_codes": [21]},
        "Any region (Country-wide)": {"code": None, "area_codes": []}
    }
},
'IE': {
    'name': 'Ireland',
    'number_types': {
        'local': 1.6,
        'mobile': None,
        'national': None,
        'tollfree': None,
    },
    'tollfree_prefixes': [1800],
    'regions': {
        "Connaught": {"code": None, "area_codes": [91]},
        "Dublin": {"code": None, "area_codes": [1]},
        "Leinster": {"code": None, "area_codes": [45]},
        "Munster": {"code": None, "area_codes": [21]},
        "Ulster": {"code": None, "area_codes": [74]},
        "Any region (Country-wide)": {"code": None, "area_codes": []}
    }
},
'IL': {
    'name': 'Israel',
    'number_types': {
        'local': 4.25,
        'mobile': 15.0,
        'national': 4.25,
        'tollfree': 15.0,
    },
    'tollfree_prefixes': [1800],
    'regions': {
        "Abu Dis": {"code": None, "area_codes": [2]},
        "Amishav": {"code": None, "area_codes": [3]},
        "Central District": {"code": None, "area_codes": [8]},
        "Haifa": {"code": None, "area_codes": [4]},
        "Israel Proper": {"code": None, "area_codes": [9]},
        "Jerusalem": {"code": None, "area_codes": [2]},
        "Southern District": {"code": None, "area_codes": [8]},
        "Tel Aviv": {"code": None, "area_codes": [3]},
        "Any region (Country-wide)": {"code": None, "area_codes": []}
    }
},
'IT': {
    'name': 'Italy',
    'number_types': {
        'local': None,
        'mobile': 30.0,
        'national': None,
        'tollfree': 25.0,
    },
    'tollfree_prefixes': [800],
    'regions': {
        "Apulia": {"code": None, "area_codes": [80]},
        "Any region (Country-wide)": {"code": None, "area_codes": []}
    }
},
'JP': {
    'name': 'Japan',
    'number_types': {
        'local': 4.5,
        'mobile': None,
        'national': 4.5,
        'tollfree': 25.0,
    },
    'tollfree_prefixes': [120, 800],
    'regions': {
        "Aichi": {"code": None, "area_codes": [52]},
        "Aomori": {"code": None, "area_codes": [17]},
        "Fukuroi Shizuoka": {"code": None, "area_codes": [53]},
        "Hokkaido": {"code": None, "area_codes": [11]},
        "Hyogo": {"code": None, "area_codes": [78]},
        "Japan Proper": {"code": None, "area_codes": [3]},
        "Nagano": {"code": None, "area_codes": [26]},
        "Oita": {"code": None, "area_codes": [97]},
        "Okinawa": {"code": None, "area_codes": [98]},
        "Shizuoka": {"code": None, "area_codes": [54]},
        "Tokyo": {"code": None, "area_codes": [3]},
        "Any region (Country-wide)": {"code": None, "area_codes": []}
    }
},
'KE': {
    'name': 'Kenya',
    'number_types': {
        'local': 16.0,
        'mobile': None,
        'national': None,
        'tollfree': None,
    },
    'tollfree_prefixes': [800],
    'regions': {
        "Nairobi Area": {"code": None, "area_codes": [20]},
        "Any region (Country-wide)": {"code": None, "area_codes": []}
    }
},
'MY': {
    'name': 'Malaysia',
    'number_types': {
        'local': 4.0,
        'mobile': None,
        'national': None,
        'tollfree': None,
    },
    'tollfree_prefixes': [1800],
    'regions': {
        "Selangor": {"code": None, "area_codes": [3]},
        "Any region (Country-wide)": {"code": None, "area_codes": []}
    }
},
'MX': {
    'name': 'Mexico',
    'number_types': {
        'local': 6.25,
        'mobile': None,
        'national': None,
        'tollfree': 30.0,
    },
    'tollfree_prefixes': [800],
    'regions': {
        "Area Metropolitana": {"code": None, "area_codes": [55]},
        "Chiapas": {"code": None, "area_codes": [961]},
        "Chihuahua": {"code": None, "area_codes": [614]},
        "Guanajuato": {"code": None, "area_codes": [477]},
        "Jalisco": {"code": None, "area_codes": [33]},
        "Mexico": {"code": None, "area_codes": [722]},
        "Mexico City": {"code": None, "area_codes": [55]},
        "Nuevo Leon": {"code": None, "area_codes": [81]},
        "Sonora": {"code": None, "area_codes": [662]},
        "Tabasco": {"code": None, "area_codes": [993]},
        "Tamaulipas": {"code": None, "area_codes": [834]},
        "Veracruz": {"code": None, "area_codes": [229]},
        "Any region (Country-wide)": {"code": None, "area_codes": []}
    }
},
'NZ': {
    'name': 'New Zealand',
    'number_types': {
        'local': 3.15,
        'mobile': None,
        'national': None,
        'tollfree': 40.0,
    },
    'tollfree_prefixes': [800],
    'regions': {
        "Auckland": {"code": None, "area_codes": [9]},
        "Bay of Plenty": {"code": None, "area_codes": [7]},
        "Canterbury": {"code": None, "area_codes": [3]},
        "Hawke's Bay": {"code": None, "area_codes": [6]},
        "Waikato": {"code": None, "area_codes": [7]},
        "Wellington": {"code": None, "area_codes": [4]},
        "Any region (Country-wide)": {"code": None, "area_codes": []}
    }
},
'PA': {
    'name': 'Panama',
    'number_types': {
        'local': 8.0,
        'mobile': None,
        'national': None,
        'tollfree': None,
    },
    'tollfree_prefixes': [800],
    'regions': {
        "Panama City": {"code": None, "area_codes": [2]},
        "Panama Proper": {"code": None, "area_codes": [3]},
        "Any region (Country-wide)": {"code": None, "area_codes": []}
    }
},
'PH': {
    'name': 'Philippines',
    'number_types': {
        'local': 15.0,
        'mobile': 120.0,
        'national': None,
        'tollfree': 25.0,
    },
    'tollfree_prefixes': [1800],
    'regions': {
        "Angeles": {"code": None, "area_codes": [45]},
        "Calabarzon": {"code": None, "area_codes": [46]},
        "Central Visayas": {"code": None, "area_codes": [32]},
        "Davao": {"code": None, "area_codes": [82]},
        "Ilocos": {"code": None, "area_codes": [77]},
        "Metro Manila": {"code": None, "area_codes": [2]},
        "Western Visayas": {"code": None, "area_codes": [33]},
        "Any region (Country-wide)": {"code": None, "area_codes": []}
    }
},
'PR': {
    'name': 'Puerto Rico',
    'number_types': {
        'local': 3.25,
        'mobile': None,
        'national': None,
        'tollfree': None,
    },
    'tollfree_prefixes': [800],
    'regions': {
        "PR": {"code": None, "area_codes": [787, 939]},
        "Any region (Country-wide)": {"code": None, "area_codes": []}
    }
},
'RO': {
    'name': 'Romania',
    'number_types': {
        'local': 3.0,
        'mobile': None,
        'national': 3.0,
        'tollfree': 25.0,
    },
    'tollfree_prefixes': [800],
    'regions': {
        "Any region (Country-wide)": {"code": None, "area_codes": []}
    }
},
'SI': {
    'name': 'Slovenia',
    'number_types': {
        'local': 5.0,
        'mobile': None,
        'national': None,
        'tollfree': None,
    },
    'tollfree_prefixes': [800],
    'regions': {
        "Celje": {"code": None, "area_codes": [3]},
        "Koper-Capodistria": {"code": None, "area_codes": [5]},
        "Kranj": {"code": None, "area_codes": [4]},
        "Ljubljana": {"code": None, "area_codes": [1]},
        "Maribor": {"code": None, "area_codes": [2]},
        "Any region (Country-wide)": {"code": None, "area_codes": []}
    }
},
'ZA': {
    'name': 'South Africa',
    'number_types': {
        'local': 1.5,
        'mobile': 4.0,
        'national': 1.5,
        'tollfree': None,
    },
    'tollfree_prefixes': [800],
    'regions': {
        "Gauteng": {"code": None, "area_codes": [11]},
        "South Africa Proper": {"code": None, "area_codes": [12]},
        "Western Cape": {"code": None, "area_codes": [21]},
        "Any region (Country-wide)": {"code": None, "area_codes": []}
    }
},
'CH': {
    'name': 'Switzerland',
    'number_types': {
        'local': 1.15,
        'mobile': 9.0,
        'national': None,
        'tollfree': None,
    },
    'tollfree_prefixes': [800],
    'regions': {
        "Any region (Country-wide)": {"code": None, "area_codes": []}
    }
},
'TH': {
    'name': 'Thailand',
    'number_types': {
        'local': 25.0,
        'mobile': 22.0,
        'national': None,
        'tollfree': 25.0,
    },
    'tollfree_prefixes': [1800],
    'regions': {
        "Bangkok": {"code": None, "area_codes": [2]},
        "Central Region": {"code": None, "area_codes": [34]},
        "Nakhon Pathom": {"code": None, "area_codes": [34]},
        "Northern Region": {"code": None, "area_codes": [53]},
        "Any region (Country-wide)": {"code": None, "area_codes": []}
    }
},
'TN': {
    'name': 'Tunisia',
    'number_types': {
        'local': 120.0,
        'mobile': None,
        'national': 120.0,
        'tollfree': None,
    },
    'tollfree_prefixes': [801, 802],
    'regions': {
        "Susah": {"code": None, "area_codes": [73]},
        "Any region (Country-wide)": {"code": None, "area_codes": []}
    }
}
}

# Export as country_data for consistency with imports
country_data = COUNTRY_DATA
