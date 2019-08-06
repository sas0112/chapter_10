file_name = "pi_digits"

with open(file_name) as file_objects:
    lines = file_objects.readlines()

pi_string = ""
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))