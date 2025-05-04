from behave import given, when, then
from playwright.sync_api import expect

from tests.pages.katalog_page import KatalogPage

@then('the book {titel} should show on Katalog page')
def step_impl(context, titel):
    page = KatalogPage(context.page)
    page.book_displays(titel)
