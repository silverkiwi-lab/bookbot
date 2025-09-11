def get_book_text(filepath):
        with open(filepath) as f:
                text = f.read()
        return text

def main():
	from main import book_path
	text = get_book_text(book_path)
	words = text.split()
	num_words = len(words)
	phrase = f"{num_words} words found in the document"
	print(phrase)

def stats():
	from main import book_path
	text = get_book_text(book_path)
	lower_words = text.lower()
	count = {}
	for x in lower_words:
		if x in count and x.isalpha():
			count[x] +=1
		elif x not in count and x.isalpha():
			count[x]=1
	print (count)

def sorted_report(count)
	return count[""]
	print(f"============ BOOKBOT ============
Analyzing book found at {book_path}...
----------- Word Count ----------
Found {num_words} total words
--------- Character Count -------
{count}
============= END ===============")

main()
stats()

#books/frankenstein.txt