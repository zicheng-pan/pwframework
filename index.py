# coding: utf8
from xin import SYLFK
from xin.view import BaseView,Controller
from xin import simple_template

app = SYLFK()
@app.route('/index', methods=['GET'])
def index():
    return '这是一个路由测试页面'


@app.route("/test/js")
def test_js():
   return '<script src="/static/test.js"></script>'

#use view to add rule

class Index(BaseView):
    def get(self, request):
        return simple_template("index.html", user="shiyanlou_001", message="实验楼，你好")

class Test(Index):
    def post(self, request):
        return "这是一个POST请求"

syl_url_map = [
    {
        'url': '/shiyanlou',
        'view': Index,
        'endpoint': 'index'
    },
    {
        'url': '/test',
        'view': Test,
        'endpoint': 'test'
    }
]

index_controller = Controller('index', syl_url_map)
app.load_controller(index_controller)

app.run()

