#!/usr/bin/env python
# coding: utf-8

# In[12]:


import numpy as np


# In[13]:


print(np.__version__)


# # Constant time (O(1)) complexity

# In[14]:


def getFirst(myList):
    return myList[0]


# In[15]:


getFirst([1,2,3])


# # Linear time (O(n)) complexity

# In[16]:


def getSum(myList):
    sum = 0
    for item in myList:
        sum = sum+item
    return sum
#perhatikan posisi spasi pada return


# In[17]:


getSum([1,2,3,4])


# #  Quadratic time (O(n^2)) complexity

# In[18]:


def getSum(myList):
    sum = 0
    for row in myList:
        for item in row:
            sum += item
    return sum


# In[19]:


getSum([[1,2,5],[3,4,7]])


# # Logaritmic time (O(log(n))) complexity

# In[24]:


def searchBinary(myList,item):
    first = 0
    last = len(myList)-1
    foundFlag = False
    while( first<=last and not foundFlag):
        mid = (first + last)//2
        if myList[mid] == item :
            foundFlag = True
        else:
            if item < myList[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return foundFlag


# In[25]:


searchBinary([8,9,10,100,1000,2000,3000], 10)


# In[26]:


searchBinary([8,9,10,100,1000,2000,3000], 5)

