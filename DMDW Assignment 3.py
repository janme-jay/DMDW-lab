#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[3]:


data = pd.read_csv(r"https://raw.githubusercontent.com/archana1822/DMDW-Lab/main/Toyota.csv")


# In[6]:


data.head()


# In[7]:


type(data)


# In[10]:


data.shape


# In[11]:


data.info()


# In[12]:


data.index


# In[13]:


data.columns


# In[14]:


data.head()


# In[15]:


data.tail()


# In[16]:


data.head(5)


# In[17]:


data[['Price',"Age"]].head(10)


# In[18]:


data[['Age','KM']].head(10)


# In[19]:


data.isnull().sum()


# In[46]:


data.dropna(inplace=True)


# In[47]:


data.isnull().sum()


# In[48]:


data.shape


# In[49]:


data.head(10)


# In[50]:


data['MetColor'].mean()


# In[51]:


data['Weight'].mean()


# In[52]:


data['MetColor'].head()


# In[53]:


import numpy as np


# In[54]:


data['MetColor'].replace(np.NaN,data['MetColor'].mean()).head()


# In[55]:


data.head(10)


# In[56]:


data['CC'].mean()


# In[57]:


data['CC'].head()


# In[59]:


data[['Age',"KM"]].head(20)


# In[ ]:




