# Your task is to print an array of size NXM with its main diagonal elements as 0's and 1's everywhere else.

# Input Format

# A single line containing the space separated values of  0 and 1. 
# N denotes the rows. 
# M denotes the columns.

### My code ###
import numpy

# print(numpy.identity(7))
# print(numpy.eye(3,4))
# print(numpy.eye(3,4, k = 1))

N , M = input().split()
numpy.set_printoptions(sign=' ')
print(numpy.eye(int(N),int(M)))

## Problem Setter's code:###

import numpy
N, M = map(int, input().split())

print(numpy.eye(N, M, k = 0))