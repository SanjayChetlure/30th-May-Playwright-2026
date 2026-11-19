import time
from playwright.sync_api import Page, expect


def test_locateElementUsingXpath(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    time.sleep(2)

    #Enter Name
    page.locator("//input[@id='name']").fill("abc")

    #Enter Email
    page.locator("//input[@id='email']").fill("xyz")

    #click on start button
    page.locator("//button[text()='START']").click()

    time.sleep(8)





