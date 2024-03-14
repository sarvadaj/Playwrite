from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False,slow_mo=5000)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.saucedemo.com/v1/")

    page.locator("xpath=//div/form/input[@id='user-name']").fill("standard_user")
    #page.locator("[data-test=\"username\"]").fill("standard_user")
    page.locator("[data-test=\"password\"]").fill("secret_sauce")


    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)