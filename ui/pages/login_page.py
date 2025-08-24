"""
Login Page Object for UI tests.
"""
from selenium.webdriver.common.by import By
from ui.pages.base_page import BasePage


class LoginPage(BasePage):
    """Login page for saucedemo.com."""
    
    URL = "https://www.saucedemo.com"
    
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    
    def open(self):
        """Open login page."""
        self.navigate_to(self.URL)
        return self
    
    def enter_username(self, username):
        """Enter username."""
        self.send_keys(self.USERNAME_INPUT, username)
        self.logger.info(f"Entered username: {username}")
        return self
    
    def enter_password(self, password):
        """Enter password."""
        self.send_keys(self.PASSWORD_INPUT, password)
        self.logger.info("Entered password")
        return self
    
    def click_login(self):
        """Click login button."""
        self.click(self.LOGIN_BUTTON)
        self.logger.info("Clicked login button")
        return self
    
    def login(self, username, password):
        """Complete login flow."""
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
        self.logger.info(f"Completed login for user: {username}")
        return self
