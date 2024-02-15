from city_scrapers.mixins.wichita_city import WichitaCityMixin


class WicksCityERSBTSpider(WichitaCityMixin):
    name = "wicks_city_ersbt"
    agency = "Wichita City - Employees Retirement System Board of Trustees"
    cid = "62"
