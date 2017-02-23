import sqlite3
from Database import *
from datetime import date, datetime
from tools import print_rows, print_ind_row

class AdminSystem():
    def __init__(self, db):
        self.db = db
        
    def run(self):
	while True:
		try:
	    	    print("\n> Welcome to Administrative Staff. Please make a selection \n")
	    	    print("> 1: Create a report that lists Doctor and Total Amount of each Drug Prescribed")
	    	    print("> 2: List Total Amount for each Drug and Category")
	    	    print("> 3: List Possible medications prescribed over time after that diagnosis.")
	    	    print("> 4: List all diagnoses for a given drug made before prescribing the drug")
	    	    print("> 5: Logout (or CTRL-C)\n")
	    	    
	    	    selection = int(raw_input("Please select task by index: \n"))
	    	    
	    	    if selection == 1:
	    		    self.admin1()
	    	    elif selection == 2:
	    		    self.admin2()    
	    	    elif selection == 3:
	    		    self.admin3()
	    	    elif selection == 4:
	    		    self.admin4()
		    elif selection == 5:
	    		print("Logging out of system...")
	    		break
		except (KeyboardInterrupt, SystemExit, EOFError):
		        print("\n> Logging out of the database...")
		        break
		except:
		    print("\n> Unexpected Error ...")
		    break

    def admin1(self):
        try:
            print '> Now looking at doctor prescription records'
            startdate=raw_input("> Start Date [yyyy-mm-dd]: ")
            enddate=raw_input("> End Date [yyyy-mm-dd]: ")
            self.db.db_cursor.execute('SELECT julianday(?);',(startdate,))
            fetchall = self.db.db_cursor.fetchall()
            self.db.db_cursor.execute('SELECT s.name, m1.staff_id, m1.drug_name, SUM(m1.amount) FROM medications m1, staff s WHERE m1.staff_id=s.staff_id GROUP BY m1.staff_id, drug_name HAVING julianday(?)<=julianday(m1.mdate) AND julianday(?)>=julianday(m1.mdate);', (startdate,enddate))
            output = self.db.db_cursor.fetchall()
            usedname=[]
            for line in output:
                if line[0] not in usedname:
                    print("\nDoctor: " + line[0])
                    print("------------------------------------------------")
                    usedname.append(line[0])
                print('- '+line[2]+' '+str(line[3]))  
        except (KeyboardInterrupt, SystemExit, EOFError):
            print("\n> Returning to main...")
            #break
        except:
            print("\n> Unexpected Error ...")
            #break      
    
    def admin2(self):
        try:
            print 'Now in Selection 2'
            startdate=raw_input("> Start Date [yyyy-mm-dd]: ")
            enddate=raw_input("> End Date [yyyy-mm-dd]: ")
            self.db.db_cursor.execute('SELECT d.category, m1.drug_name, SUM(m1.amount) FROM medications m1, drugs d WHERE m1.drug_name=d.drug_name GROUP BY d.category ,m1.drug_name HAVING julianday(?)<=julianday(m1.mdate) AND julianday(?)>=julianday(m1.mdate);',(startdate,enddate))
            output1=self.db.db_cursor.fetchall()
            self.db.db_cursor.execute('SELECT d.category, SUM(m1.amount) FROM medications m1, drugs d WHERE m1.drug_name=d.drug_name GROUP BY d.category')
            output2=self.db.db_cursor.fetchall()
            usedname=[]
            for line in output1:
                if line[0] not in usedname:
                    usedname.append(line[0])
                    for each in output2:
                        if each[0]==line[0]:
                            print(line[0] + '   Total: '+str(each[1]))
                print('  '+line[1]+' '+str(line[2]))
        except (KeyboardInterrupt, SystemExit, EOFError):
            print("\n> Returning to main...")
            #break
        except:
            print("\n> Unexpected Error ...")
            #break 
            
    def admin3(self):
        try:
            print 'Now in Selection 3'
            diagnosis=raw_input("Diagnosis: ")
            self.db.db_cursor.execute('SELECT m.drug_name FROM medications m, diagnoses d WHERE d.diagnosis=? AND d.chart_id=m.chart_id GROUP BY m.drug_name  ORDER BY  COUNT(m.drug_name) DESC;',(diagnosis,))
            print_rows(self.db.db_cursor)     
        except (KeyboardInterrupt, SystemExit, EOFError):
            print("\n> Returning to main...")
            #break
        except:
            print("\n> Unexpected Error ...")
            #break 
        
    def admin4(self):
        try:
            print 'Now in Selection 4'
            drug=raw_input("Drug: ")
            self.db.db_cursor.execute('SELECT DISTINCT d.diagnosis from medications m, diagnoses d WHERE m.drug_name=? AND d.chart_id=m.chart_id GROUP BY d.chart_id ORDER BY AVG(m.amount) DESC;',(drug,))
            self.db.commit_changes()
            print_rows(self.db.db_cursor)     
        except (KeyboardInterrupt, SystemExit, EOFError):
            print("\n> Returning to main...")
            #break
        except:
            print("\n> Unexpected Error ...")
            #break 
    

       
