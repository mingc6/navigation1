from flask import Flask, render_template, request, redirect, url_for, flash
import subprocess

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # 用于安全性，实际使用时请更改


# 登录页面
@app.route('/')
def login():
    return render_template('login.html')


# 处理登录请求
@app.route('/login', methods=['POST'])
def do_login():
    username = request.form['username']
    password = request.form['password']

    if username == 'Admin' and password == '123456':
        return redirect(url_for('map_page'))
    else:
        flash('账号或密码错误')
        return redirect(url_for('login'))


# 登录成功页面
@app.route('/success')
def success():
    return "<h1>登录成功！欢迎！</h1>"


@app.route('/map')
def map_page():
    return render_template('map.html')  # 渲染地图页面


@app.route('/')
def back_to_map():
    return render_template('map.html')  # 由地铁图页面返回主页面


@app.route('/metro_map.html')
def to_metro_map():
    return render_template('metro_map.html')    # 由主页面前往地图页面


if __name__ == '__main__':
    app.run(debug=True)
