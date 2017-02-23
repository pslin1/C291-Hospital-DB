from Database import *
import unittest

class TestDatabase(unittest.TestCase):

    def test_check_login(self):
        db = Database()
        login = "testlogin"
        encrypted = str(hashlib.sha224("testpassword").hexdigest())
        self.assertFalse(db.check_login(login))
        db.db_cursor.execute(
            "INSERT INTO STAFF VALUES(\"TSTID\", 'A', \"TEST NAME\", ?, ?);", (login, encrypted,))
        self.assertTrue(db.check_login(login))

    def test_login(self):
        db = Database()
        self.assertFalse(db.logged_in)
        self.assertFalse(db.logged_in_staff_id == "TSTID")
        login = "testlogin"
        password = "testpassword"
        encrypted = str(hashlib.sha224(password).hexdigest())
        db.db_cursor.execute(
            "INSERT INTO STAFF VALUES(\"TSTID\", 'A', \"TEST NAME\", ?, ?);", (login, encrypted,))
        
        db.login(login, password)
        self.assertTrue(db.logged_in)
        print(db.logged_in_staff_id)
        self.assertTrue(db.logged_in_staff_id == "TSTID")

    def test_determine_role(self):
        db = Database()
        login = "testlogin"
        encrypted = str(hashlib.sha224("testpassword").hexdigest())
        self.assertFalse(db.determine_role(login) == 'A')
        db.db_cursor.execute(
            "INSERT INTO STAFF VALUES(\"TSTID\", 'A', \"TEST NAME\", ?, ?);", (login, encrypted,))
        self.assertTrue(db.determine_role(login) == 'A')

if __name__ == '__main__':
    unittest.main()