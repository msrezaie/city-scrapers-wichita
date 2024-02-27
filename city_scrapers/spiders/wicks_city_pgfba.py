from city_scrapers.mixins.wichita_city import WichitaCityMixin


class WicksCityPGFBASpider(WichitaCityMixin):
    name = "wicks_city_pgfba"
    agency = "Wichita City - Plumbers & Gas Fitters Board of Appeals"
    cid = "52"
