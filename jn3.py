#Prettyprint following json data with indent level 2 and key-value separators should be(",","=")
import json
data={
    "Name":"Pavi",
    "Age":"24"
    }
data["City"]="Madurai"
#convert json string format
pretty_json=json.dumps(data,indent=2,separators=(",","="))
print(pretty_json)