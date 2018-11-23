# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 21:41:20 2018

@author: Chris
"""
import random
import string

def matrix(rows=5, cols=7, filler = 1):
    '''matrix(rows, cols) generates a matrix of values that default to zero, of size rows(m)x cols(n)'''
    rows = round(rows,0)
    cols = round(cols,0)
    mat = [[filler]*cols for i in range(rows)] # Create the matrix
    return mat
#-----------------------------------------------------------------------------
def randMat(m,n,a,b):
    '''randMat(m, n) generates a matrix of values that default to zero, of size rows(m) x cols(n)'''
    mat = [[0]*n for i in range(m)] # Create the matrix
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            mat[i][j] = random.randint(a,b)
    return mat
#-----------------------------------------------------------------------------
def displayMatrix(m):
    for i in range(len(m)):             #iterate through the rows of matrix m
        for j in range(len(m[0])):      # iterate through each element of each row
            print(m[i][j], end = " ")   # Print the given element and a space
        print()                         # go to a new line after each row
    print()                             # add an extra new line after completing the matrix
#-----------------------------------------------------------------------------
def makeDiagN(mat,n):
    '''Make all elements on the primary diagonal the given value n'''
    for i in range(len(mat)):           #Iterate through the rows
        for j in range(len(mat[0])):    # iterate through each row
            if i==j:                    # if the element is on the main diagonal
                mat[i][j] = n           # Assign the diagonal elements to be the given value n
#-----------------------------------------------------------------------------               
def makeBestFitDiagN(mat,n):
    '''Set all values to the given n along the line from top left to bottom right element'''
    m = len(mat)                #Get the number of rows
    n = len(mat[0])             # get the number of columns
    it = (n-1)/(m-1)            # get the offset for each row (may be non-integer)
    for i in range(len(mat)):   # iterate through the rows
        mat[i][round(it*i)] = 9 # for each row, find the right column and assign it the given value n
#-----------------------------------------------------------------------------        
def canAdd(A,B):
    '''Return True if the dimensions match, otherwise return False'''
    canmult = False                                     #Default to False
    if (len(A) == len(B)) and (len(A[0]) == len(B[0])): # if the dimensions match,
        canmult = True                                  # change to True
    return canmult                                      # return the boolean value
#-----------------------------------------------------------------------------
def matAdd(A,B):
    '''If the matrices have matching dimensions, add them.'''
    C = [[0] * len(A[0]) for i in range(len(A))]    #Create the base new matrix
    for i in range(len(A)):                         # iterate through the rows
        for j in range(len(A[0])):                  # iterate through each row
            C[i][j] = A[i][j] + B[i][j]             # Assign the sum to the corresponding element of C
    return C
#-----------------------------------------------------------------------------
def writeMat(g,q):
    '''Takes a filestream g, a matrix q, and a matrix name, writes to the filestream'''
    for i in range(len(q)):                 # iterate through the rows
        for j in range(len(q[0])):          # iterate through each row
            g.write(str(q[i][j]) + " ")    # write each element and a tab
        g.write('\n')                       # Write a newline after each row
#-----------------------------------------------------------------------------
def readMat(f):
    p = []
    for l in f:
        p.append(l)
    for i in range(len(p)):
        p[i] = p[i].split(' ')
        p[i].pop()
    return p
##############################################################################
##############################################################################
##############################################################################
#DRIVER
A = randMat(7,10, 1, 9)
displayMatrix(A)
f = open('testTextFile.txt', "w+")
writeMat(f,A)
f.close()
