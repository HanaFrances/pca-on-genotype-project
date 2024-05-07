# PCA on Genotype Project 

I recreated a computational biology analysis by Maria Nattestad which she detailed in a [youtube video](https://www.youtube.com/watch?v=-PCKK_nwFdA&feature=youtu.be). This video was inspired by the Nature paper Genes Mirror Georgraphy within Europe by Novembre et. Al. In this paper they used Principal Component Analysis (PCA) to produce a two-dimentional visual summary of SNP variation that mirrored a geographoc map of Europe.


### Files in this project

1. Genes and Geography Project Report.md: This is a markdown file that summarizes the project methods and results.
2. vcf_to_matrix: This is a script that extract the SNP infromation from the vcf file, runs PCA and returns a csv
3. marticx.csv: This is the csv result from extracting the SNP infromation. Rows are Sample genomes and columns are snp information
4. PCA_Genes_and_geography.ipynd: This is a Jupyter Notebooknof the code used to create the final figure.
