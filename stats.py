def get_book_text(filepath):
        with open(filepath) as f:
                text = f.read()
        return text

def num_words(text):
#	from main import book_path
	words = text.split()
	word_count = len(words)
	return word_count
	

def stats(text):
	#from main import book_path #book_path)
	lower_words = text.lower()
	count = {}
	for x in lower_words:
		if x in count and x.isalpha():
			count[x] +=1
		elif x not in count and x.isalpha():
			count[x]=1
	return (count)

def sort_on(items):
	return items["num"]

def sorted_report(text):
	counts = stats(text)
	sort_count = [
		{"char": ch, "num": n} for ch, n in counts.items()
		if ch.isalpha()]
	sort_count.sort(reverse=True, key=sort_on)
	return sort_count


#books/frankenstein.txt - for reference this is how filepath is stored.
