import random
class EnergyManagementSystem:
    def __init__(self):
        # Initial states
        self.lights_on = False
        self.fan_on = False
        self.appliances = {
            "TV": False,
            "Refrigerator": False,
            "AirConditioner": False,
            "Heater": False,
            "Geyser": False,
            "Microwave": False,
            "WashingMachine": False,
            "Dishwasher": False,
        }

        # Metrics
        self.energy_consumed = 0  # in kilowatt-hours

        # Room occupancy
        self.room_occupied = False

        # Critical appliances that should not be turned off unless specified
        self.critical_appliances = {"Refrigerator", "Heater", "Geyser"}

    def turn_on_lights(self):
        if not self.lights_on:
            self.lights_on = True
            print("Lights turned on.")
            self.energy_consumed += 0.2  # Simulated energy consumption for lights
        else:
            print("Lights are already on.")

    def turn_off_lights(self):
        if self.lights_on:
            self.lights_on = False
            print("Lights turned off.")
            self.energy_consumed += 0.1  # Simulated energy consumption for lights off
        else:
            print("Lights are already off.")

    def turn_on_fan(self):
        if not self.fan_on:
            self.fan_on = True
            print("Fan turned on.")
            self.energy_consumed += 0.3  # Simulated energy consumption for fan
        else:
            print("Fan is already on.")

    def turn_off_fan(self):
        if self.fan_on:
            self.fan_on = False
            print("Fan turned off.")
            self.energy_consumed += 0.1  # Simulated energy consumption for fan off
        else:
            print("Fan is already off.")

    def turn_on_appliance(self, appliance):
        if appliance in self.appliances and not self.appliances[appliance]:
            self.appliances[appliance] = True
            print(f"{appliance} turned on.")
            # Simulated energy consumption for appliances
            self.energy_consumed += random.uniform(0.5, 2.0)
        elif appliance not in self.appliances:
            print(f"Unknown appliance: {appliance}")
        else:
            print(f"{appliance} is already on.")

    def turn_off_appliance(self, appliance):
        if appliance in self.appliances:
            if appliance in self.critical_appliances:
                print(f"{appliance} is a critical appliance and cannot be turned off.")
            elif self.appliances[appliance]:
                self.appliances[appliance] = False
                print(f"{appliance} turned off.")
                # Simulated energy consumption for appliances off
                self.energy_consumed += random.uniform(0.1, 0.5)
            else:
                print(f"{appliance} is already off.")
        else:
            print(f"Unknown appliance: {appliance}")

    def simulate_room_occupancy(self):
        # Simulate room occupancy changes
        occupancy_change = random.choice([True, False])
        if occupancy_change:
            self.room_occupied = True
            print("Room is now occupied.")
        else:
            self.room_occupied = False
            print("Room is now empty.")

    def display_energy_consumption(self):
        print(f"Total Energy Consumed: {self.energy_consumed:.2f} kWh")

# Main program
def main():
    energy_system = EnergyManagementSystem()

    while True:
        print("\n*** Energy Management System Menu ***")
        print("1. Turn On Lights")
        print("2. Turn Off Lights")
        print("3. Turn On Fan")
        print("4. Turn Off Fan")
        print("5. Turn On Appliance")
        print("6. Turn Off Appliance")
        print("7. Simulate Room Occupancy")
        print("8. Display Energy Consumption")
        print("9. Exit")

        choices = input("Enter your choices separated by space (1-9): ")

        selected_options = [int(choice) for choice in choices.split()]

        for choice in selected_options:
            if choice == 1:
                energy_system.turn_on_lights()
            elif choice == 2:
                energy_system.turn_off_lights()
            elif choice == 3:
                energy_system.turn_on_fan()
            elif choice == 4:
                energy_system.turn_off_fan()
            elif choice == 5:
                appliance = input("Enter the appliance name: ")
                energy_system.turn_on_appliance(appliance)
            elif choice == 6:
                appliance = input("Enter the appliance name: ")
                energy_system.turn_off_appliance(appliance)
            elif choice == 7:
                energy_system.simulate_room_occupancy()
            elif choice == 8:
                energy_system.display_energy_consumption()
            elif choice == 9:
                print("Exiting Energy Management System. Goodbye!")
                return
            else:
                print("Invalid choice. Please enter a number between 1 and 9.")

if __name__ == "__main__":
    main()
