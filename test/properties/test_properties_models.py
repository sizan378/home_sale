import pytest


def test_property_user(properties):
    ''' Test properties name field with user name '''
    name = properties.user
    assert properties.user == name