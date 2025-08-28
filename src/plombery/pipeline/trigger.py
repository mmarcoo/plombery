from datetime import datetime
from typing import Annotated, Optional

from apscheduler.triggers.base import BaseTrigger
from pydantic import BaseModel, ConfigDict, PlainSerializer

SerializableBaseTrigger = Annotated[BaseTrigger, PlainSerializer(lambda v: str(v))]


class Trigger(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    id: str
    name: str
    schedule: SerializableBaseTrigger
    description: Optional[str] = __doc__
    params: Optional[BaseModel] = None
    paused: bool = False
    next_fire_time: Optional[datetime] = None
