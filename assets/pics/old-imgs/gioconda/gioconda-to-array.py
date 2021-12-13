#!/usr/bin/env python3

import pandas as pd

import numpy as np
from PIL import Image

import sys

def print_uint8_arr(a):
    for row in a:
        print(f"\t\t", end=" ")
        for col in row:
            print(f"{col:03}", end=" ")
        print("")

np.set_printoptions(threshold=32768)
img = Image.open('gioconda-32x32-grayscale.bmp')
arr = np.array(img)

# record the original shape
shape = arr.shape

#arr_str = np.array_repr(arr).replace('\n', '')

print('')
print('')
print('')
print('')
print('')
print('')

#print(arr)
print_uint8_arr(arr)

print('')
print('')
print('')
print('')
print('')
print('')

print(shape)



img = Image.open('gioconda-16x16.bmp')
def printA(a):
    for row in a:
        for col in row:
            for ch in col:
                print(f"{ch:03}", end=" ")
        print("")

arr = np.array(img)
#print(arr)
print(arr.shape)

printA(arr)
sys.exit(0)



# make a 1-dimensional view of arr
flat_arr = arr.ravel()

df = pd.DataFrame(data=flat_arr)
print(df)

# convert it to a matrix
vector = np.matrix(flat_arr)

# do something to the vector
vector[:,::10] = 128

# reform a numpy array of the original shape
arr2 = np.asarray(vector).reshape(shape)

# make a PIL image
img2 = Image.fromarray(arr2, 'RGBA')
img2.show()


