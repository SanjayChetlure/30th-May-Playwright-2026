

import time
from playwright.sync_api import Page, expect


def test_switchToNestedFrame(page:Page):
    page.goto("https://autotestsandbox.com/examples/nested-iframes")

    # Locate Outer iframe(Switch to outer frame)
    outerFrame = page.frame_locator("//iframe[@title='Outer nested frame']")

    # Locate Inner/nested frame (Switch to inner/nested frame )
    innerFrame = outerFrame.frame_locator("//iframe[@title='Inner']")

    # Get text from inner iframe
    InnerText = innerFrame.locator("//p[text()='Inner iframe content']").inner_text()

    print("Inner frame text: ",InnerText)

    page.wait_for_timeout(2000)









