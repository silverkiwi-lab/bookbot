import sys
if len(sys.argv) !=2:
    print(f"Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    book_path = sys.argv[1]


from stats import stats
from stats import num_words
from stats import sorted_report
from stats import get_book_text

def main():
    #num_w = num_words()
    #phrase = f"{num_w} words found in the document"
    #print(phrase)

    
    text = get_book_text(book_path)
    report = sorted_report(text)
    words = num_words(text)
    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")
    for item in report:
        print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")

#def calling_stats():
    #call = stats
    #print(call)

main()
