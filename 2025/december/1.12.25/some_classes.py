
import time
import os
import threading
import matplotlib.pyplot as plt

class Car:
    def __init__(self, year:int=2023, make:str="ford", model:str="fiesta", top_speed:float=102.5, acceleration:float=1):
        self.year = year
        self.make = make.strip().capitalize()
        self.model = model.strip().capitalize()
        self.top_speed = round(top_speed, 2)
        self.speed = 0
        self.acceleration = acceleration
        self.lock = threading.Lock()
        self.max_speed = False
        self.history = [] 

    def __str__(self):
        if abs(self.speed - self.top_speed) < 0.01:
            return f"{self.year} {self.make} {self.model}: {round(self.speed, 2)}‼️"
        else:
            return f"{self.year} {self.make} {self.model}: {round(self.speed, 2)}"

    def accelerate(self, current_time):
        with self.lock:
            remaining = self.top_speed - self.speed
            if remaining <= 0.05:
                self.speed = self.top_speed
                self.max_speed = True
            else:
                self.speed += remaining / (12*(self.acceleration*20))
            self.history.append((current_time, self.speed))


def acceleration_thread(car, running, start_time):
    while running.is_set():
        if not car.max_speed:
            time.sleep(0.1)
            current_time = time.time() - start_time
            car.accelerate(current_time)
        else:
            break


cars = [
    Car(),
    Car(2004, "honda", "civic", 146, 0.1)
]

threads = []
running_flag = threading.Event()
running_flag.set()
start_time = time.time()

for car in cars:
    t = threading.Thread(target=acceleration_thread, args=(car, running_flag, start_time))
    t.start()
    threads.append(t)

try:
    while True:
        time.sleep(0.1)
        os.system('clear')
        for car in cars:
            print(car)
        if all(car.max_speed for car in cars):
            break

except KeyboardInterrupt:
    pass

running_flag.clear()
for t in threads:
    t.join()

print("Stopped safely.")

# Plotting
plt.figure(figsize=(10, 6))
for car in cars:
    times = [t for t, _ in car.history]
    speeds = [s for _, s in car.history]
    plt.plot(times, speeds, label=f"{car.make} {car.model}")

plt.title("Car Acceleration Over Time")
plt.xlabel("Time (seconds)")
plt.ylabel("Speed (mph)")
plt.legend()
plt.grid(True)
plt.show()
