# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 15:11:31 2022

@author: kimyh
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("data/Traffic.csv")
df.info
df = df.dropna()

df["교통유입량"] = df["교통유입량"].str.replace(",","").astype(int)
df["교통유입량"]

plt.rc('font',family='Malgun Gothic')
sns.regplot(df.index , df['교통유입량'])
plt.xlabel("날짜")
plt.ylabel("교통유입량")
plt.text(0, 600,
         df["날짜"][0], fontsize=10, color='red')
plt.text(355, 1630,
         df["날짜"][364], fontsize=10, color='red')
plt.show()




