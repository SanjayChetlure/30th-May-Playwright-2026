import time
from playwright.sync_api import Page


def test_getCurrentUrl(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    currentUrl=page.url
    print("Current URL is: ",currentUrl)
    time.sleep(5)



