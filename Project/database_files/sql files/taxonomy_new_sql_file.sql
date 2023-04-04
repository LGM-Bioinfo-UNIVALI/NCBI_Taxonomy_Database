# Utilizando o new_taxdump
# Com o arquivo rankedlineage do new_taxdump do NCBI podemos criar um único banco com a taxonomia completa de cada organismo

CREATE DATABASE ncbi_data;
use ncbi_data;

create table organisms (
	tax_id int,
    tax_name varchar(200),
    species varchar(200),
	genus varchar(200),
	family varchar(200),
    _order varchar(200),
    class varchar(200),
    phylum varchar(200),
    kingdom varchar(200),
    superkingdom varchar(200)
);

LOAD DATA INFILE
'/var/lib/mysql-files/rankedlineage.CSV'
INTO TABLE organisms  
FIELDS TERMINATED BY '\t|\t'
LINES TERMINATED BY '\t|\n'
(tax_id, tax_name, species, genus, family, _order, class, phylum, kingdom, superkingdom);

CREATE UNIQUE INDEX organism_id ON organisms ( tax_id);


# Com essa tabela podemos obter o taxid dos organismos buscando pelo seu nome
# Dessa forma podemos consultar a tabela organisms com base no taxid obtido
create table names (
	tax_id int,
    name_txt varchar(500),
    unique_name varchar(200),
    name_class varchar(200)
);


LOAD DATA INFILE
'/var/lib/mysql-files/names.csv'
INTO TABLE names  
FIELDS TERMINATED BY '\t|\t'
LINES TERMINATED BY '\t|\n'
(tax_id, name_txt, unique_name, name_class);