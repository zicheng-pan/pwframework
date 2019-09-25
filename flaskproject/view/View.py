# encoding: utf-8
# 视图基类
class View:
    # 支持的请求方法
    methods = None

    # 请求处理函数映射
    methods_meta = None

    # 视图处理函数调度入口
    def dispatch_request(self, request, *args, **option):
        raise NotImplementedError

    # 生成视图处理函数，参数 name 其实就是节点名
    @classmethod
    def get_func(cls, name):
        # 定义处理函数
        def func(*args, **kwargs):
            # 在处理函数内部实例化视图对象
            obj = func.view_class()

            # 通过视图对象调用处理函数调度入口，返回视图处理结果
            return obj.dispatch_request(*args, **kwargs)

        # 为处理函数绑定属性
        func.view_class = cls
        func.__name__ = name
        func.__doc__ = cls.__doc__
        func.__module__ = cls.__module__
        func.methods = cls.methods

        # 返回这个处理函数
        return func
