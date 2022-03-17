#!/usr/bin/env python
# coding: utf-8

# In[11]:


import pandas as pd

Chips =['Cheetos','Fritos','Lays', 'Doritos', 'Pringles', 'Willards']
Cooldrinks = ['Stoney','Sprite', 'Coke', 'Fanta', 'Jive', 'Creme soda']
Chocolates = [' Sneakers', 'Kit-Kat', 'Lunchbar', 'PS', 'Lindt','Twix']
Pies =['Chicken Curry', 'Steak & Kidney', 'Burger pie', 'Pepper Steak', 'Cheese Burger Pie', 'Apple Pie']
Fruit =['Peach', 'Banana', 'Pineapple', 'Mango','Strawberry', 'Pear']
Cupcakes =['Choc chip', 'Blueberry', 'Red velvet', 'Sponge Cake', 'Biscuit Cake', 'Pound Cake']
Veggies =['Brocolli', 'Onion', 'Spinach', 'Potato', 'Carrot', 'Cabbage']

df = pd.DataFrame(list(zip(Chips,Cooldrinks,Chocolates,Pies,Fruit,Cupcakes,Veggies)),
                  columns=['Chips','Cooldrink,s','Chocolates','Pies', 'Fruit', 'Cupcakes', 'Veggies'])
df

# In[ ]:




