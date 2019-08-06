import json
def add_favorite_number():
    """this function adds the number in the file"""
    file_name = "favorite_number_list.json"
    with open(file_name, "a") as file_object:
        favorite_number = input("please enter your favorite number: ")
        json.dump(favorite_number, file_object)
    return favorite_number

def get_favorite_number():
    """this function gets the number from the file"""
    file_name = "favorite_number_list.json"
    try:
        with open(file_name) as file_object:
            favorite_number = json.load(file_object)
    except FileNotFoundError:
        print("it seems that you haven't a list of favorite number yet.")
        add_favorite_number()
    else:
        print(favorite_number)

get_favorite_number()