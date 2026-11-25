import time
from playwright.sync_api import Page, expect

def test_handle_alerts(page: Page):
   # Open application
   page.goto("https://skpatro.github.io/demo/links/")

   # Click NewTab link from main page
   with page.expect_popup() as popup_info:
       page.locator("//input[@name='NewTab']").click()

   # Get child window / new tab reference
   childPage = popup_info.value

   childPage.wait_for_load_state()

   # Click on Training link from child window
   childPage.locator("(//span[text()='Training'])[1]").click()
   childPage.wait_for_timeout(20000)




# with:  waiting for a new popup.
# as: Store the popup event information in popup_info

# - page.expect_popup() – Waits for a new tab/window to open.
# - popup_info – Stores information about the newly opened tab.
# - click() – Clicks the NewTab button.
# In simple words: Click NewTab and wait until the child tab opens.

# childPage.wait_for_load_state()  ->Wait until the child tab finishes loading.

# Imp Note:- Playwright does not require an explicit window switch
