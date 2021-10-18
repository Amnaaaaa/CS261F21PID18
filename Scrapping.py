#!/usr/bin/env python
# coding: utf-8

# In[9]:


import requests
from bs4 import BeautifulSoup

url = "https://www.1mg.com/"
data = requests.get(url)
dataContent = data.content

print(dataContent)


# In[ ]:





# In[ ]:




