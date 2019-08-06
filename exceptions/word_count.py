def count_words(file_name):
    """this function counts the number of words in a file"""
    try:
        with open(file_name) as file_object:
            lines = file_object.read()
    except FileNotFoundError:
        message = "sorry, the file " + file_name + " does not exist"
        print(message)
        #if you want to fail silently here, simply use 'pass'
    else:
        # count the number of words in the file
        words = lines.split()
        num_words = str(len(words))
        print("the file " + file_name + " has " + num_words + " words in it.")

file_names = ["alice", "mody", "prank"]
for file_name in file_names:
    count_words(file_name)