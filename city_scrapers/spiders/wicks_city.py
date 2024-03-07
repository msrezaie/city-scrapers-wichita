from city_scrapers.mixins.wichita_city import WichitaCityMixin

# Configuration for each spider
spider_configs = [
    {
        "class_name": "WicksCityERSBTSpider",
        "name": "wicks_city_ersbt",
        "agency": "Wichita City - Employees Retirement System Board of Trustees",
        "cid": "62",
    },
    {
        "class_name": "WicksCityMAPCSpider",
        "name": "wicks_city_mapc",
        "agency": "Wichita City - Metropolitan Area Planning Commission",
        "cid": "27",
    },
    {
        "class_name": "WicksCityPFRBTSpider",
        "name": "wicks_city_pfrbt",
        "agency": "Wichita City - Police & Fire Retirement Board of Trustees",
        "cid": "53",
    },
    {
        "class_name": "WicksCityGBGSpider",
        "name": "wicks_city_gbg",
        "agency": "Wichita City - Golf Board of Governors",
        "cid": "49",
    },
    {
        "class_name": "WicksCityDDACSpider",
        "name": "wicks_city_ddac",
        "agency": "Wichita City - Delano District Advisory Committee",
        "cid": "75",
    },
    {
        "class_name": "WicksCityDICRABSpider",
        "name": "wicks_city_dicrab",
        "agency": "Wichita City - Diversity Inclusion & Civil Rights Advisory Board",
        "cid": "46",
    },
    {
        "class_name": "WicksCityCRBSSpider",
        "name": "wicks_city_crbs",
        "agency": "Wichita City - Citizen Review Board Sub-Committee/KOMA",
        "cid": "80",
    },
    {
        "class_name": "WicksCityPRESpider",
        "name": "wicks_city_pre",
        "agency": "Wichita City - Park & Recreation Events",
        "cid": "74",
    },
    {
        "class_name": "WicksCityACABSpider",
        "name": "wicks_city_acab",
        "agency": "Wichita City - Animal Control Advisory Board",
        "cid": "31",
    },
    {
        "class_name": "WicksCityCCABSpider",
        "name": "wicks_city_ccab",
        "agency": "Wichita City - Community Corrections Advisory Board",
        "cid": "54",
    },
    {
        "class_name": "WicksCityLBSpider",
        "name": "wicks_city_lb",
        "agency": "Wichita City - Library Board",
        "cid": "51",
    },
    {
        "class_name": "WicksCityBPABSpider",
        "name": "wicks_city_bpab",
        "agency": "Wichita City - Bicycle & Pedestrian Advisory Board",
        "cid": "32",
    },
    {
        "class_name": "WicksCityWCBZASpider",
        "name": "wicks_city_wcbza",
        "agency": "Wichita-Sedgwick County Board of Zoning Appeals",
        "cid": "66",
    },
    {
        "class_name": "WicksCityWAABSpider",
        "name": "wicks_city_waab",
        "agency": "Wichita Airport Advisory Board",
        "cid": "60",
    },
    {
        "class_name": "WicksCityDAB3Spider",
        "name": "wicks_city_dab3",
        "agency": "Wichita City - District Advisory Board 3",
        "cid": "41",
    },
    {
        "class_name": "WicksCityBEASpider",
        "name": "wicks_city_bea",
        "agency": "Wichita City - Board of Electrical Appeals",
        "cid": "35",
    },
    {
        "class_name": "WicksCityBAARHSpider",
        "name": "wicks_city_baarh",
        "agency": "Wichita City - Board of Appeals - Air, Refrigeration & Heating",
        "cid": "33",
    },
    {
        "class_name": "WicksCityDAB2Spider",
        "name": "wicks_city_dab2",
        "agency": "Wichita City - District Advisory Board 2",
        "cid": "40",
    },
    {
        "class_name": "WicksCityAPCSpider",
        "name": "wicks_city_apc",
        "agency": "Wichita City - Advance Plans Committee",
        "cid": "68",
    },
    {
        "class_name": "WicksCityAHRBSpider",
        "name": "wicks_city_ahrb",
        "agency": "Wichita City - Affordable Housing Review Board",
        "cid": "30",
    },
    {
        "class_name": "WicksCitySMIDSpider",
        "name": "wicks_city_smid",
        "agency": "Wichita City - Self-Supported Municipal Improvement DAB",
        "cid": "56",
    },
    {
        "class_name": "WicksCityDAB6Spider",
        "name": "wicks_city_dab6",
        "agency": "Wichita City - District Advisory Board 6",
        "cid": "44",
    },
    {
        "class_name": "WicksCityAABSpider",
        "name": "wicks_city_aab",
        "agency": "Wichita/Sedgwick County Access Advisory Board",
        "cid": "67",
    },
    {
        "class_name": "WicksCityTABSpider",
        "name": "wicks_city_tab",
        "agency": "Wichita City - Transit Advisory Board",
        "cid": "59",
    },
    {
        "class_name": "WicksCityDAB1Spider",
        "name": "wicks_city_dab1",
        "agency": "Wichita City - District Advisory Board 1",
        "cid": "39",
    },
    {
        "class_name": "WicksCitySWABSpider",
        "name": "wicks_city_swab",
        "agency": "Wichita City - Storm Water Advisory Board",
        "cid": "57",
    },
    {
        "class_name": "WicksCityDAB5Spider",
        "name": "wicks_city_dab5",
        "agency": "Wichita City - District Advisory Board 5",
        "cid": "43",
    },
    {
        "class_name": "WicksCityBPCSpider",
        "name": "wicks_city_bpc",
        "agency": "Wichita City - Board of Park Commissioners",
        "cid": "28",
    },
    {
        "class_name": "WicksCityDAB4Spider",
        "name": "wicks_city_dab4",
        "agency": "Wichita City - District Advisory Board 4",
        "cid": "42",
    },
    {
        "class_name": "WicksCityJCABSpider",
        "name": "wicks_city_jcab",
        "agency": "Wichita City - Juvenile Corrections Advisory Board",
        "cid": "55",
    },
    {
        "class_name": "WicksCityBBCSpider",
        "name": "wicks_city_bbc",
        "agency": "Wichita City - Board of Bids & Contracts",
        "cid": "77",
    },
    {
        "class_name": "WicksCityCFCSpider",
        "name": "wicks_city_cfc",
        "agency": "Wichita City - Cultural Funding Committee",
        "cid": "37",
    },
    {
        "class_name": "WicksCityWLBBTSpider",
        "name": "wicks_city_wlbbt",
        "agency": "Wichita Land Bank Board of Trustees",
        "cid": "64",
    },
    {
        "class_name": "WicksCityBCSASpider",
        "name": "wicks_city_bcsa",
        "agency": "Wichita City - Board of Code Standards & Appeals",
        "cid": "34",
    },
    {
        "class_name": "WicksCityEDCMBSpider",
        "name": "wicks_city_edcmb",
        "agency": "Wichita City - Employees' Deferred Compensation Management Board",
        "cid": "63",
    },
    {
        "class_name": "WicksCityMYCSpider",
        "name": "wicks_city_myc",
        "agency": "Wichita City - Mayor's Youth Council",
        "cid": "70",
    },
    {
        "class_name": "WicksCityWCRBSpider",
        "name": "wicks_city_wcrb",
        "agency": "Wichita Citizens Review Board",
        "cid": "61",
    },
    {
        "class_name": "WicksCityNCPSpider",
        "name": "wicks_city_ncp",
        "agency": "Wichita City - Neighborhood Clean-Up Program",
        "cid": "86",
    },
    {
        "class_name": "WicksCityDCSpider",
        "name": "wicks_city_dc",
        "agency": "Wichita City - Design Council",
        "cid": "38",
    },
    {
        "class_name": "WicksCitySCSpider",
        "name": "wicks_city_sc",
        "agency": "Wichita City - Subdivision Committee",
        "cid": "69",
    },
    {
        "class_name": "WicksCityPGFBASpider",
        "name": "wicks_city_pgfba",
        "agency": "Wichita City - Plumbers & Gas Fitters Board of Appeals",
        "cid": "52",
    },
    {
        "class_name": "WicksCityWSIBSpider",
        "name": "wicks_city_wsib",
        "agency": "Wichita Sustainability Integration Board",
        "cid": "65",
    },
    {
        "class_name": "WicksCityHPBSpider",
        "name": "wicks_city_hpb",
        "agency": "Wichita City - Historic Preservation Board",
        "cid": "50",
    },
    {
        "class_name": "WicksCityEABSpider",
        "name": "wicks_city_eab",
        "agency": "Wichita City - Ethics Advisory Board",
        "cid": "47",
    },
    {
        "class_name": "WicksCityCSBGRCSpider",
        "name": "wicks_city_csbgrc",
        "agency": "Wichita City - Community Services Block Grant Review Committee",
        "cid": "36",
    },
    {
        "class_name": "WicksCityTBIDBSpider",
        "name": "wicks_city_tbidb",
        "agency": "Wichita City - Tourism Business Improvement District Board",
        "cid": "58",
    },
    {
        "class_name": "WicksCityWCCMSpider",
        "name": "wicks_city_wccm",
        "agency": "Wichita City Council Meetings/Workshops",
        "cid": "23",
    },
    {
        "class_name": "WicksCityWCCARSpider",
        "name": "wicks_city_wccar",
        "agency": "Wichita City Council Agenda Review",
        "cid": "45",
    },
]


def create_spiders():
    """
    Dynamically create spider classes using the spider_configs list
    and then register them in the global namespace. This approach
    is the equivalent of declaring each spider class in the same
    file but it is a little more concise.
    """
    for config in spider_configs:
        # Using config['class_name'] to dynamically define the class name
        class_name = config.pop(
            "class_name"
        )  # Remove class_name from config to avoid conflicts
        # We make sure that the class_name is not already in the global namespace
        # Because some scrapy CLI commands like `scrapy list` will inadvertently
        # declare the spider class more than once otherwise
        if class_name not in globals():
            spider_class = type(
                class_name,
                (WichitaCityMixin,),  # Base classes
                {**config},  # Attributes including name, agency, cid
            )

            # Register the class in the global namespace using its class_name
            globals()[class_name] = spider_class


# Call the function to create spiders
create_spiders()
