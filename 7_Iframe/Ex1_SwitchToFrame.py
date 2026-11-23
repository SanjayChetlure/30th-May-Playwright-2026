

import time
from playwright.sync_api import Page, expect


def test_switchToFrame(page:Page):
    page.goto("https://autotestsandbox.com/examples/nested-iframes")

    # Switch to outer frame
    outerFrame = page.frame_locator("//iframe[@title='Outer nested frame']")

    # perform action on outer frame -> Get text from Outer iframe
    outerFrameText = outerFrame.locator("//p[text()='Outer iframe']").inner_text()
    print("outerText: ",outerFrameText)








