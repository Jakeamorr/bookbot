def get_word_count(str):
    return len(str.split())

def get_char_count(str):
    lowercased = str.lower()
    char_dict = {}
    for char in lowercased:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1

    return char_dict

def sort_key(dict):
    return dict["count"]

def sort_char_dict(char_dict):
    sorted_char_dicts = []
    for (k, v) in char_dict.items():
        if k.isalpha():
            sorted_char_dicts.append({"char": k, "count": v})
    sorted_char_dicts.sort(reverse=True, key=sort_key)
    return sorted_char_dicts

def print_report(char_dict, word_count, file_path):
    sorted_dict = sort_char_dict(char_dict)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for dict in sorted_dict:
        print(f"{dict['char']}: {dict['count']}")
    print("============= END ===============")


