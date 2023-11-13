class OceanConservation:
    def __init__(self):
        self.plastic_pollution = 0
        self.fish_population = 100
        self.ecosystem_health = 100

    def raise_awareness(self):
        print("Welcome to the Ocean Conservation Simulator!")
        print("You are in charge of making decisions to conserve the ocean.")

        while True:
            print("\nCurrent Status:")
            print(f"Plastic Pollution Level: {self.plastic_pollution}%")
            print(f"Fish Population: {self.fish_population}%")
            print(f"Ecosystem Health: {self.ecosystem_health}%")

            print("\nOptions:")
            print("1. Organize a Beach Cleanup")
            print("2. Promote Sustainable Fishing Practices")
            print("3. Implement Plastic Reduction Campaign")
            print("4. Exit")

            choice = input("Enter your choice (1-4): ")

            if choice == '1':
                self.organize_beach_cleanup()
            elif choice == '2':
                self.promote_sustainable_fishing()
            elif choice == '3':
                self.implement_plastic_reduction_campaign()
            elif choice == '4':
                print("Thank you for your efforts in ocean conservation. Exiting.")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")

    def organize_beach_cleanup(self):
        self.plastic_pollution -= 10
        self.ecosystem_health += 5
        print("Beach cleanup organized! Plastic pollution reduced, and ecosystem health improved.")

    def promote_sustainable_fishing(self):
        self.fish_population -= 10
        self.ecosystem_health += 3
        print("Promoting sustainable fishing practices! Fish population affected, but ecosystem health improved.")

    def implement_plastic_reduction_campaign(self):
        self.plastic_pollution -= 15
        self.ecosystem_health += 8
        print("Plastic reduction campaign implemented! Significant reduction in plastic pollution and improved ecosystem health.")


# Usage
if __name__ == "__main__":
    ocean_simulation = OceanConservation()
    ocean_simulation.raise_awareness()
