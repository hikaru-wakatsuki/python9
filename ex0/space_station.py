from pydantic import BaseModel, Field, ValidationError
from datetime import datetime
from typing import Optional


class SpaceStation(BaseModel):
    station_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=1, max_length=50)
    crew_size: int = Field(..., ge=1, le=20)
    power_level: float = Field(..., ge=0.0, le=100.0)
    oxygen_level: float = Field(..., ge=0.0, le=100.0)
    last_maintenance: datetime = Field(...)
    is_operational: bool = Field(True)
    note: Optional[str] = Field(None, max_length=200)


def main() -> None:
    try:
        print("Space Station Data Validation")
        print("========================================")
        print("Valid station created:")
        station: SpaceStation = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=6,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance=datetime.now(),
        )
        print(f"ID: {station.station_id}")
        print(f"Name: {station.name}")
        print(f"Crew: {station.crew_size} pepple")
        print(f"Power: {station.power_level}%")
        print(f"Oxygen: {station.oxygen_level}%")
        status: str
        status = 'Operational' if station.is_operational else 'Not Operational'
        print(f"Status: {status}")
        print()
        print("========================================")
        print("Expected validation error:")
        SpaceStation(
            station_id="ISS002",
            name="International Space Station2",
            crew_size=21,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance=datetime.now(),
        )
    except ValidationError as error:
        print(error)


if __name__ == "__main__":
    main()
