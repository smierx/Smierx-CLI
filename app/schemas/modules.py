from pydantic import BaseModel,Field
from typing import Optional
from app.schemas.periods import Periods
from app.helper import ids

class Submodule(BaseModel):
    identifier: str = Field(default_factory=ids.generate_unique_id)
    module_identifier: str
    order: int
    name: str

class Module(BaseModel):
    identifier: str = Field(default_factory=ids.generate_unique_id)
    name: str
    periods: Optional[list[Periods]] = []
    submodules: Optional[list[Submodule]] = []
    semester: str
    exam_format: Optional[str] = None

