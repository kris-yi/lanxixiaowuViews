# -*- coding: utf-8 -*-
import scrapy
from lanxixiaowu.items import LanxixiaowuItem


class LxxwSpider(scrapy.Spider):
    name = 'lxxw'
    allowed_domains = ['lanxixiaowu.com']
    start_urls = ['https://www.lanxixiaowu.com/forum.php']

    cookies = {}

    def parse(self, response):
        ul = response.css('.mn dt')
        for li in ul:
            url = li.css('a::attr(href)').extract_first()
            title = li.css('a::text').extract_first()
            yield response.follow(url, meta={'title': title}, callback=self.get_ul)

    def get_ul(self, response):
        ul = response.css('#threadlisttableid .forumtit')
        title = response.meta['title']
        next_page_url = response.css('a.nxt::attr(href)').extract_first()
        if ul is None:
            url = response.css('#ttp_all a::attr(href)').extract_first()
            yield response.follow(url, meta={'title': title}, callback=self.get_ul)
        else:
            for li in ul:
                url = li.css('.forumtit a.s.xst::attr(href)').extract_first()
                name = li.css('.forumtit a.s.xst::text').extract_first()
                yield response.follow(url, meta={'name': name, 'title': title}, callback=self.get_views)

        if next_page_url is not None:
            yield response.follow(next_page_url, meta={'title': title}, callback=self.get_ul)

    def get_views(self, response):
        item = LanxixiaowuItem()
        item["title"] = response.meta['title']
        item["name"] = response.meta['name']
        error_msg = response.css('#messagetext p:nth-child(1)::text').extract_first()
        if error_msg is None:
            item["views"] = response.css('.ico_see::text').extract_first()
        else:
            item["views"] = error_msg

        item["url"] = response.url
        yield item
