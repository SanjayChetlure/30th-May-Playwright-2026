import time
import pytest
from playwright.sync_api import Page,expect

def test_DeselectAllOptions_From_MultiSelectableListbox(page:Page):
   page.goto("https://testautomationpractice.blogspot.com")
   page.wait_for_timeout(2000)

   colors=page.locator("select#colors")

   # Select Options
   colors.select_option(index=[0,1,2])
   page.wait_for_timeout(5000)

   #DeSelect selected options
   colors.select_option([])


   page.wait_for_timeout(9000)

