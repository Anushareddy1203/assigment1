# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 02:50:50 2022

@author: anush
"""

#!/usr/bin/env python
# coding: utf-8

# In[1]:


#importing libraries
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns


# In[6]:


My_Data = pd.read_csv(r'drug_use.csv') #reading csv
print(My_Data)


# In[15]:


#lineplot function
def lineplot():
    plt.figure()
    plt.plot(My_Data["age"],My_Data["alcohol-use"], label = "alcohol-use") #line plotting
    plt.plot(My_Data["age"],My_Data["marijuana-use"],label = "marijuana-use") #line plotting
    plt.plot(My_Data["age"],My_Data["cocaine-use"],label = "cocaine-use")  #line plotting
    plt.plot(My_Data["age"],My_Data["heroin-use"],label = "heroin-use")  #line plotting
    plt.plot(My_Data["age"],My_Data["hallucinogen-use"],label = "hallucinogen-use")  #line plotting
    plt.xlabel('Age',color = 'black',fontsize = 15) 
    plt.title('Drug Usage by people',color = 'red',fontsize = 20)   #title of plot
    plt.legend()
    plt.xticks(rotation=45)
    plt.yticks(rotation=0)
    plt.show()

#calling function lineplot
lineplot()


# In[124]:


#creating labels from columns
labels=My_Data.iloc[:,2:15:2].columns

# defining pie_chart 
def pie_chart():
    plt.pie(My_Data.iloc[:,2:15:2].sum(),labels=labels,explode=[0.1,0.1,0.1,2,1.3,0.1,0.1],autopct='%1.2f%%')   #gives piechart figures
    plt.title('Content of Use',color='brown',fontweight="bold",fontsize = '25')    #title of figure
    plt.show()   #shows graph              
        

#calling pie_chart function
pie_chart()


# In[120]:


#bar_chart function
def bar_chart():
    plt.bar(My_Data['age'], My_Data['alcohol-use'], tick_label = My_Data['age'],width = 0.8) #gives figure of barchart
    plt.xlabel('Age')  #x-axis label
    plt.xticks(rotation=45)
    plt.ylabel('alcohol-use')  #y-axis label
    plt.title('Effected people accordingly age',color='red')  #title of figure
    plt.show()




bar_chart()


# In[ ]:




