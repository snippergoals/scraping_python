# -*- coding: utf-8 -*-
""" Script to crawl Article from salon.com

salon
"""

try:
    from crawler import BaseCrawler
except:
    from __init__ import BaseCrawler


class CSalonCrawler(BaseCrawler):
    start_urls = [
        'https://www.salon.com/topic/cannabis',
        'https://www.salon.com/topic/marijuana',
    ]

    # source = 'Salon'
    source_id = 'salon'

    config_selectors = {

        # Css selector on articles page (the page list many articles)
        'POST_URLS': '.card-article > a::attr(href)',
        'NEXT_PAGE_URL': '.next-button::attr(href)',  # default

        # Css selector on article's detail page (the page display full content of article)
        'ARTICLE_CONTENT': '.scroll-posts > article > p',

    }


if __name__ == "__main__":
    crawler = CSalonCrawler()
    crawler.run()