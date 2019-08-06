file_name = "learning_python_feeling"

with open(file_name) as file_objects:
    lines_whole = file_objects.read()
    print(lines_whole.replace("python", "java") + "\n")

with open(file_name) as file_objects:
    line_by_line = file_objects.readlines()

for line in line_by_line:
    line = line.replace("python", "java")
    print(line.rstrip())
print("")

with open(file_name) as file_objects:
    for line in file_objects:
        line = line.replace("python", "java")
        print(line.rstrip())

