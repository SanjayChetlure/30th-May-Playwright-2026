from playwright.sync_api import Page,expect

def test_mouseHover(page:Page):

   # Open Flipkart application
   page.goto("https://www.flipkart.com/")
   page.wait_for_timeout(5000)

   # Click on close button
   page.locator("//span[@class='b3wTlE']").click()
   page.wait_for_timeout(3000)

   # 1: Identify mouse over element
   login = page.locator("//span[text()='Login']")

   # 2: Move mouse over Login element
   login.hover()
   page.wait_for_timeout(5000)

   # Click on Orders link
   page.locator("//div[text()='Orders']").click()

   page.wait_for_timeout(5000)
