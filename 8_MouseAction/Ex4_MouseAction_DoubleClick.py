from playwright.sync_api import Page

def handle_alert(dialog):
   dialog.accept()


def test_mouseDoubleClick(page: Page):
   page.goto("https://demo.guru99.com/test/simple_context_menu.html")
   page.wait_for_timeout(3000)

   # Register alert handler
   page.on("dialog", handle_alert)

   # Identify Double Click button
   element = page.locator("//button[text()='Double-Click Me To See Alert']")

   # Perform double click
   element.dblclick()
   page.wait_for_timeout(7000)
