import time
from playwright.sync_api import Page

def test_openApp(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    time.sleep(5)

    #by default script will run in Chromium browser with headless mode

    #Modes of Execution
    #1- Headed Mode:-
    #2- Headless Mode:-

