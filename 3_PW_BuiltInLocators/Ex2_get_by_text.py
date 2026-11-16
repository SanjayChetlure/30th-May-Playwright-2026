import time
from playwright.sync_api import Page, expect


def test_verifyLogoPresent(page:Page):
    # page.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html")
    # time.sleep(5)
    # linkText=page.get_by_text("Home")
    #
    # expect(linkText).to_be_visible()

    page.goto("https://www.flipkart.com/")
    time.sleep(5)

    # Apr1:
    textEle = page.get_by_text("Select delivery location")  # Full text
    expect(textEle).to_be_visible()

    # Apr2:-
    expect(page.get_by_text("Select delivery location")).to_be_visible()  # Full Text
    expect(page.get_by_text("Select delivery")).to_be_visible()  # Partial Text





