from flaskr import app, render_template
from flaskr.mode import Artical, ArticalContent, ArticalLabel, Label

@app.route("/artical/<int:id>")
def artical(id):
    content = ArticalContent.query.get(id)
    artical = Artical.query.get(id)
    label_ids = ArticalLabel.query.filter_by(artical_id=id)
    labels = []
    for label_id in label_ids:
        label = Label.query.get(int(label_id.label_id))
        labels.append(label)
    return render_template("artical.html", theme=artical.title, artical=content, labels=labels)