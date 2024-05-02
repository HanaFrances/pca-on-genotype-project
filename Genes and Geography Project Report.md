# Gene and Georgraphy Bioinformatics Project 


## Introduction
This project was modeled after the github of MariaNattestad which was inspired by the Nature paper Genes Mirror Georgraphy within Europe by Novembre et. Al. In this paper they used Principal Component Analysis (PCA) to produce a two-dimentional visual summary of SNP variation which mirrored a geographic map of Europe.

## Methods 
### Data collection
Data was sourced from the 1000 Genome Project database. I used the most recent SNP data (2021) chomosome 22 stored in a VCF file. 

Each line of a the file contains an 
**SNP ID**: This is used to identify the different SNPs sequneced 
**Sample ID**: This is a code that corresponds to the genome    
**Alleles Information**: This is where the information about what allele the sample has. Allele information is writen as two numbers because humans have two copies of thier DNA. When an sample matches the referene allele it is identified as 0. WHen the sample mathes the first allele it is identified as 1 and continues like that for the total number of alleles a SNP may have. For this project all non 0 alleles will be consider the same. 

### Extracting SNP information
To extract the SNP information the tool **pysam** was used. This is a bioinformatics tool to work with BAM & SAM formatted genetic data files. Details about this process can be found in the script vcf_to_matrix.py. The SNPs data was extracted into a numpy 2D matrix that can be used to perform the PCA on.  

### PCA 
PCA was used to reduce a matrix of SNP data into two dimentions then ploted. PCA is a method that reduces the number of variables of a data set, while perserving as much information as possible. In this case we reduce to two variables so they can be easily plotted. Tools used for this analysis were **Sklearn** and **numpy**.

### Plotting the Data 
To plot the final results of the PCA I used carried out the analysis in a Jupyter Notebook PCA_Genes_and_geography1.ipynb and used the package **altair**. This package works similarly to R's ggplot; however, to use it you need to have fewer than 5000 data points. 



## Results
![](Finalfigure.png)


## Discussion 


## Conclusion 
