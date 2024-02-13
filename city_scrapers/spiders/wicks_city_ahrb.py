from city_scrapers.mixins.wichita_city_mixin import WichitaCityMixin


class WicksCityAHRBSpider(WichitaCityMixin):
    name = "wicks_city_ahrb"
    agency = "Wichita City - Affordable Housing Review Board"
    cid = "30"
