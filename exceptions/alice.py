file_name = "alice"

try:
    with open(file_name) as file_object:
        lines = file_object.read()
except FileNotFoundError:
    message = "sorry, the file " + file_name + " does not exist"
    print(message)
else:
    #count the number of words in the file
        words = lines.split()
        num_words = str(len(words))
        print("the file " + file_name + " has " + num_words + " words in it.")