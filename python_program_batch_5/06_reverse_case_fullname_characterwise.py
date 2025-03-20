while True:
# Ask user for input
    name = input("Enter your full name (incorrect casing): ").strip()

    # Check if input is empty or invalid
    if name:
         break
    else:
        print("Invalid input, Enter your full name.")

# Swap the casing of characters