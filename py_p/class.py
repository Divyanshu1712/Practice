# Create a Car class with (attributes==varibale) like brand and model. Then create an instance of this class.

class Car: #always class name in captail letter like Car , Reverse but not like car==X
    def __init__(self,model,brand):
        #__init__ is spec. function we use this at this place
        # ___init__ is called constuctor and when object is called and it will display
        self.model=model
        self.brand=brand

    def fullname(self,):
        return f"{self.brand} {self.model}"

def ElectricCar(Car):
    def __init(self,brand,model,battery_size):
        super().__init__(model,brand) #inhertiatnce use in this by using super. method
        self.battery_size=battery_size

my_tesla=ElectricCar("model-S","Tesla","8-kWHn")
print(my_tesla)


# my_car=Car("madindra","thar") 
# #object define this only like my_car// jb Car class ho toh uska object my_car he hoga usse jada nhi khuch
# my_new_car=Car("volvo","sedan")
# print(my_car.model,my_car.brand)
# print(my_new_car.brand,my_new_car.model)
# # print(my_new_car.fullname())


