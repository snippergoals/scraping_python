# -*- coding: utf-8 -*-
""" Script to crawl Article from theguardian.com

the-guardian
"""

try:
    from crawler import BaseCrawler
except:
    from __init__ import BaseCrawler


class CTheGuardianCrawler(BaseCrawler):
    start_urls = [
        'https://www.theguardian.com/society/cannabis',
    ]

    # source = 'The Guardian'
    source_id = 'the-guardian'

    config_selectors = {

        # Css selector on articles page (the page list many articles)
        'POST_URLS': 'a[data-link-name="article"]::attr(href)',
        # 'NEXT_PAGE_URL': '.pager-next > a::attr(href)',  # default

        # Css selector on article's detail page (the page display full content of article)
        # 'ARTICLE_PUBLISHED_AT': '.published',
        'ARTICLE_AUTHOR': '[rel="author"] span[itemprop=name]::text',
        'ARTICLE_CONTENT': '.content__article-body > p',
    }

if __name__ == "__main__":
    crawler = CTheGuardianCrawler()
    crawler.run()