def unit_converter():
    print("1. KM to Miles")
    print("2. KG to Pounds")

    choice = input("Enter choice: ")

    value = float(input("Enter value: "))

    if choice == "1":
        print("Miles:", value * 0.621371)

    elif choice == "2":
        print("Pounds:", value * 2.20462)

    else:
        print("Invalid choice")