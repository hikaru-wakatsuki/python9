from enum import Enum
from pydantic import BaseModel, Field, model_validator, ValidationError
from datetime import datetime


class Rank(Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=2, max_length=50)
    rank: Rank = Field(...)
    age: int = Field(..., ge=18, le=80)
    specialization: str = Field(..., min_length=3, max_length=30)
    years_experience: int = Field(..., ge=0, le=50)
    is_active: bool = Field(True)


class SpaceMission(BaseModel):
    mission_id: str = Field(..., min_length=5, max_length=15)
    mission_name: str = Field(..., min_length=3, max_length=100)
    destination: str = Field(..., min_length=3, max_length=50)
    launch_date: datetime = Field(...)
    duration_days: int = Field(..., ge=1, le=3650)
    crew: list[CrewMember] = Field(..., min_length=1, max_length=12)
    mission_status: str = Field("planned")
    budget_millions: float = Field(..., ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def mission_validation(self) -> "SpaceMission":
        if not self.mission_id.startswith("M"):
            raise ValueError('Mission ID must start with "M"')
        has_leader: bool = any(
            member.rank in (Rank.CAPTAIN, Rank.COMMANDER)
            for member in self.crew
        )
        if not has_leader:
            raise ValueError(
                "Mission must have at least one Commander or Captain")
        experienced_count: int = sum(
            1 for member in self.crew if member.years_experience >= 5)
        if self.duration_days > 365 and experienced_count < len(self.crew) / 2:
            raise ValueError(
                "Long missions (> 365 days) need 50% "
                "experienced crew (5+ years)")
        if not all(member.is_active for member in self.crew):
            raise ValueError(
                "All crew members must be active")
        return self


def main() -> None:
    try:
        print("Space Mission Crew Validation")
        print("=========================================")
        print("Valid mission created:")
        sarah_connor: CrewMember = CrewMember(
            member_id="001",
            name="Sarah Connor",
            rank="commander",
            age=50,
            specialization="Mission Command",
            years_experience=20
        )
        john_smith: CrewMember = CrewMember(
            member_id="002",
            name="John Smith",
            rank="lieutenant",
            age=40,
            specialization="Navigation",
            years_experience=10
        )
        alice_johnson: CrewMember = CrewMember(
            member_id="003",
            name="Alice Johnson",
            rank="officer",
            age=30,
            specialization="Engineering",
            years_experience=0
        )
        valid_mission: SpaceMission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime.now(),
            duration_days=900,
            crew=[sarah_connor, john_smith, alice_johnson],
            budget_millions=2500.0
        )
        print(f"Mission: {valid_mission.mission_name}")
        print(f"ID: {valid_mission.mission_id}")
        print(f"Destination: {valid_mission.destination}")
        print(f"Duration: {valid_mission.duration_days} days")
        print(f"Budget: ${valid_mission.budget_millions}M")
        print(f"Crew size: {len(valid_mission.crew)}")
        print("Crew members:")
        for member in valid_mission.crew:
            print(f"- {member.name} ({member.rank.value}) - "
                  f"{member.specialization}")
        print()
        print("=========================================")
        print("Expected validation error:")
        SpaceMission(
            mission_id="M2025_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime.now(),
            duration_days=900,
            crew=[alice_johnson],
            budget_millions=2500.0
        )
    except ValidationError as error:
        print(error)


if __name__ == "__main__":
    main()
