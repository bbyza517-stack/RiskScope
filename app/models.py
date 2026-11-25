from sqlmodel import SQLModel, Field
from datetime import datetime, timezone
from typing import Optional


class RiskAnalysis(SQLModel, table=True):

    id: Optional[int] = Field(default=None, primary_key=True)

    coin_name: str
    symbol: str
    current_price: float
    risk_score: int
    risk_level: str

    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc)
    )