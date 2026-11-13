import time
from playwright.sync_api import Page


def test_getCurrentUrl(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    titleOfApp=page.title()
    print("Title is: ",titleOfApp)
    time.sleep(5)



