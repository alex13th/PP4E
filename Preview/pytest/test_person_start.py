import pytest

from person_start import Person

def test_person_create():
    bob = Person('Bob Smith', 42, 30000, 'software')
    sue = Person('Sue Jones', 45, 40000, 'hardware')

    assert bob.name == 'Bob Smith'
    assert sue.pay == 40000


def test_person_giveRaise():
    sue = Person('Sue Jones', 45, 40000, 'hardware')
    sue.giveRaise(0.2)

    assert sue.pay == 48000


def test_person_lastName():
    sue = Person('Sue Jones', 45, 40000, 'hardware')

    assert sue.lastName() == 'Jones'
