"""
API tests for Airport Gap service.
"""
import pytest
import allure
from api.services.airport_service import AirportGapService
from shared.core.logger import get_logger

logger = get_logger(__name__)


class TestAirportAPI:
    """Airport API test suite."""
    
    @allure.title("Verify that API returns exactly 30 airports")
    @pytest.mark.api
    def test_verify_airport_count(self, airport_service: AirportGapService):
        """
        Scenario 1: Verify Airport Count
        
        1. Send GET request to /airports endpoint
        2. Verify response contains exactly 30 airports
        """
        with allure.step("Send GET request to /airports endpoint"):
            logger.info("Starting airport count validation test")
            airports_response = airport_service.get_airports_validated()
        
        with allure.step("Verify response contains exactly 30 airports"):
            expected_count = 30
            actual_count = len(airports_response.data)
            
            assert actual_count == expected_count, f"Expected {expected_count} airports, got {actual_count}"
            logger.info(f"Airport count verified: {actual_count}")

    @allure.title("Verify specific airports are present in the response")
    @pytest.mark.api
    def test_verify_specific_airports(self, airport_service: AirportGapService):
        """
        Scenario 2: Verify Specific Airports
        
        1. Send GET request to /airports endpoint
        2. Verify response includes: Akureyri Airport, St. Anthony Airport, CFB Bagotville
        """
        with allure.step("Send GET request to /airports endpoint"):
            logger.info("Starting specific airports validation test")
            airports_response = airport_service.get_airports_validated()
        
        with allure.step("Extract airport names from response"):
            airport_names = []
            for airport in airports_response.data:
                name = airport.attributes.get("name", "")
                airport_names.append(name)
            
            logger.info(f"Found {len(airport_names)} airport names")
        
        with allure.step("Verify required airports are present"):
            required_airports = ["Akureyri Airport", "St. Anthony Airport", "CFB Bagotville"]
            
            for required_airport in required_airports:
                assert required_airport in airport_names, f"Airport '{required_airport}' not found in response"
                logger.info(f"Verified presence of: {required_airport}")

    @allure.title("Verify distance between KIX and NRT is greater than 400 km")
    @pytest.mark.api
    def test_verify_distance_between_airports(self, airport_service: AirportGapService):
        """
        Scenario 3: Verify Distance Between Airports
        
        1. Send POST request to /airports/distance with KIX and NRT parameters
        2. Verify calculated distance is greater than 400 km
        """
        with allure.step("Send POST request to calculate distance between KIX and NRT"):
            logger.info("Starting distance calculation test")
            from_airport = "KIX"
            to_airport = "NRT"
            
            distance_response = airport_service.calculate_distance_validated(from_airport, to_airport)
        
        with allure.step("Verify distance is greater than 400 km"):
            distance_km = distance_response.data.attributes.kilometers
            min_expected_distance = 400
            
            assert distance_km > min_expected_distance, f"Expected distance > {min_expected_distance} km, got {distance_km} km"
            logger.info(f"Distance verified: {distance_km} km > {min_expected_distance} km")
