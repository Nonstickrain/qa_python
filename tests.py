from main import BooksCollector

class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        assert len(collector.get_books_rating()) == 2

    def test_add_new_book_add_same_book(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Гордость и предубеждение и зомби')
        assert  len(collector.get_books_rating()) == 1
    def test_set_book_rating_set_avarege_rating(self):
        collector = BooksCollector()
        collector.add_new_book('Сантехник')
        collector.set_book_rating('Сантехник', 5)
        assert collector.books_rating['Сантехник'] == 5
    def test_set_book_rating_set_default_rating(self):
        collector = BooksCollector()
        collector.add_new_book('Generation P')
        assert collector.books_rating['Generation P'] == 1
    def test_set_book_rating_set_min_invalid_rating(self):
        collector = BooksCollector()
        collector.add_new_book('По кругу на корпоративе')
        collector.set_book_rating('По кругу на корпоративе', -3)
        assert collector.books_rating['По кругу на корпоративе'] == 1

    def test_set_book_rating_set_max_invalid_rating(self):
        collector = BooksCollector()
        collector.add_new_book('По кругу на вписке')
        collector.set_book_rating('По кругу на вписке', 23)
        assert collector.books_rating['По кругу на вписке'] == 1
    def test_add_book_in_favorites_add_one_book(seld):
        collector = BooksCollector()
        collector.add_new_book('Соната')
        collector.add_book_in_favorites('Соната')
        assert len(collector.favorites) == 1
    def test_add_book_in_favorites_add_not_existing_book(seld):
        collector = BooksCollector()
        collector.add_book_in_favorites('Соната')
        assert len(collector.favorites) == 0
    def test_add_book_in_favorites_add_same_book(seld):
        collector = BooksCollector()
        collector.add_new_book('Соната')
        collector.add_book_in_favorites('Соната')
        collector.add_book_in_favorites('Соната')
        assert len(collector.favorites) == 1
    def test_delete_book_from_favorites_delete_one_book_from_favorities(seld):
        collector = BooksCollector()
        collector.add_new_book('Соната')
        collector.add_book_in_favorites('Соната')
        collector.delete_book_from_favorites('Соната')
        assert len(collector.favorites) == 0
