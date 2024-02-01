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
