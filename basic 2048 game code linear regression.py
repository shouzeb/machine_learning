# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 22:53:16 2020

@author: Shouzeb
"""

import copy
def not_zero(row_number):
    return row_number != 0
# function to slide the row 
def slide(row):
    filtered_numbers =[]
    for i in range(len(row)):
      if row[i] != 0:   
          filtered_numbers.append(row[i])
          while len(filtered_numbers) < len(row): 
            filtered_numbers.insert(0,0)
            #filtered_numbers.reverse() 
            return filtered_numbers
def combine(row):
    for i in reversed(range(len(row))): 
        a=row[i]
        b=row[i-1] 
        if a == b:
            row[i]=a+b 
            row[i-1] = 0
        return row
def addNumber(arr,pickindex):
    opt =[]
    cur=2 
    if pickindex > len(pickvalue):
        cur =2
    else:
        cur=pickvalue[pickindex]
    if arr[0][0]==0: 
        arr[0][0] =cur 
    elif arr[0][width-1]==0: 
        arr[0][width-1]=cur 
    elif arr[height-1][width-1]==0: 
        arr[height-1][width-1]=cur 
    elif arr[height-1][0] ==0: 
        arr[height-1][0]=cur
    return arr
def operate(row):
    j = slide(row) 
    k = combine(j) 
    l = slide(k) 
    #print l 
    return l
def rev(row):
    row.reverse() 
    return row
def flipGrid(grid):
    grid2=copy.deepcopy(grid) 
    newGrid=[] 
    for i in grid2:
        j = rev(i)
        newGrid.append(j)
    return newGrid
def rotated(array_2d):
    list_of_tuples = zip(*array_2d[::-1])
    return [list(elem) for elem in list_of_tuples]

def rotatedGrid(grid): 
    gg= list(rotated(grid))
    return gg
def loop_over(arr,pickindex): 
    y=[] 
    for i in arr: 
        l=operate(i) 
        #print j 
        y.append(l) 
        #print y 
        s = y
    return s
def right(k,pickindex): 
    #print "R" 
    k=loop_over(k,pickindex) 
    s = addNumber(k,pickindex) 
    return s
def left(k,pickindex): 
    #print "L" 
    k = flipGrid(k) 
    k=loop_over(k,pickindex) 
    k = flipGrid(k) 
    s = addNumber(k,pickindex) 
    return s
def up(k,pickindex): 
    #print "U" 
    k =rotatedGrid(k) 
    k=loop_over(k,pickindex) 
    k =rotatedGrid(k) 
    k =rotatedGrid(k) 
    k =rotatedGrid(k) 
    s = addNumber(k,pickindex) 
    return s 
def down(k,pickindex): 
    #print "D" 
    k =rotatedGrid(k) 
    k =rotatedGrid(k) 
    k =rotatedGrid(k) 
    k=loop_over(k,pickindex) 
    k =rotatedGrid(k) 
    s = addNumber(k,pickindex) 
    return s
def gameover(grid,o): 
    vv=0
    for i in range(height):
        for j in range(width): 
           if grid[i][j] ==o: 
               print ("Game Over") 
               vv= 1
    return vv
def eva(grid): 
    #print grid 
    score=0 
    for i in range(height): 
        for j in range(width): 
            #print grid[i][j],i,j 
            if grid[i][j]!=0: 
                score=score + grid[i][j]*grid[i][j] 
    return score
def display1(grid): 
    for i in range(height): 
        print (grid[i])
pickvalue=[2,4]
width=4 
height=4 
x = [[0 for i in range(width)] for j in range(height)] 
x[3][1]=2 
x[3][3]=4 
#x[0][0]=2 
print (x) 
display1(up(x,0))




 
 
                      
    
            