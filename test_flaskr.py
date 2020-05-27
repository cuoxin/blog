import unittest
from flaskr import app, hello, db

class TestCase(unittest.TestCase):
    def setUp(self):
        ''' 测试前的准备 '''

        ## 更新配置
        app.config.update(
            TESTING=True,
            SQLALCHEMY_DATABASE_URI='sqlite:///:memory:'
        )

    def tearDown(self):
        ''' 测试结束的清扫 '''
        pass

    def test_hello(self):
        result = hello()
        self.assertEqual(result, "Hello World!")

if __name__ == "__main__":
    unittest.main()