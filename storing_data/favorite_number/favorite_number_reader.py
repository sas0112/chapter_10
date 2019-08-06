import json

file_name = "favorite_number_list.json"

with open(file_name) as file_object:
    favorite_number = json.load(file_object)
    print(favorite_number)