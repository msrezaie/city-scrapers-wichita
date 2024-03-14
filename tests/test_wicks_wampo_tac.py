from datetime import datetime
from os.path import dirname, join

import pytest
from city_scrapers_core.constants import BOARD, PASSED
from city_scrapers_core.utils import file_response
from freezegun import freeze_time

from city_scrapers.spiders.wicks_wampo_tac import WicksWampoTacSpider

test_response = file_response(
    join(dirname(__file__), "files", "wicks_wampo_tac.html"),
    url="https://www.wampo.org/technical-advisory-committee",
)
spider = WicksWampoTacSpider()

freezer = freeze_time(datetime(2024, 3, 14, 14, 23))
freezer.start()

parsed_items = [item for item in spider.parse(test_response)]
parsed_item = parsed_items[0]
freezer.stop()


def test_title():
    assert parsed_item["title"] == "WAMPO Transportation Policy Body Meeting"


def test_description():
    assert parsed_item["description"] == ""


def test_start():
    assert parsed_item["start"] == datetime(2024, 1, 14, 10, 0)


def test_end():
    assert parsed_item["end"] is None


def test_time_notes():
    assert parsed_item["time_notes"] == ""


def test_id():
    assert (
        parsed_item["id"]
        == "wicks_wampo_tac/202401141000/x/wampo_transportation_policy_body_meeting"
    )


def test_status():
    assert parsed_item["status"] == PASSED


def test_location():
    assert parsed_item["location"] == {
        "name": "Wichita Area Metropolitan Planning Organization",
        "address": "271 W 3rd St N, Wichita, KS 67202",
    }


def test_source():
    assert parsed_item["source"] == "https://www.wampo.org/technical-advisory-committee"


def test_links():
    assert parsed_item["links"] == [
        {
            "href": "https://www.wampo.org/_files/ugd/bbf89d_02a78f0fb9c24886998245c53019d994.pdf",  # noqa
            "title": "Agenda Pack",
        },
        {
            "href": "https://www.wampo.org/_files/ugd/bbf89d_1471b553e5e54ffdb3fa8cdd0821f829.pdf",  # noqa
            "title": "Minutes",
        },
        {"href": "https://www.youtube.com/watch?v=ATbfnexxAhg", "title": "Record"},
        {
            "href": "https://www.wampo.org/_files/ugd/bbf89d_96c56756159b4989953c130cbe6ab49c.pdf",  # noqa
            "title": "Safer Speeds Presentatio",
        },
        {
            "href": "https://www.wampo.org/_files/ugd/bbf89d_96c56756159b4989953c130cbe6ab49c.pdf",  # noqa
            "title": "n Slides",
        },
    ]


def test_classification():
    assert parsed_item["classification"] == BOARD


@pytest.mark.parametrize("item", parsed_items)
def test_all_day(item):
    assert item["all_day"] is False
