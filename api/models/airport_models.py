"""
Pydantic models for Airport Gap API responses.
"""
from typing import List, Dict, Any
from pydantic import BaseModel, Field


class AirportData(BaseModel):
    """Single airport data model."""
    
    id: str
    type: str
    attributes: Dict[str, Any]


class AirportsResponse(BaseModel):
    """Response model for airports list."""
    
    data: List[AirportData]
    links: Dict[str, Any]


class DistanceAttributes(BaseModel):
    """Distance calculation attributes."""
    
    from_airport: Dict[str, Any]
    to_airport: Dict[str, Any] 
    kilometers: float
    miles: float
    nautical_miles: float


class DistanceData(BaseModel):
    """Distance data model."""
    
    id: str
    type: str
    attributes: DistanceAttributes


class DistanceResponse(BaseModel):
    """Response model for distance calculation."""
    
    data: DistanceData
