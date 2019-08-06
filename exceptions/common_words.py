file_name = "gutenberg_projects"

with open(file_name,'r', encoding='UTF-8') as file_objects:
    contents = file_objects.read()
    common_words = contents.lower().count("the")
    print("the common word: 'the' appears " + str(common_words) + " times in the text")