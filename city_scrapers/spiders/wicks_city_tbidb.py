from city_scrapers.mixins.wichita_city import WichitaCityMixin


class WicksCityTBIDBSpider(WichitaCityMixin):
    name = "wicks_city_tbidb"
    agency = "Wichita City - Tourism Business Improvement District Board"
    cid = "58"
