file_name = "one_million_number"

with open(file_name) as file_object:
    lines = file_object.readlines()

graham = ""
for line in lines:
    graham += line

birthday = 981107
birthday = str(birthday)

if birthday in graham:
    print("Your birthday appears in the first 250 thousand digits of graham's number")
else:
    print("Your birthday seems not in the first 250 thousand digits of graham's number")