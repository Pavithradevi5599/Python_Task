import json
sampleJson="""
{
"company":{
"employee":{
"name":"emma",
"payble":{
"salary":7000,
"bonus":800
}
}
}
}"""
#json string into a python dictionary
data=json.loads(sampleJson)
salary_value=data["company"]["employee"]["payble"]["salary"]
print("Salary:",salary_value)