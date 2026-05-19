
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

<<<<<<< HEAD
# Thảo comment 221 comment
=======
# Thảo comment 221 comment branch new_test
# new test branch
>>>>>>> 95ad34d3c135cf4e0bc4952ba5244758e5e8da48
