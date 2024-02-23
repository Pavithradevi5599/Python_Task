import json
#json string format
a="""{"name":"xyz","age":20}"""
print(a)
print(type(a))
#json string format to dictionary
b=json.loads(a)
print(b)
print(type(b))
print(b["name"])
c=json.dumps(b)
print(c)
print(type(c))