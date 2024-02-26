from city_scrapers.mixins.wichita_city import WichitaCityMixin


class WicksCityBPABSpider(WichitaCityMixin):
    name = "wicks_city_bpab"
    agency = "Wichita City - Bicycle & Pedestrian Advisory Board"
    cid = "32"
