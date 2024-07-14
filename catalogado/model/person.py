from dataclasses import dataclass
import datetime
from typing import Optional

@dataclass
class Person:
    id: Optional[int] = None
    name: str
    birthdate: Optional[datetime.datetime] = None