from behave import given, when, then
from playwright.sync_api import expect

from tests.pages.lagg_till_bok_page import LaggTillBokPage

@then('the lagg till ny bok button is {expected_status}')
def step_impl(context,expected_status):
    page = LaggTillBokPage(context.page)
    if expected_status == "disabled":
         expect(page.lagg_till_ny_bok_button).to_be_disabled()
         expect(page.lagg_till_ny_bok_button).to_be_visible()
    elif expected_status == "enabled":
        expect(page.lagg_till_ny_bok_button).to_be_enabled()
        expect(page.lagg_till_ny_bok_button).to_be_visible()
    else:
        raise AssertionError(f"Status must be defined, but it was not. I got '{expected_status}' as value.")

@when('I type {text} in the book titel field')
def step_impl(context,text):
    page = LaggTillBokPage(context.page)
    page.titel.fill(text)

@when('I type {text} in the book författare field')
def step_impl(context,text):
    page = LaggTillBokPage(context.page)
    page.författare.fill(text)

@given('I create a book with titel {title} made by author {author_name}')
@when('I create a book with titel {title} made by author {author_name}')
def step_impl(context,title, author_name):
    page = LaggTillBokPage(context.page)
    page.titel.fill(title)
    page.författare.fill(author_name)
    page.lagg_till_ny_bok_button.click()

@then('{field} field should be empty')
def step_impl(context,field):
    page = LaggTillBokPage(context.page)
    if field == "titel":
        element = page.titel
    elif field == "författare":
        element = page.författare
    else: raise ValueError(f"Unknown field: {field}")

    expect(element).to_be_visible()
    expect(element).to_have_value('')

