from flaskr import app, render_template
from flaskr.mode import Artical, ArticalContent, ArticalLabel, Label, Message, MessageMessage
from flask import request, redirect, url_for
from backstage import put_message

@app.route("/artical/<int:id>")
def artical(id):

    content = ArticalContent.query.get(id)

    artical = Artical.query.get(id)

    label_ids = ArticalLabel.query.filter_by(artical_id=id)
    labels = []
    for label_id in label_ids:
        label = Label.query.get(int(label_id.label_id))
        labels.append(label)

    messages = Message.query.filter_by(artical_id=id).all()
    
    return render_template("artical.html", theme=artical.title, artical=content, time=artical.time, labels=labels, messages=messages)

@app.route("/put_message/", methods=["POST"])
def putMessage():
    if request.method == "POST":
        content = request.form.get("content")
        name = request.form.get("name")
        email = request.form.get("email")
        id = request.form.get("id")
        put_message.inputMessage(content, name, email, id)
    
    return redirect(url_for("artical", id=int(id)))