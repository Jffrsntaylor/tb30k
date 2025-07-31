"""Validation logic for army lists."""

from typing import List
from .models import Unit, ArmyList


class ListValidator:
    """Simple points validation for an army list."""

    def __init__(self, max_points: int) -> None:
        self.max_points = max_points

    def validate(self, army_list: ArmyList) -> List[str]:
        """Return a list of validation errors."""
        total = sum(u.base_cost for u in army_list.units)
        errors: List[str] = []
        if total != army_list.points:
            errors.append("Point total mismatch")
        if total > self.max_points:
            errors.append("List exceeds maximum points")
        return errors
