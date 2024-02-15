from city_scrapers.mixins.boarddocs import BoardDocsMixin


class WicksGoddardBoeSpider(BoardDocsMixin):
    name = "wicks_goddard_boe"
    agency = "Goddard Board of Education"
    timezone = "America/Chicago"
    boarddocs_slug = "usd265"
    boarddocs_committee_id = "AAUHW74A6F6A"
    location = {
        "name": "Goddard USD 265 Administration Center",
        "address": "201 S Main St, Goddard, KS 67052",
    }
