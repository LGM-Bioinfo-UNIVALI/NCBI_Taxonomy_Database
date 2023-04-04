import pymysql.cursors
from time import perf_counter


def get_organism_name(organism, cursor):
    cursor.execute(f"SELECT * FROM names WHERE tax_id = {organism} AND name_class = 'scientific name'")
    organism_name = cursor.fetchall()[0]['name_txt']

    return organism_name


def get_organism_taxid(organism, cursor):
    cursor.execute(f"SELECT * FROM names WHERE name_txt LIKE '%{organism}%' AND name_class = 'scientific name' LIMIT 1")
    taxid = cursor.fetchone()['tax_id']

    return taxid


def get_organism_data(organism, cursor):
    cursor.execute(f"SELECT parent_taxnodes_id, _rank FROM nodes WHERE tax_id = {organism} LIMIT 1")
    result = cursor.fetchone()

    return result

def get_taxonomy(cursor, organism_taxid=None, organism_name=None):
    if organism_taxid is None:
        organism_taxid = get_organism_taxid(organism_name, cursor)

    taxids = []
    taxids.append(organism_taxid)

    taxonomy = {}
    result = get_organism_data(organism_taxid, cursor)

    rank = result['_rank']
    taxonomy[organism_taxid] = rank

    while int(result['parent_taxnodes_id']) != 1:
        organism_taxid = result['parent_taxnodes_id']
        taxids.append(organism_taxid)

        result = get_organism_data(organism_taxid, cursor)
        rank = result['_rank']
        taxonomy[organism_taxid] = rank



    cursor.execute(f"SELECT name_txt, tax_id FROM names WHERE tax_id IN {tuple(taxids)} AND name_class = 'scientific name'")
    names = cursor.fetchall()
    
    taxid2name = {list(i.values())[1]: list(i.values())[0] for i in names}
    taxonomy = {taxid2name[key]: taxonomy[key] for key in taxonomy.keys()}
    print(taxonomy)
# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='batata2000',
                             database='ncbi_data',
                             cursorclass=pymysql.cursors.DictCursor)


with connection:
    with connection.cursor() as cursor:
        t1_start = perf_counter()
        organisms = ['Schistocerca gregaria', 'Bunaea alcinoe', 'Tetrapedia diversipes', 'Pamphilius', 'Schistocerca gregaria', 'Bunaea alcinoe', 'Tetrapedia diversipes', 'Pamphilius', 'Schistocerca gregaria', 'Bunaea alcinoe', 'Tetrapedia diversipes', 'Pamphilius']

        # Search by organism taxid
        # get_taxonomy(cursor, organism_taxid=organism_taxid)
        
        # Search by organism name

        for organism_name in organisms:
            get_taxonomy(cursor, organism_name=organism_name)
        

        t1_stop = perf_counter()
        print("Elapsed time:", t1_stop, t1_start) 
        print("Elapsed time during the whole program in seconds:", t1_stop-t1_start) 

        