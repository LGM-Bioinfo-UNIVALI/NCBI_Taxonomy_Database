create database taxonomy;

use taxonomy;

use ncbi_data;
create table nodes (
	tax_id int,
    parent_taxnodes_id int,
    _rank varchar(30),
    embl_code varchar(5),
    division_id int,
    inherited_div_flag boolean, 
    genetic_code_id int,
    inherited_GC_flag boolean,
    mitochondrial_genetic_code_id int,
    inherited_MGC_flag boolean,
    GenBank_hidden_flag boolean,
    hidden_subtree_root_flag boolean,
    comments varchar(240)
);

LOAD DATA LOCAL INFILE
'C:/Users/bioinfo3/Documents/Ellen/NCBI Taxonomy Database/taxdump/nodes.csv'
INTO TABLE nodes  
FIELDS TERMINATED BY '\t|\t'
LINES TERMINATED BY '\t|\n'
(tax_id, parent_taxnodes_id, _rank, embl_code, division_id, inherited_div_flag, genetic_code_id, inherited_GC_flag, mitochondrial_genetic_code_id, inherited_MGC_flag, GenBank_hidden_flag, hidden_subtree_root_flag, comments);

create table names (
	tax_id int,
    name_txt varchar(500),
    unique_name varchar(200),
    name_class varchar(200)
);

LOAD DATA LOCAL INFILE
'C:/Users/bioinfo3/Documents/Ellen/NCBI Taxonomy Database/taxdump/names.csv'
INTO TABLE names  
FIELDS TERMINATED BY '\t|\t'
LINES TERMINATED BY '\t|\n'
(tax_id, name_txt, unique_name, name_class);

create table division (
	division_id int,
    division_cde varchar(10),
    division_name varchar(100),
    comments varchar(500)
);

LOAD DATA LOCAL INFILE
'C:/Users/bioinfo3/Documents/Ellen/NCBI Taxonomy Database/taxdump/division.csv'
INTO TABLE division  
FIELDS TERMINATED BY '\t|\t'
LINES TERMINATED BY '\t|\n'
(division_id, division_cde, division_name, comments);

create table accession2taxid (
	accession varchar(150),
    accession_version varchar(200),
    taxid int,
    gi int
);


LOAD DATA LOCAL INFILE
'D:/accession2taxid/nucl_wgs.csv'
INTO TABLE accession2taxid  
FIELDS TERMINATED BY '\t'
LINES TERMINATED BY '\n'
ignore 1 lines
(accession, accession_version, taxid, gi);
