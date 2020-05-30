from flaskr import db
from flaskr.mode import Message, MessageMessage
import time

def inputMessage(content, name, email, id):
    t = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    message = Message(name=name, email=email, content=content, artical_id=int(id), time=t)

    db.session.add(message)
    db.session.commit()