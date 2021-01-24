#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

import requests


def request_crt(domain):
    url = 'https://crt.sh/?q=' + domain
    resp = requests.get(url)
    return resp

def process_body(body):
    domains = set()
    # in some cells, multiple domains separated by <BR>
    cells = re.findall(r'<TD>([^<].*)</TD>', body)
    for cell in cells:
        cell = cell.split('<BR>')
        for domain in cell:
            # 排除带通配符的域名
            if '*' not in domain:
                domains.add(domain)
    return sorted(domains)

def get_subdomains(domain):
    try:
        resp = request_crt(domain)
        return process_body(resp.text)
    except:
        print 'get info from crt.sh fail'
        return set([])