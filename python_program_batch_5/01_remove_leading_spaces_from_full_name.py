while True:
# Ask user to input their name with leading spaces
    name = input("Input your full name (put spaces at the beginning): ")

# Check if input has leading spaces
    if name != name.lstrip():

    print("Input has no spaces at the beginning")

# Print name without leading spaces