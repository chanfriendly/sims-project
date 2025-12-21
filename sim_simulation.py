import random
import time

class House:
    def __init__(self):
        self.furniture = {
            "Bed": "Sleep",
            "Fridge": "Eat",
            "TV": "Socialize"
        }

class Sim:
    def __init__(self, name):
        self.name = name
        # Initialize stats between 30 and 70 to start
        self.hunger = random.randint(30, 70)
        self.energy = random.randint(30, 70)
        self.social = random.randint(30, 70)
    
    def status(self):
        return f"Hunger: {self.hunger}, Energy: {self.energy}, Social: {self.social}"

    def eat(self):
        print(f"{self.name} is hungry ({self.hunger}/100) -> Eats at Fridge")
        self.hunger = min(100, self.hunger + 40)
        self.energy = max(0, self.energy - 5)
        
    def sleep(self):
        print(f"{self.name} is tired ({self.energy}/100) -> Sleeps in Bed")
        self.energy = min(100, self.energy + 50)
        self.hunger = max(0, self.hunger - 10)

    def socialize(self):
        print(f"{self.name} is lonely ({self.social}/100) -> Watches TV")
        self.social = min(100, self.social + 30)
        self.energy = max(0, self.energy - 10)
        self.hunger = max(0, self.hunger - 5)

    def live_day(self, house):
        # Decay stats slightly each turn
        self.hunger = max(0, self.hunger - 5)
        self.energy = max(0, self.energy - 5)
        self.social = max(0, self.social - 5)

        # Decide what to do based on lowest stat
        stats = {
            "hunger": self.hunger,
            "energy": self.energy,
            "social": self.social
        }
        
        lowest_stat = min(stats, key=stats.get)
        
        if lowest_stat == "hunger":
            if "Fridge" in house.furniture:
                self.eat()
        elif lowest_stat == "energy":
            if "Bed" in house.furniture:
                self.sleep()
        elif lowest_stat == "social":
            if "TV" in house.furniture:
                self.socialize()
        else:
            print(f"{self.name} is doing nothing.")

def run_simulation():
    my_house = House()
    my_sim = Sim("Alex")
    
    print(f"Starting simulation for {my_sim.name}...")
    print(f"Initial Stats: {my_sim.status()}")
    print("-" * 30)

    # Run for 10 'hours'
    for hour in range(1, 11):
        print(f"Hour {hour}:")
        my_sim.live_day(my_house)
        print(f"Stats: {my_sim.status()}")
        print("-" * 30)
        # time.sleep(0.5) # Optional delay for readability if running interactively

if __name__ == "__main__":
    run_simulation()
