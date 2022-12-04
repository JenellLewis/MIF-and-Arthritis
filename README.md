# MIF-and-Arthritis
# Introduction
Macrophage Migration Inhibitory Factor:
This gene encodes a lymphokine involved in cell-mediated immunity, immunoregulation, and inflammation. It plays a role in the regulation of macrophage function in host defense through the suppression of anti-inflammatory effects of glucocorticoids.  
Broad expression in kidney, prostate, and 21 other tissues 

Arthritis is the swelling of joints mainly caused by an immune response.

The MIF gene has been linked to being a cause of arthritis.

Targeting this gene can be a possible treatment option.

# Datasets
RNASeq Datasets:
Samples:
Mif knockout: ERR4368607 and ERR4368608
Wild-type: ERR4368610 and ERR4368611
Fastq format
Paired-end


Arthritis Dataset:
CDC Chronic Disease Indicator Arthritis
Features used:
YearStart
Location
Question
Stratification1
DataValue

# Hypothesis
Hypothesis for MIF gene:
The top differentially expressed genes will have functions in immunology. 


Hypothesis for Arthritis:
States with an overall large prevalence of arthritis will also have a large prevalence of patients who also have another disease. There is also a larger prevalence in women compared to men.

# Methods and Results
Initial analysis was done in the opensource Galaxy website:
FASTQC
CUTADAPT
ALIGNMENT
Differential Gene Expression
Volcano Plot and Heatmap created in R from the Differential Gene Expression results.
GO Term Enrichment Analysis done in R from the Differential Gene Expression results.

Exploratory Data Analysis
Create pivot tables to get  prevalence values for each feature
Find statistics on the features based on the prevalence values
Create heatmaps to find the correlation between the questions based on the prevalence

Volcano Plot of the top ten differentially expressed genes in Wild Type vs MIF Knockout. Most of the genes are downregulated in wild type and MIF and FGF10 are upregulated in the wild type. 

![image](https://user-images.githubusercontent.com/80493086/205506626-c2d1fc0b-df8b-463a-8607-e481295dfb6d.png)

Heatmap of Wild Type vs MIF knockout. The blue represents downregulation, and the red represents upregulation. The wild type samples had a lot of downregulated genes, while the MIF knockout had a lot of upregulated genes 

![image](https://user-images.githubusercontent.com/80493086/205506718-fda0e8ab-c9a1-4eac-9bc4-89f7eadb848a.png)

PCA graph of PC1 vs PC2. PC1 separates the samples by condition (MIF genes to the left and wild type to the right of the graph). PC2 separates the MIF samples.

![image](https://user-images.githubusercontent.com/80493086/205506733-4ff0633e-4576-4344-9974-527cb02dab93.png)

PCA of PC1 vs PC3. PC1 separates the samples by condition. PC3 separates the wild type samples.

![image](https://user-images.githubusercontent.com/80493086/205506746-1c09aeb0-f69a-4949-87d7-1021164e130a.png)

PCA of PC1 vs PC4. PC1 separates the samples by condition. PC4 separates both the MIF samples and wild type samples.

![image](https://user-images.githubusercontent.com/80493086/205506758-7b046fc5-a6a7-4b0b-b179-c80310c3b409.png)

GO Term plot of the top ten activated and suppressed genes. The count is represented by the size of the dot and the adjusted p-value is represented by the color. 

![image](https://user-images.githubusercontent.com/80493086/205506783-98c07ced-f016-4474-a30a-d413b48d3065.png)

QuestionID and Question key to read heatmaps

![image](https://user-images.githubusercontent.com/80493086/205506798-a5a5a813-db95-448c-9579-aa84c12b8aa8.png)

Correlation heatmap of the questions based on the average Stratification prevalence values.

![image](https://user-images.githubusercontent.com/80493086/205506821-dc443c8f-b312-4210-897b-4ff4558a0f32.png)

Correlation heatmap of the questions based on the average Location prevalence values. 

![image](https://user-images.githubusercontent.com/80493086/205506836-72bcee2a-558e-42fe-affd-8d0cefbbc501.png)

Correlation heatmap of the questions based on the average YearStart prevalence values. 

![image](https://user-images.githubusercontent.com/80493086/205506854-31a309fc-72ae-4fa6-bf01-75685c4c9777.png)



# Conclusion
The results of the differential gene expression of wild type vs MIF knockout show that more viral response genes are activated in MIF knockout, along with cell development genes. 
The analysis of the arthritis dataset shows that men are less likely to have arthritis than women, which supports previous literature. 
Also, the states that had a high prevalence of arthritis had the highest amount of arthritis with heart disease and diabetes. This shows that a reduction in these diseases can help in reducing arthritis. 
Since most of the differentially expressed genes did not have immunology functions, the null hypothesis of the MIF gene analysis is accepted.
Since the results for the arthritis dataset aligned with previous literature, the null hypothesis of the arthritis analysis is rejected.
A limitation of the study was having access to MIF knockout datasets in arthritis patients along with that dataset being large enough for predictive analysis. Also, there were not many publicly available arthritis datasets. 
For future work, the MIF gene in arthritis patients vs MIF knockout or MIF inhibition will be interesting, so that a better understanding of the mechanism can be understood. This can possibly help in developing treatment options.





