import time
from playwright.sync_api import Page,expect


def test_verify_pwLocators6_get_by_place(page:Page):

   page.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html")
   time.sleep(2)

   homeLink=page.get_by_title("Home page link")
   expect(homeLink).to_have_text("Home")

   htmlLink=page.get_by_title("HyperText Markup Language")
   expect(htmlLink).to_have_text("HTML")

   tooltip=page.get_by_title("Tooltip text")
   expect(tooltip).to_have_text("This text has a tooltip")
   time.sleep(5)
