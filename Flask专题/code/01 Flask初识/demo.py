from flask import Flask  # 导入 Flask 类，创建 Flask 应用对象

app = Flask(__name__)  # app = application

app.debug = True  # 设置 debug 模式，方便调试


@app.route("/index")  # 为 Flask 对象增加路由
def index():  # 与路由绑定的视图函数，函数名尽量保持唯一
    return "Hello, Flask"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)  # 启动 Flask 应用程序
    # app.run(host="0.0.0.0", port=8000, debug=True)  # 也可以在启动程序的位置设置 debug 模式
