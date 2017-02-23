from __future__ import print_function
import sqlite3
from datetime import date, datetime
from Database import *
from tools import print_rows, print_ind_row


class DoctorSystem():
	def __init__(self, db):
		self.db = db
		self.db_cursor = db.db_cursor
		
	def check_hcno(self, hcno):
		self.db_cursor.execute(
			"SELECT patients.hcno FROM patients WHERE patients.hcno = '" + hcno + "';")
		valid = True if self.db_cursor.fetchone() else False
		return valid	

	def check_chart_open(self, chart_id):
		self.db_cursor.execute(
			"SELECT * FROM charts WHERE charts.chart_id = '" + chart_id + "';")
		row = self.db_cursor.fetchone()
		if row[3] == None:
			return True
		else:
			return False

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
					print("CLOSED")
			if raw_input("> Would you like to select a chart? If not you will be return to prior menu? [y/n]: ") == 'y':
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

	def modify_chart(self, hcno, chart_id):
		while True:
			try:
				print("\n> Insert:")
				print("1. Symptom")
				print("2. Diagnosis")
				print("3. Medication")
				action = int(raw_input("\nPlease select an option by the index on the left [1,2,3]: "))
				
				if (action == 1):
					symptom = raw_input("> Enter the symptom observed: ")
					self.db_cursor.execute(
						"INSERT INTO symptoms VALUES( ?, ?, ?, ?, ?);", 
						(hcno, chart_id, self.db.logged_in_staff_id, datetime.now(), symptom,))
					self.db.commit_changes()
				elif (action == 2):
					diagnosis = raw_input("> Enter the diagnosis: ")
					self.db_cursor.execute(
						"INSERT INTO diagnoses VALUES(?, ?, ?, ?, ?);", 
						(hcno, chart_id, self.db.logged_in_staff_id, datetime.now(), diagnosis))
					self.db.commit_changes()
				elif (action == 3):
					medication = raw_input("> Enter the medication prescribed: ")
					self.db_cursor.execute("SELECT drugs.drug_name FROM drugs;")
					if medication not in [str(drug_name[0]) for drug_name in self.db_cursor.fetchall()]:
						print("\n> This medication is currently not in your hospital drug list.")
						continue

					self.db_cursor.execute(
						"SELECT r1.drug_name FROM reportedallergies r1 WHERE r1.hcno = ?", (hcno,))
					rprt_algs = [str(drug_name[0]) for drug_name in self.db_cursor.fetchall()];
					if medication in rprt_algs:
						if (raw_input("> WARNING: The patient has previously reported being allergic to "+ medication +" Do you wish to continue?[y/n]") == 'n'):
							print("> Returning to selection menu...")
							continue
					else:
						self.db_cursor.execute(
						"select i1.canbe_alg from reportedallergies r1, inferredallergies i1 WHERE r1.hcno = ? AND r1.drug_name = i1.alg UNION select i2.alg from reportedallergies r2, inferredallergies i2 WHERE r2.hcno = ? AND r2.drug_name = i2.canbe_alg;", (hcno, hcno,))
						inf_algs = [str(drug_name[0]) for drug_name in self.db_cursor.fetchall() if drug_name[0] != medication];
						if (len(inf_algs) > 0):
							print("> WARNING: The patient has previously reported allergies to similar drugs (", end=' ')
							for drug in inf_algs:
								if (drug != inf_algs[-1]):
									print(drug, end=", ")
							print(inf_algs[-1] + " )")
							if (raw_input("> Do you wish to continue?[y/n]") == 'n'):
								print("> Returning to selection menu...")
								continue

					start_date = raw_input("> Enter the start date to take the medication [Format: yyyy-mm-dd]: ")
					end_date = raw_input("> Enter the end date to take the medication [Format: yyyy-mm-dd]: ")
					
					self.db_cursor.execute(
						"SELECT patients.age_group FROM patients WHERE patients.hcno = '" + hcno + "';")
					age_group = self.db_cursor.fetchone()
					
					self.db_cursor.execute(
						"SELECT dosage.sug_amount FROM dosage WHERE dosage.age_group = ? AND dosage.drug_name = ?", (str(age_group[0]), medication,))
					suggested_amount = self.db_cursor.fetchone()
					while True:
						amount = input("> Enter the amount per day you wish to prescribe: ")
						if (amount > suggested_amount[0]):
							print("\n> Are you sure you want to prescribe this amount of "+ str(amount) +"? The suggested amount for the age group " + str(age_group[0]) + " is " + str(suggested_amount[0]) + " [y/n]")
							if (raw_input() == 'n'):
								continue
							else:
								break

					self.db_cursor.execute(
						"INSERT INTO medications VALUES(?, ?, ?, ?, ?, ?, ?, ?);",
						(hcno, chart_id, self.db.logged_in_staff_id, datetime.now(), start_date, end_date, amount, medication))
					self.db.commit_changes()
					print("> Your prescription has been added to the patient chart...")
				if raw_input("\n> Input another record?[y/n]: ") == 'y':
					continue
				else: 
					break

			except (KeyboardInterrupt, SystemExit, EOFError):
				if raw_input("\n> Cancelled insertion, would you like to go back to the main menu?[y/n]: ") == y:
					break
				else:
					continue
			except:
				print("\n> Unexpected Error ...")
				break
		return

	def run(self):
		hcno_length = 5;
		print("\n> Please enter a patient's health care number")
		print("> Or use CNTL-C Or CNTL-D To Logout.")
		while True:
			try:
				hcno = raw_input("\n> Patient health care number: ")
				if hcno == '':
					continue
				elif len(hcno) > hcno_length:
					print("\n> Invalid health care number length.")
				chart_id = self.retrieve_charts(hcno)
				if chart_id:
					self.retrieve_ind_chart(chart_id)
					if self.check_chart_open(chart_id):
						if raw_input("\n> Would you like to insert a symptom, diagnoses, or medication?[y/n]" +
							"\n> If not you will be prompted to enter a new patient ID: ") == 'y':
							self.modify_chart(hcno, chart_id)
			except (KeyboardInterrupt, SystemExit, EOFError):
				print("\n> Logging out of the database...")
				break
			except:
				print("\n> Unexpected Error ...")
				break
