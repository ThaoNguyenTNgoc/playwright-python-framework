
from playwright.sync_api import sync_playwright


def test_open_google():

    with sync_playwright() as p:

        browser = p.chromium.launch(
            headless=False
        )

        page = browser.new_page()

        page.goto("https://google.com")

        print(page.title())

        page.wait_for_timeout(3000)

        browser.close()

# Thảo comment 221 comment branch new_test