# encoding: utf-8
# 会话
from flaskproject.session import get_session_id
import os
import json
import base64


class Session:
    # Session 实例对象
    __instance = None

    # 初始化方法
    def __init__(self):

        # 会话映射表
        self.__session_map__ = {}
        # 会话本地存放目录
        self.__storage_path__ = None

    # 设置会话保存目录
    def set_storage_path(self, path):
        self.__storage_path__ = path

    # 保存会话记录到本地
    def storage(self, session_id):
        # 构造 Session 会话的本地文件路径，文件名为 Session ID
        session_path = os.path.join(self.__storage_path__, session_id)

        # 如果已设置 Session 会话存放路径，则开始缓存到本地
        if self.__storage_path__ is not None:
            with open(session_path, 'wb') as f:
                # 将会话记录序列化为字符串
                content = json.dumps(self.__session_map__[session_id])

                # 进行 base64 编码再写入文件中，防止一些特定二进制数据无法正确写入
                f.write(base64.encodebytes(content.encode()))

    # 单例模式，实现全局公用一个 Session 实例对象
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super(Session, cls).__new__(cls, *args, **kwargs)
        return cls.__instance

    # 更新或添加记录
    def push(self, request, item, value):

        # 从请求中获取客户端的 Session ID
        session_id = get_session_id(request)

        # 如果这个 Session ID 已存在与映射表中，则直接为其添加新的数据键值对，如果不存在，则先初始化为空的字典，再添加数据键值对
        if session in self.__session_map__:
            # 直接对当前会话添加数据
            self.__session_map__[get_session_id(request)][item] = value
        else:
            # 初始化当前会话
            self.__session_map__[session_id] = {}
            # 对当前会话添加数据
            self.__session_map__[session_id][item] = value

        self.storage(session_id)

    # 删除当前会话的某个项
    def pop(self, request, item, value=True):
        # 获取当前会话
        session_id = get_session_id(request)
        # 获取当前会话
        current_session = self.__session_map__.get(get_session_id(request), {})

        # 判断数据项的键是否存在于当前的会话中，如果存在则删除
        if item in current_session:
            current_session.pop(item, value)
            self.storage(session_id)


# 单例全局对象
session = Session()
