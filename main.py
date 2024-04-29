def count(file):
    words_list = file.split()
    count = len(words_list)
    return count

def count_characters(file ):
    lowerFile  = file.lower()
    dict_characters = {}
    for character in lowerFile:
        if character in dict_characters:
            dict_characters[character]  += 1
        else:
            dict_characters[character] = 1
    return dict_characters

def report(file, path):
    print("---- Begin report of " + path + "----")
    count_words = count(file)
    print( f"{count_words} words found in the document")
    char_count = count_characters(file)
    sorted_char_count =  sorted(char_count.items(), key=lambda x:x[1], reverse=True) 
    for char in sorted_char_count:
       character = char[0]
       amount_char = char[1]
       print(f"The {character} character was found {amount_char} times")        

def get_file(path):
    with open(path) as f :
        f = f.read()
        return f 

def main(path):
    file = get_file(path)
    report(file,path)

main("./books/frankenstein.txt")