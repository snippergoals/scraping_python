# -*- coding: utf-8 -*-
""" Script to crawl Article from nymag.com

new-york-magazine
"""

try:
    from crawler import BaseCrawler
except:
    from __init__ import BaseCrawler


class CNewYorkMagazineCrawler(BaseCrawler):
    start_urls = [
        'https://nymag.com/tags/cannabis/',
        'https://nymag.com/tags/marijuana/',
    ]

    # source = 'New York Magazine'
    source_id = 'new-york-magazine'

    config_selectors = {
                # Css selector on articles page (the page list many articles)
        'POST_URLS': '.main-article-content > a::attr(href)',
        'NEXT_PAGE_URL': '.container-main .more-button::attr(href)',

        # Css selector on article's detail page (the page display full content of article)
        'ARTICLE_CONTENT': '.article-content',
        'ARTICLE_PUBLISHED_AT': '[name="datePublished"]::attr(content), [itemprop="datePublished"]::attr(datetime)',
    }


if __name__ == "__main__":
    crawler = CNewYorkMagazineCrawler()
    crawler.run()