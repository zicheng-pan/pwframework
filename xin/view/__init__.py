# coding: utf8
class View:
    methods = None

    methods_meta = None

    def dispath_request(self, request, *args, **option):
        raise NotImplementedError

    @classmethod
    def get_func(cls, name):
        def func(*args, **kwargs):
            obj = func.view_class()
            return obj.dispatch_request(*args, **kwargs)

        func.view_class = cls
        func.__name__ = name
        func.__doc__ = cls.__doc__
        func.__module__ = cls.__module__
        func.methods = cls.methods

        return func

class BaseView(View):
    # 定义支持的请求方法，默认支持 GET 和 POST 方法
    methods = ['GET, POST']

    # POST 请求处理函数
    def post(self, request, *args, **options):
        pass

    # GET 请求处理函数
    def get(self, request, *args, **options):
        pass

    # 视图处理函数调度入口
    def dispatch_request(self, request, *args, **options):
        # 定义请求方法与处理函数的映射
        methods_meta = {
            'GET': self.get,
            'POST': self.post,
        }

        # 判断该视图是支持所请求的方法，如果支持则返回对应处理函数的结果，反之返回错误提示
        if request.method in methods_meta:
            return methods_meta[request.method](request, *args, **options)
        else:
            return '<h1>Unknown or unsupported require method</h1>'


class Controller:
    def __init__(self, name, url_map):
        self.url_map = url_map  # 存放映射关系，一个元素为 Dict 的 List
        self.name = name  # 控制器名字，生成节点时是会用到，为了区分不同控制器下同名的视图对象

    def __name__(self):
        # 返回控制器名字
        return self.name