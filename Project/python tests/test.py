import pymysql.cursors
from time import process_time
from time import perf_counter

import concurrent.futures

connection = pymysql.connect(
			host='localhost',
			user='root',
			password='Amora#1000',
			database='ncbi_data',
			cursorclass=pymysql.cursors.DictCursor
		)

with connection:
	with connection.cursor() as cursor:
		t1_start = perf_counter()

		cursor.execute(f"SELECT * FROM names WHERE name_txt = 'Pegasus sinensis' LIMIT 1")
		result = cursor.fetchone()
		print(result)
		if result is None:
			cursor.execute(f"SELECT * FROM names WHERE MATCH(name_txt) AGAINST('Pegasus sinensis' IN NATURAL LANGUAGE MODE)")
			result = cursor.fetchone()

		taxid = result['tax_id']
		name_txt = result['name_txt']
		print(taxid)
		print(name_txt)
		
		t1_stop = perf_counter()
 
		print("Elapsed time:", t1_stop, t1_start)
 
 
		print("Elapsed time during the whole program in seconds:", t1_stop-t1_start)


# Elapsed time: 9489.848083484 9435.250096194
# Elapsed time during the whole program in seconds: 54.597987289998855