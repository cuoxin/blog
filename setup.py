import os
import sys

def dbInit():
    ''' 数据库初始化 '''
    from flaskr import db
    db.create_all()

def passwordSet():
    ''' 设置管理员密码 '''
    pass

dbInit()