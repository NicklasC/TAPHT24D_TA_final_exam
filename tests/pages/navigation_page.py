class NavigationPage:
    def __init__(self, page):
        self.page = page

        self.katalog_button = page.locator("data-testid=catalog")
        self.lagg_till_bok_button = page.locator("data-testid=add-book")
        self.mina_bocker_button = page.locator("data-testid=favorites")
