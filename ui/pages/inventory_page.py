"""
Inventory Page Object for UI tests.
"""
from selenium.webdriver.common.by import By
from ui.pages.base_page import BasePage


class InventoryPage(BasePage):
    """Inventory page for saucedemo.com."""
    
    INVENTORY_LIST = (By.CLASS_NAME, "inventory_list")
    INVENTORY_ITEMS = (By.CLASS_NAME, "inventory_item")
    ADD_TO_CART_BUTTONS = (By.XPATH, "//button[contains(text(), 'Add to cart')]")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    INVENTORY_ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    
    def wait_for_page_load(self):
        """Wait for inventory page to load."""
        self.wait_for_element(self.INVENTORY_LIST)
        self.logger.info("Inventory page loaded successfully")
        return self
    
    def get_inventory_items_count(self):
        """Get number of inventory items."""
        items = self.find_elements(self.INVENTORY_ITEMS)
        count = len(items)
        self.logger.info(f"Found {count} inventory items")
        return count
    
    def get_first_add_to_cart_button(self):
        """Get first 'Add to cart' button."""
        buttons = self.find_elements(self.ADD_TO_CART_BUTTONS)
        if not buttons:
            raise AssertionError("No 'Add to cart' buttons found")
        return buttons[0]
    
    def get_item_name_for_button(self, button):
        """Get item name for specific add to cart button."""
        inventory_item = button.find_element(By.XPATH, "./ancestor::div[contains(@class, 'inventory_item')]")
        item_name_element = inventory_item.find_element(By.CLASS_NAME, "inventory_item_name")
        return item_name_element.text
    
    def add_first_item_to_cart(self):
        """Add first item to cart and return item name."""
        button = self.get_first_add_to_cart_button()
        item_name = self.get_item_name_for_button(button)
        
        button.click()
        self.logger.info(f"Added item to cart: {item_name}")
        return item_name
    
    def get_cart_badge_text(self):
        """Get cart badge text."""
        badge_text = self.get_text(self.CART_BADGE)
        self.logger.info(f"Cart badge shows: {badge_text}")
        return badge_text
