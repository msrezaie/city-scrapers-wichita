from datetime import datetime
from os.path import dirname, join

import pytest
from city_scrapers_core.constants import COMMITTEE, PASSED
from city_scrapers_core.utils import file_response
from freezegun import freeze_time

from city_scrapers.spiders.wicks_wampo_tabs import WicksWampoICTSSpider

test_response = file_response(
    join(dirname(__file__), "files", "wicks_wampo_icts.html"),
    url="https://www.wampo.org/ict-safe",
)
spider = WicksWampoICTSSpider()

freezer = freeze_time(datetime(2024, 3, 15, 14, 55))
freezer.start()

parsed_items = [item for item in spider.parse(test_response)]
parsed_item = parsed_items[0]
freezer.stop()


def test_title():
    assert parsed_item["title"] == "Executive Committee Meeting"


def test_description():
    assert parsed_item["description"] == ""


def test_start():
    assert parsed_item["start"] == datetime(2023, 11, 1, 9, 30)


def test_end():
    assert parsed_item["end"] is None


def test_time_notes():
    assert parsed_item["time_notes"] == ""


def test_id():
    assert (
        parsed_item["id"]
        == "wicks_wampo_icts/202311010930/x/executive_committee_meeting"
    )


def test_status():
    assert parsed_item["status"] == PASSED


def test_location():
    assert parsed_item["location"] == {
        "name": "Wichita Area Metropolitan Planning Organization",
        "address": "271 W. 3rd St. N., Suite 101, Wichita, KS 67202",
    }


def test_source():
    assert parsed_item["source"] == "https://www.wampo.org/ict-safe"


def test_links():
    assert parsed_item["links"] == [
        {
            "href": "https://www.wampo.org/_files/ugd/bbf89d_0a17c8baaddb4af7b28a8b59e05efbac.pdf",  # noqa
            "title": "Agenda",
        },
        {
            "href": "https://www.wampo.org/_files/ugd/bbf89d_2fa44cf8eb1a4d98a8191dfdc0f6a729.pdf",  # noqa
            "title": "Summary",
        },
        {
            "href": "https://www.wampo.org/_files/ugd/bbf89d_161d7db8eb714b20ba1ff4d0e72cf118.pdf",  # noqa
            "title": "CSAP & Vision Zero Slides",
        },
    ]


def test_classification():
    assert parsed_item["classification"] == COMMITTEE


@pytest.mark.parametrize("item", parsed_items)
def test_all_day(item):
    assert item["all_day"] is False
