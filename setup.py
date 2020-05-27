import mysql.connector

database = mysql.connector.connect(user='root', password='123456', database='web', charset="utf8mb4")
cursor = database.cursor()
'''
# id 题目，时间，预览
cursor.execute("CREATE TABLE artical_p (id INT AUTO_INCREMENT PRIMARY KEY, title VARCHAR(255), time VARCHAR(15), preview VARCHAR(255)) default CHARSET=utf8mb4")

# id 文章内容
cursor.execute("CREATE TABLE artical_c (id INT AUTO_INCREMENT PRIMARY KEY, content LONGTEXT) default CHARSET=utf8mb4")

# id 文章id 标签id
cursor.execute("CREATE TABLE artical_l (id INT AUTO_INCREMENT PRIMARY KEY, artical_id INT, label_id INT) default CHARSET=utf8mb4")

# id 标签 数量
cursor.execute("CREATE TABLE label (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(100), number INT) default CHARSET=utf8mb4")

# id password
cursor.execute("CREATE TABLE user (id INT AUTO_INCREMENT PRIMARY KEY, password VARCHAR(255)) default CHARSET=utf8mb4")
'''