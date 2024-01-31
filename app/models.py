from datetime import datetime, timezone
from typing import Optional
import sqlalchemy as sqla
import sqlalchemy.orm as sqlorm
from app import db


class User(db.Model):
    id: sqlorm.Mapped[int] = sqlorm.mapped_column(primary_key=True)
    username: sqlorm.Mapped[str] = sqlorm.mapped_column(sqla.String(64), index=True,
                                                        unique=True)
    email: sqlorm.Mapped[str] = sqlorm.mapped_column(sqla.String(120), index=True,
                                                     unique=True)
    password_hash: sqlorm.Mapped[Optional[str]] = sqlorm.mapped_column(sqla.String(256))

    def __repr__(self):
        return '<User {}>'.format(self.username)


class Post(db.Model):
    id: sqlorm.Mapped[int] = sqlorm.mapped_column(primary_key=True)
    body: sqlorm.Mapped[str] = sqlorm.mapped_column(sqla.String(140))
    timestamp: sqlorm.Mapped[datetime] = sqlorm.mapped_column(
        index = True, default = lambda: datetime.now(timezone.utc)
    )
    user_id: sqlorm.Mapped[User] = sqlorm.relationship(back_populates ='posts')

    def __repr__(self):
        return '<Post {}>'.format(self.body)
