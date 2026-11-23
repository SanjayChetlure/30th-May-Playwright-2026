import time
import pytest
from playwright.sync_api import Page,expect

def test_selectSingleSelectableListbox(page:Page):
   page.goto("https://testautomationpractice.blogspot.com")
   page.wait_for_timeout(2000)

   country=page.locator("#country")

   #3 ways to select option (Text/label, value, index)
   #1.1 Select option -> #Text
   country.select_option("Japan")
   # country.select_option(label="Canada")
   page.wait_for_timeout(8000)

   # 1.2 Select option -> #value
   country.select_option("uk")
   # country.select_option(label="uk")
   page.wait_for_timeout(4000)

   # 1.3 Select option -> Index  (starts with zero)
   country.select_option(index=6)

   page.wait_for_timeout(2000)

   #2: Count total no of options
   allOptions=page.locator("#country>option")
   cnt=allOptions.count()
   print("Total options : ",cnt)

   expect(allOptions).to_have_count(10)

   print("---------")

   #print all options text
   allOptionsText=allOptions.all_text_contents()
   for eachOptionText in allOptionsText:
       print(eachOptionText.strip())

