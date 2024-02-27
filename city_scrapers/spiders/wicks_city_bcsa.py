from city_scrapers.mixins.wichita_city import WichitaCityMixin


class WicksCityBCSASpider(WichitaCityMixin):
    name = "wicks_city_bcsa"
    agency = "Wichita City - Board of Code Standards & Appeals"
    cid = "34"
