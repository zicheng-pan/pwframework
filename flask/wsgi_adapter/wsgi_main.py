# encoding: utf-8
from werkzeug.serving import run_simple
from werkzeug.wrappers import Response
from flask.wsgi_adapter import wsgi_app


class FlaskMain:

    def __init__(self):
        self.host = '127.0.0.1'  # default host
        self.port = 8086  # default port

    def dispatch_request(self,request):
        status = 200  # HTTPstatus code 200 success

        headers = {
            'Server': 'Fake Flask Framework'
        }

        # 回传实现 WSGI 规范的响应体给 WSGI 模块
        return Response('<h1>Hello, Framework</h1>', content_type='text/html', headers=headers, status=status)

    def run(self, host=None, port=None, **options):
        for key, value in options.items():
            if value is not None:
                self.__setattr__(key, value)

        if host:
            self.host = host

        if port:
            self.port = port

        # 把框架本身也就是应用本身和其它几个配置参数传给 werkzeug 的 run_simple
        run_simple(hostname=self.host, port=self.port, application=self, **options)

    def __call__(self, environ, start_response):
        return wsgi_app(self, environ, start_response)
