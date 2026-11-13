import time
from playwright.sync_api import Page


def test_move_forward(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    time.sleep(3)
    page.goto("https://www.google.com/")
    time.sleep(3)
    page.go_back()
    time.sleep(3)
    page.go_forward()
    time.sleep(5)



