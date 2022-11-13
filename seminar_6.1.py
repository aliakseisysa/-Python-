#!/usr/bin/env python
# coding: utf-8

# # 1. Напишите программу вычисления арифметического выражения заданного строкой. Используйте операции +,-,/,*. приоритет операций стандартный.

# In[1]:


#     Пример:
#     2+2 => 4;
#     1+2*3 => 7;
#     1-2*3 => -5;
#     - Добавьте возможность использования скобок, меняющих приоритет операций.
#         Пример:
#         1+2*3 => 7;
#         (1+2)*3 => 9;


# In[346]:


# a = str(input('Enter expression: '))
# print(a)
expr = str('1+2*3-20/5+3*5-100/20')


# In[347]:


print(expr)


# In[348]:


import re


# In[349]:


nums = re.split('[-+]', expr)


# In[350]:


adj_nums = []
nums_ = []
for i in nums:
    try:
        float(i)
        adj_nums.append(float(i))
    except:
        try:
            nums_ = re.split('[*]', i)
            i_ = float(nums_[0])*float(nums_[1])
            adj_nums.append(i_)
        except:
            nums_ = re.split('[/]', i)
            i_ = float(nums_[0])/float(nums_[1])
            adj_nums.append(i_) 


# In[351]:


oprs = re.split('[1234567890]', expr)


# In[352]:


oprs = [i for i in oprs if i == '+' or i == '-']


# In[353]:


if len(adj_nums)%2 != 0:
    adj_nums.append(0)


# In[354]:


if oprs[0] == '+':
    res = adj_nums[0]+adj_nums[1]
else:
    res = adj_nums[0]-adj_nums[1]


# In[356]:


count_o = 1
count_n = 2


# In[357]:


for el in oprs[count_o:len(oprs)]:
    if oprs[count_o] == '+':
        res = res+adj_nums[count_n]
    else:
        res = res-adj_nums[count_n]
    count_o = count_o + 1
    count_n = count_n + 1


# In[358]:


print(res)

