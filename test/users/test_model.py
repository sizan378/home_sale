import pytest


def test_user_str(base_user):
    '''Test the custom user model string representation'''
    assert base_user.__str__() == f"{base_user.username}"


def test_user_short_name(base_user):
    '''Test the custom user models get_short_name method works'''
    short_name = f"{base_user.username}"
    assert base_user.get_short_name() == short_name


def test_user_full_name(base_user):
    'Test the custom user models get_full_name method works'''
    full_name = f"{base_user.first_name} {base_user.last_name}"
    assert base_user.get_full_name == full_name


def test_base_user_email_is_normalized(base_user):
    '''Test a new user email is normalized'''
    email = "Homesales@GMAIL.COM"
    assert base_user.email == email.lower()


def test_super_user_email_normalized(super_user):
    '''Test a super user email is normalized'''
    email = "homesales@Gmail.COM"
    assert super_user.email == email.lower()


def test_super_user_is_not_staff(user_factory):
    ''' Test that an error is raised when an admin user has is_staff set to false'''
    with pytest.raises(ValueError) as err:
        user_factory.create(is_superuser=True, is_staff=False)
    assert str(err.value) == "Superuser must have is_staff=True"


def test_super_user_is_not_superuser(user_factory):
    ''' Test that an error is raised when and admin user has is_superuser set ot False'''
    with pytest.raises(ValueError) as err:
        user_factory.create(is_superuser=False, is_staff=True)
    assert str(err.value) == "Superuser must be is_superuser=True"


def test_create_user_with_no_email(user_factory):
    '''Test that creating a new user with no email address raise an error'''
    with pytest.raises(ValueError) as err:
        user_factory.create(email=None)
    assert str(err.value) == "Email address is required"


def test_create_user_with_no_username(user_factory):
    '''Test that creating a new user with no username raise an error'''
    with pytest.raises(ValueError) as err:
        user_factory.create(username=None)
    assert str(err.value) == "User must submit a username"


def test_create_user_with_no_firstname(user_factory):
    '''Test that creating a new user with no firstname raise an error'''
    with pytest.raises(ValueError) as err:
        user_factory.create(first_name=None)
    assert str(err.value) == "User must submit a first name"


def test_create_user_with_no_lastname(user_factory):
    '''Test that creating a new user with no lastname raise an error'''
    with pytest.raises(ValueError) as err:
        user_factory.create(last_name=None)
    assert str(err.value) == "User must submit a last name"


def test_create_superuser_with_no_email(user_factory):
    'Test that creating a new superuser with no email address raise an error'''
    with pytest.raises(ValueError) as err:
        user_factory.create(email=None, is_superuser=True, is_staff=True)
    assert str(err.value) == "Email address is required"

def test_create_superuser_with_no_password(user_factory):
    'Test that creating a new superuser with no password raise an error'
    with pytest.raises(ValueError) as err:
        user_factory.create(password=None, is_superuser=True, is_staff=True)
    assert str(err.value) == "Superuser must have password"

def test_user_email_invalid(user_factory):
    'Test that an error is raised when an invalid email address is provided'
    with pytest.raises(ValueError) as err:
        user_factory.create(email='invalid')
    assert str(err.value) == "you must provide valid email"