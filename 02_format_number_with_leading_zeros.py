while True:
# Ask user to input a number (0-1000)
    try:
        number = int(input("Enter a number from 0-1000: "))

# # Check if number is within range
        if 0 <= number <= 1000:
            break
        else:
            print("Invalid Input, Enter a number between 0 and 1000.")
    except ValueError:
        print("Invalid Input, Enter a valid integer.")
    
# Print the number in 6-digit format with leading zeros
