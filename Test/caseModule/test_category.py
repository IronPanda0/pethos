import unittest
import os
import tempfile
import sqlite3
from contextlib import closing
from www import app


class SampleTestCase(unittest.TestCase):

    # setUp() and tearDown() here...
    def setUp(self):
        self.db_fd, app.config['DATABASE'] = tempfile.mkstemp()
        app.config['TESTING'] = True
        self.init_db(app.config['DATABASE'])

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(app.config['DATABASE'])

    def init_db(self, db_file):
        with closing(sqlite3.connect(db_file)) as db:
            with app.open_resource('init.sql', mode='r') as f:
                db.cursor().executescript(f.read())
            db.commit()

    # Test case
    def test_valid_addCategory(self):
        with app.test_client() as client:
            response = client.post('/category/add', data=dict(
                categoryName='内科病'
            ), follow_redirects=True)
            assert '分类添加成功' in response.msg

    def test_valid_updateCategory(self):
        with app.test_client() as client:
            response = client.post('/category/update', data=dict(
                categoryId=1,
                categoryName="内科病修改"
            ), follow_redirects=True)
            assert '分类修改成功' in response.msg

    def test_valid_deleteCategory(self):
        with app.test_client() as client:
            response = client.post('/category/delete', data=dict(
                categoryId=1,
            ), follow_redirects=True)
            assert '分类删除成功' in response.msg
