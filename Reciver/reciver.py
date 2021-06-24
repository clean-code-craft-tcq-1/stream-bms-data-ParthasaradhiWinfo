# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 02:27:08 2021

@author: VNO1COB
"""
from input_processing import read_sender_inputs
from input_processing import averagecalculation
from average import print_average_value

class main():
    input_temperature_list = []
    input_chargerate_list = []
    while True:
        temperature,chargerate=read_sender_inputs()
        input_temperature_list.append(temperature)
        input_chargerate_list.append(chargerate)
        average_dict = averagecalculation(input_temperature_list,input_chargerate_list)
        print_average_value(average_dict)