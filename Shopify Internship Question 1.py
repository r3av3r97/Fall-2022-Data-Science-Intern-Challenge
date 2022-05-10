#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


df = pd.read_csv("2019 Winter Data Science Intern Challenge Data Set - Sheet1.csv")


# In[3]:


print(df)


# In[4]:


print(df["order_amount"].mean())


# In[5]:


print(df['total_items'].skew())


# In[6]:


print(df['order_amount'].skew())


# In[7]:


print(df.describe()[["order_amount", "total_items"]])

# In[8]:


print(df.plot(x="order_id", y="order_amount", kind="line", figsize=(9, 8)))

# In[9]:


print(df.plot.scatter(x='order_id', y='order_amount', c='DarkBlue'))


# In[10]:


print(df.plot.scatter(x='order_id', y='total_items', c='DarkBlue'))


# In[11]:


print(df.order_amount.unique())


# In[12]:


print(df.plot.scatter(x='total_items', y='order_amount', c='DarkBlue'))


# In[13]:


print(df.total_items.unique())


# In[14]:


avg_amount_per_item = df.order_amount/df.total_items


# In[15]:


df = df.assign(aapi = avg_amount_per_item)
print(df)


# In[22]:


print(df.describe()[["order_amount", "aapi"]])

# In[17]:


df_filtered = df[df['order_amount'] < 1500]
print(df_filtered)


# In[18]:


print(df_filtered.total_items.unique())


# In[19]:


print(df_filtered['total_items'].skew())


# In[20]:


print(df_filtered.describe()[["order_amount", "total_items"]])


# In[21]:


print(df_filtered.plot.scatter(x='total_items', y='order_amount', c='DarkBlue'))


# In[ ]:





# In[ ]:




