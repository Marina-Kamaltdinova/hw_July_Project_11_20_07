from pages.registration_page import registration
from test_data import user


def test_registration_demoqa():
    registration.open()
    marina = user.marina
    registration.register(marina)
    registration.should_have_registered(marina)

