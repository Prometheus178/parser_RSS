from django.shortcuts import render
from xml.etree import cElementTree
import requests


def parseRSS(request):
    '''
    Parses first 10 items from https://meduza.io/rss/podcasts/meduza-v-kurse
    '''
    response = requests.get('https://meduza.io/rss/podcasts/meduza-v-kurse')
    parsed_xml = cElementTree.fromstring(response.content)
    items = []
    for node in parsed_xml.iter():
        if node.tag == 'item':
            item = {}
            for item_node in list(node):
                if item_node.tag == 'title':
                    item['title'] = item_node.text
                if item_node.tag == 'link':
                    item['link'] = item_node.text
                if item_node.tag == 'description':
                    item['description'] = item_node.text
            items.append(item)
    return render(request, 'Parser/index.html', {'items':items[:10]})
