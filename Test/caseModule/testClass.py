import os
import unittest
import tempfile
import sqlite3
from contextlib import closing
from www import app


class SampleTestCase(unittest.TestCase):

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


if __name__ == '__main__':
    unittest.main()
