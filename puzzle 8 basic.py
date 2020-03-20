
__Project_Description__ = '''
This is a python based 3x3 puzzle solver which solves the problem by using list
which represented as 1 dimensionally. (Using 1D list is the greatest challenge for me.)
Project has several methods to solve subproblems. The subproblems are:
    * Calculating inversion,
    * Checking solubility of the board,
    * Calculating Hamming Distance,
    * Calculating Manhattan Distance (BONUS),
    * If board arrangement has solution than find the 'Legal Board Arrangements' -> (changing blank tile's position)
    * Generate a heuristic function to get closest path to go to goal state.
    * Breadth First Search and Generating the Result.'''

import math, sys

#********************************#
#                +---+---+---+   #
#                | 1 | 2 | 3 |   #
#                +---+---+---+   #
#   GOAL STATE:  | 4 | 5 | 6 |   #
#                +---+---+---+   #
#                | 7 | 8 |   |   #
#                +---+---+---+   #
#********************************#

goal_state = [1, 2, 3,
              4, 5, 6,
              7, 8, 0]

worst_case = [8, 7, 6,
              5, 4, 3,
              2, 1, 0]

initial_state = [1, 2, 5,
                 6, 8, 0,
                 7, 4, 3]

example_state = [0, 1, 2,
                 3, 4, 5,
                 6, 7, 8]

example_state1 = [1, 2, 7,
                  4, 5, 6,
                  3, 8, 0]

example_state2 = [1, 2, 4,
                  3, 5, 6,
                  7, 8, 0]

example_state3 = [8, 2, 3,
                  4, 5, 6,
                  7, 0, 1]

example_state4 = [1, 2, 3,
                  4, 0, 5,
                  7, 8, 6]

example_state5 = [1, 2, 3,
                  8, 0, 4,
                  7, 5, 6]

example_state6 = [1, 2, 3,
                  6, 4, 0,
                  7, 8, 5]

example_state7 = [8, 7, 6,
                  5, 4, 3,
                  2, 1, 0]

example_state8 = [1, 2, 3,
                  0, 5, 6,
                  4, 7, 8]

example_state9 = [2, 6, 0,
                  8, 1, 5,
                  4, 7, 3]

example_state10 = [0, 1, 3,
                   4, 2, 5,
                   7, 8, 6]


def matrix_display(list):
    return '\n' \
           '+---+---+---+\n' \
           '| %s | %s | %s |\n' \
           '+---+---+---+\n' \
           '| %s | %s | %s |\n' \
           '+---+---+---+\n' \
           '| %s | %s | %s |\n' \
           '+---+---+---+\n' \
           % (list[0], list[1], list[2], list[3], list[4], list[5], list[6], list[7], list[8])


# TESTS FOR MATRIX DISPLAY
# print matrix_display([1,2,3,4,5,6,7,8,0])
# print matrix_display(example_state)
# print matrix_display(example_state1)
# print matrix_display(example_state2)


def inversions(current_state):
    total_inversion = 0
    for i in range(len(current_state)):
        for j in range(i, len(current_state)):
            if current_state[i] > current_state[j] and current_state[i] != 0 and current_state[j] != 0:
                total_inversion += 1
    return total_inversion

# TESTs for CALCULATING INVERSIONS
#print "Total inversion is: " + str(inversions(e5))
#print "Total inversion is: " + str(inversions(example_state))
#print "Total inversion is: " + str(inversions(example_state4))
#print "Total inversion is: " + str(inversions(example_state2))


def check_solubility(current_state):
    # Finds whether puzzle is available or not.
    print("current state",current_state)
    if (inversions(current_state)) % 2 == 0: #this part is probably wrong. //+ int(current_state.index(0) / 3) + 1)
        best_first_search(current_state)
        # "Total inversion is: "
        # + str(inversions(current_state))
        # + " + Blank tile is in index: "
        # + str(int(current_state.index(0) / 3)) + " ==> " + "Solvable."
    else:
        return "No Solution for this board."


#------------------------------------- HAMMING DISTANCE CALCULATING IN THIS PART -
def hamming_distance(state_i):
    distance = 0
    for i in goal_state:
        if goal_state.index(i) - state_i.index(i) != 0 and i != 0:
            distance += 1
    return distance

#  TESTs for HAMMING DISTANCE
# print "Hamming Distance: " + str(hamming_distance(example_state5))


#------------------------------------- MANHATTAN DISTANCE CALCULATING IN THIS PART -
def manhattan_distance(current_state):
    distance = 0
    kalan = 0
    bolum = 0

    for i in current_state:
        position_difference = abs(goal_state.index(i) - current_state.index(i))
        if i is not 0:
            kalan = position_difference % 3
            bolum = position_difference / 3
            distance += kalan + int(math.floor(bolum))
            if abs(goal_state.index(i) % 3 - current_state.index(i) % 3) == 2 and position_difference % 3 == 1:
                distance += 2
            print ("i: " + str(i) + " goal-index: " + str(goal_state.index(i)) + " current-index: " + str(current_state.index(i)) + " bolum: " + str(bolum) + ": kalan: " + str(kalan) + ": distance: " + str(distance))
    return distance

# TESTs for CALCULATING MANHATTAN DISTANCE
# print "Manhattan distance is: " + str(manhattan_distance(goal_state))       # Result = 0
# print "Manhattan distance is: " + str(manhattan_distance(initial_state))    # Result = 9
# print "Manhattan distance is: " + str(manhattan_distance(example_state))    # Result = 12
# print "Manhattan distance is: " + str(manhattan_distance(example_state1))   # Result = 8
# print "Manhattan distance is: " + str(manhattan_distance(example_state2))   # Result = 6
# print "Manhattan distance is: " + str(manhattan_distance(example_state3))   # Result = 4
# print "Manhattan distance is: " + str(manhattan_distance(example_state4))   # Result = 14


#------------------------------------- NEW POSSIBLE STATES ARE CREATED IN THIS PART -
def find_switch_tiles(current_state):
    blank_tile = current_state.index(0)
    switch_positions = []
    for i in current_state:
        if current_state.index(i) not in switch_positions and current_state.index(i) % 3 == blank_tile % 3 and \
                        i != 0 and abs(current_state.index(i) / 3 - blank_tile / 3) == 1 or \
                                        current_state.index(i) / 3 == blank_tile / 3 and abs(current_state.index(i) - blank_tile) == 1:
            switch_positions.append(current_state.index(i))
    return switch_positions

# TESTs for FINDING SWITCH TILES
# print find_switch_tiles(initial_state)
# print find_switch_tiles(example_state)
# print find_switch_tiles(example_state1)
# print find_switch_tiles(example_state2)
# print find_switch_tiles(example_state3)
# print find_switch_tiles(example_state4)
# print find_switch_tiles(example_state5)


#------------------------------------ THIS PART FOR SWAPPING TILES WHICH ARE ADJACENT WITH TILE '0' -
def swap(current_state, i, j):
    current_state[i], current_state[j] = current_state[j], current_state[i]
    return current_state


def generate_new_states(current_state):
    x = find_switch_tiles(current_state)
    list_of_states = []
    for i in x:
        new_current = []
        old_value = current_state[i]
        new_current += swap(current_state, current_state.index(0), i)
        list_of_states.append(new_current)
        zero_index = current_state.index(0)
        swap(current_state, current_state.index(old_value), zero_index)
    return list_of_states

# TESTs for GENERATING NEW STATES
# print generate_new_states(initial_state)
# print generate_new_states(example_state)
# print generate_new_states(example_state1)


def hamming_priority_function(legal_states):
    min_hamming = []
    for i in legal_states:
        x = min(hamming_distance(a) for a in legal_states)
        if hamming_distance(i) == x:
                min_hamming += [i]

    return min_hamming
#print hamming_priority_function(generate_new_states(example_state))
#print hamming_priority_function(generate_new_states(example_state2))
#print hamming_priority_function(generate_new_states(example_state3))
#print hamming_priority_function(generate_new_states(example_state4))


#------------------------------------- GO FOR GLORY WITH BFS (Breadth First Search) -
def best_first_search(state):

    print (matrix_display(state))
    temp_solution = [state]
    explored_set = generate_new_states(state)
    step = 0
    while goal_state:
        step += 1
        
        
        
        

        # Comment outs are for checking results to compare them individually.
        # print "TEMP SOLUTION SET: ", temp_solution
        # print "EXPLORED SET: ", explored_set
        # print "Hamming Set: ", hamming_priority_function(explored_set)
        # print "Hamming Set CHOOOSEN: ", hamming_priority_function(explored_set).pop()
        for i in explored_set:
            explored_set += generate_new_states(i)
            x = hamming_priority_function(explored_set).pop()

            if x == goal_state:
                print ("\nSolved in {} step(s)\n".format(step))
                return matrix_display(x)

            elif x not in temp_solution:
                temp_solution += [x]
                explored_set = generate_new_states(x)
            else:
                explored_set.pop(explored_set.index(x))

            print (matrix_display(x))


print ("\n<Usage:> \n<Enter a board: 231456780>\n")
board = input("Enter a board: ")
print (check_solubility(list(map(int, board))))