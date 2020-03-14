import copy
import random
import json

data = {            "factoryID": "1234",
                    "factoryName": "Bhushan Steel",
                    "sensors": [
                        {
                            "name": "CO2",
                            "type": "Gas",
                            "value": 11
                        },
                        {
                            "name": "Noise",
                            "type": "Noise",
                            "value": 12
                        }
                    ],
                    "timestamp": 1553614961
                }
                    
                    
data2 = copy.copy(data)
global sensordata
sensordata = ""
data2['factoryID'] = '5678'
data2['factoryName'] = 'Jindal Steel'
data2['timestamp'] = 1549778400
for i in range(0,50):
    data2['factoryID'] = '5678'
    data2['factoryName'] = 'Jindal Steel'
    data2['sensors'][0]['value'] = random.randrange(5, 51)
    data2['sensors'][1]['value'] = random.randrange(51, 96)
    data2['timestamp'] = str(int(data2['timestamp']) + 21600)
    sensordata = sensordata + str(json.dumps(data2)) + ","
    
data2['timestamp'] = 1549778400

for i in range(0,50):
    data2['factoryID'] = '1234'
    data2['factoryName'] = 'Bhushan Steel'
    data2['sensors'][0]['value'] = random.randrange(5, 51)
    data2['sensors'][1]['value'] = random.randrange(51, 96)
    data2['timestamp'] = str(int(data2['timestamp']) + 21600)
    sensordata = sensordata + str(json.dumps(data2)) + ","


diff = 1549778400 - 1549800000