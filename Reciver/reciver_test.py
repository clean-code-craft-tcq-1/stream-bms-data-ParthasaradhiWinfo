# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 02:28:15 2021

@author: VNO1COB
"""
import unittest
import input_processing


class test_sender_max_min_avf(unittest.TestCase):
    
   def test_avg_five_val(self):
      self.assertTrue(len(input_processing.averagecalculation([88.33 , 99, 65, 195.4, 141.6])),3)

   def test_min(self):
      self.assertTrue(input_processing.averagecalculation([94.95 , 96, 111, 100.4, 97.6])[0],111) 

   def test_max(self):
      self.assertTrue(input_processing.averagecalculation([197.204 , 392, 10, 10.4, 33.6])[1],205) 

   def test_avg(self):
      self.assertTrue(input_processing.averagecalculation([30,30,30,10,40])[2],10)
    
   def test_empty_input(self):
      with self.assertRaises(ValueError) as context:
            input_processing.classify_input(" ")
      self.assertTrue('wrong_input_data' in str(context.exception))

            input_processing.classify_input("102 CR")
      self.assertTrue('wrong_input_data' in str(context.exception))
      
   def test_single_input(self):
      with self.assertRaises(ValueError) as context:
            input_processing.classify_input("205.7")
      self.assertTrue('wrong_input_data' in str(context.exception))  

   def test_avg_less_val(self):
      self.assertTrue(len(input_processing.averagecalculation([133.33 , 144, 111])),2)    
      
  
          

#if __name__ == '__main__':
 # unittest.main()
