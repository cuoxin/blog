from flaskr import app, render_template, db
from flaskr.mode import ArticalLabel, Artical

@app.route("/search_label/<int:label_id>/<int:page>/<string:label_name>")
def searchLabel(label_id, page, label_name):
    label_articals = ArticalLabel.query.filter_by(label_id=label_id).all()

    articals_id = []
    for label_artical in label_articals:
        articals_id.append(int(label_artical.artical_id))
    
    articals = Artical.query.filter(Artical.id.in_(articals_id)).order_by(db.desc(Artical.id)).offset((page-1)*8).limit(8)


    return render_template("search.html", articals=articals, page=page, label_id=label_id, theme=label_name)