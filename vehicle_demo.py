from vehicles import Car, Truck, SUV

my_car = Car("Honda","Civic", "10,543", "$24,695.00", "4 doors" )

my_truck = Truck("Ford", "F-150", "65,396", "$40,085.00", "4x4"  )

my_SUV = SUV("Toyota","RAV4", "27,418", "$31,900.00","5 person" )

print(f''' USED CAR INVENTORY
The following car is in inventory:
Make:{my_car.get_make()} 
Model:{my_car.get_model()} 
Mileage:{my_car.get_mileage()}  
Price: {my_car.get_price()} 
Number of doors:{my_car.get_door_num()} 

The following pickup truck is in inventory:
Make:{my_truck.get_make()}
Model:{my_truck.get_model()}
Mileage:{my_truck.get_mileage()}
Price:{my_truck.get_price()}
Drive type:{my_truck.get_drive_type()}

The following SUV is in inventory:
Make:{my_SUV.get_make()} 
Model:{my_SUV.get_model()} 
Mileage:{my_SUV.get_mileage()}
Price:{my_SUV.get_price()}
Passenger capacity:{my_SUV.get_passenger_capacity()}

''')


"""
1. Which class is the superclass?
Automobile
2. Which classes are subclasses?
Car, Truck, SUV
3. What attributes are inherited by all three subclasses?
make, model, mileage, price
4. What attribute is unique to the `Car` class?
number of doors
5. What attribute is unique to the `Truck` class?
drive type
6. What attribute is unique to the `SUV` class?
passenger capacity
7. Why is inheritance useful in this example?
if you need to make changes to the attributes in the Superclass, you  only need to do it at one place and it will be inherited
8. What could go wrong if you copied and pasted the same automobile code into all three subclasses instead?
if you  need to change some part of the code, you could forget to do it at one of the locations or copy and paste error
"""