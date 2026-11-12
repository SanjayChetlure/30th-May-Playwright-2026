import time
from playwright.sync_api import Page


def test_openApp(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    time.sleep(5)

def test_getUrlAndTitle(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    currentUrl=page.url
    print("Current URL is: ",currentUrl)

    pageTitle=page.title()
    print("Current Page Title is: ",pageTitle)

    time.sleep(5)


