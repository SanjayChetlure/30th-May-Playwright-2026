from playwright.sync_api import Page

def test_scrollByAmount(page: Page):
   # Open application
   page.goto("https://testautomationpractice.blogspot.com/")
   page.wait_for_timeout(2000)

   # Scroll down (Positive Y value)
   page.mouse.wheel(0, 700)
   page.wait_for_timeout(5000)

   # Scroll up (Negative Y value)
   page.mouse.wheel(0, -300)
   page.wait_for_timeout(5000)

   # Scroll right (Positive X value)
   # page.mouse.wheel(100, 0)

   # Scroll left (Negative X value)
   # page.mouse.wheel(-100, 0)


