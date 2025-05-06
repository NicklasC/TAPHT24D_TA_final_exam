from asyncio import wait_for

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


@when('the book {expected_titel} has status {expected_status}')
@then('the book {expected_titel} has status {expected_status}')
@given('the book {expected_titel} has status {expected_status}')
def step_impl(context, expected_titel, expected_status):
    page = KatalogPage(context.page)
    all_books_data = page.get_all_books_list()
    expected_status = expected_status.lower()

    for book in all_books_data:
        if book["titel"] == expected_titel:
            if expected_status == "favorite":
                assert book["is_favorite"] == True, (
                    f"The book '{expected_titel}' should be marked as favorite, but it is not.")
            elif expected_status == "not favorite" or expected_status == "non-favorite" or expected_status == "not-favorite" or expected_status == "nonfavorite":
                assert book["is_favorite"] == False, (
                    f"The book '{expected_titel}' should not be marked as favorite, but it is.")
            else:
                raise AssertionError(
                    f"Expected_status must be defined, but it was not. I got '{expected_status}' as value.")
            return
    raise AssertionError(f"The book '{expected_titel}' was not found on the Katalog page.")


@given('I click on the book {expected_titel}')
@when('I click on the book {expected_titel}')
def step_impl(context, expected_titel):
    page = KatalogPage(context.page)
    page.click_book(expected_titel)
