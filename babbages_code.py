
# coding: utf-8

# In[1]:

import numpy as np
def statistics(grades):
    standard = np.std(grades)
    average = np.mean(grades)
    high = max(grades)
    low = min(grades)
    return average,standard,high,low

