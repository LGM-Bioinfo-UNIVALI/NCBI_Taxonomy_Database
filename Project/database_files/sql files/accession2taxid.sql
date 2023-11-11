use ncbi_data;

create table accession2taxid (
	Accession varchar(200),
    AccessionVersion varchar(200),
    TaxId varchar(200),
	GI varchar(200)
);

drop table accession2taxid;

select * from accession2taxid;

LOAD DATA INFILE
'/var/lib/mysql-files/accession2taxid_00.csv'
INTO TABLE accession2taxid  
FIELDS TERMINATED BY '\t'
LINES TERMINATED BY '\n'
(Accession, AccessionVersion, TaxId, GI);