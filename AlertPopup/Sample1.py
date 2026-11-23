import time
import pytest
from playwright.sync_api import Page,expect


def test_alert(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    def handle_alert(dialog):
        print("Alert Message:", dialog.message)
        dialog.accept()

    page.on("dialog", handle_alert)

    page.locator("//button[text()='Alert']").click()

