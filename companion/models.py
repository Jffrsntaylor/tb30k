"""Pydantic models representing game data objects."""

from typing import List, Optional
from pydantic import BaseModel


class Weapon(BaseModel):
    """A weapon profile."""

    name: str
    range: str
    type: str
    strength: str
    ap: str
    special_rules: List[str] = []


class UnitOption(BaseModel):
    """Upgrade option for a unit."""

    name: str
    cost: int
    keyword: Optional[str] = None
    exclusive_group_id: Optional[str] = None
    max_per_n_models: Optional[int] = None


class Unit(BaseModel):
    """A unit entry."""

    name: str
    base_cost: int
    faction: str
    weapons: List[str]
    options: List[UnitOption] = []
    rules: List[str] = []


class Rule(BaseModel):
    """Special rule text."""

    name: str
    text: str


class ArmyList(BaseModel):
    """User-created army list."""

    edition: str
    faction: str
    units: List[Unit]
    points: int
