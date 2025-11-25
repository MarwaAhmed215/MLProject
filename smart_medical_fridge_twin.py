"""
Digital Twin Model for Smart Medical Fridge (Manufacturing/IoT)
"""
import random
from datetime import datetime

class SmartMedicalFridgeTwin:
    def __init__(self, fridge_id, target_temp=4.0):
        self.fridge_id = fridge_id
        self.current_temp = target_temp
        self.target_temp = target_temp
        self.door_open = False
        self.inventory = {}
        self.last_update = datetime.now()
        self.alerts = []

    def update_temperature(self, sensor_temp):
        self.current_temp = sensor_temp
        self.last_update = datetime.now()
        if self.current_temp > self.target_temp + 2:
            self.alerts.append(f"High temperature alert: {self.current_temp}°C at {self.last_update}")
        elif self.current_temp < self.target_temp - 2:
            self.alerts.append(f"Low temperature alert: {self.current_temp}°C at {self.last_update}")

    def open_door(self):
        self.door_open = True
        self.last_update = datetime.now()
        self.alerts.append(f"Door opened at {self.last_update}")

    def close_door(self):
        self.door_open = False
        self.last_update = datetime.now()
        self.alerts.append(f"Door closed at {self.last_update}")

    def add_inventory(self, item, quantity):
        self.inventory[item] = self.inventory.get(item, 0) + quantity
        self.last_update = datetime.now()

    def remove_inventory(self, item, quantity):
        if item in self.inventory:
            self.inventory[item] = max(0, self.inventory[item] - quantity)
            self.last_update = datetime.now()

    def get_status(self):
        return {
            "fridge_id": self.fridge_id,
            "current_temp": self.current_temp,
            "target_temp": self.target_temp,
            "door_open": self.door_open,
            "inventory": self.inventory,
            "last_update": self.last_update,
            "alerts": self.alerts[-5:],  # last 5 alerts
        }

# Example usage
if __name__ == "__main__":
    fridge = SmartMedicalFridgeTwin(fridge_id="FRIDGE-001")
    # Simulate sensor updates
    for _ in range(10):
        temp = round(random.uniform(2.0, 8.0), 2)
        fridge.update_temperature(temp)
        if random.choice([True, False]):
            fridge.open_door()
            fridge.close_door()
        fridge.add_inventory("Vaccine", random.randint(1, 5))
        fridge.remove_inventory("Vaccine", random.randint(0, 2))
    print(fridge.get_status())
