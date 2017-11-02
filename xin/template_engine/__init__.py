# coding: utf8
import os
import re

pattern = r'{{(.*?)}}'

def parse_args(obj):
    comp = re.compile(pattern)
    ret = comp.findall(obj)
    return ret if ret else ()

def replace_template(app,path,**options):
    content = '<h1>Not Found Template</h1>'

    path = os.path.join(app.template_folder,path)

    if os.path.exists(path):
        with open(path,'rb') as f: #rb 相对于r而言 不会将\r和\n进行转义
            content = f.read().decode()

        args = parse_args(content)
        if options:
            for arg in args:
                key = arg.strip()
                print(content)
                content = content.replace("{{%s}}" % arg, str(options.get(key,"")))
                print(arg + ' = '+str(options.get(key)))
    return content
