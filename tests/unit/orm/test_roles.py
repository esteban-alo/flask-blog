"""
Roles repository class tests cases
"""

from uuid import UUID

import pytest

from src.domain.model import Role
from src.orm.repository.roles import RoleRepository
from src.orm.unit_of_work import SQLAlchemyUnitOfWork


@pytest.fixture()
def dummy_role():
    """
    Dummy role for unit tests
    :return:
    """
    dummy_role = Role(
        name="dummy_role", public_id=UUID("4f03aefe-cef7-4352-b814-01d8d704f48f")
    )

    return dummy_role


@pytest.fixture()
def roles_repository():
    """
    Fixture to RoleRepository
    :return:
    """
    unit_of_work = SQLAlchemyUnitOfWork()
    return RoleRepository(unit_of_work)


def test_add(roles_repository, dummy_role):
    """
    Test adding a role
    :param roles_repository:
    :param dummy_role:
    :return:
    """

    result = roles_repository.add(dummy_role)

    assert result.name == dummy_role.name
    assert result.id is not None
    assert result.public_id is not None


def test_all(roles_repository):

    result = roles_repository.all(5, 0)

    assert len(result) > 0


def test_get(roles_repository, dummy_role):

    role = roles_repository.all(5, 0)[-1]

    result = roles_repository.get(role.id)

    assert result.name == "dummy_role"


def test_update(roles_repository, dummy_role):

    role = roles_repository.all(5, 0)[-1]

    roles_repository.update(role.id, name="update_dummy_role")


def test_delete(roles_repository, dummy_role):

    roles_init = roles_repository.all(5, 0)
    role = roles_init[-1]

    roles_repository.delete(role.id)

    roles_updated = roles_repository.all(5, 0)

    assert len(roles_init) != len(roles_updated)
