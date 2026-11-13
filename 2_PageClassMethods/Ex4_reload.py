import time
from playwright.sync_api import Page


def test_refresh(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    time.sleep(3)
    page.reload()



