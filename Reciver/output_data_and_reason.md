i am getting out put of sender in json format string and in that only i am using 2 parameter to calculate average..

please find my local console output with sender inputs given in every first in console,

INPUT FROM SENDER:{"temperature":30.72,"soc":76.67,"chargerate":0.64}
Temperature - Minimum value: 30.72  Maximum value: 30.72  
Chargerate - Minimum value: 0.64   Maximum value: 0.64   

Input From Sender : {"temperature":10.5,"soc":76.67,"chargerate":50.2}
OUTPUT:
Temperature - Minimum value: 10.5   Maximum value: 30.72  
Chargerate - Minimum value: 0.64   Maximum value: 50.2   

Input From Sender :{"temperature":1.5,"soc":76.67,"chargerate":20.2}
OUTPUT:
Temperature - Minimum value: 1.5    Maximum value: 30.72  
Chargerate - Minimum value: 0.64   Maximum value: 50.2   

Input From Sender :{"temperature":100.5,"soc":76.67,"chargerate":0.2}
OUTPUT:
Temperature - Minimum value: 1.5    Maximum value: 100.5  
Chargerate - Minimum value: 0.2    Maximum value: 50.2   

Input From Sender :{"temperature":30.72,"soc":76.67,"chargerate":0.64}
OUTPUT:
Temperature - Minimum value: 1.5    Maximum value: 100.5   Average of last five input reading: 34.788
Chargerate - Minimum value: 0.2    Maximum value: 50.2    Average of last five input reading: 14.376000000000001

Input From Sender :{"temperature":30.72,"soc":76.67,"chargerate":0.64}
OUTPUT:
{'temperature': [1.5, 100.5, 28.99], 'chargerate': [0.2, 50.2, 11.980000000000002]}
Temperature - Minimum value: 1.5    Maximum value: 100.5   Average of last five input reading: 28.99
Chargerate - Minimum value: 0.2    Maximum value: 50.2    Average of last five input reading: 11.980000000000002





