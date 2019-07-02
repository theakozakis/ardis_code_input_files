# ardis_code_input_files
Codes to generate input files for ardis


There are five codes here:

### read_chem_files.py:

Code to read in chem files outputted by CHEMCLIM and search for specific molecule: 

    read_chem_files(filename,molname) 
    
Inputs: chem file name, molecule name

    filename:  path to chem file as a string 
    
    molname:  molecule name as a string     
    
Outputs: 

    Element 0: list of mixing ratios
    
    Element 1: list of corresponding altitudes (km)
    
    
### read_LAYERS.py:
Code to extract effective altitudes and the lowest altitude temperature from a LAYERS file:

    read_LAYERS(filename)   
    
Input:  LAYERS file

    filename:  path to LAYERS file as a string 
    
Outputs:

    Element 0:  list of effective altitudes
    
    Element 1: temperature of the lowest layer
    
### make_AUTOSPEC_reflectance.py:
Code to create reflectance AUTOSPEC files:

    make_AUTOSPEC_reflectance(layersfile,chemfile,mollist,temp)
    
Inputs: LAYERS file, chem file, molecule list, stellar host temperature

    layersfile:  path to LAYERS file as a string
    
    chemfile:  path to chem file as a string
    
    mollist: list of molecules (all as strings written exactly as in the chem file)
    
    temp: stellar host temperature as a string with two decimal places
    
Output: reflectance AUTOSPEC file

    Reflectance file:  original LAYERS file name with suffix _AUTOSPEC_reflectance
    
### make_AUTOSPEC_emission.py:
Code to create emission AUTOSPEC files:

    make_AUTOSPEC_emission(layersfile,chemfile,mollist)
    
Inputs: LAYERS file, chem file, molecule list, stellar host temperature

    layersfile:  path to LAYERS file as a string
    
    chemfile:  path to chem file as a string
    
    mollist: list of molecules (all as strings written exactly as in the chem file)
    
Output: emission AUTOSPEC file

    Emission file:  original LAYERS file name with suffix _AUTOSPEC_emission

### make_AUTOSPEC.py:
Code to create both reflectance and emission AUTOSPEC files:

    make_AUTOSPEC(layersfile,chemfile,mollist,temp)
    
Inputs: LAYERS file, chem file, molecule list, stellar host temperature

    layersfile:  path to LAYERS file as a string
    
    chemfile:  path to chem file as a string
    
    mollist: list of molecules (all as strings written exactly as in the chem file)
    
    temp: stellar host temperature as a string with two decimal places
    
Outputs: reflectance and emission AUTOSPEC files

    Reflectance file:  original LAYERS file name with suffix _AUTOSPEC_reflectance
    
    Emission file:  original LAYERS file name with suffix _AUTOSPEC_emission  
    
    
## Instructions
Put all 5 codes in the same directory and run make_AUTO with your LAYERS file, chem file, molecule list, and stellar host temperature as inputs.  At the end of make_AUTO.py there is an example run with an example molecule list.
    
    
    
