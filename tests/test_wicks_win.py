from datetime import datetime
from os.path import dirname, join

import pytest
from city_scrapers_core.constants import NOT_CLASSIFIED, PASSED
from city_scrapers_core.utils import file_response
from freezegun import freeze_time

from city_scrapers.spiders.wicks_win import WicksWinSpider

test_response = file_response(
    join(dirname(__file__), "files", "wicks_win.ics"),
    url="https://winwichita.org/events/list/?ical=1",
)
spider = WicksWinSpider()

freezer = freeze_time(datetime(2024, 3, 9, 8, 22))
freezer.start()

parsed_items = [item for item in spider.parse(test_response)]
parsed_item = parsed_items[0]
freezer.stop()


def test_title():
    assert parsed_item["title"] == "Executive Board Meeting"


def test_description():
    assert (
        parsed_item["description"]
        == "This is the closed monthly meeting of WIN’s Executive Board. We meet the second Thursday of every month beginning in January."  # noqa
    )


def test_start():
    assert parsed_item["start"] == datetime(2024, 3, 8, 18, 0)


def test_end():
    assert parsed_item["end"] == datetime(2024, 3, 8, 19, 30)


def test_time_notes():
    assert parsed_item["time_notes"] == ""


def test_id():
    assert parsed_item["id"] == "wicks_win/202403081800/x/executive_board_meeting"


def test_status():
    assert parsed_item["status"] == PASSED


def test_location():
    assert parsed_item["location"] == {
        "name": "",
        "address": "General Membership Meeting Locale, 2418 E 9th St N, Wichita, KS, 67214, United States",  # noqa
    }


def test_source():
    assert (
        parsed_item["source"]
        == "https://winwichita.org/event/executive-board-meeting-23/"
    )


def test_links():
    assert parsed_item["links"] == []


def test_classification():
    assert parsed_item["classification"] == NOT_CLASSIFIED


@pytest.mark.parametrize("item", parsed_items)
def test_all_day(item):
    assert item["all_day"] is False
