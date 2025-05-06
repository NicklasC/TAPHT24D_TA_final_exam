from behave import then
from playwright.sync_api import expect

from tests.pages.mina_bocker_page import MinaBockerPage


@then('the no favorites selected text should show')
def step_impl(context):
    page = MinaBockerPage(context.page)
    expect(page.no_favorites_selected_text).to_be_visible()


@then('the no favorites selected text should not show')
def step_impl(context):
    page = MinaBockerPage(context.page)
    expect(page.no_favorites_selected_text).to_be_hidden()


@then('the dina favoriter text should show')
def step_impl(context):
    page = MinaBockerPage(context.page)
    expect(page.your_favorites_text).to_be_visible()


@then('the dina favoriter text should not show')
def step_impl(context):
    page = MinaBockerPage(context.page)
    expect(page.your_favorites_text).to_be_hidden()


@then('the book {expected_book} should be listed')
def step_impl(context, expected_book):
    page = MinaBockerPage(context.page)
    book_that_should_be_listed = page.get_book_description(expected_book)
    expect(book_that_should_be_listed).to_be_visible()


@then('the book {expected_book} should not be listed')
def step_impl(context, expected_book):
    page = MinaBockerPage(context.page)
    book_that_should_be_listed = page.get_book_description(expected_book)
    expect(book_that_should_be_listed).to_be_hidden()
