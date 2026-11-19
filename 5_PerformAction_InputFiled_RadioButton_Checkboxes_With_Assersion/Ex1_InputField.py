
import time
from playwright.sync_api import Page,expect


def test_PerformActionOnInputFiled_WithAssertion(page:Page):
   page.goto("https://testautomationpractice.blogspot.com")
   # page.locator("input#name").fill("abc")

   nameInpField=page.locator("input#name")

   #check visibility/presence of element
   expect(nameInpField).to_be_visible()

   #Enable of not
   expect(nameInpField).to_be_enabled()

   #check attr value of element
   expect(nameInpField).to_have_attribute("maxlength","15")      #PW assertion

   #get any attribute value
   length=nameInpField.get_attribute("maxlength")
   assert length=="15"                      #pytest assertion
   print("max length: ",length)


   #In PW python we are not going use pytest assertion
   #will use PW assertion
   #in selenium -python  we prefer to use pytest assertion
   # PW with python assertion provided only on locators, but not the value


   #fill value
   nameInpField.fill("abc")


   #get value from inputText
   valueFromInpField=nameInpField.input_value()
   print("Value present in Input field ",valueFromInpField)
   time.sleep(5)



