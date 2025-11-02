from sqlalchemy import Column, BigInteger, String, DateTime
from datetime import datetime, timezone
from bot.database.database_settings import Base

class Blacklist(Base):
    __tablename__ = 'blacklist'

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    type = Column(String(20), default='default', nullable=False)
    banned_chat_id = Column(BigInteger, nullable=False, unique=True)
    date = Column(DateTime, default=lambda: datetime.now(), nullable=False)

    def __repr__(self):
        return f"<Blacklist(type='{self.type}', banned_chat_id={self.banned_chat_id})>"