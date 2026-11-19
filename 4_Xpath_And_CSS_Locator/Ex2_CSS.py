import time
from playwright.sync_api import Page, expect


def test_locateElementUsingCSS(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    time.sleep(2)

    #Enter Name
    page.locator("input#name").fill("abc")

    #Enter Email
    page.locator("input#email").fill("xyz")

    #click on start button
    page.locator("button.start").click()

    time.sleep(8)





