from datetime import datetime, time
from unicodedata import normalize

from city_scrapers_core.constants import BOARD
from city_scrapers_core.items import Meeting
from city_scrapers_core.spiders import CityScrapersSpider
from dateutil.parser import parse


class WicksWampoTacSpider(CityScrapersSpider):
    name = "wicks_wampo_tac"
    agency = (
        "Wichita Area Metropolitan Planning Organization - Technical Advisory Committee"
    )
    timezone = "America/Chicago"
    start_urls = ["https://www.wampo.org/technical-advisory-committee"]
    meeting_time = time(10, 0)
    location = {
        "name": "Wichita Area Metropolitan Planning Organization",
        "address": "271 W 3rd St N, Wichita, KS 67202",
    }

    def parse(self, response):
        """
        Parse HTML from agency page. Note that certain key details are absent
        like title and meeting time, so we hardcode them. However, page offers
        good collection of links to meeting agendas and minutes.
        """
        columns = response.css(
            'section.wixui-column-strip div[data-testid="columns"] div[data-testid="richTextElement"]'  # noqa
        )
        for column in columns:
            # get year
            year = column.css("h2 span::text").extract()
            if not year:
                continue
            year_parsed = "".join(year[:2]).strip()
            # parse rows
            for item in column.css("ul > li > p"):
                start = self._parse_start(item, year_parsed)
                if not start:
                    self.logger.info("No start time found – skipping")
                    continue
                meeting = Meeting(
                    title="WAMPO Transportation Policy Body Meeting",
                    description="",
                    classification=BOARD,
                    start=start,
                    end=None,
                    all_day=False,
                    time_notes="",
                    location=self.location,
                    links=self._parse_links(item),
                    source=response.url,
                )
                meeting["status"] = self._get_status(meeting)
                meeting["id"] = self._get_id(meeting)

                yield meeting

    def _parse_start(self, item, parsed_year):
        """Parse start datetime as a naive datetime object."""
        date_str = item.css("span[style*='font-weight:bold']::text").extract_first()
        if not date_str:
            return None
        try:
            # parse date in format "01/01/2020"
            date_str_w_year = f"{date_str}/{parsed_year}"
            parsed_date = parse(date_str_w_year, fuzzy=True)
            full_start = datetime.combine(parsed_date, self.meeting_time)
            return full_start
        except ValueError:
            self.logger.info(f"Failed to parse date: {date_str}")
            return None

    def _parse_links(self, item):
        """Parse links to meeting agendas and minutes. HTML is
        very messy. Display text is often split across multiple
        span tags. In some cases, multiple a tags make up the same
        link (Eg. "Re", "cording")."""
        link_text = []
        link_hrefs = []
        for link in item.css("a"):
            url = link.attrib["href"]
            # get text from all child spans
            title = "".join(link.css("::text").extract()).strip()
            # Strip white space and remove special characters
            clean_title = (
                normalize("NFKD", title).encode("ascii", "ignore").decode("utf-8")
            )
            if url in link_hrefs:
                # if link already exists, append to corresponding text
                index = link_hrefs.index(url)
                link_text[index] += clean_title
            else:
                link_hrefs.append(url)
                link_text.append(clean_title)
        # zip together
        links = []
        for i, title in enumerate(link_text):
            links.append({"title": title, "href": link_hrefs[i]})
        return links
