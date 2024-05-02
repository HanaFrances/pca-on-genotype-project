# Parse PCF

from pysam import VariantFile # what does this do ?
import numpy as np
from sklearn import decomposition
import pandas as pd

vcf_filename = "ALL.chr22.phase3_shapeit2_mvncall_integrated_v5b.20130502.genotypes.vcf"
panel_filename = "integrated_call_samples_v3.20130502.ALL.panel"

genotypes = [] #list of the different allele information 
samples = [] #list of the different genome samples
variant_ids = [] #list of the SNPs aka recods 

# Loop through samples and pull information about the allels at each SNP
with VariantFile(vcf_filename) as vcf_reader:
    counter = 0
    for record in vcf_reader:
        counter += 1 # adds one to the counter every itteration of loop 
        if counter % 100 == 0: #if the remainder of counter/100 is 0 proceed to collect information about SNPs 
            alleles = [record.samples[x].allele_indices for x in record.samples] # loops through every SPN in each genome (sample) to pull the allele information ex (1,0)
            samples = [sample for sample in record.samples] # loops through every genome and records the identifying name
            genotypes.append(alleles) # saves the allele information. Sample names don't matter becuase they are the same for every SPN 
            variant_ids.append(record.id) #record.id is the SNP id. Every SNP that is chosen is recordered here 
        if counter % 11035 == 0: # use grep -v "^#" ALL.chr22.phase3_shapeit2_mvncall_integrated_v5b.20130502.genotypes.vcf|wc -l to determine how many SNPS are in the file
            print(counter)
            print(f'{round(100 * counter / 1103547)}%')

# Loop through the panel table to get the populaiton codes in a dictionary. Why is dictionary important here? why not a table?
            
with open(panel_filename) as panel_file:
    labels={} # this is a dictionary and will have the format {sample_id: population_code}
    for line in panel_file:
        line=line.strip().split('\t') #split the table on the tab 
        labels[line[0]]=line[1] #this is adding lines to the dictionary where line[0] is the indexed value/sample_id and line[1] is the population code 


print(variant_ids) #the snp ids
genotypes= np.array(genotypes) #why stored as an array? Each genotype has three peices of infromation: The sample ID?
print(genotypes.shape) #three dimention array?

#Build a matrix with the genotype array
matrix = np.count_nonzero(genotypes, axis=2) #to understand who has a polymorphism and who doesn't we count up the nonzero's in the alleles (bc there are two for diploids). Axis 2 just means you are looking in the 3rd dimensoin acess for the snp data  

matrix = matrix.T #transpose? matrix to get the SNP record on the y axis and the samples & snp counts on the x axes 
print(matrix.shape)

# PCA

pca = decomposition.PCA(n_components=2) #set up PCS with 2 components. the model
pca.fit(matrix) #fit the matrix data to the model
print(pca.singular_values_) #print out the pca values
to_plot = pca.transform(matrix) #actually applies dimensionality reduction to data  
print(to_plot.shape) #print shape of reduced data 

df = pd.DataFrame(matrix, columns=variant_ids, index=samples) #make df with matrix and varient id's (aks snp id) samples are intexed which allows you to attached the population to df 
df['Population code'] = df.index.map(labels) #map values using labels. by indexing the sample we can avoid a merge and we can use index.map 
df.to_csv("matrix.csv") #export to csv
