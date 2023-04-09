from pages.registration_form_page import RegistrationForm
from data.User import User


def test_fill_and_submit_form(set_options_in_browser):

    ivan = User(subjects=('Maths', 'History'), firstname='Ivan', lastname='Ivanov', email='testName@test.kk',
                phone='9232455644', address='testAddress', state='Rajasthan', city='Jaipur')
    form = RegistrationForm()

    form.open_student_registration_form()

    form.fill_registration_form(ivan)

    form.submit_form()

    form.assert_typed_form()
