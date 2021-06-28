i am getting out put of sender in json format string and in that only i am using 2 parameter to calculate average..

please find my local console output with sender inputs given in every first in console,

OUTPUT:
{"temperature":30.72,"soc":76.67,"chargerate":0.64}
30.72
0.64
[30.72, 30.72]
[0.64, 0.64]
{'temperature': [30.72, 30.72], 'chargerate': [0.64, 0.64]}
Temperature - Minimum value: 30.72  Maximum value: 30.72  
Chargerate - Minimum value: 0.64   Maximum value: 0.64   

{"temperature":10.5,"soc":76.67,"chargerate":50.2}
10.5
50.2
[10.5, 30.72]
[0.64, 50.2]
{'temperature': [10.5, 30.72], 'chargerate': [0.64, 50.2]}
Temperature - Minimum value: 10.5   Maximum value: 30.72  
Chargerate - Minimum value: 0.64   Maximum value: 50.2   

{"temperature":1.5,"soc":76.67,"chargerate":20.2}
1.5
20.2
[1.5, 30.72]
[0.64, 50.2]
{'temperature': [1.5, 30.72], 'chargerate': [0.64, 50.2]}
Temperature - Minimum value: 1.5    Maximum value: 30.72  
Chargerate - Minimum value: 0.64   Maximum value: 50.2   

{"temperature":100.5,"soc":76.67,"chargerate":0.2}
100.5
0.2
[1.5, 100.5]
[0.2, 50.2]
{'temperature': [1.5, 100.5], 'chargerate': [0.2, 50.2]}
Temperature - Minimum value: 1.5    Maximum value: 100.5  
Chargerate - Minimum value: 0.2    Maximum value: 50.2   

{"temperature":30.72,"soc":76.67,"chargerate":0.64}
30.72
0.64
[1.5, 100.5]
[1.5, 100.5, 34.788]
[0.2, 50.2]
[0.2, 50.2, 14.376000000000001]
{'temperature': [1.5, 100.5, 34.788], 'chargerate': [0.2, 50.2, 14.376000000000001]}
Temperature - Minimum value: 1.5    Maximum value: 100.5   Average of last five input reading: 34.788
Chargerate - Minimum value: 0.2    Maximum value: 50.2    Average of last five input reading: 14.376000000000001

{"temperature":30.72,"soc":76.67,"chargerate":0.64}
30.72
0.64
[1.5, 100.5]
[1.5, 100.5, 28.99]
[0.2, 50.2]
[0.2, 50.2, 11.980000000000002]
{'temperature': [1.5, 100.5, 28.99], 'chargerate': [0.2, 50.2, 11.980000000000002]}
Temperature - Minimum value: 1.5    Maximum value: 100.5   Average of last five input reading: 28.99
Chargerate - Minimum value: 0.2    Maximum value: 50.2    Average of last five input reading: 11.980000000000002




But issue is i am running my reciver after sender executed only.so already every 200ms one json keyword string printer and all 5 line updted for every 200ms and then i am running my reciver so it will not work as expected.
if we run parllel when ever sender sending any parameter file .my reciver will capable of reading all the json string line by line and it will calculate average based on that.


and also some jave compilation related thing printed in console that also should be avoided.
