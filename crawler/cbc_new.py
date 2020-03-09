# -*- coding: utf-8 -*-
""" Script to crawl Article from cbc.ca

cbc-news
"""

try:
    from crawler import BaseCrawler
except:
    from __init__ import BaseCrawler


class CCBCNewsCrawler(BaseCrawler):
    start_urls = [
        'https://www.cbc.ca/news/topic/Tag/Cannabis',
    ]

    # source = 'CBC News'
    source_id = 'cbc-news'

    config_selectors = {

        # Css selector on articles page (the page list many articles)
        'POST_URLS': 'a.cardListing::attr(href)',
        # 'NEXT_PAGE_URL': '.pager-next > a::attr(href)',  # default

        # Css selector on article's detail page (the page display full content of article)
        'ARTICLE_PUBLISHED_AT': '.bylineDetails time::attr(datetime)',
        'ARTICLE_AUTHOR': '.bylineDetails .authorText a::text',
        'ARTICLE_CONTENT': '.byline + *'
    }


if __name__ == "__main__":
    crawler = CCBCNewsCrawler()
    crawler.run()