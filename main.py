def main():
    path = "books/frankenstein.txt"
    with open(path) as f:
        book = f.read()
    lowered_string = book.lower()

    word_num(book)
    char_num(lowered_string)

def word_num(book):
    words = len(book.split())
    print(f"{words} words in document")

def sort_on(dict):
    return dict["num"]

def char_num(lowered_string):
    text = {}
    
    for i in lowered_string:
        if i.isalpha():
            if (i in text):
                text[i] = text[i] + 1
            else:
                text[i] = 1

    dict_list = []
    for char, count in text.items():
        char_dict = {"char" : char, "num" : count}
        dict_list.append(char_dict)

    dict_list.sort(reverse = True, key = sort_on)
    
    for item in dict_list:
        print(f"The '{item['char']}' character was found {item['num']} times")
    
main()