from pages.registration_form_page import RegistrationForm


def test_fill_and_submit_form(set_options_in_browser):

    form = RegistrationForm()

    form.open_student_registration_form()

    form.type_first_name_field('Ivan')
    form.type_last_name_field('Ivanov')
    form.type_email_field('testName@test.kk')
    form.choose_radio_male_gender()
    form.type_phone_field('9232455644')
    form.choose_date_of_birth()
    form.choose_subjects('Maths', 'History')
    form.choose_hobbies()
    form.upload_picture()
    form.type_current_address('testAddress')
    form.select_state('Rajasthan')
    form.select_city('Jaipur')

    form.submit_form()

    form.assert_typed_form()
