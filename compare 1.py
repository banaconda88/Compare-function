#!/usr/bin/env python
# coding: utf-8

# In[4]:


def compare():
    x = input("What is the number you would like to be compared?")
    y = input("What is the number you want to the previous number?")
    if x > y:
        print("1")
    elif x == y:
        print("0")
    else:
        print("-1")
compare()

