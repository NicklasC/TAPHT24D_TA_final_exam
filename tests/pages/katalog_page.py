from playwright.sync_api import expect


class KatalogPage:
    def __init__(self, page):
        self.page = page
        self.booklist_div = page.locator("div.catalog")
        self.a_book = page.get_by_text("❤️\"Hur man tappar bort sin TV")

    def get_all_books(self):
        books = self.page.locator('.book').all()
        return books

    def a_book_is_visible(self):
        return self.a_book.is_visible()

    def count_books(self):
        return self.booklist_div.locator("div.book").count()

    def book_displays(self, titel):
        book = self.page.get_by_test_id(f"star-{titel}")
        expect(book).to_be_visible()
