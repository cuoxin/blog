from flaskr import db
from flaskr.mode import Artical, ArticalContent, ArticalLabel, Label
import markdown, time, re


def mdTransformation(text):

    html = markdown.markdown(text, output_format="html5", extensions=['markdown.extensions.toc','markdown.extensions.fenced_code'])

    return html


def htmlSave(html, filename):
    title = filename.split(".")[0]
    date = time.strftime("%Y-%m-%d", time.localtime())
    preview = re.sub('<[^<]+?>', '', html).replace('\n', '').strip()
    preview = preview[:200]

    artical = Artical(title=title, time=date, preview=preview)
    content = ArticalContent(content=html)
    db.session.add(artical)
    db.session.flush()  ## 获取主键的值
    artical_id = artical.id
    db.session.add(content)
    db.session.commit()
    return artical_id

def labelNumAdd(id):
    label = Label.query.get(id)
    label.number += 1
    db.session.commit()

def labelSave(labels, artical_id):
    for num in labels:
        num = int(num)
        artical_label = ArticalLabel(artical_id=artical_id, label_id=num)
        db.session.add(artical_label)
        labelNumAdd(num)

def operateFile(text, filename, labels):
    html = mdTransformation(text)
    artical_id = htmlSave(html, filename)
    labelSave(labels, artical_id)