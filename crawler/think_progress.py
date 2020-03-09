# -*- coding: utf-8 -*-
""" Script to crawl Article from thinkprogress.org

thinkprogress
"""

try:
    from crawler import BaseCrawler
except:
    from __init__ import BaseCrawler


class CThinkProgressCrawler(BaseCrawler):
    start_urls = [
        'https://thinkprogress.org/tag/marijuana',
        'https://thinkprogress.org/tag/cannabis',
    ]

    # source = 'ThinkProgress'
    source_id = 'thinkprogress'

    config_selectors = {

        # Css selector on articles page (the page list many articles)
        'POST_URLS': '.post__title > a::attr(href)',
        'NEXT_PAGE_URL': '.load-more a::attr(href)',  # default

        # Css selector on article's detail page (the page display full content of article)
        'ARTICLE_PUBLISHED_AT': '.post__date::attr(datetime)',
        'ARTICLE_AUTHOR': '.post__byline__author > a[href*="/author/"]::text',
        'ARTICLE_CONTENT': '.post__content > *:not(.ad-wrapper)',

    }


if __name__ == "__main__":
    crawler = CThinkProgressCrawler()
    crawler.run()