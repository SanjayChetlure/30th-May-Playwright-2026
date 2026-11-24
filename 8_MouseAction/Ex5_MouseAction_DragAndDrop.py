from playwright.sync_api import Page


def test_dragAndDrop(page: Page):

   # Open application
   page.goto("https://demo.guru99.com/test/drag_drop.html")

   page.wait_for_timeout(5000)

   # Identify source element
   src = page.locator("(//a[@class='button button-orange'])[2]")

   # Identify destination element
   dest = page.locator("(//div[@class='ui-widget-content'])[3]")

   # Perform drag and drop
   src.drag_to(dest)

   page.wait_for_timeout(5000)
