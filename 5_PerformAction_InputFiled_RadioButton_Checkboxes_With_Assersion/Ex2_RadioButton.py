import pytest
from playwright.sync_api import Page,expect

def test_verify_css_locator(page:Page):
   page.goto("https://testautomationpractice.blogspot.com")

   maleRadioBtn=page.locator("#male")

   #check visibility & enabled/disable
   expect(maleRadioBtn).to_be_visible()
   expect(maleRadioBtn).to_be_enabled()

   #check radio button by default should not check
   expect(maleRadioBtn).not_to_be_checked()

  #Select/check radio button
   maleRadioBtn.check()

   # check radio button should be checked
   expect(maleRadioBtn).to_be_checked()

   page.wait_for_timeout(5000)

