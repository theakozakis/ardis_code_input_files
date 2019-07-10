#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Code to extract effective altitudes and the lowest altitude temperature from a LAYERS file:
    read_LAYERS(filename)
    
Input:  LAYERS file
    filename:  path to LAYERS file as a string
    
Outputs:
    Element 0:  list of effective altitudes
    Element 1:  list of temperatures for all layers
"""

def read_LAYERS(filename):
    
    import numpy as np
    
    # File structure:
    # Very lowest layer    #
    # \n
    # Altitudes   #1   #2  #3   #4 ^
    # (data, 4 elements per line) ^
    # (last line of data, no ^)
    # \n
    # Effective altitudes   #1   #2  #3   #4 ^
    # (data, 4 elements per line) ^
    # (last line of data, no ^)
    
    
    # Open file
    f = open(filename)
    
    rows = f.readlines()
    
    # Find the number of layers and where the effective altitudes start
    for i in range(len(rows)):
        
        m1 = rows[i].find('Very lowest layer')
        m2 = rows[i].find('Effective altitudes')
        m3 = rows[i].find('Temperatures (K)')
        
        # The 3rd element in the matching line for layers is the number of layers
        if m1 != -1:
            
            row = rows[i].split()
            n = int(row[3])

        # Starting point of effective altitudes
        if m2 != -1:
            ind1 = i
            
        # Starting point of temperatures
        if m3 != -1:
            indT = i
            
            
    # Calculate number of lines of altitude data
    # There will be n elements of data with 4 elements per line
    nrow = int(np.ceil(n/4))
    
    # Read effective altitude data
    ealt = []
    # For the first row don't read in the first two and last elements
    # The first row will be the second list of altitudes
    row = rows[ind1].split()
    for i in range(2,len(row)-1):
        ealt.append(float(row[i]))
    
    ind2 = ind1+nrow-1
    # For the 'middle rows' use every element except the last (^)
    for i in range(ind1+1,ind2):
        row = rows[i].split()
        for k in range(len(row)-1):
            ealt.append(float(row[k]))
            
    # For the last row read in all elements
    row = rows[ind2].split()
    for i in range(len(row)):
        ealt.append(float(row[i]))
        
        
    # Read temperature data
    t = []
    # For the first row don't read in the first two and last elements
    # The first row will be the second list of altitudes
    row = rows[indT].split()
    for i in range(2,len(row)-1):
        t.append(float(row[i]))
    
    ind2 = indT+nrow-1
    # For the 'middle rows' use every element except the last (^)
    for i in range(indT+1,ind2):
        row = rows[i].split()
        for k in range(len(row)-1):
            t.append(float(row[k]))
            
    # For the last row read in all elements
    row = rows[ind2].split()
    for i in range(len(row)):
        t.append(float(row[i]))
        

    

    return ealt,t


    
    

