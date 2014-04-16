#!/usr/bin/env python
import cssselect
from lxml.html import document_fromstring
import datetime
from requests import get
import ipdb

#amazon_string = 'http://www.amazon.com/gp/search/ref=sr_adv_b/?search-alias=digital-text&unfiltered=1&field-keywords=&field-author=Ray+Bradbury&field-title=&field-publisher=&node=&field-subject=&field-language=English&field-dateop=After&field-datemod=2&field-dateyear=2013&sort=relevanceexprank&Adv-Srch-Books-Submit.x=42&Adv-Srch-Books-Submit.y=11'
amazon_string = 'http://www.amazon.com/gp/search/ref=sr_adv_b/?search-alias=digital-text&unfiltered=1&field-keywords=&field-author=%s&field-title=&field-publisher=&node=&field-subject=&field-language=English&field-dateop=%s&field-datemod=%s&field-dateyear=%s&sort=relevanceexprank&Adv-Srch-Books-Submit.x=43&Adv-Srch-Books-Submit.y=7'


def fname():
    """docstring for fname"""
    pass

def get_results(url=None):
    doc = document_fromstring(get(url).text)
    res = [x for x in doc.cssselect('div') if 'result_' in x.attrib.get('id', '')]
    #ipdb.set_trace()
    if doc.cssselect('a#pagnNextLink'):
        res.extend(get_results(doc.cssselect('a#pagnNextLink')[0].attrib.get('href')))
    return res

def get_document(url = None):
    return document_fromstring(get(url).text)
    

  
def main():
    """docstring for main"""
    date_op = 'After'
    author = 'Ray+Bradbury'
    month = '2'
    year = '2013'
    results = get_results(amazon_string % (author, date_op, month, year))
    for d in results:
        print d.attrib
if __name__ == '__main__':
    main()