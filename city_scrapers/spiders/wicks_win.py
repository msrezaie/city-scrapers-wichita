from city_scrapers_core.constants import NOT_CLASSIFIED
from city_scrapers_core.items import Meeting
from city_scrapers_core.spiders import CityScrapersSpider
from icalendar import Calendar


class WicksWinSpider(CityScrapersSpider):
    name = "wicks_win"
    agency = "Wichita Independent Neighborhoods"
    timezone = "America/Chicago"
    start_urls = ["https://winwichita.org/events/list/?ical=1"]
    custom_settings = {
        "DEFAULT_REQUEST_HEADERS": {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",  # noqa
            "Accept": "text/calendar,*/*;q=0.9",
        }
    }

    def parse(self, response):
        """
        Parses the iCalendar feed and yields a Meeting object for each event.
        """
        cal = Calendar.from_ical(response.body)
        for component in cal.walk():
            if component.name == "VEVENT":
                meeting = Meeting(
                    title=component.get("summary"),
                    description=component.get("description"),
                    classification=NOT_CLASSIFIED,
                    start=self._parse_start(component),
                    end=self._parse_end(component),
                    all_day=False,
                    time_notes="",
                    location=self._parse_location(component),
                    links=[],
                    source=(
                        component.get("url") if component.get("url") else response.url
                    ),
                )
                meeting["status"] = self._get_status(meeting)
                meeting["id"] = self._get_id(meeting)

                yield meeting

    def _parse_start(self, component):
        """Gets a start date from an iCalendar component and
        converts the datetime to a Timezone naive datetime object."""
        start_date = component.get("dtstart")
        return start_date.dt.replace(tzinfo=None) if start_date else None

    def _parse_end(self, component):
        """Gets an end date from an iCalendar component and
        converts the datetime to a Timezone naive datetime object."""
        end_date = component.get("dtend")
        return end_date.dt.replace(tzinfo=None) if end_date else None

    def _parse_location(self, component):
        """Parse or generate location."""
        location = component.get("location")
        if not location:
            return {
                "name": "TBD",
                "address": "",
            }
        return {
            "name": "",
            "address": str(location),
        }
