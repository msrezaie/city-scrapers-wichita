from city_scrapers.mixins.wichita_city import WichitaCityMixin


class WicksCityNCPSpider(WichitaCityMixin):
    name = "wicks_city_ncp"
    agency = "Wichita City - Neighborhood Clean-Up Program"
    cid = "86"
