def word_counter(file):
    with open(file) as f:
        words = f.read()
        split = words.split()
        # print (f"{len(split)} words found in the document")
        return len(split)
        
def letter_counter(file):
    letter_count = {}
    with open(file) as f:
        words = f.read()
        words = words.lower()
        for letter in words:
            if letter in letter_count:
                letter_count[letter] += 1
            else:
                letter_count[letter] = 1
        # print(letter_count)
        return letter_count

def sorter(file):
    word_count = word_counter(file)
    letter_count = letter_counter(file)
    letter_list = [] # Empty list for sorting the letter_count dictionary
    print(f"Analyzing book found at {file}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words") # get word count from the word_counter function
    print("--------- Character Count -------")
    for letter, num in letter_count.items(): # Loop over items in letter_count dictionary
        letter_list.append({"char": letter, "num": num}) # Create a tuple for the letter_list list
    letter_list.sort(key=lambda x: x['num'], reverse=True) # Sort the letter_list list, in reverse from high to low
    for letter in letter_list:
        if letter["char"].isalpha():
            print(f"{letter['char']}: {letter['num']}") # Print the list dictionary, in the style of 'char': 'num'
    print("============= END ===============")


# def sorter(file):
#     word_count = word_counter(file)
#     letter_count = letter_counter(file)
#     # letter_count.sort(reverse=True, key=dict_sorter)
#     for letter in letter_count:
#         if letter.isalpha() == True:
#             print(letter)

# def sorter(file):
#     print("============ BOOKBOT ============")
#     print(f"Analyzing book found at {file}...")
#     print("----------- Word Count ----------")
#     print(f"Found {word_counter(file)} total words")
#     print("--------- Character Count -------")
    