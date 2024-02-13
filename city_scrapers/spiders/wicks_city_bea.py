from city_scrapers.mixins.wichita_city_mixin import WichitaCityMixin


class WicksCityBEASpider(WichitaCityMixin):
    name = "wicks_city_bea"
    agency = "Wichita City - Board of Electrical Appeals"
    cid = "35"
