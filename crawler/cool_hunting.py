# -*- coding: utf-8 -*-
""" Script to crawl Article from coolhunting.com

cool-hunting
"""

try:
    from crawler import BaseCrawler
except:
    from __init__ import BaseCrawler


class CCoolHuntingCrawler(BaseCrawler):
    start_urls = [
        'https://coolhunting.com/tag/marijuana',
        'https://coolhunting.com/tag/cannabis',
        'https://coolhunting.com/tag/weed',
    ]

    # source = 'COOL HUNTING'
    source_id = 'cool-hunting'

    config_selectors = {
        # Css selector on articles page (the page list many articles)
        'POST_URLS': '.entry-title > a::attr(href)',
        'NEXT_PAGE_URL': 'a.next::attr(href)',  # default

        # Css selector on article's detail page (the page display full content of article)
        'ARTICLE_CONTENT': '#main div.entry-content',
    }


if __name__ == "__main__":
    crawler = CCoolHuntingCrawler()
    crawler.run()