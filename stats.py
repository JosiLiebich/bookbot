def count_words(text):
        word_list = text.split()
        return len(word_list)

def count_chars(text):
	counted = {}
	lowercase_text = text.lower()
	words = lowercase_text.split()
	for word in words:
		for char in word:
			amount = 1
			if char in counted:
				amount += counted[char]
			counted[char] = amount
	return counted 

def sort_on(items):
	return items["num"]

def dict_to_sorted_list(counted):
	list = []
	for el in counted:
		new_dic = {}
		val = counted[el]
		new_dic["char"] = el
		new_dic["num"] = val
		list.append(new_dic)
	list.sort(reverse=True, key=sort_on)
	return list	
