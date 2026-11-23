

import time
from playwright.sync_api import Page, expect


def test_switchToNestedFrame(page:Page):
    page.goto("https://autotestsandbox.com/examples/nested-iframes")

    # Locate/Switch to Outer iframe
    outerFrame = page.frame_locator("//iframe[@title='Outer nested frame']")

    # Switch to inner frame
    innerFrame = outerFrame.frame_locator("//iframe[@title='Inner']")

    # Get text from inner iframe
    InnerText = innerFrame.locator("//p[text()='Inner iframe content']").inner_text()
    print("Inner frame: text",InnerText)

    page.wait_for_timeout(2000)

    #Switch to main page from Nested frame
    page.locator("(//a[text()='Home'])[1]").click()


    page.wait_for_timeout(10000)








