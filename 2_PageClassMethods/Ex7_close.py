import time
from playwright.sync_api import Page


def test_close_Browser(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    time.sleep(5)
    page.close()

    time.sleep(5)



