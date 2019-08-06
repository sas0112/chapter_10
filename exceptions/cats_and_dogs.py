file_name_1 = "cats"
file_name_2 = "dogs"

print("\n" + "here are the dogs' name:")
try:
    with open(file_name_1) as file_object_1:
        cats_name = file_object_1.readlines()
except FileNotFoundError:
    pass
else:
    for cat_name in cats_name:
        print(cat_name.rstrip())

print("\n" + "here are the cats' name:")
try:
    with open(file_name_2) as file_object_2:
        dogs_name = file_object_2.readlines()
except FileNotFoundError:
    print("it seems that the file " + file_name_1 + " doesn't exist")
else:
    for dog_name in dogs_name:
        print(dog_name.rstrip())

