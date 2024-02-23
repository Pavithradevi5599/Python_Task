#convert data.txt file to data.js and the file contents must be in json format
import json
with open('data.txt','r')as txt_file:
    data=txt_file.read().splitlines()
dict={}
for line in data:
    key,value=line.split(':')
    dict[key]=value
with open('data.json','w')as json_file:
    json.dump(dict,json_file,indent=4)
print("Successfully converted data.txt file to data.json")