#!/usr/bin/env python
# coding: utf-8

# In[303]:


import pandas as pd
from sklearn.preprocessing import LabelEncoder
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import ticker


# In[304]:


#Differential Gene Expression Dataset


# In[305]:


dge = pd.read_csv(r"C:\Users\jenel\Downloads\WT_MKO_limma.csv")
dge.head()


# In[306]:


#find top 5 gene names
dge['GENENAME'].head(5)


# In[307]:


#GO Term Enrichment Dataset


# In[308]:


go = pd.read_csv(r"C:\Users\jenel\Documents\gse.csv")


# In[309]:


go.head()


# In[310]:


#go.drop("Unnamed: 0", inplace = True, axis=1)


# In[311]:


#find top five decriptions
go['Description'].head(5)


# In[312]:


#Arthritis Dataset


# In[313]:


arthritis = pd.read_csv(r"C:\Users\jenel\Downloads\U.S._Chronic_Disease_Indicators__Arthritis.csv")


# In[314]:


arthritis.head()


# In[315]:


#find statistics about the dataset
arthritis.describe()


# In[316]:


#get more information on the datatypes and null values
arthritis.info()


# In[317]:


#check to if there is more than one data value units
arthritis["DataValueUnit"].unique()


# In[318]:


#select yearstart, location, question, questionID, stratification1, DataValueType, and DataValueAlt columns
arthritis = arthritis[["YearStart","LocationDesc", "Question", "QuestionID","Stratification1", "DataValueType","DataValueAlt"]]


# In[319]:


arthritis.head()


# In[320]:


#count the number of entries per year

year = arthritis["YearStart"].value_counts()
print(year)

#plot the counts
year.plot(kind='bar')


# In[321]:


#count the number of entries per stratification
stratification = arthritis["Stratification1"].value_counts()
print(stratification)

#plot the counts
stratification.plot(kind='bar')


# In[322]:


#count the number of entries per location

location = arthritis["LocationDesc"].value_counts()
print(location)


# In[323]:


#plot the counts
plt.figure(figsize = (12,12))
location.plot(kind='bar')


# In[324]:


##count the number of entries per question
question = arthritis["Question"].value_counts()
print(question)

#plot the counts
question.plot(kind='barh')


# In[325]:


#create pivot table to see data value per question
question_pivot = arthritis.pivot_table(index=['QuestionID','Question','DataValueType'],columns=None,dropna=True)
question_pivot.drop(columns=['YearStart'],axis=1).round(2).head(25)


# In[326]:


#create a pivot table with stratification

stratification_pivot = arthritis.pivot_table(values='DataValueAlt',index=['Question','DataValueType'], columns='Stratification1',aggfunc='mean',dropna=True).round(2)

#drop nulls
stratification_pivot.dropna(inplace=True)
stratification_pivot


# In[327]:


#find statistical summary of the pivot table
stratification_pivot.describe()


# In[341]:


#create stacked horizontal bar graph of the data values for each stratification

ax = stratification_pivot.plot(kind='barh', stacked=True, title='Stratification per Question')
ax.invert_yaxis() 
ax.set(xlabel='Data Value %', ylabel='Question')

#format legend
ax.legend(title='Stratification', ncol=8, bbox_to_anchor=(-0.2, -0.2),loc='upper left')

#show xaxis in thousands
ax.xaxis.set_major_formatter(ticker.EngFormatter())

# remove the top and right lines from the figure to make it less boxy
for spine in ['top', 'right']:ax.spines[spine].set_visible(False)


# In[329]:


#create heatmap of average crude and age adjusted values for each question based on stratification

#change index to questionID
stratification_pivot2 = arthritis.pivot_table(values='DataValueAlt',index=['QuestionID'], columns='Stratification1',aggfunc='mean',dropna=True).round(2)

#drop nulls
stratification_pivot2.dropna(inplace=True)

#transponse and find correlation
stratification_corr = stratification_pivot2.transpose().corr()

#plot heatmap
plt.figure(figsize = (12,12))
sns.heatmap(stratification_corr,annot=True)
plt.show()


# In[330]:


#create a pivot table with location

location_pivot = arthritis.pivot_table(values='DataValueAlt',index=['Question','DataValueType'], columns='LocationDesc',aggfunc='mean',dropna=True).round(2)

#drop nulls
location_pivot.dropna(inplace=True)
location_pivot


# In[331]:


#find statistical summary of the pivot table
with pd.option_context('display.max_columns', 55):
    display(location_pivot.describe(include='all'))


# In[340]:


#https://opendatascience.com/how-to-pivot-and-plot-data-with-pandas/
#create stacked horizontal bar graph of the data values for each stratification

plt.figure(figsize = (12,12))
ax = location_pivot.plot(kind='barh', stacked=True, title='Location per Question')
ax.invert_yaxis() 
ax.set(xlabel='Data Value %', ylabel='Question')

#format legend
ax.legend(title='Location', ncol=10, bbox_to_anchor=(-0.2, -0.2),loc='upper left')

#show xaxis in thousands
ax.xaxis.set_major_formatter(ticker.EngFormatter())

# remove the top and right lines from the figure to make it less boxy
for spine in ['top', 'right']:ax.spines[spine].set_visible(False)


# In[333]:


#create heatmap of average crude and age adjusted values for each question based on stratification

#change index to questionID
location_pivot2 = arthritis.pivot_table(values='DataValueAlt',index=['QuestionID'], columns='LocationDesc',aggfunc='mean',dropna=True).round(2)

#drop nulls
location_pivot2.dropna(inplace=True)

#transponse and find correlation
location_corr = location_pivot2.transpose().corr()

#plot heatmap
plt.figure(figsize = (12,12))
sns.heatmap(location_corr,annot=True)
plt.show()


# In[334]:


#create a pivot table with yearstart

yearstart_pivot = arthritis.pivot_table(values='DataValueAlt',index=['Question','DataValueType'], columns='YearStart',aggfunc='mean', dropna=True).round(2)

#drop nulls
yearstart_pivot.dropna(inplace=True)
yearstart_pivot


# In[335]:


#find statistical summary of the pivot table
yearstart_pivot.describe()


# In[339]:


#create stacked horizontal bar graph of the data values for each stratification

ax = yearstart_pivot.plot(kind='barh', stacked=True, title='Year per Question')
ax.invert_yaxis() 
ax.set(xlabel='Data Value %', ylabel='Question')

#format legend
ax.legend(title='YearStart',ncol=10, bbox_to_anchor=(-0.2, -0.2),loc='upper left')

#show xaxis in thousands
ax.xaxis.set_major_formatter(ticker.EngFormatter())

# remove the top and right lines from the figure to make it less boxy
for spine in ['top', 'right']:ax.spines[spine].set_visible(False)


# In[337]:


#create heatmap of average crude and age adjusted values for each question based on stratification

#change index to questionID
yearstart_pivot2 = arthritis.pivot_table(values='DataValueAlt',index=['QuestionID'], columns='YearStart',aggfunc='mean',dropna=True).round(2)

#drop nulls
yearstart_pivot2

#transponse and find correlation
yearstart_corr = yearstart_pivot2.transpose().corr()

#plot heatmap
plt.figure(figsize = (12,12))
sns.heatmap(yearstart_corr,annot=True)
plt.show()

