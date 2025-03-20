while True:
    # Ask user to input their name with leading spaces
    name = input("Input your full name (put spaces at the beginning): ")

    # Check if input has no leading spaces
    if name == name.lstrip():
        print("Input has no spaces at the beginning. Please try again.")
        continue  # Ask for input again

    # Print name without leading spaces
    print(name.lstrip())
    break  
