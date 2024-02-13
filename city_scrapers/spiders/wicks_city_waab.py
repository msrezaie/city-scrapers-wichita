from city_scrapers.mixins.wichita_city_mixin import WichitaCityMixin


class WicksCityWAABSpider(WichitaCityMixin):
    name = "wicks_city_waab"
    agency = "Wichita Airport Advisory Board"
    cid = "60"
