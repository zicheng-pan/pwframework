from flask.wsgi_adapter.wsgi_main import FlaskMain as Flask

app = Flask()

@app.route('/index', methods=['GET'])
def index():
    return '这是一个路由测试页面'

@app.route("/test/js")
def test_js():
    return '<script src="/static/test/test.js"></script>'

app.run()
