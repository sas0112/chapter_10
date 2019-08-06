import json
def add_user_name():
    """this function adds new user name into the file"""
    user = input("what is your name?")
    file_name = "user_list.json"
    with open(file_name, "a") as file_object:
        json.dump(user.title(), file_object)
        print("we will remember you when you come back, " + user + "!")

def get_user_name():
    """this function loads user name from the file"""
    file_name = "user_list.json"
    try:
        with open(file_name) as file_object:
            user_name = json.load(file_object)
    except FileNotFoundError:
        print("it seems that you haven't created the file yet")
        add_user_name()
    else:
        print("welcome back, " + user_name)

get_user_name()