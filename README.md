# MIF-and-Arthritis
# Introduction
MIF (Macrophage Migration Inhibitory Factor) is a gene that has been linked to many diseases such as arthritis, lung cancer, kidney disease, etc. This project focused on analyzing the effect of MIF knockout in mice. This was done to find the top differentially expressed genes when comparing wild type to MIF knockout. 
Since the MIF gene is most commonly known to be linked to arthritis, an analysis of the CDC Chronic Disease Indicator Arthritis dataset was performed. This was done to find the prevalence of arthritis and to see if there is any correlation between the different indicators or questions

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

Fig1: Volcano Plot of the top ten differentially expressed genes in Wild Type vs MIF Knockout. Most of the genes are downregulated in wild type and MIF and FGF10 are upregulated in the wild type. 

![image](https://user-images.githubusercontent.com/80493086/205506626-c2d1fc0b-df8b-463a-8607-e481295dfb6d.png)

Fig2: Heatmap of Wild Type vs MIF knockout. The blue represents downregulation, and the red represents upregulation. The wild type samples had a lot of downregulated genes, while the MIF knockout had a lot of upregulated genes 

![image](https://user-images.githubusercontent.com/80493086/205506718-fda0e8ab-c9a1-4eac-9bc4-89f7eadb848a.png)

Fig3: PCA graph of PC1 vs PC2. PC1 separates the samples by condition (MIF genes to the left and wild type to the right of the graph). PC2 separates the MIF samples.

![image](https://user-images.githubusercontent.com/80493086/205506733-4ff0633e-4576-4344-9974-527cb02dab93.png)

Fig4: PCA of PC1 vs PC3. PC1 separates the samples by condition. PC3 separates the wild type samples.

![image](https://user-images.githubusercontent.com/80493086/205506746-1c09aeb0-f69a-4949-87d7-1021164e130a.png)

Fig5: PCA of PC1 vs PC4. PC1 separates the samples by condition. PC4 separates both the MIF samples and wild type samples.

![image](https://user-images.githubusercontent.com/80493086/205506758-7b046fc5-a6a7-4b0b-b179-c80310c3b409.png)

Fig6: GO Term plot of the top ten activated and suppressed genes. The count is represented by the size of the dot and the adjusted p-value is represented by the color. 

![image](https://user-images.githubusercontent.com/80493086/205506783-98c07ced-f016-4474-a30a-d413b48d3065.png)

Fig7: QuestionID and Question key to read heatmaps

![image](https://user-images.githubusercontent.com/80493086/205506798-a5a5a813-db95-448c-9579-aa84c12b8aa8.png)

Fig8: Correlation heatmap of the questions based on the average Stratification prevalence values.

![image](https://user-images.githubusercontent.com/80493086/205506821-dc443c8f-b312-4210-897b-4ff4558a0f32.png)

Fig9: Correlation heatmap of the questions based on the average Location prevalence values. 

![image](https://user-images.githubusercontent.com/80493086/205506836-72bcee2a-558e-42fe-affd-8d0cefbbc501.png)

Fig10: Correlation heatmap of the questions based on the average YearStart prevalence values. 

![image](https://user-images.githubusercontent.com/80493086/205506854-31a309fc-72ae-4fa6-bf01-75685c4c9777.png)



# Conclusion
The results of the differential gene expression of wild type vs MIF knockout show that more viral response genes are activated in MIF knockout, along with cell development genes. 
The analysis of the arthritis dataset shows that men are less likely to have arthritis than women, which supports previous literature. 
Also, the states that had a high prevalence of arthritis had the highest amount of arthritis with heart disease and diabetes. This shows that a reduction in these diseases can help in reducing arthritis. 
Most of the top five differentially expressed genes have immunology functions, so the null hypothesis of the MIF gene analysis is rejected.
Since the results for the arthritis dataset aligned with previous literature, the null hypothesis of the arthritis analysis is rejected.
A limitation of the study was not having access to MIF knockout datasets in arthritis patients along with that dataset being large enough for predictive analysis. Also, there were not many publicly available arthritis datasets. 
For future work, the MIF gene in arthritis patients vs MIF knockout or MIF inhibition will be interesting, so that a better understanding of the mechanism can be accomplished. This can possibly help in developing treatment options.



# References
U.S. National Library of Medicine. (n.d.). Mif macrophage migration inhibitory factor [homo sapiens (human)] - gene. National Center for Biotechnology Information. Retrieved from https://www.ncbi.nlm.nih.gov/gene/4282 

Rowe, M. A., Harper, L. R., et.al. (2017, February). Reduced osteoarthritis severity in aged mice with deletion of macrophage migration inhibitory factor. Arthritis & rheumatology (Hoboken, N.J.). Retrieved from https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5274570/ 

Gua, Y., Xiaob, L., et.al. (2021, July 24). Gene knockout or inhibition of macrophage migration inhibitory factor alleviates lipopolysaccharide-induced liver injury via inhibiting inflammatory response. Hepatobiliary & Pancreatic Diseases International. Retrieved from https://www.sciencedirect.com/science/article/abs/pii/S1499387221001259 

Mawhinney, L., Armstrong, M. E., et.al. (2014). Macrophage Migration Inhibitory Factor (MIF) Enzymatic Activity and Lung Cancer. Molecular Medicine, 20(1), 729–735. https://doi.org/10.2119/molmed.2014.00136

Li, Y., Lee, P. Y., Sobel, E. S., et.al. (2009). Increased expression of FcgammaRI/CD64 on circulating monocytes parallels ongoing inflammation and nephritis in lupus. Arthritis Research & Therapy, 11(1), R6. https://doi.org/10.1186/ar2591

Barbour, K. E., Moss, S., Croft, J. B., et al.Geographic Variations in Arthritis Prevalence, Health-Related Characteristics, and Management — United States, 2015. MMWR Surveillance Summaries, 67(4), 1–28. https://doi.org/10.15585/mmwr.ss6704a1 

IRF7 Gene - GeneCards | IRF7 Protein | IRF7 Antibody. (n.d.). Www.genecards.org. Retrieved December 4, 2022, from https://www.genecards.org/cgi-bin/carddisp.pl?gene=IRF7 

Evans, D. T., Serra-Moreno, R., Singh, R. K., & Guatelli, J. C. (2010). BST-2/tetherin: a new component of the innate immune response to enveloped viruses. Trends in Microbiology, 18(9), 388–396. https://doi.org/10.1016/j.tim.2010.06.010

FGF10 gene: MedlinePlus Genetics. (n.d.). Medlineplus.gov. Retrieved December 4, 2022, from https://medlineplus.gov/genetics/gene/fgf10/

OAS2 Gene - GeneCards | OAS2 Protein | OAS2 Antibody. (n.d.). Www.genecards.org. https://www.genecards.org/cgi-bin/carddisp.pl?gene=OAS2#:~:text=This%20gene%20encodes%20a%20member






