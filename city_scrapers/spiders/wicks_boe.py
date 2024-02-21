import json
from datetime import datetime, timedelta

import requests
from city_scrapers_core.constants import BOARD
from city_scrapers_core.items import Meeting
from city_scrapers_core.spiders import CityScrapersSpider
from dateutil.parser import parser
from scrapy import Request


class WicksBoeSpider(CityScrapersSpider):
    name = "wicks_boe"
    agency = "Wichita Board of Education"
    timezone = "America/Chicago"
    meeting_materials_link = {
        "title": "Agenda Page",
        "href": "https://www.usd259.org/Page/7121",
    }
    location = "North High Lecture Hall, 1437 N Rochester St, Wichita, KS 67203"

    def start_requests(self):

        # Make a GET request to retrieve the bearer token
        r = requests.get(
            url="https://www.usd259.org/Generator/TokenGenerator.ashx/ProcessRequest"
        )
        token = r.json()["Token"]

        # Calculate the date one month prior and format the date
        # Calculate the date six months ahead and format the date
        current_datetime = datetime.utcnow()
        one_month_prior = current_datetime - timedelta(days=30)
        one_month_prior_formated = one_month_prior.strftime("%Y-%m-%d")
        six_months_ahead = current_datetime + timedelta(days=180)
        six_months_prior_formated = six_months_ahead.strftime("%Y-%m-%d")

        # Construct the URL with query parameters
        # The url returns xml by default, therefore request the response to be in json format  # noqa
        url = f"https://awsapieast1-prod21.schoolwires.com/REST/api/v4/CalendarEvents/GetEvents/13328?StartDate={one_month_prior_formated}&EndDate={six_months_prior_formated}&ModuleInstanceFilter=&CategoryFilter=&IsDBStreamAndShowAll=true"  # noqa

        headers = {
            "Authorization": f"Bearer {token}",
            "Accept": "application/json",
        }

        # Make the request to the url, and after the request is complete execute parse()
        yield Request(url, headers=headers, callback=self.parse)

    def parse(self, response):
        # Only filter for 'BOE Meeting' items
        data = json.loads(response.text)
        for item in data:
            if item["Title"] == "BOE Meeting":
                meeting = Meeting(
                    title=item["Title"],
                    description="",
                    classification=BOARD,
                    start=parser().parse(item["Start"]),
                    end=parser().parse(item["End"]),
                    all_day=False,
                    time_notes=None,
                    location=self.location,
                    links=self.meeting_materials_link,
                    source=response.url,
                )
                meeting["status"] = self._get_status(meeting)
                meeting["id"] = self._get_id(meeting)
                yield meeting
            else:
                continue
