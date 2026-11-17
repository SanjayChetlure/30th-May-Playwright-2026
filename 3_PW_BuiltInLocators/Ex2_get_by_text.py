import time
from playwright.sync_api import Page, expect


def test_verifyLogoPresent(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    time.sleep(5)

    linkText = page.get_by_text("PlaywrightPractice")
    expect(linkText).to_be_visible()

    linkText.click()
    time.sleep(5)








