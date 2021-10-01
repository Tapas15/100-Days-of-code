import requests

USERS_ENDPOINT = "https://v2-api.sheety.co/95d949299830cb0ec6024f9a48eab1b1/flightDeals/users"

print("Welcome to Angela's Flight Club.")
print("We find the best flight deals and email you.")
f_name = input("What is your first name?\n")
l_name = input("What is your last name?\n")
email = input("What is your email?\n")
email_validation = input("Type your email again.\n")

while email != email_validation:
    print("That's not right, let's try again:")
    email = input("What is your email?\n")
    email_validation = input("Type your email again.\n")

user_data = {
    "user": {
        "firstName": f_name,
        "lastName": l_name,
        "email": email,
    }
}

response = requests.post(
    url=USERS_ENDPOINT,
    json=user_data,
)
# print(response.text)
if response.status_code == 200:
    print("Success! Your email has been added, look forwards to some amazing flight deals!")
else:
    print("There was an issue, please try again later.")
