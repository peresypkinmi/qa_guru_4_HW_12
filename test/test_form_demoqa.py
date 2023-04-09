from pages.registration_form_page import RegistrationForm


def test_fill_and_submit_form(set_options_in_browser):
    form = RegistrationForm()

    form.open_student_registration_form()

    form.fill_registration_form('Maths', 'History', first_name='Ivan', last_name='Ivanov', email='testName@test.kk',
                                phone='9232455644', address='testAddress', state='Rajasthan', city='Jaipur')

    form.submit_form()

    form.assert_typed_form()
