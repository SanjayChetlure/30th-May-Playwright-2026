import time
from playwright.sync_api import Page


def test_close_Browser(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    page.wait_for_timeout(5000)           # Wait for 5 seconds (5000 milliseconds)


