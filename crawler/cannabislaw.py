# -*- coding: utf-8 -*-
""" Script to crawl Article from cannabislaw.report

cannabis-law-report
"""
try:
    from crawler import BaseCrawler
except:
    from __init__ import BaseCrawler

class CannabisLawReportCrawler(BaseCrawler):
    start_urls = [
        'https://cannabislaw.report/category/breaking-news/',
        'https://cannabislaw.report/category/cannabis-law-news/',
        'https://cannabislaw.report/category/dope/',
        'https://cannabislaw.report/category/medical-cannabis-news/',
    ]

    # source = 'Cannabis Law Report'
    source_id = 'cannabis-law-report'

    config_selectors = {
        'POST_URLS': '.paginated_content article .header >a::attr(href)',
        'ARTICLE_CONTENT': '.post-content',
        'ARTICLE_TITLE': 'h1.entry-title::text',
        'ARTICLE_URL_TO_IMAGE': '.post-thumbnail.header img::attr(src)',
    }


if __name__ == "__main__":
    crawler = CannabisLawReportCrawler()
    crawler.run()