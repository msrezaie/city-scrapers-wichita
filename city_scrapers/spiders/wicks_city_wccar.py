from city_scrapers.mixins.wichita_city import WichitaCityMixin


class WicksCityWCCARSpider(WichitaCityMixin):
    name = "wicks_city_wccar"
    agency = "Wichita City Council Agenda Review"
    cid = "45"
