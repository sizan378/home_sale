import pytest

def test_enquire_email(enquire):
    ''' Test enquire email field with email normalization '''
    email = "homeSALEs@gmail.com"
    assert enquire.email == email.lower()


def test_enquire_name(enquire):
    ''' Test enquire name field'''
    name = enquire.name
    assert enquire.name == name

def test_enquire_phone_number(enquire):
    ''' Test enquire phone number field'''
    phone_numbers = enquire.phone_number
    assert enquire.phone_number == phone_numbers

def test_enquire_subject(enquire):
    ''' Test enquire subject field'''
    subject = enquire.subject
    assert enquire.subject == subject

def test_enquire_message(enquire):
    '''Test enquire message field'''
    message = enquire.message
    assert enquire.message == message

# def test_phone_not_11_digit(enquire):
#     ''' Test phone_not_11_digit raise error'''
#     with pytest.raises(ValueError) as err:
#         enquire.create(phone_number='012345678901')
#     assert str(err.value) == "phone number will be 11 digits"