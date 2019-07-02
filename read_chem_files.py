#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Code to read in chem files outputted by CHEMCLIM and search for specific molecule:
    read_chem_files(filename,molname)
    
Inputs: chem file name, molecule name
    filename:  path to chem file as a string
    molname:  molecule name as a string
    
Outputs:
    Element 0: list of mixing ratios
    Element 1: list of corresponding altitudes (km)
"""



def read_chem_files(filename,molname):
    
    # File structure:
    # Molecule 'name'
    # \n
    # 'name' _ALT (altitude data) ^
    # (altitude data) ^
    # \n
    # 'name' _MR (mixing ratio data) ^
    # (mixing ratio data) ^
    # \n
    
    f = open(filename)
    
    rows = f.readlines()
    
    
    # Search all rows for molecule name
    # Start and end indicies of molecule
    ind1 = 0
    ind2 = 0
    for i in range(len(rows)):
        m = rows[i].find('Molecule '+molname+' ')
        
        # If it is found, extract data
        if m != -1:
            ind1 = i
            
            # Find the end of the data (the beginning of the next molecule)
            for k in range(i+1,len(rows)):
                # Look for the next iteration of the word 'Molecule'
                m2 = rows[k].find('Molecule')
                
                if m2 != -1 and ind2 == 0:
                    ind2 = k
                    
                    
            # If this was the last molecule, just use the last index
            if ind2 == 0:
                ind2 = len(rows) + 1
                
                
    
    # Extract altitudes and mixing ratios
    mr = []
    alt = []
    
    # Calculate number of data rows
    drow = int((ind2-ind1 - 4)/2)
        
    # Mixing ratios
    # First row don't use the first two elements
    row = rows[ind1+2].split()
    for i in range(2,len(row)-1):
        mr.append(float(row[i]))
    # For all other rows don't use the last element
    for i in range(ind1+3,ind1+2+drow):
        row = rows[i].split()
        
        for k in range(len(row)-1):
            mr.append(float(row[k]))
            
    # Altitudes
    # First row don't use the first two elements
    row = rows[ind1+3+drow].split()
    for i in range(2,len(row)-1):
        alt.append(float(row[i]))
    # For all other rows don't use the last element
    for i in range(ind1+4+drow,ind1+4+2*drow-1):
        row = rows[i].split()
        
        for k in range(len(row)-1):
            alt.append(float(row[k]))

        
    # Return mixing ratios and altitudes
    return mr,alt
                
    



    
    
    
 





