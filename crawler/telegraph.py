# -*- coding: utf-8 -*-
""" Script to crawl Article from telegraph.co.uk

the-telegraph
"""

try:
    from crawler import BaseCrawler
except:
    from __init__ import BaseCrawler


class CTelegraphCrawler(BaseCrawler):
    start_urls = [
        'https://www.telegraph.co.uk/cannabis/',

    ]

    # source = 'The Telegraph'
    source_id = 'the-telegraph'

    config_selectors = {
        # Css selector on articles page (the page list many articles)
        'POST_URLS': '.card__heading > a::attr(href)',
        'NEXT_PAGE_URL': '.pagination__link--next::attr(href)',

        # Css selector on article's detail page (the page display full content of article)
        'ARTICLE_CONTENT': '[itemprop="articleBody"]',
        # 'ARTICLE_AUTHOR': '#engadget-article-meta-bar a.th-meta[data-ylk*=author]::text',
        'ARTICLE_PUBLISHED_AT': '[itemprop="datePublished"]::attr(datetime)',
    }


if __name__ == "__main__":
    crawler = CTelegraphCrawler()
    crawler.run()