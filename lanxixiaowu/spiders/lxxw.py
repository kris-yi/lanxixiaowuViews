# -*- coding: utf-8 -*-
import scrapy
from lanxixiaowu.items import LanxixiaowuItem


class LxxwSpider(scrapy.Spider):
    name = 'lxxw'
    allowed_domains = ['lanxixiaowu.com']
    start_urls = [
        'https://www.lanxixiaowu.com/forum.php?mod=forumdisplay&fid=215&filter=author&orderby=dateline',
        'https://www.lanxixiaowu.com/forum.php?mod=forumdisplay&fid=63&filter=author&orderby=dateline',
        'https://www.lanxixiaowu.com/forum.php?mod=forumdisplay&fid=75&filter=author&orderby=dateline',
        'https://www.lanxixiaowu.com/forum.php?mod=forumdisplay&fid=75&filter=author&orderby=dateline',
        'https://www.lanxixiaowu.com/forum.php?mod=forumdisplay&fid=127&filter=author&orderby=dateline',
        'https://www.lanxixiaowu.com/forum.php?mod=forumdisplay&fid=132&filter=author&orderby=dateline',
        'https://www.lanxixiaowu.com/forum.php?mod=forumdisplay&fid=89&filter=author&orderby=dateline',
        'https://www.lanxixiaowu.com/forum.php?mod=forumdisplay&fid=295&filter=author&orderby=dateline',
        'https://www.lanxixiaowu.com/forum.php?mod=forumdisplay&fid=296&filter=author&orderby=dateline',
        'https://www.lanxixiaowu.com/forum.php?mod=forumdisplay&fid=297&filter=author&orderby=dateline',
        'https://www.lanxixiaowu.com/forum.php?mod=forumdisplay&fid=200&filter=author&orderby=dateline',
        'https://www.lanxixiaowu.com/forum.php?mod=forumdisplay&fid=67&filter=author&orderby=dateline',
        'https://www.lanxixiaowu.com/forum.php?mod=forumdisplay&fid=68&filter=author&orderby=dateline',
        'https://www.lanxixiaowu.com/forum.php?mod=forumdisplay&fid=69&filter=author&orderby=dateline',
        'https://www.lanxixiaowu.com/forum.php?mod=forumdisplay&fid=115&filter=author&orderby=dateline',
        'https://www.lanxixiaowu.com/forum.php?mod=forumdisplay&fid=99&filter=author&orderby=dateline',
        'https://www.lanxixiaowu.com/forum.php?mod=forumdisplay&fid=216&filter=author&orderby=dateline',
        'https://www.lanxixiaowu.com/forum.php?mod=forumdisplay&fid=105&filter=author&orderby=dateline',
        'https://www.lanxixiaowu.com/forum.php?mod=forumdisplay&fid=153&filter=author&orderby=dateline',
        'https://www.lanxixiaowu.com/forum.php?mod=forumdisplay&fid=90&filter=author&orderby=dateline',
        'https://www.lanxixiaowu.com/forum.php?mod=forumdisplay&fid=74&filter=author&orderby=dateline',
        'https://www.lanxixiaowu.com/forum.php?mod=forumdisplay&fid=106&filter=author&orderby=dateline',
        'https://www.lanxixiaowu.com/forum.php?mod=forumdisplay&fid=45&filter=author&orderby=dateline',
        'https://www.lanxixiaowu.com/forum.php?mod=forumdisplay&fid=49&filter=author&orderby=dateline',
        'https://www.lanxixiaowu.com/forum.php?mod=forumdisplay&fid=119&filter=author&orderby=dateline',
        'https://www.lanxixiaowu.com/forum.php?mod=forumdisplay&fid=70&filter=author&orderby=dateline',
    ]

    # cookies = {}
    # headers = {
    #     'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.82 Safari/537.36'
    # }
    # meta = {
    #     'dont_redirect': True,  # 禁止网页重定向
    #     'handle_httpstatus_list': [301, 302]  # 对哪些异常返回进行处理
    # }

    def parse(self, response):
        ul = response.css('#threadlisttableid .forumtit')
        item = LanxixiaowuItem()
        item["title"] = response.css('title::text').extract_first().split('-')[0]
        for li in ul:
            item["name"] = li.css('.forumtit a.s.xst::text').extract_first()
            item["views"] = li.css('.lx_view::text').extract_first()
            yield item

        next_page_url = response.css('a.nxt::attr(href)').extract_first()
        if next_page_url is not None:
            yield response.follow(next_page_url, callback=self.parse)
