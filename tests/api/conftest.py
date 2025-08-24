"""
API fixtures for Airport Gap tests.
"""
import pytest
from api.services.airport_service import AirportGapService


@pytest.fixture
def airport_service() -> AirportGapService:
    """Airport Gap service fixture."""
    return AirportGapService()
