class Car():
    def __init__(self, max_speed):
        self.max_speed = max_speed
        self.current_speed = 0

    def accelerate(self, delta=5):
        max_accelerate = self.max_speed
        new_accelerate = self.current_speed + delta
        self.current_speed = new_accelerate if new_accelerate <= max_accelerate else max_accelerate
        return self.current_speed

    def stop(self, delta=5):
        new_stop = self.current_speed - delta
        self.current_speed = new_stop if new_stop >= 0 else 0
        return self.current_speed


if __name__ == "__main__":
    car = Car(180)

    for _ in range(25):
        print(car.accelerate(8))

    for _ in range(10):
        print(car.stop(delta=20))
