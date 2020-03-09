# -*- coding: utf-8 -*-
""" Script to crawl Article from newyorker.com

the-new-yorker
"""

try:
    from crawler import BaseCrawler
except:
    from __init__ import BaseCrawler


class CTheNewYorkerCrawler(BaseCrawler):
    start_urls = [
        'https://www.newyorker.com/tag/marijuana',
    ]

    # source = 'The New Yorker'
    source_id = 'the-new-yorker'

    config_selectors = {

        # Css selector on articles page (the page list many articles)
        'POST_URLS': 'ul[class*=River__list___] li > div > a:nth-child(2)::attr(href)',
        'NEXT_PAGE_URL': '[rel="next"]::attr(href)',  # default

        # Css selector on article's detail page (the page display full content of article)
        'ARTICLE_CONTENT': 'div#articleBody',

    }


if __name__ == "__main__":
    crawler = CTheNewYorkerCrawler()
    crawler.run()