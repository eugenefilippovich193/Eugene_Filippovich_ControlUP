"""
Base Page Object class for UI tests.
"""
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from shared.core.logger import get_logger
from shared.config.settings import settings


class BasePage:
    """Base page with common functionality."""
    
    def __init__(self, driver):
        """Initialize base page."""
        self.driver = driver
        self.wait = WebDriverWait(driver, settings.ui.EXPLICIT_WAIT)
        self.logger = get_logger(self.__class__.__name__)
    
    def find_element(self, locator):
        """Find element with wait."""
        return self.wait.until(EC.presence_of_element_located(locator))
    
    def find_elements(self, locator):
        """Find multiple elements."""
        return self.driver.find_elements(*locator)
    
    def click(self, locator):
        """Click element with wait."""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()
        return element
    
    def send_keys(self, locator, text):
        """Send keys to element."""
        element = self.find_element(locator)
        element.send_keys(text)
        return element
    
    def get_text(self, locator):
        """Get element text."""
        element = self.find_element(locator)
        return element.text
    
    def navigate_to(self, url):
        """Navigate to URL."""
        self.driver.get(url)
        self.logger.info(f"Navigated to {url}")
    
    def wait_for_element(self, locator):
        """Wait for element to be present."""
        return self.wait.until(EC.presence_of_element_located(locator))
