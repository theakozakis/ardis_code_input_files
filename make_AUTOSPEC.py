#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Code to create both reflectance and emission AUTOSPEC files:
    make_AUTOSPEC(layersfile,chemfile,mollist,temp)

Inputs: LAYERS file, chem file, molecule list, stellar host temperature
    layersfile:  path to LAYERS file as a string
    chemfile:  path to chem file as a string
    mollist: list of molecules (all as strings written exactly as in the chem file)
    temp: stellar host temperature as a string with two decimal places
    clist: list of cloud altitudes as floats
    
Outputs: reflectance and emission AUTOSPEC files
    Reflectance file:  original LAYERS file name with suffix _AUTOSPEC_reflectance
    Emission file:  original LAYERS file name with suffix _AUTOSPEC_emission
"""

def make_AUTOSPEC(layersfile,chemfile,mollist,temp,clist):
    
    # Code to create reflectance files
    from make_AUTOSPEC_reflectance import make_AUTOSPEC_reflectance
    # Code to create emission files
    from make_AUTOSPEC_emission import make_AUTOSPEC_emission
    # Code to create emission files with cloud layers
    from make_AUTOSPEC_emission_clouds import make_AUTOSPEC_emission_clouds
    
    # Create reflectance file
    make_AUTOSPEC_reflectance(layersfile,chemfile,mollist,temp)
    
    # Create emission file
    make_AUTOSPEC_emission(layersfile,chemfile,mollist)
    
    # Create emission files with clouds
    if len(clist) != 0:
        # Run the program for each cloud altitude
        for i in range(len(clist)):   
            make_AUTOSPEC_emission_clouds(layersfile,chemfile,mollist,clist[i])
    
    
    
    
    
    
    
    
    
##### Example run
##### Example molecule list    
#mlist = ['H2O','CO2','N2O','CFC11','CFC12','NO2','HNO3','O3','O3ISO','CH4','O2','CO','OH','H2CO','CH3CL','O']
#clist = [1.0,6.0,12.0]    

#ldir = '/Users/Admin/Documents/Research_Lisa/biosignatures_WD_RG/RT_output/running_IR0.01/layers_IR/'
#cdir = '/Users/Admin/Documents/Research_Lisa/red_giants/RT_input/'

##### alpha Boo at seff = 1.0
#lfile = ldir+'LAYERS.atmZL_altPT_aBo_100_ff1.0.txt'
#cfile = cdir+'chem_aBo_100_ff1.0'
#startemp = '4286.00'
