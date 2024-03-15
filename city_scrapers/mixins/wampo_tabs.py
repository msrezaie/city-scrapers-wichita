import re
from datetime import datetime

from city_scrapers_core.constants import COMMITTEE
from city_scrapers_core.items import Meeting
from city_scrapers_core.spiders import CityScrapersSpider
from dateutil.parser import parse


class WampoMixinTabsMeta(type):
    """
    Metaclass that enforces the implementation of required static
    variables in child classes that inherit from WampoMixinTabs.
    """

    def __init__(cls, name, bases, dct):
        required_static_vars = [
            "name",
            "agency",
            "start_urls",
            "start_time",
        ]
        missing_vars = [var for var in required_static_vars if var not in dct]

        if missing_vars:
            missing_vars_str = ", ".join(missing_vars)
            raise NotImplementedError(
                f"{name} must define the following static variable(s): {missing_vars_str}."  # noqa
            )

        super().__init__(name, bases, dct)


class WampoMixinTabs(CityScrapersSpider, metaclass=WampoMixinTabsMeta):
    """
    This mixin is designed for scraping meeting data from specific pages on the
    website of the Wichita Area Metropolitan Planning Organization (WAMPO) that use
    a tabbed interface. It is not applicable for all WAMPO pages.

    Child classes must define 'name', 'agency', 'start_urls', 'start_time', and 'location'  # noqa
    as static variables.
    """

    name = None
    agency = None
    start_urls = None
    location = {
        "name": "Wichita Area Metropolitan Planning Organization",
        "address": "271 W. 3rd St. N., Suite 101, Wichita, KS 67202",
    }
    timezone = "America/Chicago"
    start_time = None

    def parse(self, response):
        """
        Parse the page and extract the meeting information.
        """
        for item in response.css("div[role='tabpanel'] ul li p"):
            start = self._parse_start(item)
            if start is None:
                self.logger.warn("Skipping row with no date")
                continue
            meeting = Meeting(
                title="Executive Committee Meeting",
                description="",
                classification=COMMITTEE,
                start=start,
                end=None,
                all_day=False,
                time_notes="",
                location=self.location,
                links=self._parse_links(item),
                source=response.url,
            )
            meeting["status"] = self._get_status(meeting)
            meeting["id"] = self._get_id(meeting)
            yield meeting

    def _parse_start(self, item):
        """
        Extracts all the text from the row and parses the first
        column that looks formatted like 11/1/2024 or November 12, 2024.
        """
        item.css("span::text").extract()
        for text in item.css("span::text").extract():
            clean_text = text.strip()
            if re.match(
                r"(?:[a-zA-Z]+\s\d{1,2},\s\d{4})|(?:\d{1,2}\/\d{1,2}\/\d{2,4})",
                clean_text,
            ):
                try:
                    start_date = parse(clean_text)
                    start_datetime = datetime.combine(start_date, self.start_time)
                    return start_datetime
                except ValueError:
                    self.logger.info(f"Could not parse date from {clean_text}")
                    return None
        self.logger.info("Could not find date in row")
        return None

    def _parse_links(self, item):
        """
        Parse all links in the row.
        """
        links = []
        for link in item.css("a"):
            links.append(
                {
                    "href": link.attrib["href"],
                    "title": link.css("::text").extract_first(),
                }
            )
        return links
