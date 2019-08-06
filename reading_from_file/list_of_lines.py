file_name = "pi_digits"

with open(file_name) as file_objects:
    lines = file_objects.readlines()

for line in lines:
    print(line.rstrip())