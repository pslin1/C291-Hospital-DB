from __future__ import print_function


def print_ind_row(array, end_param='\n'):
	for item in array:
		if item != array[-1]:
			print(item, end=" | ")
		else: 
			print(item, end=end_param)

def print_rows(db_cursor):
	column_names = [description[0] for description in db_cursor.description]			
	print_ind_row(column_names)
	data = db_cursor.fetchall()
	if len(data) == 0:
		print("No records found")
	else:
		print_ind_row(data[0])