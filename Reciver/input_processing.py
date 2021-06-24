# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 02:25:37 2021

@author: VNO1COB
"""
import json

def read_sender_inputs():
    input_value = input()
    input_dict = json.loads(input_value)
    print(input_dict)
    print(input_dict["temperature"])
    print(input_dict["chargerate"])
    return input_dict["temperature"],input_dict["chargerate"]  

def average_of_input_list(list_of_input_readings):
    min_max_avg_list = []
    min_max_avg_list.append(min(list_of_input_readings))
    min_max_avg_list.append(max(list_of_input_readings))
    if len(list_of_input_readings) >= 5:
        min_max_avg_list.append(sum(list_of_input_readings[-5:])/len(list_of_input_readings))
    return min_max_avg_list  

def averagecalculation(temperature,chargerate):
      min_max_dict = {}
      min_max_dict["temperature"] = average_of_input_list(temperature)
      min_max_dict["chargerate"] = average_of_input_list(chargerate)
      print(min_max_dict)
      return min_max_dict
        
   