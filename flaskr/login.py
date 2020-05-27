from flaskr import app, login_manager
from flaskr.mode import User
from flask import request, render_template, redirect, url_for, flash
from flask_login import current_user, login_user, login_required


@login_manager.user_loader
def load_user(user_id):
    user = User.query.get(int(user_id))
    return user

@app.context_processor
def logining_user():
    '''
        上下文处理，
        在模板中可以使用此变量
    '''
    user = User.query.first() ## 注意以后用户增多后得修改
    return dict(user=user)

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/checkpassword/', methods=["POST"])
def checkpassword():
    if request.method == "POST":
        password = request.form.get("password")

        user = User.query.first()

        if user.checkPassword(password):
            login_user(user)

            return redirect(url_for("backstage"))
        else:
            flash("密码错误")
            return redirect(url_for("login"))
        