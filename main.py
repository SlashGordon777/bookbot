def sort_on(dict):
    return dict["count"]

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        lowered_file_content = file_contents.lower()
        lowered_file_content.split()

        unique_letters_with_count = {}

        for i in lowered_file_content:
            if i.isalpha() and i not in unique_letters_with_count:
                unique_letters_with_count[i] = 1
            elif i.isalpha():
                unique_letters_with_count[i] += 1

        unique_letters_count_list = [{'char': k, 'count': v} for k, v in unique_letters_with_count.items()]

        unique_letters_count_list.sort(reverse=True, key=sort_on)

        words_count = (len(file_contents.split()))

        print("--- Begin report of books/frankenstein.txt --")
        print(f"{words_count} words found in the document")
        print("\n")
        for i in range(0, len(unique_letters_count_list)):
            print(f"The '{unique_letters_count_list[i]['char']}' character was found {unique_letters_count_list[i]['count']} times")
        print("--End report--")

main()
