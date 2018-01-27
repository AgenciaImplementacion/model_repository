#!/usr/bin/python3
import os
import pystache

def parse(origin, destiny, obj):
    f = open(origin, 'r')
    text = f.readlines()
    text = str.join('', text)
    f.close()
    parsed = pystache.render(text, obj)

    f = open(destiny, 'w')
    f.write(parsed)
    f.close()


obj = {'items': [
        {'name': 'LADM_COL', 'link': 'LADM_COL', 'img': 'img/folder.gif'},
        {'name': 'tools', 'link': 'tools', 'img': 'img/folder.gif'},
        {'name': 'ilimodels.xml', 'link': 'ilimodels.xml', 'img': 'img/file.gif'},
        {'name': 'ilisite.xml', 'link': 'ilisite.xml', 'img': 'img/file.gif'},
        {'name': 'ModelRepository.pdf', 'link': 'ModelRepository.pdf', 'img': 'img/file.gif'}
        ]}
parse('html_template/index.html', 'html/index.html', obj)

obj = {'items': [
        {'name': 'IliVErrors.ili', 'link': 'IliVErrors.ili', 'img': '../img/file.gif'}
        ]}
parse('html_template/tools/index.html',
      'html/tools/index.html', obj)

items = [ {'name': i, 'link': i, 'img': '../img/file.gif'} for i in os.listdir('html/LADM_COL') ]
obj = {'items': items}
parse('html_template/LADM_COL/index.html',
      'html/LADM_COL/index.html', obj)
