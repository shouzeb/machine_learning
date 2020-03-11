# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 21:22:58 2020

@author: Shouzeb
"""
import copy
length=0

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

#function to combine values in the row
def combine(row):
    for i in reversed(range(len(row))):
        a=0
        b=0
        if i !=0:
            a=row[i]
            b=row[i-1]
            if a == b:
                row[i]=a+b
                row[i-1] = 0
    return row

#function to add the spawn value on the empty corners of the grid with sequence top left, top right, bottom right, bottom left. 
def addNumber(arr,pickindex):
    #print pickindex
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

# main operation to slide, combine and then slide
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


   
# function to evaluate the score of the current state of the grid. weigth * value  
def eva(grid):
    #print grid
    score=0
    for i in range(height):
        for j in range(width):
            #print grid[i][j],i,j
            if grid[i][j]!=0:
                score=score + score[i][j]*grid[i][j]
    return score

# function to display the grid 
def display1(grid):
    for i in range(height):
        print (grid[i])

pickvalue=[2]

def bfs(grid,o,pickindex):
    frontier =[]
    g_v =[grid,[]]
    frontier.append(g_v)
    #old1=4
    #old2=2
    while frontier !=[]:
        #print (frontier)
        length=len(frontier)
        if pickindex >= len(pickvalue):
            pickindex=0
        g=copy.deepcopy(frontier[length-1])
        #print (g) # you can see this value to make sure what is currently being executed
        frontier.pop(0)
        #print g
        if g[0] == None:
            break
        if gameover(g[0],o)==1:
            print ("Game end")
            frontier=[]
            return g
        else:
            grid1=copy.deepcopy(g)
            grid2=copy.deepcopy(g)
            grid3=copy.deepcopy(g)
            grid4 =copy.deepcopy(g)
    
            grid11 = left(grid1[0],pickindex)
            grid22 = right(grid2[0],pickindex)
            grid33 = up(grid3[0],pickindex)
            grid44 = down(grid4[0],pickindex)
            
            path1 = copy.deepcopy(grid1[1])
            path1.append("L")
            
            path2 = copy.deepcopy(grid2[1])
            path2.append("R")
            
            path3 = copy.deepcopy(grid3[1])
            path3.append("U")
            
            path4 = copy.deepcopy(grid4[1])
            path4.append("D")
            
            frontier.append([grid11,path1])
            frontier.append([grid22,path2])
            frontier.append([grid33,path3])
            frontier.append([grid44,path4])
            
        pickindex=pickindex+1

#---------------------------- testing
width=4
height=4

x = [[0 for i in range(width)] for j in range(height)]
x[3][0]=2
x[3][3]=4
print (x)
g=bfs(x,16,0)
display1(g[0])
print (g[1])