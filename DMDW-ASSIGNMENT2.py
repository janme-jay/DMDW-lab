#!/usr/bin/env python
# coding: utf-8

# In[1]:


#ASSIGNMENT 2
#10 programs using numpy library

import numpy  as np

#1D array
a=np.array([1,2,3])
print(a)

#2D array
a=np.array([(1,2,3),(4,5,6)])
print(a)

#finding the dimension of array
a = np.array([(1,2,3),(4,5,6)])
print(a.ndim)

#finding the itemsize
a = np.array([(1,2,3)])
print(a.itemsize)

#finding the particular datatype
a = np.array([(1,2,3)])
print(a.dtype)

#finding the size and dimension of array
a = np.array([(1,2,3,4,5,6)])
print(a.size)
print(a.shape)

#reshaping the dimensions
a = np.array([(8,9,10),(11,12,13)])
a=a.reshape(3,2)                   #2,3 dimensional matrix is converted to 3,2
print(a)

#FINDING THE MAX,MIN AND  sum
a= np.array([1,2,3])
print(a.min())
print(a.max())
print(a.sum())

#multiplications subtraction and division of two matrices
x= np.array([(1,2,3),(3,4,5)])
y= np.array([(1,2,3),(3,4,5)])
print(x-y)
print(x*y)
print(x/y)


# In[14]:


import pandas as pd


# In[11]:


pwd


# In[18]:


var = pd.read_csv(r"C:\Users\ASUS\Downloads\Bank_churn_modelling.csv")
var.head()


# In[20]:


#checking for missing values
var.isnull().sum()


# In[21]:


var.shape


# In[25]:


#columns
var.columns


# In[26]:


var.info()


# In[28]:


var.describe()


# In[29]:


var.columns


# In[30]:


var.Geography.unique()


# In[31]:


var.duplicated().sum()


# In[ ]:




