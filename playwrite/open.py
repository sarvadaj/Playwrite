from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:


    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # Start tracing before creating / navigating a page.
    context.tracing.start(screenshots=True, snapshots=True, sources=True)

    page.goto("https://www.google.com/search?q=playwrite&oq=playwrite&gs_lcrp=EgZjaHJvbWUyBggAEEUYOdIBCDI3OTZqMGoyqAIAsAIA&sourceid=chrome&ie=UTF-8")
    page.get_by_role("link", name="Playwright: Fast and reliable").click()

    # ---------------------
    # Stop tracing and export it into a zip archive.
    context.tracing.stop(path="trace.zip")
    context.close()
    browser.close()




with sync_playwright() as playwright:
    run(playwright)