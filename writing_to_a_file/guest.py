file_name = "guest_list"

with open(file_name, "a") as file_object:
    index = 0
    while index <3:
        guest_name = input("please enter your name")
        file_object.write(guest_name.title() + "\n")
        print("thank you for your coming")
        index += 1