from playwright.sync_api import expect


class KatalogPage:
    def __init__(self, page):
        self.page = page
        self.booklist_div = page.locator("div.catalog")
        self.a_book = page.get_by_text("❤️\"Hur man tappar bort sin TV")

    def get_all_books_list(self):
        books = self.page.locator('.book').all()
        all_books_data=[]
        for book in books:

            book_text = book.inner_text()
            book_text = book_text.replace('❤️','').strip()#Remove heart

            titel =book_text[0:book_text.rfind('"')+1]
            author = book_text[book_text.rfind('"') + 1:].strip(", ")

            #Find out if the book is favorite and also test id
            star_element = book.locator('.star')
            book_test_id = star_element.get_attribute('data-testid')
            star_classes = star_element.get_attribute('class')
            is_favorite = 'selected' in star_classes

            all_books_data.append({
                "book_test_id": book_test_id,
                "titel": titel,
                "author": author,
                "is_favorite": is_favorite
            })
        return all_books_data

    def a_book_is_visible(self):
        return self.a_book.is_visible()

    def count_books(self):
        books=self.get_all_books_list()
        return books.count()

    def book_displays(self, titel):
        book = self.page.get_by_test_id(f"star-{titel}")
        expect(book).to_be_visible()

