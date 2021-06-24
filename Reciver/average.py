# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 02:25:16 2021

@author: VNO1COB
"""
def print_average_value(average_dict):
    print_min_max_avg("Temperature",average_dict["temperature"])
    print_min_max_avg("Chargerate",average_dict["chargerate"])   
    
    
def print_min_max_avg(name_of_reading,min_max_average_readings):
    avg_val = ""
    if len(min_max_average_readings) == 3:
        avg_val = " Average of last five input reading: " + str(min_max_average_readings[2])
    print(f'{name_of_reading:>5} - Minimum value: {str(min_max_average_readings[0]):<5}  Maximum value: {str(min_max_average_readings[1]):<5}  {avg_val}') 
