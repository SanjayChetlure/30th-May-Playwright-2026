import time
from playwright.sync_api import Page


def test_openApp(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    time.sleep(5)



