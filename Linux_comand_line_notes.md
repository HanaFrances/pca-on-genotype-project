These are the comands used to work with the Vcf file. Samtools requires linux to run. Use Ubuntu app.

### Command to get the file from the 1000 genomes website 
curl -O http://ftp.1000genomes.ebi.ac.uk/vol1/ftp/release/20130502/ALL.chr22.phase3_shapeit2_mvncall_integrated_v5b.20130502.genotypes.vcf.gz

### Command to unzip and keep the gz file 
gunzip -k ALL.chr22.phase3_shapeit2_mvncall_integrated_v5b.20130502.genotypes.vcf.gz

### Command to count the number of snp in the file 
grep -v "^#" ALL.chr22.phase3_shapeit2_mvncall_integrated_v5b.20130502.genotypes.vcf|wc -l
1103547

test
