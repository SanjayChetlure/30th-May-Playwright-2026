import time
import pytest
from playwright.sync_api import Page,expect

def test_selectMultiSelectableListbox(page:Page):
   page.goto("https://testautomationpractice.blogspot.com")
   page.wait_for_timeout(2000)

   colors=page.locator("select#colors")

   #3 ways to select option (Text/label, value, index)
   #1.1 Select option -> #Text or label
   # colors.select_option(["Blue","Red"])
   # page.wait_for_timeout(5000)

   # 1.2 Select option -> #value
   # colors.select_option(["red","blue","green"])
   page.wait_for_timeout(4000)

   # # 1.3 Select option -> Index  (starts with zero)
   colors.select_option(index=[0,1,3])

   page.wait_for_timeout(9000)

