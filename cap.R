#install packages and load libraries
if (!requireNamespace("BiocManager", quietly=TRUE))
  install.packages("BiocManager")
BiocManager::install("clusterProfiler")

if (!requireNamespace("BiocManager", quietly=TRUE))
  install.packages("BiocManager")

BiocManager::install("AnnotationDbi")

if (!requireNamespace("BiocManager", quietly=TRUE))
  install.packages("BiocManager")

BiocManager::install("org.Mm.eg.db")

install.packages("gplots")

library(clusterProfiler)
library(org.Mm.eg.db)
library(AnnotationDbi)

library(ggplot2) #graphics
library(clusterProfiler) #package that does most of the actual GO term analyses
library(enrichplot) #graphics for GO term enrichment
library(ggridges) #graphics
library(ggnewscale) #graphics
library(europepmc) #lets us query the PMC publication database

library(gplots)

#load in normalized counts
norm_counts <- read.csv("C:/Users/jenel/Downloads/WT_MKO_normalized_counts.csv")

#load in differential gene expression
WT_MKO_limma <- read.csv("C:/Users/jenel/Downloads/WT_MKO_limma.csv")
#sort dataset based on adjusted p value
WT_MKO_limma_sort <- WT_MKO_limma[order(WT_MKO_limma$adj.P.Val),]
#select top 100 differentially expressed genes
WT_MKO_limma_top100 <- WT_MKO_limma_sort[1:100,]
#get the top 100 normalized counts based on the symbols in the top 100 differentially expressed genes
top_norm_counts <- norm_counts[norm_counts$SYMBOL %in% WT_MKO_limma_top100$SYMBOL,]

#make the symbol column the rownames
row.names(top_norm_counts) <- top_norm_counts$SYMBOL
#get the columns with the counts
top_norm_counts_relevant <- top_norm_counts[,4:7]
#save as a matrix
top_norm_counts_mat <- as.matrix(top_norm_counts_relevant)
#make heatmap
heatmap.2(x=top_norm_counts_mat,trace="none", main="Wild-Type vs. Mif Knockout: Top 100 DE Genes", xlab="Sample", ylab="Genes", scale="row",col="bluered",dendrogram="row",keysize=1.0, density.info="none",cexCol=0.5,srtCol=45)

#read in normalized counts with header=True
#norm_counts <- read.csv("C:/Users/jenel/Downloads/WT_MKO_normalized_counts.csv", header=TRUE)
#create a pca from matrix
norm_pca=prcomp(t(top_norm_counts_mat),center = T,scale. = T)
#look at the summary
summary(norm_pca)
#x values of norm_pca
norm_pca$x
#compare the different components
# PC2 vs. PC1
plot(norm_pca$x[,2]~norm_pca$x[,1],xlab = "PC1",ylab = "PC2",cex=0.1)
text(norm_pca$x[,2]~norm_pca$x[,1],labels=rownames(norm_pca$x),cex=0.9,font=2)

# PC3 vs. PC1
plot(norm_pca$x[,3]~norm_pca$x[,1],xlab = "PC1",ylab = "PC3",cex=0.1)
text(norm_pca$x[,3]~norm_pca$x[,1],labels=rownames(norm_pca$x),cex=0.9,font=2)

# PC4 vs. PC1
plot(norm_pca$x[,4]~norm_pca$x[,1],xlab = "PC1",ylab = "PC4",cex=0.1)
text(norm_pca$x[,4]~norm_pca$x[,1],labels=rownames(norm_pca$x),cex=0.9,font=2)

# PC3 vs. PC2
plot(norm_pca$x[,3]~norm_pca$x[,2],xlab = "PC2",ylab = "PC3",cex=0.1)
text(norm_pca$x[,3]~norm_pca$x[,2],labels=rownames(norm_pca$x),cex=0.9,font=2)

# PC4 vs. PC2
plot(norm_pca$x[,4]~norm_pca$x[,2],xlab = "PC2",ylab = "PC4",cex=0.1)
text(norm_pca$x[,4]~norm_pca$x[,2],labels=rownames(norm_pca$x),cex=0.9,font=2)

# PC4 vs. PC3
plot(norm_pca$x[,4]~norm_pca$x[,3],xlab = "PC3",ylab = "PC4",cex=0.1)
text(norm_pca$x[,4]~norm_pca$x[,3],labels=rownames(norm_pca$x),cex=0.9,font=2)

#GO Term Enrinchment Analysis

# get the log2 fold change stored as a vector
original_gene_list <- WT_MKO_limma$logFC

# name the vector with the EntrezIDs
names(original_gene_list) <- WT_MKO_limma$ENTREZID

# omit any NA values (here shouldn't be any missing values for either variable, but this is always a good thing to check.) 
gene_list<-na.omit(original_gene_list)

# sort the list in decreasing order (required for clusterProfiler)
gene_list = sort(gene_list, decreasing = TRUE)

#perform go term enrichment
gse <- gseGO(geneList=gene_list, 
             ont ="BP", 
             keyType = "ENTREZID",
             minGSSize = 3, 
             maxGSSize = 800, 
             pvalueCutoff = 0.05, 
             verbose = TRUE, 
             OrgDb = org.Mm.eg.db, 
             pAdjustMethod = "none")

#create dotplot of the go term enrichment results
dotplot(gse, showCategory=10,x="NES", split=".sign") + facet_grid(.~.sign)

#save gse as a file for future use
write.csv(gse, "C:/Users/jenel/Documents/gse.csv", row.names = TRUE)
