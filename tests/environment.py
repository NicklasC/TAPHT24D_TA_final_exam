from playwright.sync_api import sync_playwright


# Initialize Playwright and the browser before any feature or scenario
def before_all(context):
    # Start Playwright and launch the browser
    context.playwright = sync_playwright().start()
    context.browser = context.playwright.chromium.launch(
        headless=False)  # Use `headless=True` if you want to run silently

    # Example for development
    # context.browser = context.browsertype.launch(headless=False, slow_mo=500)


def before_scenario(context, scenario):
    # Create a new page for each scenario
    context.page = context.browser.new_page()
    context.page.goto(f'https://tap-ht24-testverktyg.github.io/exam-template/')


def after_scenario(context, scenario):
    # Close the page after each scenario
    context.page.close()


def after_all(context):
    # Close the browser and stop Playwright after all features
    context.browser.close()
    context.playwright.stop()
