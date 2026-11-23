import time
from operator import index

import pytest
from playwright.sync_api import Page,expect

def test_DeselectOptions_From_selectMultiSelectableListbox(page:Page):
   page.goto("https://testautomationpractice.blogspot.com")
   page.wait_for_timeout(2000)

   colors=page.locator("select#colors")

   # Select Options
   colors.select_option(index=[0,1,2])
   page.wait_for_timeout(5000)

   #DeSelect selected options
   colors.select_option(index=[0])        #select options at index =0 & deselect other selected options


   page.wait_for_timeout(9000)

