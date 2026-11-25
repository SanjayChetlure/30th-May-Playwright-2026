from playwright.sync_api import Page
def test_handle_multiple_windows(page: Page):
   # Open main page
   page.goto("https://skpatro.github.io/demo/links/")

   # 1: Click NewTab link from main page
   with page.expect_popup() as popup_info:
       page.locator("//input[@name='NewTab']").click()

   # Get Child Tab 1 reference
   childPage1 = popup_info.value
   childPage1.wait_for_load_state()

   # Click on Training link from Child Tab 1
   childPage1.locator("(//span[text()='Training'])[1]").click()
   page.wait_for_timeout(5000)


   # 2: Switch back to main page
   # No need to switch explicitly
   # 'page' already represents the main page

   # 3: Click NewWindow link from main page
   with page.expect_popup() as popup_info2:
       page.locator("//input[@name='NewWindow']").click()

   # Get Child Window 2 reference
   childPage2 = popup_info2.value
   childPage2.wait_for_load_state()
   page.wait_for_timeout(2000)

   # 4: Close Child Window 2
   childPage2.close()
   page.wait_for_timeout(2000)
   childPage1.close()
   page.wait_for_timeout(2000)
   page.close()
   page.wait_for_timeout(20000)
