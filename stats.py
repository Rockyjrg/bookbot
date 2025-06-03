def get_num_words(text):
    split_words = text.split()
    return len(split_words)

def get_each_char(text):
    count_dict = {}
    for char in text.lower():
        if char not in count_dict:
            count_dict[char] = 1
        else:
            count_dict[char] += 1
    return count_dict

def sort_on(dict):
    return dict["num"]

def sort_dict(dict):
    list_of_dicts = []
    for char in dict:
        if char.isalpha():
            num = dict[char]
            list_of_dicts.append({"char": char, "num": num})
    list_of_dicts.sort(reverse=True, key=sort_on)
    return list_of_dicts
