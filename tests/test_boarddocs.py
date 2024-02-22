from datetime import datetime, timedelta
from unittest.mock import MagicMock

import pytest

from city_scrapers.mixins.boarddocs import BoardDocsMixin


class TestBoardDocsMixin:
    @pytest.fixture
    def mixin(self):
        # Setup a basic instance of the mixin
        # Ensure the required static vars are set
        class TestSpider(BoardDocsMixin):
            name = "test_spider"
            boarddocs_slug = "test_slug"
            boarddocs_committee_id = "test_committee_id"
            timezone = "America/Chicago"

        return TestSpider()

    def test_gen_random_int(self, mixin):
        # Test if gen_random_int generates a number within the expected range
        random_int = mixin.gen_random_int()
        assert 10**14 <= random_int < 10**15

    def test_get_clean_meetings(self, mixin):
        # Mocking data to test the cleaning process
        mock_data = [
            {"numberdate": "20230101", "unique": "1"},  # More than 2 months ago
            {"numberdate": datetime.now().strftime("%Y%m%d"), "unique": "2"},  # Today
            {},  # Empty item
        ]
        result = mixin._get_clean_meetings(mock_data)
        assert len(result) == 1  # Only one item should pass the filter
        assert result[0]["unique"] == "2"  # Ensure the correct item is retained

    def test_parse_start_with_time(self, mixin):
        # Mocking response and start_date to test _parse_start
        start_date = datetime.now().date()
        response = MagicMock()
        response.css.return_value.get.return_value = "10:00 AM │ Some description"

        parsed_start = mixin._parse_start(response, start_date)
        assert parsed_start.hour == 10 and parsed_start.minute == 0

    def test_parse_start_without_time(self, mixin):
        # Test parsing when no time is provided in the description
        start_date = datetime.now().date()
        response = MagicMock()
        response.css.return_value.get.return_value = "Some description without time"

        parsed_start = mixin._parse_start(response, start_date)
        assert parsed_start.hour == 0 and parsed_start.minute == 0

    def test_parse_title(self, mixin):
        # Mocking response to test _parse_title
        response = MagicMock()
        expected_title = "Test Meeting Title"
        response.css.return_value.get.return_value = expected_title

        title = mixin._parse_title(response)
        assert (
            title == expected_title
        ), "The parsed title does not match the expected value."

    def test_parse_description(self, mixin):
        # Mocking response to test _parse_description, including cleaning
        # HTML tags and normalizing whitespace
        response = MagicMock()
        response.css.return_value.getall.return_value = [
            "Description with  ",
            "  multiple spaces and line breaks  ",
        ]

        description = mixin._parse_description(response)
        assert (
            description == "Description with multiple spaces and line breaks"
        ), "The parsed description does not match the expected cleaned and normalized value."  # noqa

    def test_mixin_initialization_requires_vars(self):
        # Testing that the mixin raises NotImplementedError if required
        # static vars are not defined
        with pytest.raises(NotImplementedError) as exc_info:

            class InvalidSpider(BoardDocsMixin):
                pass  # Missing required vars

        assert "must define the following static variable(s)" in str(
            exc_info.value
        ), "Mixin should raise NotImplementedError for missing required static variables."  # noqa

    def test_get_clean_meetings_future_date(self, mixin):
        # Testing _get_clean_meetings with a future date to ensure it's included
        future_date = (datetime.now() + timedelta(days=60)).strftime("%Y%m%d")
        mock_data = [{"numberdate": future_date, "unique": "future_meeting"}]

        result = mixin._get_clean_meetings(mock_data)
        assert (
            len(result) == 1
        ), "Future meeting should be included in the cleaned data."
        assert (
            result[0]["unique"] == "future_meeting"
        ), "The unique identifier of the future meeting does not match."
