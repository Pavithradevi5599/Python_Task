import json
#json string
data="""{"Name":"Pavi","Age":24}"""
print("Json string: ",data)
#convert dictionary format
data2=json.loads(data)
print(data2)
print(type(data2))
print("Name:",data2["Name"])
#convert json string format
data3=json.dumps(data2)
print(data3)
print(type(data3))