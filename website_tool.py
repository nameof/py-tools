#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

import requests
from bs4 import BeautifulSoup as BS

charset_utf8 = 'utf8'
charset_gbk = 'gbk'
charset_gb2312 = 'gb2312'
charset_unicode = 'unicode'

def get_url_title(url):
    try:
        url = url.strip()
        header = {"Accept": "text/html,application/xhtml+xml,application/xml;",
                   "Accept-Encoding": "gzip",
                   "Accept-Language": "zh-CN,zh;q=0.8",
                   "Referer": "http://www.baidu.com/link?url=www.so.com&url=www.soso.com&&url=www.sogou.com",
                   "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36"
                   }
        html = requests.get(url, timeout=3, verify=False, headers=header).content
        if re.search(charset_gbk, html):
            html = html.decode(charset_gbk, 'replace').encode(charset_utf8)
        soup = BS(html, "lxml")
        if (soup.title):
            return to_utf8(soup.title.text)
        return BS(html, "xml").title.text
    except:
        return ''

def get_coding(strInput):
    if isinstance(strInput, unicode):
        return charset_unicode
    try:
        strInput.decode(charset_utf8)
        return charset_utf8
    except:
        pass
    try:
        strInput.decode(charset_gbk)
        return charset_gbk
    except:
        pass

def to_utf8(strInput):
    try:
        strCodingFmt = get_coding(strInput)
        if strCodingFmt == charset_utf8:
            return strInput
        elif strCodingFmt == charset_unicode:
            return strInput.encode(charset_utf8)
        elif strCodingFmt == charset_gbk:
            return strInput.decode(charset_gbk).encode(charset_utf8)
    except:
        return strInput