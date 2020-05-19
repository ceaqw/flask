# describe: flask 初次使用测试

from flask import Flask, redirect, abort, make_response, request, render_template
from werkzeug.routing import BaseConverter
from flask_script import Manager


class Regex_url(BaseConverter):
    """声明正则表达式方法"""
    def __init__(self, url_map, *args):
        super(Regex_url, self).__init__(url_map)
        self.regex = args[0]


app = Flask(__name__)
app.url_map.converters['re'] = Regex_url

# manger管理运行函数
# manger = Manager(app)

# 捕获整形数据
@app.route("/<int:id>")
def index(id):
    # 中断函数，执行后面代码不执行
    abort(404)
    return """<h1 style="font-size: 600px;"> %s </h1>""" % id


@app.route("/abort")
def abort_deal():
    # 中断函数，执行后面代码不执行
    abort(404)
    return "The part is no show!"


# 异常捕获
@app.errorhandler(404)
def error(e):
    return "Get a error request! %s" % e


# 重定向
@app.route("/baidu")
def redirect_baidu():
    return redirect("https://www.baidu.com")


@app.route('/<re(r"[a-z]{3}"):str>')
def getStrByRe(str):
    return "Choose string is %s" % str


# 设置cookie
@app.route("/set_cookie")
def set_cookies():
    resp = make_response("The will set a cookie")
    resp.set_cookie("username", "ceaqw")

    return resp


# 获取cookie
@app.route("/get_cookie")
def get_cookies():
    resp = request.cookies.get("username")
    return resp


# 模板语法测试if语句
@app.route('/user/<name>')
def temp_user(name):
    print(name)
    return render_template('user_temp_test.html', name=name)


if __name__ == '__main__':
    app.run(debug=True)
