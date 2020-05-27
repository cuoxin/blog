from flaskr import db
from flaskr.mode import Label

def addLabel(text):
    new_label = Label(name=text, number=0)
    db.session.add(new_label)
    db.session.commit()