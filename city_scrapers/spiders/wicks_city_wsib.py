from city_scrapers.mixins.wichita_city import WichitaCityMixin


class WicksCityWSIBSpider(WichitaCityMixin):
    name = "wicks_city_wsib"
    agency = "Wichita Sustainability Integration Board"
    cid = "65"
