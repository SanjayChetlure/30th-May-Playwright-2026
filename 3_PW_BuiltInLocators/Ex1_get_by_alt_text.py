import time
from playwright.sync_api import Page, expect


def test_verifyLogoPresent(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html")
    time.sleep(2)
    pwLogo=page.get_by_alt_text("logo image")

    expect(pwLogo).to_be_visible()




