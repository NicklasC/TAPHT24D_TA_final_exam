class KatalogPage:
    def __init__(self, page):
        self.page = page
        self.booklist_div = page.locator("div.catalog")
        self.a_book = page.get_by_text("❤️\"Hur man tappar bort sin TV")

    def a_book_is_visible(self):
        return self.a_book.is_visible()
