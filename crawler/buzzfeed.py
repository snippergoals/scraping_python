# -*- coding: utf-8 -*-
""" Script to crawl Article from buzzfeed.com

buzzfeed
"""

try:
    from crawler import BaseCrawler
except:
    from __init__ import BaseCrawler


class CBuzzFeedCrawler(BaseCrawler):
    start_urls = [
        'https://www.buzzfeed.com/tag/marijuana',

    ]

    # source = 'BuzzFeed'
    source_id = 'buzzFeed'

    config_selectors = {
        # Css selector on articles page (the page list many articles)
        'POST_URLS': '.js-card__content h2 > a::attr(href)',

        # Css selector on article's detail page (the page display full content of article)
        'ARTICLE_CONTENT': '[data-module="subbuzz-text"]',
        'ARTICLE_AUTHOR': 'span.news-byline-full__name ::text, .buzz-byline  a.bold::text',
        'ARTICLE_PUBLISHED_AT': '.news-article-header__timestamps-posted::text, .buzz-timestamp__time::text',
    }

    # override method
    def extract_published_at(self, selector):
        v = super().extract_published_at(selector)
        if v is not None:
            v = v.split('Posted on')[-1].strip()
        return v

if __name__ == "__main__":
    crawler = CBuzzFeedCrawler()
    crawler.run()