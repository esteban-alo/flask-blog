"""
Permissions repository class tests cases
"""

from uuid import UUID

import pytest

from src.domain.model import Permission
from src.orm.repository.permissions import PermissionRepository
from src.orm.unit_of_work import SQLAlchemyUnitOfWork


@pytest.fixture()
def dummy_permission():
    """
    Dummy permission for unit tests
    :return:
    """
    dummy_permission = Permission(
        name="dummy_permission", public_id=UUID("692564ec-8a17-4b9d-a940-2ed1def6a37b")
    )

    return dummy_permission


@pytest.fixture()
def permission_repository():
    """
    Fixture to RoleRepository
    :return:
    """
    unit_of_work = SQLAlchemyUnitOfWork()
    return PermissionRepository(unit_of_work)


def test_add(permission_repository, dummy_permission):
    """
    Test adding a role
    :param permission_repository:
    :param dummy_permission:
    :return:
    """

    result = permission_repository.add(dummy_permission)

    assert result.name == dummy_permission.name
    assert result.id is not None
    assert result.public_id == dummy_permission.public_id


def test_all(permission_repository):

    result = permission_repository.all(5, 0)

    assert len(result) > 0


def test_get(permission_repository, dummy_permission):

    permission = permission_repository.all(100, 0)[-1]

    result = permission_repository.get(permission.id)

    assert result.name == "dummy_permission"


def test_update(permission_repository, dummy_permission):

    role = permission_repository.all(5, 0)[-1]

    permission_repository.update(role.id, name="update_dummy_permission")


def test_delete(permission_repository):

    permission_init = permission_repository.all(100, 0)
    permission = permission_init[-1]

    permission_repository.delete(permission.id)

    permissions_updated = permission_repository.all(5, 0)

    assert len(permission_init) != len(permissions_updated)
