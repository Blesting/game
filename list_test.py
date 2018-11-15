# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 15:35:04 2018

@author: Nestea
"""

    # test it  

    
def FindDuplicates(liste):  
    unique = set(liste)  
    for each in unique:  
        count = liste.count(each)  
        if count > 1:  
            print( 'There are duplicates in this list')  
            return True  
    print('There are no duplicates in this list')
    return False 

a = [8, 64, 16, 32, 4, 24]  
b = [2,2,3,6,78,65,4,4,5]  
  
FindDuplicates(a)  
FindDuplicates(b)