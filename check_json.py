import json
 #comma missing in salary.
json_data={
"company":{
"employee":{
"name":"emma",
"payble":{
"salary":7000, 
"bonus":800
}
}
}
}
data2=json.dumps(json_data,indent=2)
print(data2)
print("This is valid json format")
