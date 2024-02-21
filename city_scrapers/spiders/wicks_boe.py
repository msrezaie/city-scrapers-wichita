from city_scrapers_core.constants import BOARD
from city_scrapers_core.items import Meeting
from city_scrapers_core.spiders import CityScrapersSpider
from scrapy import Request
import requests
import json
from datetime import datetime, timedelta


class WicksBoeSpider(CityScrapersSpider):
    name = "wicks_boe"
    agency = "Wichita Board of Education"
    timezone = "America/Chicago"
    meeting_materials_link = {
        "title": "Agenda Page",
        "href": "https://www.usd259.org/Page/7121",
    }

    def start_requests(self):

        #make a GET request to retrieve the bearer token
        r = requests.get(url = 'https://www.usd259.org/Generator/TokenGenerator.ashx/ProcessRequest')
        token = r.json()["Token"]

        # calculate the date one month prior and format the date
        # calculate the date six months ahead and format the date
        current_datetime = datetime.utcnow()
        one_month_prior = current_datetime - timedelta(days=30)
        one_month_prior_formated = one_month_prior.strftime("%Y-%m-%d")
        six_months_ahead = current_datetime + timedelta(days=180)
        six_months_prior_formated = six_months_ahead.strftime("%Y-%m-%d")

        # Construct the URL with query parameters
        url = f"https://awsapieast1-prod21.schoolwires.com/REST/api/v4/CalendarEvents/GetEvents/13328?StartDate={one_month_prior_formated}&EndDate={six_months_prior_formated}&ModuleInstanceFilter=&CategoryFilter=&IsDBStreamAndShowAll=true"  # noqa

        headers = {
            'Authorization': f'Bearer {token}',
        }

        yield Request(url, headers=headers, callback=self.parse)

    def parse(self, response):
        """
        `parse` should always `yield` Meeting items.

        Change the `_parse_title`, `_parse_start`, etc methods to fit your scraping
        needs.
        """
        data = json.loads(response.text)
        print(data)
        for item in data["items"]:
            meeting = Meeting(
                title=self._parse_title(item),
                description="",
                classification=BOARD,
                start=self._parse_datetime(item["start"]),
                end=None,
                all_day=False,
                time_notes=None,
                location=self.location,
                links=self.meeting_materials_link,
                source=response.url,
            )
            meeting["status"] = self._get_status(meeting)
            meeting["id"] = self._get_id(meeting)
            yield meeting

    def _parse_title(self, item):
        """Parse or generate meeting title."""
        return ""

    def _parse_start(self, item):
        """Parse start datetime as a naive datetime object."""
        return None

    def _parse_end(self, item):
        """Parse end datetime as a naive datetime object. Added by pipeline if None"""
        return None

    def _parse_location(self, item):
        """Parse or generate location."""
        return {
            "address": "",
            "name": "",
        }

    def _parse_source(self, response):
        """Parse or generate source."""
        return response.url
