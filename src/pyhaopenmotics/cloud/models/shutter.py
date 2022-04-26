"""Shutter Model for the OpenMotics API."""
from __future__ import annotations

from typing import Any, Optional

from pydantic import BaseModel, Field

from .location import Location


class Status(BaseModel):
    """Class holding the status."""

    locked: Optional[bool]
    manual_override: Optional[bool]
    state: Optional[str]
    position: Optional[int]
    last_change: Optional[float]
    preset_position: Optional[int]


class Attributes(BaseModel):
    """Class holding the attributes."""

    azimuth: Optional[str]
    compass_point: Optional[str]
    surface_area: Optional[str]


class Shutter(BaseModel):
    """Object holding an OpenMotics Shutter.

    # noqa: E800
    # {
    # "_version": <version>,
    # "configuration": {
    #     "group_1": null | <group id>,
    #     "group_2": null | <group id>,
    #     "name": "<name>",
    #     "steps": null | <number of steps>,
    #     "timer_down": <timer down>,
    #     "timer_up": <timer up>,
    #     "up_down_config": <up down configuration>
    # },
    # "id": <id>,
    # "capabilities": ["UP_DOWN", "POSITION", "RELATIVE_POSITION",
    #          "HW_LOCK"|"CLOUD_LOCK", "PRESET", "CHANGE_PRESET"],
    # "location": {
    #     "floor_coordinates": {
    #         "x": null | <x coordinate>,
    #         "y": null | <y coordinate>
    #     },
    #     "floor_id": null | <floor id>,
    #     "installation_id": <installation id>,
    #     "room_id": null | <room_id>
    # },
    # "name": "<name>",
    # "status": {
    #     "last_change": <epoch in seconds>
    #     "position": null | <position>,
    #     "state": null | "UP|DOWN|STOP|GOING_UP|GOING_DOWN",
    #     "locked": true | false,
    #     "manual_override": true | false
    # }
    # }
    """

    # pylint: disable=too-many-instance-attributes
    idx: int = Field(..., alias="id")
    local_id: Optional[int]
    name: str
    shutter_type: str = Field(..., alias="type")
    capabilities: Optional[list[Any]]
    status: Status
    location: Optional[Location]
    attributes: Optional[Attributes]
    metadata: Optional[str]
    version: Optional[str] = Field(..., alias="_version")

    def __str__(self) -> str:
        """Represent the class objects as a string.

        Returns:
            string

        """
        return f"{self.idx}_{self.name}"
