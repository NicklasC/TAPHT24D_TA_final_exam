import time

from behave import given, when, then
from tests.pages.navigation_page import NavigationPage
from tests.pages.katalog_page import KatalogPage
from tests.pages.lagg_till_bok_page import LaggTillBokPage


@given('I am at the start page')
def step_impl(context):
    context.page.goto(f'https://tap-ht24-testverktyg.github.io/exam-template/')


@then('I navigate to the "{page_name}" page')
@given('I navigate to the "{page_name}" page')
def step_impl(context, page_name):
    time.sleep(1)
    page_name = page_name.lower()
    page = NavigationPage(context.page)
    if page_name == "katalog":
        page.katalog_button.click()
    elif page_name == "lägg till bok":
        page.lagg_till_bok_button.click()
    elif page_name == "mina böcker":
        page.mina_bocker_button.click()
    else:
        raise AssertionError(f"Page name must be defined, but it was not. I got '{page_name}' as value.")


@then('I should be on the "{expected_page}" page')
def step_impl(context, expected_page):
    expected_page = expected_page.lower()
    if expected_page == "katalog":
        page = KatalogPage(context.page)
        if page.a_book_is_visible():
            pass
        else:
            raise AssertionError(f"A book is not visible on the page.")

    elif expected_page == "lägg till bok":
        page = LaggTillBokPage(context.page)
        if page.titel_is_visible():
            pass
        else:
            raise AssertionError(f"Titel is not visible on the page.")

    elif expected_page == "mina böcker":
        pass
    else:
        raise AssertionError(f"Page name must be defined, but it was not. I got '{expected_page}' as value.")

@then('the "{navigation_button_name}" navigation button should be {expected_status}')
def step_impl(context, navigation_button_name, expected_status):
    navigation_button_name = navigation_button_name.lower()
    page = NavigationPage(context.page)
    if navigation_button_name == "katalog":
        button = page.katalog_button
    elif navigation_button_name =="lägg till bok":
        button = page.lagg_till_bok_button
    elif navigation_button_name == "mina böcker":
        button = page.mina_bocker_button
    else:
        raise AssertionError(f"Navigation button name must be defined, but it was not. I got '{navigation_button_name}' as value.")

    if expected_status == "enabled":
        if button.is_enabled():
            pass
        else:
            raise AssertionError(f"The navigation button '{navigation_button_name}'  does not have status '{expected_status}'.")

    if expected_status == "disabled":
        if button.is_disabled():
            pass
        else:
            raise AssertionError(f"The navigation button '{navigation_button_name}'  does not have status '{expected_status}'.")