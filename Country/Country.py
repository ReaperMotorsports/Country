#Christopher Morgan
#CIS 261
#Country

def main_menu():
    print("Command Menu")
    print("view - View County name")
    print("add - Add a Country")
    print("del - Delete a Country")
    print("exit - Exit Program")
    print()

def display_codes(countries):
    codes = list(countries.keys())
    codes.sort()
    code_tag = "Country Code:  "
    for code in codes:
        code_tag += code + " "
    print(code_tag)

def view(countries):
    display_codes(countries)
    code = input("Enter Country Code:  ")
    code = code.upper()
    if code in countries:
        name = countries[code]
        print(f"Country Name: {name}.\n")
    else:
        print("There is no country with that name.\n")

def add(countries):
    code = input("Enter Country Code:  ")
    code = code.upper()
    if code in countries:
        name = countries[code]
        print(f"{name} is already using this code. Try again.\n")
    else:
        name = input("Enter Country Name:  ")
        name = name.title()
        countries[code] = name
        print(f"{name} was added.\n")

def delete(countries):
    code = input("Enter Country Code:  ")
    code = code.upper()
    if code in countries:
        name = countries.pop(code)
        print(f"{name} was deleted.\n")
    else:
        print("There is no country with that code.\n")

def main():
    countries = {"US": "United States","DE": "Germany","AT": "Austria"}

    main_menu()
    while True:
        command = input("Command: ")
        command = command.lower()
        if command == "view":
            view(countries)
        elif command == "add":
            add(countries)
        elif command == "del":
            delete(countries)
        elif command  == "exit":
            print("Bye")
            break
        else:
            print("Not a valid command. Please try again.\n")
        

if __name__ == "__main__":
    main()
    