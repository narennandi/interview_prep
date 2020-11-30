import numpy as np
import pickle
import json
import requests

##################################################################
# Converting NumPy array to byte format
byte_output = np.array([ [1, 2, 3], [4,5,6] ,[7,8,9] ]).tobytes()
#print(byte_output)

# Converting byte format back to NumPy array
array_format = np.frombuffer(byte_output, dtype="int32")
#print(array_format)	
##################################################################

##################################################################
#Here's an example dict
grades = { 'Alice': 89, 'Bob': 72, 'Charles': 87 }

#Use dumps to convert the object to a serialized string
serial_grades = pickle.dumps( grades )
# print(serial_grades)

#Use loads to de-serialize an object
received_grades = pickle.loads( serial_grades )
# print(received_grades)
##################################################################

##################################################################
data = {
	"user": {
		"name": "Naren Nandi",
		"age" : 93
	}
}

with open("data_file.json", "w") as write_file:
	json.dump(data, write_file, indent = 4)

json_str = json.dumps(data)
# print(json_str)
##################################################################

##################################################################
with open("data_file.json", 'r') as read_file:
	data = json.load(read_file)
# print(data)

json_string = """
{
    "researcher": {
        "name": "Ford Prefect",
        "species": "Betelgeusian",
        "relatives": [
            {
                "name": "Zaphod Beeblebrox",
                "species": "Betelgeusian"
            }
        ]
    }
}
"""
data = json.loads(json_string)
##################################################################

##################################################################
response = requests.get("https://jsonplaceholder.typicode.com/todos")
todos = json.loads(response.text)





