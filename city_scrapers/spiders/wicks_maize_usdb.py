from city_scrapers.mixins.boarddocs import BoardDocsMixin


class WicksMaizeUSDB(BoardDocsMixin):
    name = "wicks_maize_usdb"
    agency = "Maize Unified School District Board"
    timezone = "America/Chicago"
    boarddocs_slug = "mzufsd266"
    boarddocs_committee_id = "AAUHT84A019F"
    location = {
        "name": "Maize Performing Arts and Aquatics Center (MPAAC)",
        "address": "1055 W Academy Ave, Maize, KS 67101",
    }
