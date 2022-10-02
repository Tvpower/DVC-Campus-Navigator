def get_all_nodes():
    all_nodes = {"n1": [1740, 490],
                 "n2": [1724, 800],
                 "n3": [1920, 800],
                 "n4": [1970, 960],
                 "n5": [2060, 950],
                 "n6": [1480, 820],
                 "n7": [1410, 1075],
                 "n8": [1150, 1075],
                 "n9": [1400, 1300],
                 "n10": [1280, 1440],
                 "n11": [1120, 1440],
                 "n12": [860, 1440],
                 "n13": [590, 1520],
                 "n14": [520, 1900],
                 "n15": [540, 2060],
                 "n16": [180, 2030],
                 "n17": [590, 1435],
                 "n18": [470, 1600],
                 "n19": [400, 1435],
                 "n20": [175, 1485],
                 "n21": [295, 1645],
                 "n22": [375, 1160],
                 "n23": [1590, 1670],
                 "n24": [2140, 1330],
                 "n25": [2170, 1200],
                 "n26": [1720, 1020],
                 "n27": [1700, 1220],
                 "n28": [1620, 1465],
                 "n29": [1815, 1510],
                 "n30": [1950, 1400],

                 "e1": [1780, 670],
                 "e2": [1910, 720],
                 "e3": [1890, 962],
                 "e4": [1800, 970],
                 "e5": [1410, 805],
                 "e6": [1420, 970],
                 "e7": [1350, 1140],
                 "e8": [2050, 1435],
                 "e9": [1875, 1580],
                 "e10": [1350, 1590],
                 "e11": [910, 1710],
                 "e12": [460, 1700],
                 "e13": [450, 1900],
                 "e14": [345, 1611],
                 "e15": [100, 1690],
                 "e16": [90, 1515],
                 "e17": [90, 1160],
                 "e18": [100, 2000],
                 "e19": [1365, 1350],

                 "PAC": [1930, 660],
                 "SU": [1800, 900],
                 "HSF": [1250, 760],
                 "SSC": [1250, 945],
                 "BC": [1275, 1200],
                 "MA": [1370, 1535],
                 "M": [1960, 1520],
                 "L": [750, 1700],
                 "PS": [370, 1960],
                 "LHS": [110, 1824],
                 "ATC": [80, 1330]
                 }
    return all_nodes


def get_init_main():
    init_main = {}
    for single_node, location in get_all_nodes().items():
        init_main[single_node] = {}

    init_main["n1"]["e1"] = -1
    init_main["n1"]["n2"] = -1
    init_main["n1"]["n6"] = -1

    init_main["n2"]["e1"] = -1
    init_main["n2"]["n3"] = -1
    init_main["n2"]["n26"] = -1
    init_main["n2"]["n6"] = -1
    init_main["n2"]["n7"] = -1

    init_main["n3"]["e2"] = -1
    init_main["n3"]["n4"] = -1

    init_main["n4"]["e3"] = -1
    init_main["n4"]["n5"] = -1
    init_main["n4"]["n27"] = -1

    init_main["n5"]["n25"] = -1

    init_main["n6"]["e5"] = -1
    init_main["n6"]["e6"] = -1
    init_main["n6"]["n7"] = -1
    init_main["n6"]["n26"] = -1

    init_main["n7"]["e6"] = -1
    init_main["n7"]["e7"] = -1
    init_main["n7"]["n9"] = -1
    init_main["n7"]["n8"] = -1
    init_main["n7"]["n26"] = -1

    init_main["n8"]["e7"] = -1
    init_main["n8"]["n11"] = -1

    init_main["n9"]["e7"] = -1
    init_main["n9"]["e19"] = -1
    init_main["n9"]["n10"] = -1
    init_main["n9"]["n23"] = -1

    init_main["n10"]["e10"] = -1
    init_main["n10"]["n11"] = -1

    init_main["n11"]["n12"] = -1

    init_main["n12"]["e11"] = -1
    init_main["n12"]["n13"] = -1
    init_main["n12"]["n17"] = -1

    init_main["n13"]["n14"] = -1

    init_main["n14"]["e13"] = -1
    init_main["n14"]["n15"] = -1

    init_main["n15"]["n16"] = -1

    init_main["n16"]["e18"] = -1

    init_main["n13"]["n14"] = -1

    init_main["n17"]["n18"] = -1
    init_main["n17"]["n19"] = -1
    init_main["n18"]["e12"] = -1

    init_main["n19"]["n21"] = -1
    init_main["n19"]["n20"] = -1
    init_main["n19"]["n22"] = -1

    init_main["n21"]["e14"] = -1
    init_main["n21"]["e15"] = -1
    init_main["n21"]["n16"] = -1

    init_main["n20"]["e16"] = -1
    init_main["n20"]["e15"] = -1

    init_main["n22"]["e17"] = -1

    init_main["n23"]["e9"] = -1
    init_main["n23"]["e9"] = -1
    init_main["n23"]["e10"] = -1

    init_main["n24"]["n30"] = -1
    init_main["n24"]["e8"] = -1

    init_main["n25"]["n24"] = -1

    init_main["n26"]["n27"] = -1
    init_main["n26"]["e4"] = -1

    init_main["n27"]["n28"] = -1

    init_main["n28"]["n29"] = -1
    init_main["n28"]["n23"] = -1

    init_main["n29"]["e9"] = -1

    init_main["n30"]["n29"] = -1

    # Edges: BUILDINGS
    init_main["PAC"]["e1"] = -1
    init_main["PAC"]["e2"] = -1

    init_main["SU"]["e4"] = -1
    init_main["SU"]["e3"] = -1

    init_main["HSF"]["e5"] = -1

    init_main["SSC"]["e6"] = -1

    init_main["BC"]["e7"] = -1

    init_main["MA"]["e10"] = -1
    init_main["MA"]["e19"] = -1

    init_main["M"]["e8"] = -1
    init_main["M"]["e9"] = -1

    init_main["L"]["e11"] = -1

    init_main["PS"]["e12"] = -1
    init_main["PS"]["e13"] = -1
    init_main["PS"]["e14"] = -1

    init_main["LHS"]["e15"] = -1
    init_main["LHS"]["e18"] = -1

    init_main["ATC"]["e16"] = -1
    init_main["ATC"]["e17"] = -1

    return init_main
