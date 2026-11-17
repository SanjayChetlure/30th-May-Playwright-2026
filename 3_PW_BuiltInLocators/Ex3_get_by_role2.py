import time
from playwright.sync_api import Page, expect


def test_verifyHeadingPresent(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html")
    time.sleep(2)

    page.get_by_role("checkbox", name="Accept terms").click()

    page.get_by_role("textbox", name="Username:").fill("abcd")

    time.sleep(20)






