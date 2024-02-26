from city_scrapers.mixins.wichita_city import WichitaCityMixin


class WicksCityAPCSpider(WichitaCityMixin):
    name = "wicks_city_apc"
    agency = "Wichita City - Advance Plans Committee"
    cid = "68"
