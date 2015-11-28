import pytest


@pytest.fixture
def ascribe_wrapper():
    from ascribe import AscribeWrapper
    token = 'token'
    return AscribeWrapper(token)
