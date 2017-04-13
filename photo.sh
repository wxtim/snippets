#!/bin/bash
# A SCRIPT TO COPY ALL FILES OF A GIVEN TYPE
# TO A SINGLE OUTPUT DIRECTORY

# Tim Pillinger 2017

# Instructions
# 1. Copy this script or save it to your preferred
#    location.
# 2. Change the details of the following variable
export search_path=~/ # location from which files are coming
export extension=".jp*g" # search criterion
export destination=~/Videos/ # destination folder
# 3. Run programme by navigating to the folder with this
#    script and running \. photo.sh 


# Main Script
for file in $(find $search_path -type f | grep $extension);
        
    do   
        echo $file
        # put your destination directory here
        cp $file $destination
    done
