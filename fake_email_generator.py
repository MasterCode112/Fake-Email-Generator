import random
import string
from colorama import Fore, init
import pyfiglet

# Initialize colorama
init(autoreset=True)

# Use pyfiglet for large font text
ascii_banner = pyfiglet.figlet_format("MasterCode Fake Email Generator")

def generate_random_email(length=7):
    # Generate a random string of letters and digits
    characters = string.ascii_lowercase + string.digits
    random_string = ''.join(random.choice(characters) for _ in range(length))
    # Return the email address
    return f"{random_string}@gmail.com"

def generate_emails(count):
    emails = []
    for _ in range(count):
        email = generate_random_email()
        emails.append(email)
    return emails

# Display log message in red with large font
print(Fore.RED + ascii_banner)

# Ask user to enter the number of emails to generate
try:
    number_of_emails = int(input("Enter the number of emails to generate: "))
    if number_of_emails <= 0:
        raise ValueError("Number of emails should be a positive integer.")
except ValueError as e:
    print(f"Invalid input: {e}")
else:
    # Generate the requested number of emails
    email_list = generate_emails(number_of_emails)

    # Write the emails to a file
    with open('random_emails.txt', 'w') as file:
        for email in email_list:
            file.write(f"{email}\n")

    print(f"{number_of_emails} emails generated and saved to 'random_emails.txt'.")
