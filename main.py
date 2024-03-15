def count_letters(file_contents):
    text = file_contents.lower()
    lower_counts = {}
    for i in text:
        if i.isalpha():
            if i in lower_counts:
                lower_counts[i] += 1
            else:
                lower_counts[i] = 1
    return(lower_counts)

def report_sort(lower_counts):
    count_list = []

    for character, count in lower_counts.items():
        characters_dict = {"character": character, "count": count}
        count_list.append(characters_dict)
    
    count_list.sort(key=lambda x: x['count'], reverse=True)
    #print(count_list)

    for item in count_list:
        print(f"The '{item['character']}' character was found {item['count']} times")

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    letter_counts = count_letters(file_contents)
    #sorted_counts = sorted(letter_counts.items())
    report_sort(letter_counts)

if __name__ == "__main__":
    main()