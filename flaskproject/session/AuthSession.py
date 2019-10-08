# encoding: utf-8
class AuthSession:

    # Session 校验装饰器
    @classmethod
    def auth_session(cls, f, *args, **options):

        def decorator(obj, request):
            return f(obj, request) if cls.auth_logic(request, *args, **options) else cls.auth_fail_callback(request, *args, **options)
        return decorator

    # 验证逻辑的接口，返回一个布尔值
    @staticmethod
    def auth_logic(request, *args, **options):
        raise NotImplementedError

    # 验证失败的回调接口
    @staticmethod
    def auth_fail_callback(request, *args, **options):
        raise NotImplementedError