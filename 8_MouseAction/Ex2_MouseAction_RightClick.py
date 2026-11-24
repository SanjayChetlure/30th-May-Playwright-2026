from playwright.sync_api import Page,expect

def test_mouseRightClick(page:Page):
   # Open Flipkart application
   page.goto("https://www.flipkart.com/")
   page.wait_for_timeout(5000)

   # Click on close button
   page.locator("//span[@class='b3wTlE']").click()
   page.wait_for_timeout(1000)

   # Identify Cart element
   Cart = page.locator("//span[text()='Cart']")

   # Right click on Cart element
   Cart.click(button="right")

   page.wait_for_timeout(5000)
   page.close()
