from playwright.sync_api import Page

def test_scrollToElement(page: Page):

   # Open application
   page.goto("https://testautomationpractice.blogspot.com/")
   page.wait_for_timeout(5000)

   # Identify Section 3 element
   section3 = page.locator("//h4[text()='Section 3']")

   # Scroll to Section 3
   section3.scroll_into_view_if_needed()

   page.wait_for_timeout(5000)
