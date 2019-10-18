#!/usr/bin/python3.4
import os
import pystache
import glob
import datetime

def parse(origin, destiny, obj):
    f = open(origin, 'r')
    text = f.readlines()
    text = str.join('', text)
    f.close()
    parsed = pystache.render(text, obj)

    f = open(destiny, 'w')
    f.write(parsed)
    f.close()

datestamp = '{0:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())

obj = {
    'items': [
        {'name': 'LADM_COL', 'link': 'LADM_COL', 'img': 'img/folder.gif'},
        {'name': 'ilimodels.xml', 'link': 'ilimodels.xml', 'img': 'img/file.gif'},
        {'name': 'ilisite.xml', 'link': 'ilisite.xml', 'img': 'img/file.gif'},
        {'name': 'ModelRepository.pdf', 'link': 'ModelRepository.pdf', 'img': 'img/file.gif'}
    ],
    'img_return': 'img/back.gif',
    'img_logo': 'img/agencia_implementacion_swissphoto_incige.png',
    'rel_path': '',
    'datestamp': datestamp
}
parse('html_template/index.html', 'html/index.html', obj)

retval = os.getcwd()

def generate_index(pathname):
    global retval, datestamp
    html_path = retval + os.sep + 'html'
    abs_path = os.getcwd()
    rel_path = os.path.relpath(html_path, abs_path)
    rel_path = rel_path.replace('\\', '/') # chante to URI
    rel_path += '/'
    current_path = os.path.relpath(abs_path, html_path)
    current_path = current_path.replace('\\', '/') # chante to URI in Windows
    current_path += '/'
    img_folder = 'img/folder.gif'
    img_file = 'img/file.gif'
    img_return = 'img/back.gif'
    img_logo = 'img/agencia_implementacion_swissphoto_incige.png'
    #print('rel_path', img_folder, img_file)
    items = [{'name': os.path.dirname(path), 'link': path, 'img': img_folder} for path in sorted(glob.glob('*/'))]
    items.extend([{'name': file, 'link': file, 'img': img_file} for file in sorted(glob.glob('*.ili'))])
    obj = {
        'items': items,
        'img_return': img_return,
        'img_logo': img_logo,
        'rel_path': rel_path,
        'current_path': current_path,
        'datestamp': datestamp
    }
    parse(retval + os.sep + 'html_template/index.html', 'index.html', obj)

os.chdir('html/LADM_COL')
initial_path = os.getcwd()
all_paths = [path[0] for path in os.walk('.')]
#print('all_paths', all_paths)
for current_path in all_paths:
    abs_path = initial_path + os.sep + current_path
    #print('abs_path', abs_path, initial_path, os.pathsep, current_path)
    os.chdir(abs_path)
    pathname = os.path.dirname(current_path)
    #print('pathname', pathname)
    generate_index(pathname)
    os.chdir(initial_path)
