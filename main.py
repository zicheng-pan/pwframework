from flaskproject.view.BasicView import BaseView
from flaskproject.view.Controller import Controller
from flaskproject.wsgi_adapter.wsgi_main import FlaskMain as Flask

app = Flask()


@app.route('/index', methods=['GET'])
def index():
    return '这是一个路由测试页面'


@app.route("/test/js")
def test_js():
    return '<script src="/static/test/test.js"></script>'


class Index(BaseView):
    def get(self, request):
        return '你好'


class Test(Index):
    def post(self, request):
        return "这是一个POST请求"


syl_url_map = [
    {
        'url': '/index/index',
        'view': Index,
        'endpoint': 'index'
    },
    {
        'url': '/index/test',
        'view': Test,
        'endpoint': 'test'
    }
]
index_controller = Controller('index', syl_url_map)
app.load_controller(index_controller)

app.run()
