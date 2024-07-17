def main():
    opened_text = open_text("books/frankenstein.txt")
    amount = counter(opened_text)
    chars = char_count(opened_text)
    sorted_list = sorter(chars)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{amount} words found in the document")
    print("")
    for d in sorted_list:
        for k, v in d.items():
            print(f"The '{k}' character was found {v} times")
    print("--- End report ---")

def sorter(d_list):
    dict_list = [{k: v} for k, v in d_list.items() if k.isalpha()]
    sorted_list = sorted(dict_list, key=lambda d: list(d.values())[0], reverse=True)
    return sorted_list

def counter(contents):
    words = contents.split()
    return len(words)

def open_text(path):
    with open(path) as f:
        return f.read()

def char_count(text):
    chars = {}
    lowcase_str = text.lower()
    for char in lowcase_str:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars
    
main()