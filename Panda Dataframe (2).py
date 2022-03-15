#!/usr/bin/env python
# coding: utf-8

# In[4]:


#!/usr/bin/env python
# coding: utf-8

# In[11]:


import pandas as pd

Chips =['Cheetos','Fritos','Lays']
Cooldrinks = ['Stoney','Sprite', 'Coke']
Chocolates = [' Sneakers', 'Kit-Kat', 'Lunchbar']
Pies =['Chicken Curry', 'Steak & Kidney', 'Burger pie']
Fruit =['Peach', 'Banana', 'Pineapple']
Cupcakes =['Choc chip', 'Blueberry', 'Red velvet']
Veggies =['Brocolli', 'Onion', 'Spinach']

df = pd.DataFrame(list(zip(Chips,Cooldrinks,Chocolates,Pies,Fruit,Cupcakes,Veggies)),
                  columns=['Chips','Cooldrinks','Chocolates','Pies', 'Fruit', 'Cupcakes', 'Veggies'])
df


# In[ ]:




