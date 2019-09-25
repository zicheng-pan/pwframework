# encoding: utf-8
from flaskproject.view.View import View


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
