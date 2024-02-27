from city_scrapers.mixins.boarddocs import BoardDocsMixin


class WicksAndoverBoeSpider(BoardDocsMixin):
    name = "wicks_andover_boe"
    agency = "Andover Board of Education"
    timezone = "America/Chicago"
    boarddocs_slug = "usd385"
    boarddocs_committee_id = "AAUHXC4A9B8F"
