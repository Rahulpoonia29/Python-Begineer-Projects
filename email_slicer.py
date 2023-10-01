# Taking email input from user
email = input("Enter your Email")

# Slicing the email
details = email.split("@")

# printing the final details
print(f"Your username is {details[0]} and your provider is {details[1]}")
