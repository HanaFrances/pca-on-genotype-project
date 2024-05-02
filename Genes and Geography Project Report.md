## Gene and Georgraphy Bioinformatics Project 


### Introduction
This project was modeled after the github of MariaNattestad whcih was inspired by the Nature paper Genes Mirror Georgraphy within Europe by Novembre et. Al. In this paper they used Principal Component Analysis (PCA) to produce a two-dimentional visual summary of SNP variation mirrored a geographoc map of Europe.

### Methods 
To practice bioinfromatic and data science techniques I followed MariaNattestad methods for recreating this anaylsis with 1000 genome project SNP data.  What is PCA?

#### Data 
Data was sourced from the 1000 Genome Project database. I used the most recent SNP data (2021) chomosome 22 stored in a VCF file. 

Each line of a the file contains an 
**SNP ID**: This is used to identify the different SNPs sequneced 
**Sample ID**: This is a code that corresponds to the genome    
**Alleles Information**: This is where the information about what allele the sample has. Allele information is writen as two numbers because humans have two copies of thier DNA. When an sample matches the referene allele it is identified as 0. WHen the sample mathes the first allele it is identified as 1 and continues like that for the total number of alleles a SNP may have. For this project all non 0 alleles will be consider the same. 

#### Tools 
**pysam**: This is a bioinformatics tool to work with BAM & SAM formatted genetic data files. VariantFile: is used to iterate through VCF and BCF files 

**Numpy**: To work with multi dimentional arrays and matrixs.

**Sklearn**: This package is used to carry out the PCA. 

**Pandas**: For making figures. 




#### Other note 
with Statment python code
used in exception handling to make the code cleaner and readable.
* you don't need to close script the with statment takes care of that 
* Ensure that you never leave any resources open
* I need to find out the lenght of the stupid vcf file 
* 