class LithiumBattery:
    def __init__(self, capacity):
        self.capacity = capacity
        self.charge_level = 100  # Initial charge level

    def discharge(self, amount):
        if self.charge_level >= amount:
            self.charge_level -= amount
            print(f"Discharged {amount}% from the battery. Current charge: {self.charge_level}%")
        else:
            print("Insufficient charge to discharge.")

    def recycle(self):
        # Simulate the recycling process
        self.charge_level = 0
        print("Recycling the lithium battery. Thank you for contributing to recycling efforts!")

# Example usage
battery = LithiumBattery(capacity=3000)  # Assume a battery with a capacity of 3000 mAh

# Simulate usage
battery.discharge(20)
battery.discharge(30)

# Recycling the battery
battery.recycle()

#Clean environment 
