from datetime import datetime
from os.path import dirname, join

import pytest
from city_scrapers_core.constants import COMMITTEE, PASSED
from city_scrapers_core.utils import file_response
from freezegun import freeze_time

from city_scrapers.spiders.wicks_wampo_tabs import WampoECSpider

test_response = file_response(
    join(dirname(__file__), "files", "wicks_wampo_ec.html"),
    url="https://www.wampo.org/executive-committee",
)
spider = WampoECSpider()

freezer = freeze_time(datetime(2024, 3, 15, 13, 37))
freezer.start()

parsed_items = [item for item in spider.parse(test_response)]
parsed_item = parsed_items[0]
freezer.stop()


def test_title():
    assert parsed_item["title"] == "Executive Committee Meeting"


def test_description():
    assert parsed_item["description"] == ""


def test_start():
    assert parsed_item["start"] == datetime(2023, 5, 4, 11, 0)


def test_end():
    assert parsed_item["end"] is None


def test_time_notes():
    assert parsed_item["time_notes"] == ""


def test_id():
    assert (
        parsed_item["id"] == "wicks_wampo_ec/202305041100/x/executive_committee_meeting"
    )


def test_status():
    assert parsed_item["status"] == PASSED


def test_location():
    assert parsed_item["location"] == {
        "name": "Wichita Area Metropolitan Planning Organization",
        "address": "271 W. 3rd St. N., Suite 101, Wichita, KS 67202",
    }


def test_source():
    assert parsed_item["source"] == "https://www.wampo.org/executive-committee"


def test_links():
    assert parsed_item["links"] == [
        {
            "href": "https://www.wampo.org/_files/ugd/bbf89d_f0a9bee735da48f8ab7bfcc65d518586.pdf",  # noqa
            "title": "Agenda Packet",
        }
    ]


def test_classification():
    assert parsed_item["classification"] == COMMITTEE


@pytest.mark.parametrize("item", parsed_items)
def test_all_day(item):
    assert item["all_day"] is False
