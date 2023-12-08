#Charna Notes: This code was used to create graphs from the data extracted from the Senior's Survey
#!/usr/bin/env python
# coding: utf-8
# In[2]:


#libraries imported to create plots
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import textwrap


# In[3]:


#CSV with results from SQL analysis are imported
df = pd.read_csv('results.csv')
df.head()


# In[85]:


#Bar charts will be made for the data

#lists are made of column titles, and a list of the first row are made
X = list(['totalrespondents', 'Use TTC', 'Frequently Use TTC', "Do not Frequently Use TTC", 'TTC Too Far', 'TTC Inaccessible']) 
Y = df.iloc[0].tolist()

#updating values to percentage points
divisor = Y[0] #this was the total respondents
Y_pct = [((x/divisor)*100) for x in Y] #iteration through each element to transform into percentage points


#figure made to plot results, and grid made below it
fig, ax = plt.subplots(figsize =(6, 10))
plt.grid(axis = 'y')
plt.yticks(range(0, 110, 10)) #sets the tick marks for the grid, in a range from 0-100
ax.set_axisbelow(True) #sets the grid to be below the plot


# The data is plotted using bar() method 
#only the second, third, and fourth columns are displayed - as they relate to transit use
plt.bar(X[1:4], Y_pct[1:4], color='lightgrey', edgecolor='black')
plt.ylim(top = 100) #upper limit of graph

#titles and labels added
plt.title("2017 Survey Results from Seniors") 
plt.xlabel("Criteria", fontweight='bold') 
plt.ylabel("Percentage of Respondents (n=6939)", fontweight='bold') 
ax.set_xticklabels(ax.get_xticklabels(), rotation=90)


#labels added with the % above each bar
ax.bar_label(ax.containers[0], label_type='edge', padding=5, fmt='%.2f%%')

#because the labels were long for each bar, this textwrap code was utilized
#source for code is Petrou, 2021, see citations
def wrap_labels(ax, width, break_long_words=False):
    labels = []
    for label in ax.get_xticklabels():
        text = label.get_text()
        labels.append(textwrap.fill(text, width=width,
                      break_long_words=break_long_words))
    ax.set_xticklabels(labels, rotation=0)
wrap_labels(ax, 10)
#ax.figure

# Show the plot 
plt.show() 


# In[84]:


#Creating a bar plot to showcase accesibility/proximity issues as hilighted by respondents

#updating count values to percentage points
divisor = Y[3] #this was the total who don't Frequently Use TTC"
Y_pct_sub = [((x/divisor)*100) for x in Y] #iteration through each element to transform into percentage points

#figure made to plot results, and grid made below it
fig, bx = plt.subplots(figsize =(6, 10))

#grid made to ease 
plt.grid(axis = 'y')
plt.yticks(range(0, 110, 10)) #sets the tick marks for the grid, in a range from 0-100
bx.set_axisbelow(True) #sets the grid to be below the plot


# Data is plotted using bar() method 
#only the last two columns are used as they relate to seniors not using TTC
ax = plt.bar(X[4:], Y_pct_sub[4:], color='lightgrey', edgecolor='black')
plt.ylim(top = 100)
plt.title("Results from Seniors Who Don't Frequently Use TTC") 
plt.xlabel("Reason", fontweight='bold') 
plt.ylabel("Percentage of Respondents (n=3002)", fontweight='bold') 


#labels added with the % above each bar
bx.bar_label(bx.containers[0], label_type='edge', padding=5, fmt='%.2f%%')

# Show the plot 
plt.show() 

