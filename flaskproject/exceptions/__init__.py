# encoding: utf-8
class FlaskException(Exception):
    def __init__(self, code='', message='Error'):
        self.code = code
        self.message = message

    def __str__(self):
        return self.message


# 节点已存在存在
class EndpointExistsError(FlaskException):
    def __init__(self, message='Endpoint exists'):
        super(EndpointExistsError, self).__init__(message)


# URL 已存在异常
class URLExistsError(FlaskException):
    def __init__(self, message='URL exists'):
        super(URLExistsError, self).__init__(message)
