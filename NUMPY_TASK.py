#!/usr/bin/env python
# coding: utf-8
###TASK1
import numpy as np
data=np.array([1,2,3,4,5,6,7,8,9,10])
x=np.mean(data)
print("Mean:",x)
y=np.std(data)
print("Standard Deviation:",y)

###TASK 2
matrix = np.random.rand(5, 5)
print("Matrix:",matrix)
##MIN AND MAX VALUE ALONG EACH ROW
min_values_row = np.min(matrix, axis=1)
max_values_row = np.max(matrix, axis=1)
##MIN AND MAX VALUE ALONG EACH COLUMN
min_values_col = np.min(matrix, axis=0)
max_values_col = np.max(matrix, axis=0)
print("\nMinimum values along each row:")
print(min_values_row)
print("\nMaximum values along each row:")
print(max_values_row)
print("\nMinimum values along each column:")
print(min_values_col)
print("\nMaximum values along each column:")
print(max_values_col)

###TASK 3
def cosine_similarity(a,b):
    a= np.array(a)
    b= np.array(b)
    dot_product = np.dot(a,b)
    norm_a= np.linalg.norm(a)
    norm_b= np.linalg.norm(b)
    cosine_sim = dot_product / (norm_a * norm_b)
    return cosine_sim
a= np.array([1, 2, 3])
b= np.array([4, 5, 6])
cosine_sim = cosine_similarity(a,b)
print("Cosine Similarity:", cosine_sim)


