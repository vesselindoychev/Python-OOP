import unittest

from Exam_10_April_2021.project import Library


class Test(unittest.TestCase):
    name = 'Author'

    def setUp(self) -> None:
        self.library = Library(self.name)

    def test_init(self):
        self.assertEqual(self.name, self.library.name)
        self.assertEqual({}, self.library.books_by_authors)
        self.assertEqual({}, self.library.readers)

    def test_name__when_name_is_empty__expect_exception(self):
        with self.assertRaises(ValueError) as context:
            self.library.name = ''
        self.assertEqual("Name cannot be empty string!", str(context.exception))

    def test_name__when_is_valid(self):
        self.assertEqual(self.name, self.library.name)

    def test_add_book_method__expect_author_and_title_to_be_added(self):
        author = 'Author'
        title = 'Title1'
        title2 = 'Title2'

        self.library.add_book(author, title)
        self.library.add_book(author, title)
        self.library.add_book(author, title2)
        self.assertEqual(1, len(self.library.books_by_authors))
        self.assertTrue(author in self.library.books_by_authors)
        self.assertTrue(title in self.library.books_by_authors[author])
        self.assertTrue(title2 in self.library.books_by_authors[author])
        self.assertEqual([title, title2], self.library.books_by_authors[author])
        self.assertEqual(2, len(self.library.books_by_authors[author]))

    def test_add_reader_method__when_reader_is_already_added__expect_exception(self):
        reader_name = 'Pesho'
        self.library.add_reader(reader_name)
        result = self.library.add_reader(reader_name)

        self.assertEqual(f"{reader_name} is already registered in the {self.library.name} library.", result)

    def test_add_reader_method__should_add_reader(self):
        reader_name = 'Pesho'
        self.library.add_reader(reader_name)

        self.assertEqual(1, len(self.library.readers))
        self.assertEqual([], self.library.readers[reader_name])
        self.assertTrue(reader_name in self.library.readers)

    def test_rent_a_book_method__when_reader_is_not_registered__expect_error_massage(self):
        reader_name = 'Pesho'
        book_author = 'Author'
        book_title = 'Title'

        result = self.library.rent_book(reader_name, book_author, book_title)
        self.assertEqual(f"{reader_name} is not registered in the {self.library.name} Library.", result)
        self.assertTrue(reader_name not in self.library.readers)

    def test_rent_a_book_method__when_author_is_not_registered__expect_error_massage(self):
        reader_name = 'Pesho'
        book_author = 'Author'
        book_title = 'Title'

        self.library.add_reader(reader_name)

        result = self.library.rent_book(reader_name, book_author, book_title)
        self.assertEqual(f"{self.library.name} Library does not have any {book_author}'s books.", result)
        self.assertEqual(0, len(self.library.books_by_authors))
        self.assertTrue(book_author not in self.library.books_by_authors)

    def test_rent_a_book_method__when_title_is_not_registered__expect_error_message(self):
        reader_name = 'Pesho'
        book_author = 'Author'
        book_title = 'Title'

        self.library.add_reader(reader_name)
        self.library.add_book(book_author, 'JS Advanced')

        result = self.library.rent_book(reader_name, book_author, book_title)
        self.assertEqual(f"""{self.library.name} Library does not have {book_author}'s "{book_title}".""", result)
        self.assertTrue(book_title not in self.library.books_by_authors[book_author])

    def test_rent_a_book__expect_correct_result(self):
        reader_name = 'Pesho'
        book_author = 'Author'
        book_title = 'Title'
        second_book_title = 'Title2'

        self.library.add_reader(reader_name)
        self.library.add_book(book_author, book_title)
        self.library.add_book(book_author, second_book_title)

        self.library.rent_book(reader_name, book_author, book_title)
        self.assertEqual([{book_author: book_title}], self.library.readers[reader_name])
        self.assertTrue({book_author: book_title} in self.library.readers[reader_name])

        self.assertTrue(book_title not in self.library.books_by_authors[book_author])
        self.assertTrue(second_book_title in self.library.books_by_authors[book_author])
        self.assertEqual(1, len(self.library.books_by_authors[book_author]))


if __name__ == '__main__':
    unittest.main()