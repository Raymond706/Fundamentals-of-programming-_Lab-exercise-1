from datetime import date

# Ask the user for name and birth year
name = input("Enter your name: ")
birth_year = int(input("Enter your birth year: "))

# Get the current year
current_year = date.today().year

# Calculate age
age = current_year - birth_year

# Print the result
print(f"Hello {name}, you are {age} years old.")
