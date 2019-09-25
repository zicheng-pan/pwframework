# encoding: utf-8
# 控制器类
class Controller:

    def __init__(self, name, url_map):
        self.url_map = url_map  # 存放映射关系，一个元素为 Dict 的 List
        self.name = name  # 控制器名字，生成节点时是会用到，为了区分不同控制器下同名的视图对象

    def __name__(self):
        # 返回控制器名字
        return self.name
