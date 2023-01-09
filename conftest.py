import pytest
from pytest_factoryboy import register
from test.factories import UserProfileFactory, UserFactory, EnquireFactory, PropertiesFactory


register(UserProfileFactory)
register(UserFactory)
register(EnquireFactory)
register(PropertiesFactory)



@pytest.fixture
def base_user(db, user_factory):
    new_user = user_factory.create()
    return new_user


@pytest.fixture
def super_user(db, user_factory):
    new_user = user_factory.create(is_staff=True, is_superuser=True)
    return new_user


@pytest.fixture
def profile(db, user_profile_factory):
    user_profile = user_profile_factory.create()
    return user_profile


@pytest.fixture
def enquire(db, enquire_factory):
    new_enquire = enquire_factory.create()
    return new_enquire

@pytest.fixture
def properties(db, properties_factory):
    new_properties = properties_factory.create()
    return new_properties