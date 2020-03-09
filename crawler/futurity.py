# -*- coding: utf-8 -*-
""" Script to crawl Article from futurity.org

futurity

https://www.futurity.org/topic/cannabis/
"""
import json
import scrapy
try:
    from crawler import BaseCrawler
except:
    from __init__ import BaseCrawler


class CFuturityCrawler(BaseCrawler):
    start_urls = [
        'https://www.futurity.org/wp/wp-admin/admin-ajax.php?id=&post_id=16182&slug=cannabis&canonical_url=https%3A%2F%2Fwww.futurity.org%2Ftopic%2Fcannabis%2F&posts_per_page=12&page=0&offset=0&post_type=post&repeater=default&seo_start_page=1&preloaded=false&preloaded_amount=0&tag=cannabis&order=DESC&orderby=date&action=alm_get_posts&query_type=standard',
    ]

    # source = 'Futurity'
    source_id = 'futurity'

    config_selectors = {
        # Css selector on articles page (the page list many articles)
        'POST_URLS': '.article-link::attr(href)',

        # Css selector on article's detail page (the page display full content of article)
        'ARTICLE_AUTHOR': '[rel="author"]::text',
        'ARTICLE_CONTENT': '.sticy-share-block ~ *',
    }

    def extract_post_urls(self, selector, html):
        jo = json.loads(html, strict=False)
        try:
            sel = scrapy.Selector(text=jo.get('html'))
            return sel.css(self.config_selectors.get('POST_URLS')).extract()
        except:
            return []

if __name__ == "__main__":
    crawler = CFuturityCrawler()
    crawler.run()