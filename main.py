import getpass
from Database import *
from DoctorSystem import *
from NurseSystem import *
from AdminSystem import *

# User Interface:
# - State Machine
# - Entering and Exiting the database application
# - Proper password encryption and decryption


if __name__=='__main__':
	username_length = 8
	password_length = 60
	hosp_db = Database()

	while True:
		try:
			if raw_input("> Before starting the application would you like to add any users to the system?[y/n]") == 'y':
				username = raw_input("> Please enter your desired username: ")
				if hosp_db.check_login(username):
					print("> Sorry username already taken... Please enter another one...")
					continue
				while True:
					password = raw_input("> Please enter a password: ")
					if password == '':
						continue
					elif len(password) > password_length:
						print("> Invalid password length")
						continue
					break

				name = raw_input("> Please enter your name [first last]: ")
				role = raw_input("> Please choose a role A:Admin, D:Doctor, or N:Nurse [A,D,N]: ")
				hosp_db.create_user(username, password, name, role)
				if raw_input("> Would you like to add more users to the system?[y/n]") == 'y':
					continue
				else:
					break
			else:
				break
		except (KeyboardInterrupt, SystemExit, EOFError):
			if raw_input("\n> Would you like to exit the application[y/n]: ") == 'y':
				print("Login...")
				break
			else:
				continue
		except:
			print("\n> Unexpected Error ...")
			break

 	print("\n> Hospital Database System: Please enter your employee login and password.")
	print("> Use CNTL-C Or CNTL-D To Exit the program.")
	
	while True:
		try:
			username = raw_input("\n> USERNAME: ")

			if username == '':
				continue
			elif len(username) > username_length:
				print("> Invalid username length")

			password = getpass.getpass("> PASSWORD: ")
			if password == '':
				continue
			elif len(password) > password_length:
				print("> Invalid password length")

			if hosp_db.check_login(username):
				hosp_db.login(username, password)
				if hosp_db.logged_in:
					print("> Successfully logged in")
					role = hosp_db.determine_role(username)
					if role == 'D':
						DoctorSystem(hosp_db).run()
					elif role == 'N':
						NurseSystem(hosp_db).run()
					elif role == 'A':
						AdminSystem(hosp_db).run()
				else:
					print("> Invalid password, please try again.")
		except (KeyboardInterrupt, SystemExit, EOFError):
			if raw_input("\n> Would you like to exit the application[y/n]: ") == 'y':
				print("Shutting down...")
				break
			else:
				continue
		except:
			print("\n> Unexpected Error ...")
			break
