import sys
if len(sys.argv) !=2:
    print(f"Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    book_path = sys.argv[1]


from stats import sorted_report
