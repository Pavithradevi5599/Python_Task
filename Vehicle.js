const jsonData=
{
    "name":"Toyota Rav4",
    "engine":"2.5L",
    "price":32000
}
function Vehicle(name,engine,price)
{
    this.name=name;
    this.engine=engine;
    this.price=price;

}
const VehicleObj=new Vehicle(jsonData.name,jsonData.engine,jsonData.price);
console.log(VehicleObj.name);
console.log(VehicleObj.engine);
console.log(VehicleObj.price);