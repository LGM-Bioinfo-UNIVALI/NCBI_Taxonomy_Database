import pymysql.cursors
from time import process_time
from time import perf_counter


# Connect to the database
connection = pymysql.connect(host='localhost',
							 user='root',
							 password='pmore2712',
							 database='taxonomy',
							 cursorclass=pymysql.cursors.DictCursor)

with connection:
	with connection.cursor() as cursor:
		t1_start = perf_counter()
		organism_taxid = "2763546"

		cursor.execute(f"SELECT A.tax_id, A._rank, B._rank, B.tax_id, B.parent_taxnodes_id FROM nodes A JOIN nodes B ON A.parent_taxnodes_id = B.tax_id WHERE A.tax_id = {organism_taxid}")

		results = []
		result = cursor.fetchall()[0]

		results.append(result)

		while result['B._rank'] != "no rank":
			organism_taxid = result['parent_taxnodes_id']
			cursor.execute(f"SELECT A.tax_id, A._rank, B._rank, B.tax_id, B.parent_taxnodes_id FROM nodes A JOIN nodes B ON A.parent_taxnodes_id = B.tax_id WHERE A.tax_id = {organism_taxid} LIMIT 1")
			result = cursor.fetchone()
			results.append(result)

		taxids = []
		for result in results:
			taxids.append(result['tax_id'])
			taxids.append(result['B.tax_id'])

		cursor.execute(f"SELECT name_txt FROM names WHERE tax_id IN {tuple(taxids)} AND name_class = 'scientific name'")
		result = cursor.fetchall()

		t1_stop = perf_counter()
 
		print("Elapsed time:", t1_stop, t1_start)
 
 
		print("Elapsed time during the whole program in seconds:", t1_stop-t1_start)


# Elapsed time: 9489.848083484 9435.250096194
# Elapsed time during the whole program in seconds: 54.597987289998855