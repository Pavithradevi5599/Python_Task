#print the value of key2
import json
data="""
{
    "Name":"Pavi",
    "Age":24,
    "City":"Madurai"
    }"""
#convert dictionary format
json=json.loads(data)
print("Key and value pair: ",data)
print("Print the value of key 2: ",json['Age'])
