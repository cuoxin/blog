from flaskr import app, render_template
from flask import request, redirect, url_for
from backstage import file_post, label, file_delete
from flaskr.mode import Label
from flaskr.login import login_required

@app.route("/backstage")
@login_required
def backstage():
    labels = Label.query.all()
    return render_template("backstage.html", theme="Backstage", labels=labels)

@app.route("/backstage_md_file/", methods=['POST'])
def backstageMdFile():
    if request.method == "POST":
        file = request.files['file']
        labels = request.form.getlist("label") ## 标签
        text = file.read()
        text = text.decode("utf-8")
        file_post.operateFile(text, file.filename, labels)

    return redirect(url_for("backstage"))

@app.route("/backstage_lable/", methods=['POST'])
def backstageLable():
    if request.method == "POST":
        text = request.form.get("new_label")
        label.addLabel(text)
    
    return redirect(url_for("backstage"))

@app.route("/backstage_delet/", methods=['POST'])
def backstageDelet():
    if request.method == "POST":
        text = request.form.get("delet")
        text_list = text.split(",")
        file_delete.deleteFile(text_list)

    return redirect(url_for("backstage"))