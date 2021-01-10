import time 
# Time module provides many ways of representing time
import pandas as pd 
# Used for Data Structure 
import numpy as np 
# For multi dimensional array

def uForLoop(lst1, lst2):
    '''uForLoop

    Parameters:
    lst1 (list): List of elements to be checked with list 2
    lst2 (list): List of all elements

    Prints:
    len(verified_elements) : Number of elements which are there in list 2
    time.time() - start: Total time to execute the loop 
    '''

    start = time.time() 
    verified_elements = [] # Empty list

    for element in lst1:
        if element in lst2:
            verified_elements.append(element) # Adding element to the list
    
    print(len(verified_elements))
    print('Duration: {} seconds, is used by for loop'.format(time.time() - start))


def uNumpy(lst1, lst2):
    '''uForLoop

    Parameters:
    lst1 (list): List of elements to be checked with list 2
    lst2 (list): List of all elements

    Prints:
    len(verified_elements) : Number of elements which are there in list 2
    time.time() - start: Total time to execute the loop 
    '''
    start = time.time()

    # Creating a 1D array for lst1 and lst2
    a = np.array(lst1) 
    b = np.array(lst2)
    
    verified_elements = a[np.in1d(a, b)] # Finds all elements in b that has elements in a

    print(len(verified_elements))
    print('Duration: {} seconds, is used by numpy'.format(time.time() - start))


def uSet(lst1, lst2):
    '''uForLoop

    Parameters:
    lst1 (list): List of elements to be checked with list 2
    lst2 (list): List of all elements

    Prints:
    len(verified_elements) : Number of elements which are there in list 2
    time.time() - start: Total time to execute the loop 
    '''

    start = time.time()
    a = set(lst1)
    b = set(lst2)
    verified_elements = a.intersection(b) # Finding Elements in b that has a

    print(len(verified_elements))
    print('Duration: {} seconds, is used by set'.format(time.time() - start))

def main():
    with open('subset_elemets.txt') as f:
        subset_elements = f.read().split('\n')
    
    with open('all_elements.txt') as f:
        all_elements = f.read().split('\n')
    
    # Calling uForLoop function
    uForLoop(subset_elements, all_elements) 

    # Calling uNumpy function
    uNumpy(subset_elements, all_elements)

    # Calling uSet function
    uSet(subset_elements, all_elements)

# Calls main function
if __name__=="__main__":    
    main()