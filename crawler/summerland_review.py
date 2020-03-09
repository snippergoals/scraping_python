# -*- coding: utf-8 -*-
""" Script to crawl Article from summerlandreview.com

summerland-review
"""

try:
    from crawler import BaseCrawler
except:
    from __init__ import BaseCrawler


class CSummerlandReviewCrawler(BaseCrawler):
    start_urls = [
        'https://www.summerlandreview.com/tag/marijuana/',
    ]

    # source = 'Summerland Review'
    source_id = 'summerland-review'

    config_selectors = {

        # Css selector on articles page (the page list many articles)
        'POST_URLS': '.main-content h4 > a::attr(href)',
        'NEXT_PAGE_URL': 'a.next::attr(href)',  # default

        # Css selector on article's detail page (the page display full content of article)
        'ARTICLE_CONTENT': '.entry-content > p',

    }


if __name__ == "__main__":
    crawler = CSummerlandReviewCrawler()
    crawler.run()