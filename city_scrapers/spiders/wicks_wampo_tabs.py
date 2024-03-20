from datetime import time

from city_scrapers_core.constants import COMMITTEE

from city_scrapers.mixins.wampo_tabs import WampoMixinTabs

# Configuration for each spider
spider_configs = [
    {
        "class_name": "WampoECSpider",
        "name": "wicks_wampo_ec",
        "agency": "Wichita Area Metropolitan Planning Organization – Executive Committee",  # noqa
        "start_urls": ["https://www.wampo.org/executive-committee"],
        "start_time": time(11, 0),
        "classification": COMMITTEE,
    },
    {
        "class_name": "WampoATCSpider",
        "name": "wicks_wampo_atc",
        "agency": "Wichita Area Metropolitan Planning Organization – Active Transportation Committee",  # noqa
        "start_urls": ["https://www.wampo.org/active-transportation"],
        "start_time": time(9, 30),
        "classification": COMMITTEE,
    },
    {
        "class_name": "WicksWampoICTSSpider",
        "name": "wicks_wampo_icts",
        "agency": "Wichita Area Metropolitan Planning Organization – ICT Safe",
        "start_urls": ["https://www.wampo.org/ict-safe"],
        "start_time": time(9, 30),
        "classification": COMMITTEE,
    },
    {
        "class_name": "WicksWampoUCTCSpider",
        "name": "wicks_wampo_uctc",
        "agency": "Wichita Area Metropolitan Planning Organization – United Community Transit Coalition",  # noqa
        "start_urls": ["https://www.wampo.org/uctc"],
        "start_time": time(14, 0),
        "classification": COMMITTEE,
    },
]


def create_spiders():
    """
    Dynamically create spider classes using the spider_configs list
    and then register them in the global namespace. This approach
    is the equivalent of declaring each spider class in the same
    file but it is more concise and centralized.
    """
    for config in spider_configs:
        class_name = config.pop("class_name")
        if class_name not in globals():
            spider_class = type(
                class_name,
                (WampoMixinTabs,),  # Base class
                {**config},  # Attributes
            )
            globals()[class_name] = spider_class


create_spiders()
