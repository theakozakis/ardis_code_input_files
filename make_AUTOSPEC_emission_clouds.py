#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Code to create emission AUTOSPEC files with a specified cloud altitude # (km):
    make_AUTOSPEC_emission(layersfile,chemfile,mollist,calt)

Inputs: LAYERS file, chem file, molecule list, stellar host temperature
    layersfile:  path to LAYERS file as a string
    chemfile:  path to chem file as a string
    mollist: list of molecules (all as strings written exactly as in the chem file)
    calt: altitude of cloud layer in km (as a float)

Output: emission AUTOSPEC file with cloud layer
    Emission file:  original LAYERS file name with suffix _AUTOSPEC_emission_#km
"""


def make_AUTOSPEC_emission_clouds(layersfile,chemfile,mollist,calt):
    
    # Code that finds a specified molecule in a chem file and returns mixing ratios
    # and altitudes
    from read_chem_files import read_chem_files
    # Code that reads effective altitudes from LAYERS file
    from read_LAYERS import read_LAYERS

    import numpy as np
    
    f = open(layersfile+'_AUTOSPEC_emission_'+str(calt)+'km','w')
    
    print('******************************************\n')
    print('Creating emission AUTOSPEC file...')
    
    # Find effective altitudes and lowest altitude temperature from LAYERS file
    lay = read_LAYERS(layersfile)
    ealt = lay[0]
    tlist = lay[1]
    
    # Find index of layer with closest cloud altitude altitude
    caltc = min(ealt, key=lambda x:abs(x-calt))
    # Find the index of that altitude
    inc = ealt.index(caltc)
    print(str(calt)+' km: layer '+str(inc+1))
    
    # Reference temperature should be the temperature of that layer
    tlow = tlist[inc]
    

    
    # Write header info
    f.write('! Parameter file for AUTOSPEC.\n')
    f.write('\n')
    f.write('Model number			1\n')
    f.write('Ray number/ray			1\n')
    f.write('\n')
    f.write('Lab spectrum?			0\n')
    f.write('Absorption spectrum?		0\n')
    f.write('Pade Adjustable parameter	0.7\n')
    f.write('Perfect ends?			1\n')
    f.write('Smearing function code		4\n')
    f.write('\n')
    f.write('Wavenumber shift/shift				0.000\n')
    f.write('Step size (cm-1)				0.01\n')
    f.write('Extra calculation range beyond limits		250.0\n')
    f.write('Minimum line depth for inclusion in output	1.0e-5\n')
    f.write('Wing cutoff					1.0e-6\n')
    f.write('Validity range for Van Vleck-Weisskopf factors	10.0\n')
    f.write('Voigt/Lorentz switchover point (A-value)	2.0\n')
    f.write('Voigt core width (Gaussian half-widths)		12.0\n')
    f.write('\n')
    f.write('Width of instrumental smearing profile (cm-1)	0.1\n')
    f.write('Sinc function asymmetry/asymmetry		0.0\n')
    f.write('Instrument Entrance Diameter                    0.4\n')
    f.write('Instrument Focal Length                         58.0\n')
    # Reference temperature is the temperature at the lowest layer
    f.write('Temperature reference at spectrometer		'+str(tlow)+'\n')
    f.write('Maximum points in smearing function		20\n')
    f.write('\n')
    f.write('Line databases	"SAO2012,UV_CROSS"\n')
    f.write('\n')
    
    # Find effective altitudes from LAYERS file
    lay = read_LAYERS(layersfile)
    ealt = lay[0]
    
    
    # Extracts relevant molecules from chem files
    for i in range(len(mollist)):
        mrlist = []
        print('-----------------------\n')
        print('Locating data for '+str(mollist[i]))
        
        mr,alt = read_chem_files(chemfile,mollist[i])
        
        # If there isn't a match
        if len(mr) == 0:
            print('Molecule not found, excluding from AUTOSPEC')
        
        # If the molecule is found
        if len(mr) != 0:
            print('Molecule found, adding to AUTOSPEC')
            
            
            # Rebin chem file data to LAYERS effective altitudes
            mri = np.interp(ealt,alt,mr)
            
            # Write molecule info
            # Convert numbers to fortran format
            for k in range(len(mri)):
                
                # Scientific notation, two decimal places, two exponent digits
                val = np.format_float_scientific(mri[k],precision=2,pad_left=True,exp_digits=2)
                
                
                
                # Convert to string and break up into number and exponent
                vals = str(val)
                vs = vals.split('e')
                
                # Number part
                v1 = vs[0]
                # If the length of the number isn't 4, add zeros onto end
                if len(v1) < 4:
                    # If the length is 2, add two zeros
                    if len(v1) == 2:
                        v1 = vs[0] + '00'
                    # If the length is 3, add one zero
                    if len(v1) == 3:
                        v1 = vs[0] + '0'
                    
                # Put together as string and add to mixing ratio list
                v2 = vs[1]
                
                mrlist.append(v1+'E'+v2)
                
            #print(mrlist)
                
            # Write molecule info to file
            # If this is a reflectance spectrum the first mixing ratio should be 0.00E+00
            
            # File structure
            #Molecule   1(0)  0.00E+00 #2 #3 #4 #5 #6 ^
            #	 #7 #8 #9 #10 #11 #12 ^
            # (until the numbers of layers is reached)
            
            # Calculate the number of rows
            arow = int(np.ceil(len(ealt)/6))
            # First row
            f.write(mollist[i]+'   ')
            # If it is the first molecule in the list the first entry will be 1
            if i == 0:
                f.write('1  ')
            if i != 0:
                f.write('0  ')
            # Write the first 6 elements
            f.write(str(mrlist[0])+' '+str(mrlist[1])+' '+str(mrlist[2])
                +' '+str(mrlist[3])+' '+str(mrlist[4])+' '+str(mrlist[5])+' ^\n')
            # Go through the all 'middle' lines but the last
            for i in range(1,arow-1):
                # Write the next 6 entries
                n = i*6
                f.write('	 '+str(mrlist[n+0])+' '+str(mrlist[n+1])+' '+str(mrlist[n+2])
                +' '+str(mrlist[n+3])+' '+str(mrlist[n+4])+' '+str(mrlist[n+5])+' ^\n')
            # The last row
            f.write('	 ')
            # Number of elements left
            ni = n+5
            nf = len(ealt)-ni-1
            for i in range(nf):
                f.write(mrlist[ni+i+1]+' ')
                
            f.write('\n')
            
            
    # Write cont info
    cont = []
    for i in range(len(ealt)):
        cont.append('0.00E+00')
        
    # For an emission spectrum with clouds, the altitude of clouds should be 1.00E-05    
    cont[inc] = '1.00E-05'
        
    # First row
    f.write('CONT   0  ')

    # Write the first 6 elements,
    f.write(str(cont[0])+' '+str(cont[1])+' '+str(cont[2])
                +' '+str(cont[3])+' '+str(cont[4])+' '+str(cont[5])+' ^\n')
    # Go through the all 'middle' lines but the last
    for i in range(1,arow-1):
        # Write the next 6 entries
        n = i*6
        f.write('	 '+str(cont[n+0])+' '+str(cont[n+1])+' '+str(cont[n+2])
        +' '+str(cont[n+3])+' '+str(cont[n+4])+' '+str(cont[n+5])+' ^\n')
    # The last row
    f.write('	 ')
    # Number of elements left
    ni = n+5
    nf = len(ealt)-ni-1
    for i in range(nf):
        f.write(cont[ni+i+1]+' ')
                
    f.write('\n')

    
    # Write remaining necessary text
    f.write('Base/base     0  0.00E+00    0  0.00E+00    0  0.00E+00\n')
    f.write('Height/height 0  1.00E+00    0  0.00E+00    0  0.00E+00\n')
    f.write('\n')
    f.write('Number of iterations	0\n')
    f.write('Epsilon one		1.E-4\n')
    f.write('Epsilon two		1.E-3\n')
    f.write('Lambda			.01\n')
    f.write('Nu			10.\n')
    f.write('\n')
                
            
            
    f.close()
                
                
             
