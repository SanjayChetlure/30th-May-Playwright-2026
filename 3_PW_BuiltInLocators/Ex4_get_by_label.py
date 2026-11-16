import time
from playwright.sync_api import Page


def test_verify_pwLocators4_get_by_label(page:Page):
   page.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html")
   time.sleep(5)

   # fill is method like sendkeys in selenium
   #Enter Email Address
   page.get_by_label("Email Address:").fill("abc123@gmail.com")

   # #Enter LN
   # page.get_by_label("Last name:").fill("xyz")
   #
   # # Enter Email
   # page.get_by_label("Email:").fill("abc@123")
   time.sleep(50)
