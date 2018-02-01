#!/usr/bin/python3
import os
import pystache
import glob

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

retval = os.getcwd()

def generate_index(pathname):
    global retval
    html_paht = retval + os.sep + 'html'
    rel_path = os.path.relpath(html_paht, os.getcwd())
    rel_path = rel_path.replace('\\', '/') # chante to URI
    img_folder = rel_path + '/img/folder.gif'
    img_file = rel_path + '/img/file.gif'
    #print('rel_path', img_folder, img_file)
    items = [{'name': os.path.dirname(path), 'link': path, 'img': img_folder} for path in glob.glob('*/')]
    items.extend([{'name': file, 'link': file, 'img': img_file} for file in glob.glob('*.ili')])
    obj = {'items': items}
    parse(retval + os.sep + 'html_template/LADM_COL/index.html', 'index.html', obj)

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
