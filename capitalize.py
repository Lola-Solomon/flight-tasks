#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    #name is every word in the sentence
    for name in s[:].split(): 
        #replace every word in the sentence with a capital letter
        s=s.replace(name,name.capitalize())
    return s    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
