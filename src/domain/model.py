"""
Moodels class
"""

from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional
from uuid import UUID


@dataclass
class TableBase:
    """
    Table base model definition
    """

    id: Optional[int]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]


@dataclass
class TableQuery(TableBase):
    """
    Model can be queried
    """

    public_id: Optional[UUID]


@dataclass
class Role(TableQuery):
    """
    Role model definition
    """

    name: str


@dataclass
class Permission(TableQuery):
    """
    Permission model definition
    """

    name: str


@dataclass
class RolePermission(TableBase):
    """
    RolePermission model definition
    """

    permission_id: id
    role_id: id


@dataclass
class Post(TableQuery):
    """
    Post model definition
    """

    tite: str
    text: str
    tags: List[str]
    url_path: str
    enabled: bool


@dataclass
class User(TableQuery):
    """
    User model definition
    """

    first_name: str
    last_name: str
    email: str
    profile_picture: Optional[str]
    username: str
    is_active: bool
    role_id: int


@dataclass
class UserPost(TableBase):
    """
    UserPost model definition
    """

    post_id: id
    user_id: id


@dataclass
class Password(TableQuery):
    """
    User model definition
    """

    password: str
    salt: str
    user_id: int
