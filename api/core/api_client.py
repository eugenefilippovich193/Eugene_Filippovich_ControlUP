"""
API HTTP client for Airport Gap service.
"""
from typing import Optional, Dict, Any
import requests
from requests import Response
from requests.exceptions import RequestException
from shared.core.logger import get_logger
from shared.config.settings import settings


class APIClient:
    """Simple API client with logging."""
    
    def __init__(self, base_url: Optional[str] = None):
        """Initialize API client."""
        self.base_url = (base_url or "").rstrip('/')
        self.session = requests.Session()
        self.logger = get_logger(self.__class__.__name__)
        
        self.session.headers.update({
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        })
    
    def get(self, endpoint: str, params: Optional[Dict] = None) -> Response:
        """Make GET request."""
        url = f"{self.base_url}{endpoint}"
        
        try:
            self.logger.info(f"GET {url} with params: {params}")
            response = self.session.get(url, params=params, timeout=settings.api.REQUEST_TIMEOUT)
            self.logger.info(f"Response: {response.status_code}")
            return response
        except RequestException as e:
            self.logger.error(f"GET request failed: {e}")
            raise
    
    def post(self, endpoint: str, json_data: Optional[Dict[str, Any]] = None, 
             params: Optional[Dict] = None) -> Response:
        """Make POST request."""
        url = f"{self.base_url}{endpoint}"
        
        try:
            self.logger.info(f"POST {url} with data: {json_data}, params: {params}")
            response = self.session.post(
                url, 
                json=json_data, 
                params=params,
                timeout=settings.api.REQUEST_TIMEOUT
            )
            self.logger.info(f"Response: {response.status_code}")
            return response
        except RequestException as e:
            self.logger.error(f"POST request failed: {e}")
            raise
