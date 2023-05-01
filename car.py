class Car:
    def __init__(self,max_speed,color,type):
        self.max_speed = max_speed
        self.color = color
        self.type = type
        self.num_of_wheels = 4
        self.speed = 0
    def Speedup(self,speedup):
        self.speed += speedup
    def Fly(self):
        if self.max_speed == self.speed:
            print("The car " + self.type + " is flying with the speed of " + str(self.speed))
    def Land(self):
        print("Car has safly landed")
    def __str__(self):
        return("The car " + self.type + " has the color of " + self.color + " and its max speed is " + str(self.max_speed) + " its current speed is " + str(self.speed))


