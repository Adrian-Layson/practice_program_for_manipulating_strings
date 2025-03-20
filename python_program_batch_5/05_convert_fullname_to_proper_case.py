while True:
# Ask user to input their full name in incorrect casing
    name = input("Enter your full name (incorrect casing): ").strip()

# Check if input is empty
    if name:
        break
    else:
        print("Invalid input, Enter your full name.")

# Print the name in proper casing
print(name.title())
