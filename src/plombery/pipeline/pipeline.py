from typing import Any, List, Optional, Type

from pydantic import BaseModel, ConfigDict, Field, model_validator

from ._utils import prettify_name
from .task import Task
from .trigger import Trigger


class Pipeline(BaseModel):
    model_config = ConfigDict(validate_assignment=True)

    id: str
    tasks: List[Task]
    name: Optional[str]
    description: Optional[str] = None
    params: Optional[Type[BaseModel]] = Field(exclude=True, default=None)
    triggers: List[Trigger] = Field(default_factory=list)

    @model_validator(mode="before")
    @classmethod
    def generate_default_name(cls, data: Any) -> Any:
        if isinstance(data, dict):
            if not data.get("name", None):
                data["name"] = prettify_name(data["id"]).title()

            if not data.get("description", None):
                data["description"] = cls.__doc__

        return data
