#   Python Standard Library
from typing import List

#   Third-party Libraries
from pydantic import BaseModel, Field, field_validator

class AnchorModel(BaseModel):
    href: str = Field(default="")
    label: str = Field(default="")
    cls: List[str] = Field(default_factory=list)

    @field_validator("cls", mode="before")
    def validate_cls(cls, value: str | List[str]) -> str | List[str]:
        if isinstance(value, str): return [value]
        else: return [str(c) for c in value]     

    @property
    def is_external(self) -> bool:
        link = ["https://", "http://", "www."]
        return any(self.href.startswith(i) for i in link)