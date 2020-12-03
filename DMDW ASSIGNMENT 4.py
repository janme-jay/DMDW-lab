#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[3]:


path="https://raw.githubusercontent.com/archana1822/DMDW-Lab/main/Toyota.csv"


# In[4]:


import pandas as pd
data=pd.read_csv(path)


# In[5]:


data.shape


# In[6]:


data.head()


# In[7]:


plt.scatter(data['Age'],data['Price'],c='crimson')
plt.xlabel('Age(months)')
plt.ylabel('Price)(Euros)')
plt.show()


# In[8]:


plt.hist(data['KM'])


# In[9]:


plt.hist(data['KM'],
color = 'green',
edgecolor = 'orange',
bins = 5)
plt.title('Histograms of kilometers')
plt.xlabel('kilometer')
plt.ylabel('Frequency')
plt.show()


# In[10]:


counts = [979, 120, 12]
fuelType = ('Petrol', 'Diesel', 'CNG')
index = np.arange(len(fuelType))
plt.bar(index, counts, color=['red', 'blue', 'cyan'])
plt.title('Bar plot of fuel types')
plt.xlabel('Fuel Types')
plt.ylabel('Frequency')
plt.xticks(index, fuelType, rotation = 90)
plt.show()


# In[11]:


import seaborn as sns
sns.set(style="darkgrid")
sns.regplot(x=data['Age'],y=data['Price'])


# In[15]:


sns.countplot(x="FuelType", data=data, hue = "Automatic")


# In[16]:


sns.countplot(x="FuelType", data=data)


# In[17]:


sns.distplot(data['Age'],kde=False,bins=5)


# In[19]:


#box plot diagram
sns.boxplot(y=data["Price"])


# In[20]:


#muliple data representation on box plot
sns.boxplot(x=data['FuelType'], y=data["Price"])


# In[21]:


sns.boxplot(x = "FuelType", y=data["Price"], hue = "Automatic",data=data)


# In[22]:


f,(ax_box, ax_hist)=plt.subplots(2, gridspec_kw={"height_ratios":(.20,.80)})


# In[23]:


f,(ax_box, ax_hist)=plt.subplots(2, gridspec_kw={"height_ratios":(.20,.80)})
sns.boxplot(data["Price"],ax=ax_box)
sns.distplot(data["Price"],ax=ax_hist,kde=False)


# In[24]:


sns.pairplot(data, kind="countplot",hue="FuelType")
plt.show()


# In[ ]:




