# -*- coding: utf-8 -*-
"""Gorcnakan 1 2025.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1_Z6okXf5_SdCURUUdn9vKT2-8fO2BJsK
"""

def find_sum_index(l,target):
  indexner=[]
  for i in range(n-1):
    k=target-l[i]
    for j in range(i+1,n):
      if l[j]==k:
        indexner.append((i,j))
  if not indexner:
    print("not found")
  return indexner

l=[2,3,6,10,7,8,5,4,6]
target=6
n=len(l)
result=find_sum_index(l,target)
if result:
  for pair in result:
    print(pair)