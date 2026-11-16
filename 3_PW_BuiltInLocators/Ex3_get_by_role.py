import time
from playwright.sync_api import Page, expect


def test_verifyHeadingPresent(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    time.sleep(5)

    headingEle=page.get_by_role("heading", name="Automation Testing Practice")
    expect(headingEle).to_be_visible()





