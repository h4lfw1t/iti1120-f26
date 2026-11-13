from datetime import datetime


def create_books_2Dlist(file_name: str) -> list:
    """
    Return a list containing one sublist for each book in file_name.
    Each sublist contains the date, title, author, publisher, and category,
    in that order.

    :param file_name: the name of the file containing the book data
    :type file_name: str
    :return: a list of books, where each book is represented as a list of its attributes
    :rtype: list
    """
    books = []

    with open(file_name) as book_file:
        for line in book_file:
            title, author, publisher, date, category = (
                field.strip() for field in line.rstrip('\n').split('\t')
            )
            # Could format dates using `date.replace('/', '-')` or `date.split('/')` and then
            # reformatting, but using datetime is more robust.
            date = datetime.strptime(date, '%m/%d/%Y').date().isoformat()
            books.append([date, title, author, publisher, category])

    return books


def search_by_year(books: list, year1: int, year2: int):
    """
    Print the books whose first-best-seller date falls between year1 and
    year2, inclusive.

    :param books: a list of books, where each book is represented as a list of its attributes
    :type books: list
    :param year1: the start year for the search range
    :type year1: int
    :param year2: the end year for the search range
    :type year2: int
    """
    for book in books:
        year = int(book[0][:4])
        if year1 <= year <= year2:
            print(book)
