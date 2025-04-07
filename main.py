from stats import get_num_words
import sys

def sort_on(item):
    return item["count"]

def extract_book_text(text):
    # Markers used in many Project Gutenberg texts.
    start_marker = '*** START OF THIS PROJECT GUTENBERG EBOOK'
    end_marker = '*** END OF THIS PROJECT GUTENBERG EBOOK'

    start = text.find(start_marker)
    end = text.find(end_marker)

    if start != -1 and end != -1:
        # Move to the end of the header line.
        start = text.find('\n', start) + 1
        return text[start:end]
    return text

def main():
    if len(sys.argv) != 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)

    with open(sys.argv[1]) as f:
        file_contents = f.read()

    # Remove Project Gutenberg header and footer.
    file_contents = extract_book_text(file_contents)

    # Count words using the provided function.
    words_count = get_num_words(file_contents)

    # Convert text to lowercase for letter counting.
    lowered_file_content = file_contents.lower()

    unique_letters_with_count = {}
    for char in lowered_file_content:
        if char.isalpha():
            if char not in unique_letters_with_count:
                unique_letters_with_count[char] = 1
            else:
                unique_letters_with_count[char] += 1

    unique_letters_count_list = [{'char': k, 'count': v}
                                 for k, v in unique_letters_with_count.items()]
    unique_letters_count_list.sort(reverse=True, key=sort_on)

    print(f"--- Begin report of {sys.argv[1]} --")
    print(f"{words_count} words found in the document")
    print("\n")
    for item in unique_letters_count_list:
        print(f"The '{item['char']}' character was found {item['count']} times")
    print("--End report--")

if __name__ == "__main__":
    main()
