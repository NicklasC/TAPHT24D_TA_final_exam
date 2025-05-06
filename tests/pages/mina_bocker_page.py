class MinaBockerPage:
    def __init__(self, page):
        self.page = page

        self.no_favorites_selected_text = page.locator("text=När du valt, kommer dina favoritböcker att visas här.")
        self.your_favorites_text = page.locator("text=Dina favoriter:")

    def get_book_description(page, book_name):
        dynamic_book = page.page.get_by_test_id(f"fav-{book_name}")
        return dynamic_book
