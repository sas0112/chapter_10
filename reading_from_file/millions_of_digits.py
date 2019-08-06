file_name = "one_million_number"
with open(file_name) as file_object:
    lines = file_object.readlines()

graham_string = ""
for line in lines:
    graham_string += line

print(graham_string[:52])
print(len(graham_string))