class LaggTillBokPage:
    def __init__(self, page):
        self.page = page
        self.titel = page.get_by_test_id("add-input-title")
        self.författare = page.get_by_test_id("add-input-author")
        self.lagg_till_ny_bok_button = page.get_by_test_id("add-submit")

    def titel_is_visible(self):
        return self.titel.is_visible()

    def forfattare_is_visible(self):
        return self.författare.is_visible()
