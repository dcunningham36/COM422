class Car:

    def __init__(self, currentSpeed, fuelLevel, maxSpeed):
        self.currentSpeed = currentSpeed
        self.fuelLevel = fuelLevel
        self.maxSpeed = maxSpeed

    def accelerate(self, accel):
        if self.fuelLevel > 0:
            if self.currentSpeed + accel <= self.maxSpeed:
                self.currentSpeed += accel
                self.fuelLevel -= 1
            else:
                self.currentSpeed = self.maxSpeed
            return True
        self.currentSpeed = 0
        return False

    def brake(self, dec):
        if self.currentSpeed - dec >= 0:
            self.currentSpeed -= dec
        else:
            self.currentSpeed = 0

    def refuel(self, changeBy):
        if self.fuelLevel + changeBy <= 100:
            self.fuelLevel += changeBy
        else:
            self.fuelLevel = 100

