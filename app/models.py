from datetime import datetime, timezone
from typing import Optional
import sqlalchemy as sqla
import sqlalchemy.orm as sqlorm
from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login


class User(UserMixin, db.Model):
    id: sqlorm.Mapped[int] = sqlorm.mapped_column(primary_key=True)
    username: sqlorm.Mapped[str] = sqlorm.mapped_column(sqla.String(64), index=True,
                                                        unique=True)
    email: sqlorm.Mapped[str] = sqlorm.mapped_column(sqla.String(120), index=True,
                                                     unique=True)
    password_hash: sqlorm.Mapped[Optional[str]] = sqlorm.mapped_column(sqla.String(256))

    posts: sqlorm.WriteOnlyMapped['Post'] = sqlorm.relationship(
        back_populates='author')

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    @login.user_loader
    def load_user(id):
        return db.session.get(User, int(id))


class Post(db.Model):
    id: sqlorm.Mapped[int] = sqlorm.mapped_column(primary_key=True)
    body: sqlorm.Mapped[str] = sqlorm.mapped_column(sqla.String(140))
    timestamp: sqlorm.Mapped[datetime] = sqlorm.mapped_column(
        index=True, default=lambda: datetime.now(timezone.utc))
    user_id: sqlorm.Mapped[int] = sqlorm.mapped_column(sqla.ForeignKey(User.id),
                                                       index=True)

    author: sqlorm.Mapped[User] = sqlorm.relationship(back_populates='posts')

    def __repr__(self):
        return '<Post {}>'.format(self.body)
