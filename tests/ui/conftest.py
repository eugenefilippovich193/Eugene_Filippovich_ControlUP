"""
Pytest configuration for UI tests
"""
import os
import pytest
from typing import Dict
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
from dotenv import load_dotenv

from shared.core.logger import get_logger

load_dotenv()


@pytest.fixture(scope="session")
def credentials() -> Dict[str, str]:
    """Credentials for saucedemo.com login"""
    return {
        "username": os.getenv("SAUCE_USERNAME", "standard_user"),
        "password": os.getenv("SAUCE_PASSWORD", "secret_sauce"),
    }


@pytest.fixture
def browser_driver(request) -> WebDriver:
    """Chrome WebDriver fixture for UI tests"""
    headless = request.config.getoption("--headless")
    
    logger = get_logger(__name__)
    logger.info(f"Starting Chrome browser (headless: {headless})")

    options = webdriver.ChromeOptions()
    if headless:
        options.add_argument("--headless=new")
    
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-password-manager-reauthentication")
    options.add_argument("--disable-password-generation")
    options.add_argument("--disable-save-password-bubble")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-translate")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-web-security")
    options.add_argument("--disable-features=VizDisplayCompositor,PasswordManager,PasswordGeneration")
    options.add_argument("--disable-password-manager")
    options.add_argument("--disable-auto-reload")
    
    prefs = {
        "profile.password_manager_enabled": False,
        "credentials_enable_service": False,
        "autofill.profile_enabled": False,
        "autofill.credit_card_enabled": False,
        "profile.default_content_setting_values.notifications": 2,
        "profile.default_content_settings.popups": 0,
        "profile.managed_default_content_settings.popups": 0,
        "profile.password_manager_leak_detection": False,
        "password_manager.enabled": False,
        "password_manager.password_manager_enabled": False
    }
    options.add_experimental_option("prefs", prefs)
    options.add_experimental_option("excludeSwitches", ["enable-logging", "enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    yield driver
    driver.quit()
    logger.info("Chrome browser closed")
