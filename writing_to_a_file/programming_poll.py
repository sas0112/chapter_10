file_name = "reasons_to_program"

with open(file_name, "a") as file_object:
    response = input("why you want to do programming?")
    file_object.write(response + "\n")
