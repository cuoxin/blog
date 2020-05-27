from flaskr import app, render_template
from flask import request, redirect, url_for
from backstage import file_post, label
from flaskr.mode import Label
from flaskr.login import login_required

@app.route("/backstage")
@login_required
def backstage():
    labels = Label.query.all()
    return render_template("backstage.html", theme="Backstage", labels=labels)

@app.route("/backstage_md_file/", methods=['POST'])
def backstage_md_file():
    if request.method == "POST":
        file = request.files['file']
        labels = request.form.getlist("label") ## 标签
        text = file.read()
        text = text.decode("utf-8")
        file_post.operateFile(text, file.filename, labels)

    return redirect(url_for("backstage"))

@app.route("/backstage_lable/", methods=['POST'])
def backstage_lable():
    if request.method == "POST":
        text = request.form.get("new_label")
        label.addLabel(text)

    
    return redirect(url_for("backstage"))
