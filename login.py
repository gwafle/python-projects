def login():
    # Hardcoded valid username and password (modify these)
    validUsername = "gracewafle"
    validPassword = "myPass0414"

    # Get user input for username and password
    # Convert the entered username to lowercase or uppercase by using a method for case-insensitive comparison
    # Check if the entered username and password match the valid credentials
    # Call the function to check credentials

username = input("Please Insert Your Username:")
password = input("Please Insert Your Password:")
username = username.lower()
if username == "gracewafle" and password == "myPass0414":
    print ("You Have Logged In.")
else:
    print("Username or Password don't match.")

login()
