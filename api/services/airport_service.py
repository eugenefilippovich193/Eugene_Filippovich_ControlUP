"""
Airport Gap API service.
"""
from typing import Dict, Any
from api.core.api_client import APIClient
from shared.core.logger import get_logger
from shared.config.settings import settings
from api.models.airport_models import AirportsResponse, DistanceResponse


class AirportGapService:
    """Service for Airport Gap API interactions."""
    
    def __init__(self):
        """Initialize service."""
        self.client = APIClient(settings.api.BASE_URL)
        self.logger = get_logger(self.__class__.__name__)
    
    def get_airports_validated(self) -> AirportsResponse:
        """Get airports list with validation."""
        self.logger.info("Fetching airports list")
        
        response = self.client.get("/airports")
        response.raise_for_status()
        
        validated_response = AirportsResponse.model_validate(response.json())
        self.logger.info(f"Successfully validated airports response with {len(validated_response.data)} airports")
        
        return validated_response
    
    def calculate_distance_validated(self, from_airport: str, to_airport: str) -> DistanceResponse:
        """Calculate distance between airports with validation."""
        self.logger.info(f"Calculating distance from {from_airport} to {to_airport}")
        
        data = {
            "from": from_airport,
            "to": to_airport
        }
        
        response = self.client.post("/airports/distance", json_data=data)
        response.raise_for_status()
        
        validated_response = DistanceResponse.model_validate(response.json())
        distance_km = validated_response.data.attributes.kilometers
        self.logger.info(f"Distance calculated: {distance_km} km")
        
        return validated_response
