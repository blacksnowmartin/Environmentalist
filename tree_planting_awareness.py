import time

class Tree:
    def __init__(self, name):
        self.name = name
        self.watered = False

    def water(self):
        self.watered = True
        print(f"{self.name} has been watered. Good job!")

    def is_watered(self):
        return self.watered

def encourage_to_plant_trees():
    print("Welcome to the Tree Planting Encouragement Program!")
    print("Let's make the world greener!")

    tree_name = input("Enter a name for your tree: ")
    my_tree = Tree(tree_name)

    print(f"Great choice! Your tree, {my_tree.name}, has been planted.")

    while True:
        action = input("\nEnter 'water' to water your tree, 'quit' to exit: ").lower()

        if action == 'water':
            my_tree.water()
        elif action == 'quit':
            print("Thank you for planting trees. Keep up the good work!")
            break
        else:
            print("Invalid input. Please enter 'water' or 'quit'.")

def remind_to_water_tree(tree, interval=60):
    while True:
        if not tree.is_watered():
            print(f"Don't forget to water your tree, {tree.name}!")
        time.sleep(interval)

if __name__ == "__main__":
    encourage_to_plant_trees()
    # Uncomment the line below if you want to enable reminders
    # remind_to_water_tree(my_tree)
