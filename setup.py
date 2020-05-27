from pip._internal import main

def install():
    ''' 安装相关模块 '''
    with open ("./modList.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            line.strip()
            main(["install", line])

def dbInit():
    ''' 数据库初始化 '''
    from flaskr import db
    db.create_all()


install()

dbInit()