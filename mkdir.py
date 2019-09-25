# this file to init project directory structure
# encoding: utf-8
###
#  folder structure
# ├── __init__.py  # 框架主体
# ├── dbconnector  # 数据库连接模块
# │     └── __init__.py
# ├── exceptions  # 异常模块
# │     └── __init__.py
# ├── helper  # 辅助模块
# │     └── __init__.py
# ├── route  # 路由模块
# │     └── __init__.py
# ├── session  # 会话模块
# │     └── __init__.py
# ├── template_engine  # 模版引擎模块
# │     └── __init.py
# ├── view  # 视图模块
# │     └── __init__.py
# └── wsgi_adapter  # WSGI 入口模块
# └── __init__.py
###

import os

root_path = os.getcwd()

directory_list = [
    'dbconnector',
    'exceptions',
    'helper',
    'route',
    'session',
    'template_engine',
    'view',
    'wsgi_adapter'
]

# base __init__.py file to create folder as module
children = {'name': '__init__.py', 'children': None, 'type': 'file'}

# build folder structure by object
dir_map = [{
    'name': 'flaskproject',  # project name
    'children': [
        {
            'name': directory_name,
            'children': [children],
            'type': 'directory'
        } for directory_name in directory_list
    ],
    'type': 'directory'
}
          ] + [children]


# notice: reminder to add folder hard where in disk
def create_folder(path, type):
    if 'file' == type:
        open(path, 'w').close()
    elif 'directory' == type:
        os.mkdir(path)


def create_project_module(path, dir_map):
    for line in dir_map:
        parent_path = os.path.join(path, line.get('name'))
        create_folder(parent_path, line.get('type'))
        if line.get('children'):
            create_project_module(parent_path, line.get('children'))


def main():
    create_project_module(root_path, dir_map)


if __name__ == '__main__':
    main()
