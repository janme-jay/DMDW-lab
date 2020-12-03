#!/usr/bin/env python
# coding: utf-8

# In[6]:


#Assignment 1
#program to find mean, median & mode without using library
a=list(map(int,input().split(",")))
n=len(a)
a.sort()

#finding mean
mean=sum(a)//len(a)

#finding median
if len(a)%2==1:
    median = a[(n+1)//2]
else:
    median = [a[(n-1)//2]+a[(n+1)//2]/2]
    
print(mean)
print(median)


# In[4]:


#Finding Mode
from collections import Counter
a = list(map(int,input().split(",")))
n = len(a)
data = Counter(a)
get_mode = dict(data)
mode = [k for k, v in get_mode.items() if v==max(list(data.values()))]
if len(mode) == n:
    get_mode = "No mode found"
else:
    get_mode = "Mode is / are: " + ', '.join(map(str,mode))
print(get_mode)


# In[19]:


#STANDARD DEVIATION
import math
a=list(map(int,input().split(",")))
mean = sum(a) / len(a) 
variance = sum([((x - mean) ** 2) for x in a]) / len(a) 
res = variance ** 0.5
print("standard deviation "+str(res))
#VARIANCE
var=math.sqrt(res)
print("variance "+str(var))


# In[20]:


#MEAN MEDIAN standard deviation and variance using library functions
import numpy as np
a=list(map(int,input().split(",")))
avg=np.mean(a)
med=np.median(a)
sd=np.std(a)
V=np.var(a)
print("mean is "+str(avg))
print("median is "+str(med))
print("standard deviation is "+str(sd))
print("variance is "+str(V))


# In[21]:


import statistics  as s
a=list(map(int,input().split(",")))
m=s.mode(a)
print("mode is "+str(m))


# In[ ]:




