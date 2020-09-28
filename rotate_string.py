#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'getShiftedString' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER leftShifts
#  3. INTEGER rightShifts
#

def validate_args(s, leftShifts, rightShifts):
    proceed_flag = True
    if s.islower() == False:
        print ("String isnt in Lowercase. Exiting...")
        proceed_flag = False
        exit(1)
    if s.isalpha() == False:
        print ("String contains characters apart from a..z. Exiting...")
        proceed_flag = False
        exit(1)
    if len(s)<1 or len(s) >= pow(10,5):
        print ("String length out of permissible limit. Exiting...")
        proceed_flag = False
        exit(1)
    if leftShifts < 0:
        print ("Left Shifts cannot be negative. Exiting...")
        proceed_flag = False
        exit(1)
    if rightShifts > pow(10,9):
        print ("Right Shifts out of permissible limit. Exiting...")
        proceed_flag = False
        exit(1)
    return proceed_flag

def getShiftedString(s, leftShifts, rightShifts):
    # Write your code here

    if leftShifts > rightShifts:
        rotate = leftShifts-rightShifts
        output = rotate_left(s,rotate)
    elif leftShifts < rightShifts:
        rotate = rightShifts-leftShifts
        output = rotate_right(s,rotate)
    elif leftShifts == rightShifts:
        rotate = 0
        output = s
    return output

def rotate_left(s,rotate):
    i=0
    while i <= leftShifts:
        left_shifting = s[i:] + s[:i]

def rotate_right(s,rotate):
    j=0
    while j <= rightShifts:
        right_shifting = s[-j:] + s[:-j]

    return right_shifting

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    leftShifts = int(input().strip())

    rightShifts = int(input().strip())
    proceed_flag = validate_args(s, leftShifts, rightShifts)
    
    if proceed_flag == True:
        result = getShiftedString(s, leftShifts, rightShifts)
    else:
        print ("Pre-requisites failed in validation...")
    fptr.write(result + '\n')

    fptr.close()
