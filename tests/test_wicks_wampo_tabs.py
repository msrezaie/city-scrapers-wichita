from datetime import datetime, time
from unittest.mock import MagicMock

import pytest
import scrapy

from city_scrapers.mixins.wampo_tabs import WampoMixinTabs


class TestWampoMixinTabs:
    @pytest.fixture
    def mixin(self):
        # Setup a basic instance of the mixin
        # Ensure the required static vars are set
        class TestSpider(WampoMixinTabs):
            name = "test_spider"
            agency = "Test Agency"
            start_urls = ["http://example.com"]
            start_time = time(9, 0)
            location = {
                "name": "Test Location",
                "address": "123 Test St, Test City, Test State",
            }

        return TestSpider()

    def test_parse_start_with_valid_date(self, mixin):
        # Mocking item to test _parse_start with a valid date format
        item = MagicMock()
        item.css().extract.return_value = ["November 12, 2024"]
        mixin.start_time = time(9, 30)  # Setting start time for the test

        parsed_start = mixin._parse_start(item)
        assert parsed_start == datetime(
            2024, 11, 12, 9, 30
        ), "Failed to parse start date and time correctly."

    def test_parse_start_with_invalid_date(self, mixin):
        # Mocking item to test _parse_start with an invalid date format
        item = MagicMock()
        item.css().extract.return_value = ["Invalid Date"]

        parsed_start = mixin._parse_start(item)
        assert parsed_start is None, "Should return None for invalid date formats."

    def test_parse_links(self, mixin):
        item = scrapy.Selector(
            text="<p><a href='http://example.com/meeting-details'><span>Meeting</span> <span>details</span></a></p>"  # noqa
        )
        links = mixin._parse_links(item)
        assert len(links) == 1, "Failed to parse the correct number of links."
        assert (
            links[0]["href"] == "http://example.com/meeting-details"
        ), "Link href parsed incorrectly."
        assert links[0]["title"] == "Meeting details", "Link title parsed incorrectly."

    def test_mixin_initialization_requires_vars(self):
        # Testing that the mixin raises NotImplementedError if required
        # static vars are not defined
        with pytest.raises(NotImplementedError) as exc_info:

            class InvalidSpider(WampoMixinTabs):
                pass  # Missing required vars

        assert "must define the following static variable(s)" in str(
            exc_info.value
        ), "Mixin should raise NotImplementedError for missing required static variables."  # noqa
