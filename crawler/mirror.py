# -*- coding: utf-8 -*-
""" Script to crawl Article from mirror.co.uk

mirror
"""

try:
    from crawler import BaseCrawler
except:
    from __init__ import BaseCrawler


class CMirrorCrawler(BaseCrawler):
    start_urls = [
        'https://www.mirror.co.uk/all-about/cannabis',

    ]

    # source = 'Mirror'
    source_id = 'mirror'

    config_selectors = {
        # Css selector on articles page (the page list many articles)
        'POST_URLS': 'a.headline::attr(href)',
        'NEXT_PAGE_URL': '.pagi-next > a::attr(href)',

        # Css selector on article's detail page (the page display full content of article)
        'ARTICLE_CONTENT': 'div.article-body > p',
    }


if __name__ == "__main__":
    crawler = CMirrorCrawler()
    crawler.run()