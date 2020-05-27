from flaskr import db
from flaskr.mode import Artical, ArticalContent, Label, ArticalLabel

def deleteArtical(id):
    ''' 删除文章信息 '''
    artical = Artical.query.get(id)
    db.session.delete(artical)
    db.session.commit()

def deleteArticalContent(id):
    ''' 删除文章内容 '''
    artical = ArticalContent.query.get(id)
    db.session.delete(artical)
    db.session.commit()

def deleteLabelNum(id_list):
    ''' 删除标签数字 '''
    for id in id_list:
        label = Label.query.get(id)
        label.number -= 1
    db.session.commit()

def deleteArticalLabel(id):
    ''' 删除文章标签 '''
    artical_labels = ArticalLabel.query.filter(ArticalLabel.artical_id == id).all()
    label_id_list = []
    for artical_label in artical_labels:
        label_id_list.append(int(artical_label.label_id))
        db.session.delete(artical_label)
    db.session.commit()
    
    return label_id_list

def deleteFile(artical_id_list):

    for id in artical_id_list:
        id = int(id)
        deleteArtical(id)
        deleteArticalContent(id)
        label_id_list = deleteArticalLabel(id)
        deleteLabelNum(label_id_list)