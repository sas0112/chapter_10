import json
"""load the username, if it has been stored previously
otherwise, prompt for the username and store it"""

def get_stored_username():
    """greet user by name"""
    file_name = "user_list.json"
    try:
        with open(file_name) as file_object:
            user_names = json.load(file_object)
    except FileNotFoundError:
        return None
    else:
        return user_names

def get_new_username():
    """prompt for a new username"""
    user_names = input("what is your name?")
    file_name = "user_list.json"
    with open(file_name, "a") as file_object:
        json.dump(user_names.title(), file_object)
    return user_names

def greet_user():
    """greet the user by name"""
    user_names = get_stored_username()
    if user_names:
        print("welcome back, " + user_names)
    else:
        user_names = get_new_username()
        print("we will remember you when you come back, " + user_names + "!")

greet_user()