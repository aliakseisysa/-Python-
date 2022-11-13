#!/usr/bin/env python
# coding: utf-8

# # 43. Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
# # Пример:
# # [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]

# In[1]:


import random


# In[2]:


array = [1, 2, 3, 5, 1, 5, 3, 10]
#array = [random.randint(1,10) for i in range(50)]
print(array)


# In[3]:


my_dict = {}


# In[4]:


for el in array:
    if el in my_dict:
        my_dict[el] = my_dict[el] + 1
    else:
        my_dict[el] = 1


# In[5]:


print(my_dict)


# In[6]:


uniq = []


# In[7]:


for item in my_dict:
    if my_dict[item] ==1:
        uniq.append(item)


# In[8]:


print(uniq)

