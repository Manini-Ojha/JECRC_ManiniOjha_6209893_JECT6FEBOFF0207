class Car:
    #below are the properties/states/members of the class
    wheeler=4
    engine='Petrol'
    base_speed='40kmph'
    max_speed='120kmph'
    gears=4
#instances of the above class
TATA=Car()
print(TATA)#prints object location and object name + which class the object got created from

#to access all properties we follow the following syntax
print('---TATA---')
print(f'No. of wheelers:{TATA.wheeler}')
print(f'Type of engine:{TATA.engine}')
print(f'Base speed:{TATA.base_speed}')
print(f'Max speed:{TATA.max_speed}')
print(f'No. of gears:{TATA.gears}')

TATA.air_bags=True
TATA.security='Level 5'

print(f'No. of Air bags:{TATA.air_bags}')
print(f'Security Level:{TATA.security}')
print()

mahindra=Car()

print('---Mahindra---')
print(f'No. of wheelers:{mahindra.wheeler}')
print(f'Type of engine:{mahindra.engine}')
print(f'Base speed:{mahindra.base_speed}')
print(f'Max speed:{mahindra.max_speed}')
print(f'No. of gears:{mahindra.gears}')
print()

suzuki=Car()

print('---Suzuki---')
print(f'No. of wheelers:{suzuki.wheeler}')
print(f'Type of engine:{suzuki.engine}')
print(f'Base speed:{suzuki.base_speed}')
print(f'Max speed:{suzuki.max_speed}')
print(f'No. of gears:{suzuki.gears}')
print()

toyota=Car()

print('---Toyota---')
print(f'No. of wheelers:{toyota.wheeler}')
print(f'Type of engine:{toyota.engine}')
print(f'Base speed:{toyota.base_speed}')
print(f'Max speed:{toyota.max_speed}')
print(f'No. of gears:{toyota.gears}')
