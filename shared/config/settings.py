"""
Shared configuration settings.
"""


class APISettings:
    """API configuration."""
    
    BASE_URL: str = "https://airportgap.com/api"
    REQUEST_TIMEOUT: int = 5


class UISettings:
    """UI configuration."""
    
    IMPLICIT_WAIT: int = 10
    EXPLICIT_WAIT: int = 10
    PAGE_LOAD_TIMEOUT: int = 10


class Settings:
    """Combined settings."""
    
    api = APISettings()
    ui = UISettings()


settings = Settings()
