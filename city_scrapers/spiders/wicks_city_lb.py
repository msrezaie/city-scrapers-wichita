from city_scrapers.mixins.wichita_city import WichitaCityMixin


class WicksCityLBSpider(WichitaCityMixin):
    name = "wicks_city_lb"
    agency = "Wichita City - Library Board"
    cid = "51"
