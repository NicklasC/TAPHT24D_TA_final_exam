class LaggTillBokPage:
    def __init__(self, page):
        self.page = page
        self.titel = page.get_by_test_id("add-input-title")
        self.forfattare = page.get_by_test_id("add-input-author")

    def titel_is_visible(self):
        return self.titel.is_visible()

    def forfattare_is_visible(self):
        return self.forfattare.is_visible()

