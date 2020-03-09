# -*- coding: utf-8 -*-
""" Script to crawl Article from refinery29.com

refinery29
"""

try:
    from crawler import BaseCrawler
except:
    from __init__ import BaseCrawler


class CRefinery29Crawler(BaseCrawler):
    start_urls = [
        'https://www.refinery29.com/en-us/marijuana',
    ]

    # source = 'Refinery29'
    source_id = 'refinery29'

    config_selectors = {

        # Css selector on articles page (the page list many articles)
        'POST_URLS': '.card  > a::attr(href)',
        # 'NEXT_PAGE_URL': '.pager-next > a::attr(href)',  # default

        # Css selector on article's detail page (the page display full content of article)
        'ARTICLE_PUBLISHED_AT': '.modified a ::text',
        'ARTICLE_AUTHOR': '.contributor a::text',
        'ARTICLE_CONTENT': '.body > div.section-outer-container:not(:first-child)',
    }

    def extract_published_at(self, selector):
        """
            Extract published date of article
            @param selector Scrapy.Selector object (https://docs.scrapy.org/en/latest/topics/selectors.html)

            @return Text Published date of article, return None if not found
        """
        return selector.xpath('//script[contains(., "datePublished")]/text()').re_first(r'"datePublished":"(.*?)"')
        
if __name__ == "__main__":
    crawler = CRefinery29Crawler()
    crawler.run()