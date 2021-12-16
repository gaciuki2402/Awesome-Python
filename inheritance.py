class vehicle(object):
    def __init__(self,vehicle,price,speed):
        self.vehicle=vehicle
        self.price=price
        self.speed=speed
class car(vehicle):
    def __init__(self,vehicle,price,speed,model):
        super().__init__(vehicle,price,speed)
        self.model=model

Range_Rover=car('Range_Rover','$67,200','9-speed automatic','R-Dynamic HSE P300')
print('This vehicle is:',Range_Rover.vehicle)
print('This vehicle has a price of',Range_Rover.price)
print('This vehicle has a speed of',Range_Rover.speed)
print('This vehicle has this model:',Range_Rover.model)