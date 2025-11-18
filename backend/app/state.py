from dataclasses import dataclass
from datetime import datetime
from typing import Dict

@dataclass
class SessionState:
    stage: str
    product_name: str = None
    user_name: str = None
    created_at: datetime = None

sessions: Dict[str, SessionState] = {}
