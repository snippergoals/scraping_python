# -*- coding: utf-8 -*-
""" Script to crawl Article from engadget.com

engadget
"""

try:
    from crawler import BaseCrawler
except:
    from __init__ import BaseCrawler


class CEndgadgetCrawler(BaseCrawler):
    start_urls = [
        'https://www.engadget.com/tag/cannabis/',

    ]

    # source = 'Endgadget'
    source_id = 'engadget'

    config_selectors = {
        # Css selector on articles page (the page list many articles)
        'POST_URLS': '.o-hit__link::attr(href), .th-title > h2 > a::attr(href)',
        'NEXT_PAGE_URL': '.table-cell .th-btn::attr(href)',

        # Css selector on article's detail page (the page display full content of article)
        'ARTICLE_CONTENT': '#page_body div.o-article_block .article-text',
        'ARTICLE_AUTHOR': '#engadget-article-meta-bar a.th-meta[data-ylk*=author]::text',
        'ARTICLE_PUBLISHED_AT': '[name="published_at"]::attr(content)',
        
    }


if __name__ == "__main__":
    crawler = CEndgadgetCrawler()
    crawler.run()