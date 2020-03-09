# -*- coding: utf-8 -*-
""" Script to crawl Article from sfgate.com

sfgate
"""

import json
import re
from scrapy import Selector

try:
    from crawler import BaseCrawler
except:
    from __init__ import BaseCrawler


class CSFGateCrawler(BaseCrawler):
    start_urls = [
        'https://www.sfgate.com/cannabis',
        'https://blog.sfgate.com/smellthetruth/',
        'https://blog.sfgate.com/smellthetruth/section/business/',
        'https://blog.sfgate.com/smellthetruth/section/health/',
        'https://blog.sfgate.com/smellthetruth/section/lifestyle/',
        'https://blog.sfgate.com/smellthetruth/section/law/',
        'https://blog.sfgate.com/smellthetruth/category/activism/',
        'https://blog.sfgate.com/smellthetruth/category/science/',
        'https://blog.sfgate.com/smellthetruth/category/reviews-2/',
    ]

    # source = 'SFGate'
    source_id = 'sfgate'

    config_selectors = {

        # Css selector on articles page (the page list many articles)
        'POST_URLS': 'a[class*=blogPost]::attr(href), .blog-headline > a::attr(href), a[href*="/smellthetruth/"]:not([href*=author])::attr(href)',
        'NEXT_PAGE_URL': '.show-more-posts::attr(data-base-url)',
        # Css selector on article's detail page (the page display full content of article)
        'ARTICLE_AUTHOR': '[rel="author"]::text',
        'ARTICLE_CONTENT': '.article-body > p, .entry > p',
    }

    def __init__(self):
        super(CSFGateCrawler, self).__init__()
        # html = self._http_get('https://blog.sfgate.com/smellthetruth/').text
        # sel = Selector(text=html)
        # self.start_urls.extend(sel.css('[name="archive-dropdown"] option[value*=http]::attr(value)').getall())

    def extract_post_urls(self, selector, html):
        post_urls = super(CSFGateCrawler, self).extract_post_urls(selector, html)
        if not post_urls:
            jo = json.loads(html, strict=False)
            sel = Selector(text=jo.get('payload', ''))
            post_urls = super(CSFGateCrawler, self).extract_post_urls(sel, html)
        post_urls = [x.split('?')[0].split('#')[0] for x in post_urls]
        return post_urls

    def extract_next_page_url(self, selector, html, url):
        next_page_url = super(CSFGateCrawler, self).extract_next_page_url(selector, html, url)
        if not next_page_url and '"more_posts":true' in html:
            offset = url.split('&n=')[-1].split('&')[0]
            if offset.isdigit():
                offset = int(offset) + 10
                next_page_url = re.sub('&n=\d+', '&n={}'.format(offset), url)
        if next_page_url and 'admin-ajax.php' in next_page_url and '&n=' not in next_page_url:
            next_page_url = '{}&n=10'.format(next_page_url)
        return next_page_url


if __name__ == "__main__":
    crawler = CSFGateCrawler()
    crawler.run()