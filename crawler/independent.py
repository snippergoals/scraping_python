# -*- coding: utf-8 -*-
""" Script to crawl Article from independent.co.uk

independent
"""

try:
    from crawler import BaseCrawler
except:
    from __init__ import BaseCrawler


class CIndependentCrawler(BaseCrawler):
    start_urls = [
        'https://www.independent.co.uk/topic/cannabis',
        'https://www.independent.co.uk/topic/marijuana',

    ]

    # source = 'Independent'
    source_id = 'independent'

    config_selectors = {
        # Css selector on articles page (the page list many articles)
        'POST_URLS': '.article  > a::attr(href)',
        # 'NEXT_PAGE_URL': '.table-cell .th-btn::attr(href)',

        # Css selector on article's detail page (the page display full content of article)
        'ARTICLE_CONTENT': '.body-content',
        # 'ARTICLE_AUTHOR': '#engadget-article-meta-bar a.th-meta[data-ylk*=author]::text',
        # 'ARTICLE_PUBLISHED_AT': '[name="published_at"]::attr(content)',
    }


if __name__ == "__main__":
    crawler = CIndependentCrawler()
    crawler.run()