import time
from playwright.sync_api import Page, expect


def test_handle_alerts(page: Page):
   # Open application
   page.goto("https://demo.guru99.com/test/delete_customer.php")
   page.wait_for_timeout(2000)

   # Enter customer ID
   page.locator("//input[@name='cusid']").fill("123")

   # 1: Get text from first alert popup
   page.once("dialog", lambda dialog: print("Alert message:", dialog.message))

    # 2: Click on Cancel button (Dismiss first alert)
   # page.once("dialog", lambda dialog: dialog.dismiss())

   # 3: Click on OK button from first alert popup
   page.once("dialog", lambda dialog: dialog.accept())

   # Click on Submit button
   page.locator("//input[@name='submit']").click()
   page.wait_for_timeout(20000)
