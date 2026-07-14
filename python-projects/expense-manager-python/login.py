users = {
"jeferson":"1234"
}


username = input(
"Username: "
)


password = input(
"Password: "
)


if username in users:

    if users[username] == password:

        print("Login successful")

    else:

        print("Wrong password")

else:

    print("User not found")
