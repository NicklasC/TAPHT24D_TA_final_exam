from behave import given, when, then
from playwright.sync_api import expect

from tests.pages.katalog_page import KatalogPage


@then('the book {expected_titel} with forfattare {expected_forfattare} should show on Katalog page')
def step_impl(context, expected_titel, expected_forfattare):
    page = KatalogPage(context.page)

    books = page.get_all_books_list()

    book_found = False
    for book in books:
        if book["titel"] == expected_titel and book["author"] == expected_forfattare:
            book_found = True
            break
    if not book_found:
        raise AssertionError(
            f"The book '{expected_titel}' with forfattare '{expected_forfattare}' was not found on the Katalog page.")

@then('Number of displayed books is {expected_number}')
@given('Number of displayed books is {expected_number}')
def step_impl(context, expected_number):
    page = KatalogPage(context.page)
    number_of_displayed_books = page.count_books()
    assert number_of_displayed_books == int(expected_number), (
    f"Expected {expected_number} books, but found {number_of_displayed_books} displayed on the Katalog page."
)

