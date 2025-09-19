from stats import (
	count_words,
	count_chars,
	dict_to_sorted_list
	)
import sys

def main():
	if len(sys.argv) != 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	file_path = sys.argv[1]
	text = get_book_text(file_path)
	num_words = count_words(text)
	char_dict = count_chars(text)
	sorted_char_dict = dict_to_sorted_list(char_dict)
	print_report(file_path, num_words, sorted_char_dict)

def get_book_text(file_path):
        with open(file_path) as file:
                return file.read()

def print_report(file_path, num_words,sorted_char_dict):
	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {file_path}...")
	print("----------- Word Count ----------")
	print(f"Found {num_words} total words")
	print("--------- Character Count -------")
	for el in sorted_char_dict:
		if not el["char"].isalpha():
			continue
		print(f"{el["char"]}: {el["num"]}") 
	print("============= END ===============")

main()
