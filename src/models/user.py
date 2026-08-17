from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.core.database import Base
from src.models.site import Site

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column()
    email: Mapped[str] = mapped_column(unique=True, index=True)
    hashed_password: Mapped[str] = mapped_column()
    sites: Mapped[list['Site']] = relationship(back_populates='user')
