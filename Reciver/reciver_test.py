# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 02:28:15 2021
@author: VNO1COB
"""
import unittest
import input_processing


class test_sender_max_min_avg(unittest.TestCase):
    
   def test_mininmum_value(self):
      minimum_value=input_processing.average_of_input_list([94.95 , 96, 112, 100.4, 97.6])[0]
      print(minimum_value)
      self.assertEqual(minimum_value,94.95) 

   def test_maximum_value(self):
      maximum_value=input_processing.average_of_input_list([88.33 , 99, 65, 195.4, 141.6])[1]
      print(maximum_value)
      self.assertEqual(maximum_value,195.4)
   def test_average_value(self):
      average_store=input_processing.average_of_input_list([88.33 , 99, 65, 195.4, 141.6])[2]
      print(average_store)
      self.assertEqual(average_store,117.86600000000001)

   
      
   def test_avg_val_for_more_than_six_input(self):
            average_last_five_value=input_processing.average_of_input_list([88.33 , 99, 65, 195.4,140.0,140.0,106.56666666666666])[2]
            print(average_last_five_value)
            self.assertEqual(average_last_five_value,92.42380952380952) 
  
   def test_avg_val_for_less_than_five_input(self):
            average_less_than_five_value=input_processing.average_of_input_list([88.33 , 99, 65, 195.4])
            print(average_less_than_five_value)
            self.assertEqual(average_less_than_five_value,[65, 195.4]) 
  
          

#if __name__ == '__main__':
# unittest.main()
