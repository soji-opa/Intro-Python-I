class Store:
    def __init__(self, name, department):
        self.name = name
        self.department = department

    def print_welcome(self):
        print(f" welcome {self.name}! which department would you like to visit")

        for d in self.department:
            print(d)


class Department:
    def __init__(self, id, name, product):
        self.id = id
        self.name = name
        self.product = product

    def __str__(self):
        return f"{self.id}: {self.name}"


store = Store("The Dugout", [
    Department(1, "Baseball", []),
    Department(2, "Basketball", []),
    Department(3, "Football", []),
    Department(4, "Golf", [])
])


while True:
    #  print a welcome message for the store

    store.print_welcome()

    # get the department number the user wants to visit
    selection = (input("which department would you like to visit? "))

    # if the user types "quit", exit the program
    if selection == "quit":
        break

    chosen_department = store.department[int(selection)-1]

    print (f"You selected the {chosen_department.name} department.\n")