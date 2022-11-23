#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Sasika Pamith Amarasinghe
# DATE CREATED:  23.11.2022                                
# REVISED DATE: 
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir

def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    
    all_files = listdir(image_dir)
    
    # An empty dictionary to store the pet image file name and relevant value
    results_dic = dict()
    
    for i in range(len(all_files)):
        file_name = all_files[i]
        
        if file_name[0] != ".":   
       # Skips file if starts with . (like .DS_Store of Mac OSX) because it 
       # isn't an pet image file
            file_name2 = file_name.lower()
            file_name2 = file_name2.split("_")
            pet_label = " ".join(file_name2[:-1])
            
           # If filename doesn't already exist in dictionary add it and it's
           # pet label - otherwise print an error message because indicates 
           # duplicate files (filenames)
            if file_name not in results_dic:
                results_dic[file_name] = [pet_label]
            else:
               print("** Warning: Duplicate files exist in directory:", file_name)   
    
    
    return results_dic
