import pymysql.cursors

organism = 'Schistocerca gregaria (Forskal, 1775)'


# Connect to the database
connection = pymysql.connect(host='localhost',
							 user='root',
							 password='Amora#1000',
							 database='ncbi_data',
							 cursorclass=pymysql.cursors.DictCursor)


def get_organism_taxid(organism, cursor):
    cursor.execute(f"SELECT * FROM names WHERE name_txt LIKE '%{organism}%' LIMIT 1")
    taxid = cursor.fetchone()['tax_id']

    return taxid


with connection:
	with connection.cursor() as cursor:
		cursor.execute(f"SELECT * FROM organisms WHERE tax_name LIKE '%{organism}%' LIMIT 1")
		result = cursor.fetchone()

		if result is None:
			taxid = get_organism_taxid(organism, cursor)
			cursor.execute(f"SELECT * FROM organisms WHERE tax_id = {taxid} LIMIT 1")
			result = cursor.fetchone()

		if result['species'] == '':
			result['species'] = result['tax_name']
		
		result.pop('tax_id')
		result.pop('tax_name')
		print(result)