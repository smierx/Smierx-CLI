from typing import List

from pydantic import BaseModel,Field
from app.helper import ids

class Periods(BaseModel):
    identifier: str = Field(default_factory=ids.generate_unique_id)
    name: str
    submodules: List[str]
    module_identifier: str