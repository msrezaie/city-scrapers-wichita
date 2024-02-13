from city_scrapers.mixins.wichita_city_mixin import WichitaCityMixin


class WicksCityBPCSpider(WichitaCityMixin):
    name = "wicks_city_bpc"
    agency = "Wichita City - Board of Park Commissioners"
    cid = "28"
