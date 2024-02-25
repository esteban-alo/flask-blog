"""
Tables mapper class
"""

from sqlalchemy import (
    ARRAY,
    TIMESTAMP,
    UUID,
    Boolean,
    Column,
    ForeignKeyConstraint,
    Integer,
    MetaData,
    PrimaryKeyConstraint,
    String,
    Table,
    Text,
    UniqueConstraint,
    text,
)
from sqlalchemy.orm import registry, relationship
from sqlalchemy.sql.functions import now

from src.domain.model import Password, Permission, Post, Role, User

metadata = MetaData()

roles = Table(
    "roles",
    metadata,
    Column("id", Integer, autoincrement=True),
    Column("name", String(50)),
    Column("public_id", UUID, nullable=False, server_default=text("gen_random_uuid()")),
    Column("created_at", TIMESTAMP, nullable=False, server_default=now()),
    Column(
        "updated_at",
        TIMESTAMP,
        nullable=False,
        onupdate=now(),
        server_default=now(),
    ),
    PrimaryKeyConstraint("id", name="role_pk"),
    UniqueConstraint("name"),
    UniqueConstraint("public_id"),
    schema="blog",
)


permissions = Table(
    "permissions",
    metadata,
    Column("id", Integer, autoincrement=True),
    Column("name", String(50)),
    Column("public_id", UUID, nullable=False, server_default=text("gen_random_uuid()")),
    Column("created_at", TIMESTAMP, nullable=False, server_default=now()),
    Column(
        "updated_at",
        TIMESTAMP,
        nullable=False,
        onupdate=now(),
        server_default=now(),
    ),
    PrimaryKeyConstraint("id", name="permission_pk"),
    UniqueConstraint("name"),
    UniqueConstraint("public_id"),
    schema="blog",
)

roles_permissions = Table(
    "roles_permissions",
    metadata,
    Column("id", Integer, autoincrement=True),
    Column("role_id", Integer),
    Column("permission_id", Integer),
    Column("created_at", TIMESTAMP, nullable=False, server_default=now()),
    Column(
        "updated_at",
        TIMESTAMP,
        nullable=False,
        onupdate=now(),
        server_default=now(),
    ),
    PrimaryKeyConstraint("id", name="role_permission_pk"),
    ForeignKeyConstraint(
        [
            "role_id",
        ],
        [
            "blog.roles.id",
        ],
        onupdate="CASCADE",
        ondelete="SET NULL",
    ),
    ForeignKeyConstraint(
        [
            "permission_id",
        ],
        [
            "blog.permissions.id",
        ],
        onupdate="CASCADE",
        ondelete="SET NULL",
    ),
    UniqueConstraint("role_id", "permission_id"),
    schema="blog",
)


posts = Table(
    "posts",
    metadata,
    Column("id", Integer, autoincrement=True),
    Column("title", String(256)),
    Column("text", Text),
    Column("tags", ARRAY(String(25))),
    Column("url_path", String(256)),
    Column("enabled", Boolean, default=False),
    Column("public_id", UUID, nullable=False, server_default=text("gen_random_uuid()")),
    Column("created_at", TIMESTAMP, nullable=False, server_default=now()),
    Column(
        "updated_at",
        TIMESTAMP,
        nullable=False,
        onupdate=now(),
        server_default=now(),
    ),
    PrimaryKeyConstraint("id", name="post_pk"),
    UniqueConstraint("title"),
    UniqueConstraint("public_id"),
    schema="blog",
)


users = Table(
    "users",
    metadata,
    Column("id", Integer, autoincrement=True),
    Column("first_name", String(50)),
    Column("last_name", String(50)),
    Column("email", String(254)),
    Column("profile_picture", String(250)),
    Column("username", String(15)),
    Column("is_active", Boolean, nullable=False, server_default="t"),
    Column("role_id", Integer),
    Column("public_id", UUID, nullable=False, server_default=text("gen_random_uuid()")),
    Column("created_at", TIMESTAMP, nullable=False, server_default=now()),
    Column(
        "updated_at",
        TIMESTAMP,
        nullable=False,
        onupdate=now(),
        server_default=now(),
    ),
    PrimaryKeyConstraint("id", name="user_pk"),
    ForeignKeyConstraint(
        [
            "role_id",
        ],
        [
            "blog.roles.id",
        ],
    ),
    UniqueConstraint("email", "username"),
    UniqueConstraint("public_id"),
    schema="blog",
)


users_posts = Table(
    "users_posts",
    metadata,
    Column("id", Integer, autoincrement=True),
    Column("user_id", Integer),
    Column("post_id", Integer),
    Column("likes", ARRAY(UUID)),
    Column("created_at", TIMESTAMP, nullable=False, server_default=now()),
    Column(
        "updated_at",
        TIMESTAMP,
        nullable=False,
        onupdate=now(),
        server_default=now(),
    ),
    PrimaryKeyConstraint("id", name="user_post_pk"),
    ForeignKeyConstraint(
        [
            "user_id",
        ],
        [
            "blog.users.id",
        ],
        onupdate="CASCADE",
        ondelete="SET NULL",
    ),
    ForeignKeyConstraint(
        [
            "post_id",
        ],
        [
            "blog.posts.id",
        ],
        onupdate="CASCADE",
        ondelete="SET NULL",
    ),
    UniqueConstraint("user_id", "post_id"),
    schema="blog",
)

passwords = Table(
    "passwords",
    metadata,
    Column("id", Integer, autoincrement=True),
    Column("password", String(140)),
    Column("salt", String(40)),
    Column("user_id", Integer),
    Column("created_at", TIMESTAMP, nullable=False, server_default=now()),
    Column(
        "updated_at",
        TIMESTAMP,
        nullable=False,
        onupdate=now(),
        server_default=now(),
    ),
    PrimaryKeyConstraint("id", name="password_pk"),
    ForeignKeyConstraint(
        [
            "user_id",
        ],
        [
            "blog.users.id",
        ],
        onupdate="CASCADE",
        ondelete="SET NULL",
    ),
    schema="blog",
)


mapper_registry = registry()

mapper_registry.map_imperatively(
    Role,
    roles,
    properties={
        "_permissions": relationship(
            Permission, secondary=roles_permissions, backref="_roles"
        ),
        "_user": relationship(User, backref="_role"),
    },
)

mapper_registry.map_imperatively(
    Permission,
    permissions,
)

mapper_registry.map_imperatively(
    User,
    users,
    properties={
        "_posts": relationship(Post, secondary=users_posts, backref="_user"),
    },
)

mapper_registry.map_imperatively(
    Post,
    posts,
)

mapper_registry.map_imperatively(
    Password,
    passwords,
    properties={"_user": relationship(User, backref="_password", uselist=False)},
)
