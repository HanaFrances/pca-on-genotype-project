# Gene and Geography Bioinformatics Project

## Introduction
The goal of this project was to practice new skills in computational biology and learn how to use git to showcase data science projects. For this project, I recreated a computational biology analysis by Maria Nattestad, as demonstrated in her [YouTube video](https://www.youtube.com/watch?v=-PCKK_nwFdA&feature=youtu.be). This video was inspired by the Nature paper "Genes Mirror Geography within Europe" by Novembre et al. In this paper, they used Principal Component Analysis (PCA) to produce a two-dimensional visual summary of SNP variation that mirrored a geographic map of Europe.

## Background
Single nucleotide polymorphisms (SNPs) are a type of genetic variation found in DNA. SNPs occur when one DNA building block, or nucleotide, is replaced with another, for example, a cytosine with a thymine. These mutations usually occur in non-coding regions of the DNA and can be passed on to subsequent generations.

## Methods

### Data Collection
Data was sourced from the 1000 Genome Project database. I used the most recent SNP data (2021) from chromosome 22, stored in a VCF file.

Each line of the file contains:
- **SNP ID**: Used to identify the different SNPs sequenced.
- **Sample ID**: A code that corresponds to the genome.
- **Alleles Information**: Information about what allele the sample has. Allele information is written as two numbers because humans have two copies of their DNA. When a sample matches the reference allele it is identified as 0. When the sample matches the first allele it is identified as 1, and so on for the total number of alleles a SNP may have. For this project, all non-0 alleles will be considered the same.

### Extracting SNP Information
To extract the SNP information, the tool **pysam** was used. This is a bioinformatics tool to work with BAM & SAM formatted genetic data files. Details about this process can be found in the script `vcf_to_matrix.py`. The SNP data was then organized into a numpy 2D matrix, which facilitated the subsequent PCA. A SNP variation was identified whenever one or both alleles at a particular SNP differed from the reference SNP.

### PCA
PCA was used to reduce a matrix of SNP data into two dimensions then plotted. PCA is a method that reduces the number of variables of a data set while preserving as much information as possible. In this case, we reduce to two variables so they can be easily plotted. Tools used for this analysis were **Sklearn** and **numpy**.

### Plotting the Data
To plot the final results of the PCA, I carried out the analysis in a Jupyter Notebook, `PCA_Genes_and_Geography1.ipynb`, and used the package **altair**. This package works similarly to R's ggplot; however, to use it you need to have fewer than 5000 data points.

## Results
The figure below shows the final result of the PCA. The first and second principal components are plotted on the x and y axes, respectively. Each point represents one sample of genome, and each genome is colored based on which geographic region the sample was collected from. Samples were collected from 5 regions: Africa, America, East Asia, Europe, and Southern Asia.

### Interesting Findings:
- African and East Asian genomes have fairly unique clusters, whereas American, European, and South Asian genomes have a lot more overlapping.
- American genomes are fairly dispersed compared to other regions, overlapping with European and South Asian genomes the most.

![](Finalfigure.png)

## Discussion
The results of this project are consistent with the logic that SNPs are very similar in genomes from the same regions previously studied in "Genes Mirror Geography within Europe" by Novembre et al. Additionally, it is interesting to see more variation in the American genomes suggesting that they may have less in common with each other than genomes from other regions.

## Conclusion
In conclusion, this project was effective in pulling together concepts of computational biology and data science, and I am more confident in my ability to apply these techniques going forward.
