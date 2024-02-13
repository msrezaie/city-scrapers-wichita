from city_scrapers.mixins.wichita_city_mixin import WichitaCityMixin


class WicksCityWCCARSpider(WichitaCityMixin):
    name = "wicks_city_wccar"
    agency = "Wichita City Council Agenda Review"
    cid = "45"
