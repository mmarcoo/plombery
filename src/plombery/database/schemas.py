from datetime import datetime
from typing import List

from pydantic import BaseModel, ConfigDict, Field

from plombery.schemas import PipelineRunStatus, TaskRun


class PipelineRunBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    pipeline_id: str
    trigger_id: str
    status: PipelineRunStatus
    start_time: datetime
    tasks_run: List[TaskRun] = Field(default_factory=list)


class PipelineRun(PipelineRunBase):
    id: int
    duration: float


class PipelineRunCreate(PipelineRunBase):
    pass
