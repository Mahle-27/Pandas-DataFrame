#!/usr/bin/env python
# coding: utf-8

# In[4]:


#!/usr/bin/env python
# coding: utf-8

# In[11]:


import pandas as pd

Chips =['Cheetos','Fritos','Lays', 'Doritos']
Cooldrinks = ['Stoney','Sprite', 'Coke', 'Fanta']
Chocolates = [' Sneakers', 'Kit-Kat', 'Lunchbar', 'PS']
Pies =['Chicken Curry', 'Steak & Kidney', 'Burger pie', 'Pepper steak']
Fruit =['Peach', 'Banana', 'Pineapple', 'Strawberry']
Cupcakes =['Choc chip', 'Blueberry', 'Red velvet', 'Sponge cake']
Veggies =['Brocolli', 'Onion', 'Spinach', 'Potato']

df = pd.DataFrame(list(zip(Chips,Cooldrinks,Chocolates,Pies,Fruit,Cupcakes,Veggies)),
                  columns=['Chips','Cooldrinks','Chocolates','Pies', 'Fruit', 'Cupcakes', 'Veggies'])
df


# In[ ]:




