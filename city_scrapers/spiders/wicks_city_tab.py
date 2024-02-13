from city_scrapers.mixins.wichita_city_mixin import WichitaCityMixin


class WicksCityTABSpider(WichitaCityMixin):
    name = "wicks_city_tab"
    agency = "Wichita City - Transit Advisory Board"
    cid = "59"
