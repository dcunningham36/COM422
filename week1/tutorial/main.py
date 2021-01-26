from Car import Car

if __name__ == '__main__':

    c1 = Car(30, 50, 120)
    c2 = Car(50, 30, 100)

    print(f"Car 1 is moving at {c1.currentSpeed}mph with {c1.fuelLevel}% fuel")

    c1.accelerate(10)
    print(f"Car 1 is moving at {c1.currentSpeed}mph with {c1.fuelLevel}% fuel")