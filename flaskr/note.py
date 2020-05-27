from flaskr import app, render_template, url_for, db
from flaskr.mode import Artical
from flask import abort

## TODO: 当网页没有文章时会出现网页渲染错误，原因是网页中的“下一页”我使用了对列表取[-1]，如果列表是空的就会报错。

@app.route("/note/<int:page>")
def note(page):
    articals = Artical.query.order_by(db.desc(Artical.id)).offset((page-1)*8).limit(8)
    return render_template("note.html", theme="Note", articals=articals, page=page)