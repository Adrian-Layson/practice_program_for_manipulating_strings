while True:
    # Ask user for input or their fullname
    name = input("Enter your full name: ").strip()

    # Check for any invalid input
    if name:
        break
    else:
        print("Invalid input. Enter your full name.")

# Print the input in uppercase
print(name.upper())