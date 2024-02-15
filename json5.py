import json
class Vehicle:
    def __init__(self,name,engine,price):
        self.name=name
        self.engine=engine
        self.price=price
vehicle=Vehicle("Toyota Rav4","2.5L",3200)
#create a dictionary
vechicle_dict={
    "name":vehicle.name,
    "engine":vehicle.engine,
    "price":vehicle.price
}
#convert dictionary to a json string
json_string=json.dumps(vechicle_dict,indent=4)
print(json_string)