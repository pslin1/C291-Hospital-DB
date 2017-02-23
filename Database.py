import sqlite3
import hashlib
import random

class Database():
	"""docstring for Database"""
	def __init__(self):
		self.db = sqlite3.connect("hospital.db")
		self.db_cursor = self.db.cursor()
		self.logged_in = False
		self.logged_in_staff_id = None
		

	def check_login(self,login):
		self.db_cursor.execute(
			"SELECT staff.login FROM staff WHERE staff.login = '" + login + "';")
		valid = True if self.db_cursor.fetchone() else False
		return valid
	
	def login(self, login, password):
		self.db_cursor.execute(
			"SELECT staff.password FROM staff WHERE staff.login = '" + login + "';")
		# no need to check if
		if str(hashlib.sha224(password).hexdigest()) == str(self.db_cursor.fetchone()[0]):
			self.logged_in = True
			self.db_cursor.execute(
			"SELECT staff.staff_id FROM staff WHERE staff.login = '" + login + "';")
			self.logged_in_staff_id = str(self.db_cursor.fetchone()[0])
		return
			
	def check_id_unique(self, id):
		self.db_cursor.execute("SELECT * FROM staff WHERE staff.staff_id = ?;", (id,))
		valid = False if self.db_cursor.fetchone() else True
		return valid

	def create_user(self, username, password, name, role):
		while True:
			staff_id = '%05i'%random.randint(0,99999)
			if self.check_id_unique(staff_id) == True:
				break
		self.db_cursor.execute("INSERT INTO staff VALUES(?, ?, ?, ?, ?);", (staff_id, role, name, username, hashlib.sha224(password).hexdigest(),))
		self.db.commit()

	def determine_role(self, login):
		self.db_cursor.execute("SELECT staff.role FROM staff WHERE staff.login = '" + login + "';")
		return str(self.db_cursor.fetchone())[3]

	def commit_changes(self):
		self.db.commit()
		return