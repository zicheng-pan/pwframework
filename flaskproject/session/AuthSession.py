class AuthSession:

    # Session У��װ����
    @classmethod
    def auth_session(cls, f, *args, **options):

        def decorator(obj, request):
            return f(obj, request) if cls.auth_logic(request, *args, **options) else cls.auth_fail_callback(request, *args, **options)
        return decorator

    # ��֤�߼��Ľӿڣ�����һ������ֵ
    @staticmethod
    def auth_logic(request, *args, **options):
        raise NotImplementedError

    # ��֤ʧ�ܵĻص��ӿ�
    @staticmethod
    def auth_fail_callback(request, *args, **options):
        raise NotImplementedError