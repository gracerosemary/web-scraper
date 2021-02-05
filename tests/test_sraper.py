from web_scraper.scraper import get_citations_needed_count, get_citations_needed_report
import re

# verify that correct count of citations needed is calculated
def test_count():
    url = 'https://en.wikipedia.org/wiki/GameStop'
    actual = get_citations_needed_count(url)
    expected = 5
    assert actual == expected

# verify that preceding passage
def test_report():
    url = 'https://en.wikipedia.org/wiki/GameStop'
    def check():
        sentence = get_citations_needed_report(url)
        if '[citation needed]' in sentence:
            return 'Success!'
    check = check()
    actual = check
    expected = 'Success!'
    assert actual == expected 