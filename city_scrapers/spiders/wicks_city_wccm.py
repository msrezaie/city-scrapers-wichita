from city_scrapers.mixins.wichita_city import WichitaCityMixin


class WicksCityWCCMSpider(WichitaCityMixin):
    name = "wicks_city_wccm"
    agency = "Wichita City Council Meetings/Workshops"
    cid = "23"
