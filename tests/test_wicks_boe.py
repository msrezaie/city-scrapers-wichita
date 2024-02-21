from datetime import datetime
from os.path import dirname, join

import pytest
from city_scrapers_core.constants import BOARD, PASSED
from city_scrapers_core.utils import file_response
from freezegun import freeze_time

from city_scrapers.spiders.wicks_boe import WicksBoeSpider

test_response = file_response(
    join(dirname(__file__), "files", "wicks_boe.json"),
    url="https://awsapieast1-prod21.schoolwires.com/REST/api/v4/CalendarEvents/GetEvents/13328?StartDate=2024-01-22&EndDate=2024-08-19&ModuleInstanceFilter=&CategoryFilter=&IsDBStreamAndShowAll=true",  # noqa
)
spider = WicksBoeSpider()

freezer = freeze_time("2024-02-20")
freezer.start()

parsed_items = [item for item in spider.parse(test_response)]

freezer.stop()


"""
Uncomment below
"""


def test_title():
    assert parsed_items[0]["title"] == "BOE Meeting"


def test_description():
    assert parsed_items[0]["description"] == ""


def test_start():
    assert parsed_items[0]["start"] == datetime(2024, 1, 22, 18, 0)


def test_end():
    assert parsed_items[0]["end"] == datetime(2024, 1, 22, 23, 59, 59)


def test_time_notes():
    assert parsed_items[0]["time_notes"] is None


def test_id():
    assert parsed_items[0]["id"] == "wicks_boe/202401221800/x/boe_meeting"


def test_status():
    assert parsed_items[0]["status"] == PASSED


def test_location():
    assert parsed_items[0]["location"] == {
        "name": "Wichita North High School - Lecture Hall",
        "address": "1437 N Rochester St, Wichita, KS 67203",
    }


def test_source():
    assert (
        parsed_items[0]["source"]
        == "https://awsapieast1-prod21.schoolwires.com/REST/api/v4/CalendarEvents/GetEvents/13328?StartDate=2024-01-22&EndDate=2024-08-19&ModuleInstanceFilter=&CategoryFilter=&IsDBStreamAndShowAll=true"  # noqa
    )


def test_links():
    assert parsed_items[0]["links"] == [
        {"title": "Agenda Page", "href": "https://www.usd259.org/Page/7121"}
    ]


def test_classification():
    assert parsed_items[0]["classification"] == BOARD


@pytest.mark.parametrize("item", parsed_items)
def test_all_day(item):
    assert item["all_day"] is False
