from datetime import datetime
from os.path import dirname, join

import pytest
from city_scrapers_core.constants import BOARD, PASSED
from city_scrapers_core.utils import file_response
from freezegun import freeze_time

from city_scrapers.spiders.wicks_wampo_tpb import WicksWampoTPBSpider

test_response = file_response(
    join(dirname(__file__), "files", "wicks_wampo_tpb.html"),
    url="https://www.wampo.org/transportation-policy-body",
)
spider = WicksWampoTPBSpider()

freezer = freeze_time(datetime(2024, 3, 19, 11, 39))
freezer.start()

parsed_items = [item for item in spider.parse(test_response)]
parsed_item = parsed_items[0]
freezer.stop()


def test_title():
    assert parsed_item["title"] == "WAMPO Transportation Policy Body Meeting"


def test_description():
    assert parsed_item["description"] == ""


def test_start():
    assert parsed_item["start"] == datetime(2024, 1, 9, 15, 0)


def test_end():
    assert parsed_item["end"] is None


def test_time_notes():
    assert parsed_item["time_notes"] == ""


def test_id():
    assert (
        parsed_item["id"]
        == "wicks_wampo_tpb/202401091500/x/wampo_transportation_policy_body_meeting"
    )


def test_status():
    assert parsed_item["status"] == PASSED


def test_location():
    assert parsed_item["location"] == {
        "name": "Wichita Area Metropolitan Planning Organization",
        "address": "271 W 3rd St N, Wichita, KS 67202",
    }


def test_source():
    assert parsed_item["source"] == "https://www.wampo.org/transportation-policy-body"


def test_links():
    assert parsed_item["links"] == [
        {
            "title": "Agenda Packet",
            "href": "https://www.wampo.org/_files/ugd/bbf89d_bc9c575ffcd9480ca7bd7b8c7611857b.pdf",  # noqa
        },
        {
            "title": "Minutes",
            "href": "https://www.wampo.org/_files/ugd/bbf89d_8cf9fc33872e44d2a7ade0d2db6e5fae.pdf",  # noqa
        },
        {"title": "Recording", "href": "https://youtu.be/LsMI1EClvnI"},
    ]


def test_classification():
    assert parsed_item["classification"] == BOARD


@pytest.mark.parametrize("item", parsed_items)
def test_all_day(item):
    assert item["all_day"] is False
