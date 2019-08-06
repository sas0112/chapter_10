file_name = "one_million_number"
index = 0
grahams_number = 3

while index <= 12:
    grahams_number = grahams_number ** 3
    index += 1
grahams_number = str(grahams_number)
print(len(grahams_number))

with open(file_name, "w") as file_object:
    file_object.write(grahams_number)
