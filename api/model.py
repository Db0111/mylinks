from datetime import datetime, timezone
from sqlmodel import SQLModel, Field


class Link(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    url: str
    title: str
    memo: str | None = None
    # lambda: 나중에 수행할 함수
    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc)
    )