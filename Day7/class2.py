class Car:
    #below are the properties/states/members of the class
    wheeler=4
    engine='Petrol'
    base_speed='40kmph'
    max_speed='120kmph'
    gears=4
    def __init__(self,air_bags,security,base_budget,varient,total_sale):
        self.air_bags=air_bags
        self.security=security
        self.base_budget=base_budget
        self.varient=varient
        self.total_sale=total_sale

    #object method
    def display_properties(self):
        print({
            'wheeler':self.wheeler,
            'engine':self.engine,
            'base_speed':self.base_speed,
            'max_speed':self.max_speed,
            'gears':self.gears,
            'air_bags':self.air_bags,
            'security':self.security,
            'base_budget':self.base_budget,
            'varient':self.varient,
            'total_sale':self.total_sale
        })
        
    #class method
    @classmethod
    def update_gears(cls,new_gears):
        cls.gears=new_gears
        print(f'Np. of gears:{cls.gears}')
    def update_base_speed(self,new_speed):
        self.base_speed=new_speed
        print(f'New base speed:{self.base_speed}')
    def update_max_speed(self,new_speed):
        self.max_speed=new_speed
        print(f'New Max Speed:{self.max_speed}')
# TATA=Car()

'''instead of writing many lines of code, we'll simply write an innit constructor'''

# TATA.engine=['Petrol','Diesel','EV']
# TATA.air-bags=True
# TATA.no_of_air_bags=4
# TATA.base_budget='2L'
# TATA.no_of_varient=12

#costructor to initialize the state of an object:__init__(also known as magic function)



TATA=Car(True,'Level 5', '2L',12,100000)
print('properties before updation:')
TATA.display_properties()
print()

print('Properties after updation:')
TATA.update_base_speed('60kmph')
TATA.update_max_speed('160kmph')
TATA.update_gears(5)
TATA.display_properties()

print('Mahindra:')
mahindra=Car(True,'Level 4','4L',20,250000)
mahindra.display_properties()
