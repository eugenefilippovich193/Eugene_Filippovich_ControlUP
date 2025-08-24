"""
UI tests for saucedemo.com website.
"""
import pytest
import allure
from ui.pages.login_page import LoginPage
from ui.pages.inventory_page import InventoryPage
from shared.core.logger import get_logger

logger = get_logger(__name__)


class TestSauceDemoUI:
    """UI tests for SauceDemo website."""

    @allure.title("Verify inventory page displays exactly 6 items")
    @pytest.mark.ui
    def test_verify_inventory_items(self, browser_driver, credentials):
        """
        Scenario 1: Verify Inventory Items
        
        1. Navigate to saucedemo.com and login with standard_user/secret_sauce
        2. Verify inventory page displays exactly 6 items
        """
        with allure.step("Open login page and login"):
            login_page = LoginPage(browser_driver)
            login_page.open().login(credentials["username"], credentials["password"])
        
        with allure.step("Wait for inventory page to load and count items"):
            inventory_page = InventoryPage(browser_driver)
            inventory_page.wait_for_page_load()
            
            actual_count = inventory_page.get_inventory_items_count()
            expected_count = 6
            
            assert actual_count == expected_count, f"Expected {expected_count} items, found {actual_count}"
            logger.info(f"Inventory items count verified: {actual_count}")

    @allure.title("Add first item to cart and verify cart badge shows 1")
    @pytest.mark.ui
    def test_add_item_to_cart(self, browser_driver, credentials):
        """
        Scenario 2: Add Item to Cart
        
        1. Login as in Scenario 1
        2. Add first inventory item to shopping cart
        3. Verify cart badge shows number 1
        """
        with allure.step("Open login page and login"):
            login_page = LoginPage(browser_driver)
            login_page.open().login(credentials["username"], credentials["password"])
        
        with allure.step("Wait for inventory page and add first item to cart"):
            inventory_page = InventoryPage(browser_driver)
            inventory_page.wait_for_page_load()
            
            item_name = inventory_page.add_first_item_to_cart()
            logger.info(f"Added first item to cart: {item_name}")
        
        with allure.step("Verify cart badge displays number 1"):
            badge_text = inventory_page.get_cart_badge_text()
            expected_badge_count = "1"
            
            assert badge_text == expected_badge_count, f"Expected cart badge to show '{expected_badge_count}', got '{badge_text}'"
            logger.info(f"Cart badge verified: {badge_text}")
