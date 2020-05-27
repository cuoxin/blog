## 说明
[Flask 中文文档](https://dormousehole.readthedocs.io/en/latest/index.html)

## 学习进度
### 部署环境
1. 建议使用虚拟环境
通过 `python -m venv (文件夹名字)` 安装虚拟环境，在环境内安装 `pip install Flask` 国内最好使用镜像
2. 调试环境配置
Flask 默认从 app.py 启动。但是本次使用包开发，需要设置启动方法，官方提供的设置方法为:
- Linux/Mac

```
$ export FLASK_APP=flaskr
$ export FLASK_ENV=development
$ flask run
```

- Windows

```
> set FLASK_APP=flaskr
> set FLASK_ENV=development
> flask run
```

但是在部署时多次失败。查询搜索引擎后选择 `python_dotenv` 进行环境部署

正常的 pip 安装后创建文件 `.env` `.flaskenv` 将配置文件写入第二个文件中
```
FLASK_ENV=development
FLASK_APP=flaskr
```

之后就可以使用 `flask run` 启动服务了
----------初期部署结束----------
### __init__.py
在 `__init__.py` 中进行
[中文文档地址](https://dormousehole.readthedocs.io/en/latest/tutorial/factory.html)

- SECRET_KEY 在实际生产中应该用**随机值**，开发中可先固定(官方使用'dev')
- 配置写在 /instance/ 下，可用函数 `app.config.from_pyfile()` 读取文件夹下配置文件
- 官方推荐使用函数工厂。但是能力有限，无法理解实际运作。
### 数据库
个人认为数据库是比较难的部分，因为需要学习一样新东西
- 注意在sqlalchemy中变量名需要和数据库中的字段名一致