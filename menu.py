
class Menu:
    def __init__(self):
        self.options = {
            1: "Add a new contact",
            2: "View all contacts",
            3: "Search for a contact",
            4: "Update a contact",
            5: "Delete a contact",
            6: "Exit"
        }

    def display(self):
        print("\nMenu:")
        for key, value in self.options.items():
            print(f"{key}. {value}")

    def get_choice(self):
        while True:
            try:
                choice = int(input("Please enter your choice (1-6): "))
                if choice in self.options:
                    return choice
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 6.")
    