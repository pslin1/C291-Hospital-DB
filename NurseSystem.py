from __future__ import print_function
import sqlite3
import random
from datetime import date, datetime
from Database import *
from tools import print_rows, print_ind_row


class NurseSystem():
	def __init__(self, db):
		self.db = db
		self.db_cursor = db.db_cursor
		
		
	def run(self):
		while True:
			try:
				print("\n> Welcome to the nurses' database system")
				print("\n> Please Select a Task: \n")
				print("> 1: Create a new chart for a patient")
				print("> 2: Close a chart for a patient")
				print("> 3: List all charts for a given patient")
				print("> 4: Add a symptom for a given patient")
				print("> 5: Logout (CTRL-C)\n")
				
				selection = int(raw_input("Please select task by index: \n"))
				
				if selection == 1:
					self.create_new_chart()
				if selection == 2:
					self.dismiss_patient()
				if selection == 3:
					self.list_charts()
				if selection == 4:
					self.add_symptom()
				if selection == 5:
					print("\n> Logging out of the nurses' system...")
					break
			except (KeyboardInterrupt, SystemExit, EOFError):
				print("\n> Logging out of the database...")
				break
			except:
				print("\n> Unexpected Error ...")
				break
			
	def provide_hcno(self):
		while True:
			hcno = raw_input("Please enter the patients' health care number: ")
			if len(hcno) != 5:
				print("Please enter a valid, 5 digit health care number")
				continue
			else:
				break
				
		return hcno
		

		
	def check_if_open(self,hcno): #note that this will return false if the hcno doesn't exist
		self.db_cursor.execute(
			"SELECT * FROM charts WHERE charts.hcno = ? AND charts.edate IS NULL;", (hcno,))
		#row=db_cursor.fetchall()
		if self.db_cursor.fetchone():
			return True
		else:
			return False

			
	def check_if_is_patient(self, hcno):
		self.db_cursor.execute(
			'''SELECT * FROM patients WHERE patients.hcno = ?;''', (hcno,))
		if self.db_cursor.fetchone():
			return True
		else:
			return False
			
	def check_for_previous(self, hcno):
		self.db_cursor.execute(
			'''SELECT * FROM patients WHERE patients.hcno = ?;''', (hcno,))
		if self.db_cursor.fetchone():
			return True
		else: 
			return False
			
	def close_chart(self,hcno):
		now=datetime.now()
		self.db_cursor.execute(
			'''UPDATE charts SET edate = ? WHERE ? = charts.hcno AND charts.edate IS NULL;''', (now, hcno,))
			
	def check_if_unique(self, chart_id):
		self.db_cursor.execute(
			'''SELECT * FROM charts WHERE charts.chart_id = ?;''', (chart_id,))
		if self.db_cursor.fetchone():
			return False
		else:
			return True
			
	def add_new_patient(self, hcno, name, age_grp, address, phone, emg_phone, chart_id, adate):
		self.db_cursor.execute(
			'''INSERT INTO patients VALUES(?, ?, ?, ?, ?, ?);''', (hcno, name, age_grp, address, phone, emg_phone,))
		self.db_cursor.execute(
			'''INSERT INTO charts VALUES(?, ?, ?, NULL);''', (chart_id, hcno, adate,))
			
	def add_existing_patient(self, chart_id, hcno, adate):
		self.db_cursor.execute(
			'''INSERT INTO charts VALUES(?, ?, ?, NULL);''', (chart_id, hcno, adate, ))
	
	def retrieve_charts(self, hcno):
		self.db_cursor.execute(
			"SELECT * FROM charts WHERE charts.hcno = '" + hcno + "' ORDER BY date(adate) DESC;")
		data = self.db_cursor.fetchall()
		is_charts = True if len(data) > 0 else False
		if is_charts:
			column_names = [description[0] for description in self.db_cursor.description]			
			column_names = ["Index"] + column_names + ["Chart Status"]
			print_ind_row(column_names)
			num_row = 0		
			for num_row, row in enumerate(data, start=1):		
				print(num_row, end=" | ")
				print_ind_row(row, ' ')
				if row[3] == None:
					print("OPEN")
				else:
					print("Closed")
			if raw_input("> Would you like to select a chart or return to prior menu? [y/n]: ") == 'y':
				while True:				
					try:
						selection = int(raw_input("> Please select chart by index on the left: "))	
						if (selection <= num_row):	
							chart_id = str(data[selection - 1][0])	
							return chart_id
					except (KeyboardInterrupt, SystemExit, EOFError):
						print("\n> Returning to patient ID entry page.")
					except:
						print("\n> Unexpected Error ...")
						break
			else: 
				return 0
		else:
			print("> No charts availible for patient, please choose another patient.")
			return 0
			
	def retrieve_ind_chart(self, chart_id):
		print("\n###################################################################")
		print("\nChart ID: ", chart_id)

		print("\nSymptoms:")
		print("-------------------------------------------------------------------")
		
		self.db_cursor.execute(
			"SELECT * FROM symptoms WHERE symptoms.chart_id = '" + chart_id + "' ORDER BY date(obs_date) DESC;")
		print_rows(self.db_cursor)
		
		print("\nDiagnoses:")
		print("-------------------------------------------------------------------")		
		
		self.db_cursor.execute(
			"SELECT * FROM diagnoses WHERE diagnoses.chart_id = '" + chart_id + "'ORDER BY date(ddate) DESC;")
		print_rows(self.db_cursor)
		
		print("\nMedications:")
		print("-------------------------------------------------------------------")		
		
		self.db_cursor.execute(
			"SELECT * FROM medications WHERE medications.chart_id = '" + chart_id + "'ORDER BY date(mdate) DESC;")
		print_rows(self.db_cursor)

		print("\n###################################################################")
		
	def get_chart_id(self, hcno): #will get chart id for patients that have an open chart and is a patient
		self.db_cursor.execute(
			'''SELECT chart_id FROM charts WHERE ? = charts.hcno;''',(hcno,))
		return self.db_cursor.fetchone()
		
				
	def create_new_chart(self):
		hcno = self.provide_hcno()
		is_open = self.check_if_open(hcno)
		unique = False
		if is_open == True:
			if (raw_input("> There is currently a chart open for this patient. Would you like to close it? (y/n): ")) in ['y', 'Y']:
				self.close_chart(hcno)
				self.db.commit_changes()
				print("> Chart Closed...")
			else:
				print("> Returning to main...")
				return 0
		else:
			if self.check_for_previous(hcno) == False:
				if (raw_input("> There is currently no patient in the database with that health care number, would you like to add this patient to the database? (y/n): ")) in ['y', 'Y']:
					while unique == False:
						chart_id = '%05i'%random.randint(0,99999)
						if self.check_if_unique(chart_id) == True:
							unique = True
					name = raw_input("> Please enter the patients name (15 characters): ")
					age_grp = raw_input("> Please enter the patients age group (##-##): ")
					address = raw_input("> Please enter the patients address (30 characters max): ")
					phone = raw_input("> Please enter the patients phone number (###-###-####): ")
					emg_phone = raw_input("> Please enter the patients emergency phone number (###-###-####): ")
					adate = datetime.now()
					self.add_new_patient(hcno, name, age_grp, address, phone, emg_phone, chart_id, adate)
					self.db.commit_changes()
					print("> Chart has been created...")
				else:
					return 0
			else:
				if (raw_input("> This patients' information is in the database, would you like to import it into a new chart? (y/n): ")) in ['y', 'Y']:
					while unique == False:
						chart_id = '%05i'%random.randint(0,99999)
						if self.check_if_unique(chart_id) == True:
							unique = True
					adate = datetime.now()
					self.add_existing_patient(chart_id, hcno, adate)
					self.db.commit_changes()
					print("> Chart has been created...")
				else:
					return 0
					

	def dismiss_patient(self):
		hcno = self.provide_hcno()
		if self.check_if_open(hcno) == False:
						
			print("> This patient does not have an open chart to close!")
			print("> Returning to main...")			
		else: 
			self.close_chart(hcno)
			self.db.commit_changes()
			print("> Chart has been closed...")
		
	def list_charts(self):
		hcno = self.provide_hcno()
		chart_id = self.retrieve_charts(hcno)
		if chart_id:
			self.retrieve_ind_chart(chart_id)
			
	def add_symptom(self): 
		hcno = self.provide_hcno()
		staff_id = self.db.logged_in_staff_id
		obs_date = datetime.now()
		#chart_id = self.retrieve_charts(hcno)
		if self.check_if_open(hcno) == True and self.check_if_is_patient(hcno) == True:
			symptom = raw_input("Please enter a symptom (15 characters): ")
			chart_id = str(self.get_chart_id(hcno)[0])
			
			#print(chart_id)
			#print(type(chart_id))
			self.db_cursor.execute(
			'''INSERT INTO symptoms VALUES( ?, ?, ?, ?, ?);''', (hcno, chart_id, staff_id, obs_date, symptom,))
			self.db.commit_changes()
			
		else:
			if self.check_if_open(hcno) == False or self.check_if_is_patient(hcno) == False:
				print("Please enter a patient currently staying at the hospital, exiting to main...: ")
				
				
			
			
#db = sqlite3.connect("hospital.db")
#db_cursor = db.cursor()
#nurse_system = NurseSystem(db)
#nurse_system.run()
