import os
from selene import be, have
from selene.support.shared import browser
from selenium.webdriver import Keys
from data.User import User



class RegistrationForm:

    def open_student_registration_form(self):
        browser.open('automation-practice-form')


    def type_first_name_field(self, value):
        browser.element('#firstName').type(value)


    def type_last_name_field(self, value):
        browser.element('#lastName').type(value)


    def type_email_field(self, value):
        browser.element('#userEmail').type(value)


    def choose_radio_male_gender(self):
        browser.element('[for=gender-radio-1]').click()


    def type_phone_field(self, value):
        browser.element('#userNumber').type(value)



    def choose_date_of_birth(self):
        browser.element('#dateOfBirthInput').click()
        browser.element(f'[value="2000"]').click()
        browser.element(f'option[value="2"]').click()
        browser.element(f'[aria-label="Choose Friday, March 10th, 2000"]').click()


    def choose_subjects(self, subjects):
        browser.element("#subjectsInput").click()
        [browser.element("#subjectsInput").type(subject).press(Keys.ENTER) for subject in subjects]


    def choose_hobbies(self):
        browser.element("[for=hobbies-checkbox-2]").should(be.clickable).click()


    def upload_picture(self):
        os.chdir(f'{os.getcwd()}/source')
        browser.element("#uploadPicture").type(os.getcwd() + '/testPicture.png')


    def type_current_address(self, value):
        browser.element("#currentAddress").type(value)


    def select_state(self, value):
        browser.element("#react-select-3-input").type(value).press(Keys.ENTER)


    def select_city(self, value):
        browser.element("#react-select-4-input").type(value).press(Keys.ENTER)


    def submit_form(self):
        browser.element("#submit").press(Keys.ENTER)


    def fill_registration_form(self, User):
        self.type_first_name_field(User.firstname)
        self.type_last_name_field(User.lastname)
        self.choose_radio_male_gender()
        self.choose_date_of_birth()
        self.type_phone_field(User.phone)
        self.type_email_field(User.email)
        self.type_current_address(User.address)
        self.choose_subjects(User.subjects)
        self.choose_hobbies()
        self.upload_picture()
        self.select_state(User.state)
        self.select_city(User.city)


    def assert_typed_form(self):
        browser.element("[class='modal-title h4']").should(have.exact_text('Thanks for submitting the form'))
        browser.all("table>tbody>tr:nth-of-type(1)").should(have.exact_texts('Student Name Ivan Ivanov'))
        browser.all("table>tbody>tr:nth-of-type(2)").should(have.exact_texts('Student Email testName@test.kk'))
        browser.all("table>tbody>tr:nth-of-type(3)").should(have.exact_texts('Gender Male'))
        browser.all("table>tbody>tr:nth-of-type(4)").should(have.exact_texts('Mobile 9232455644'))
        browser.all("table>tbody>tr:nth-of-type(5)").should(have.exact_texts('Date of Birth 10 March,2000'))
        browser.all("table>tbody>tr:nth-of-type(6)").should(have.exact_texts('Subjects Maths, History'))
        browser.all("table>tbody>tr:nth-of-type(7)").should(have.exact_texts('Hobbies Reading'))
        browser.all("table>tbody>tr:nth-of-type(8)").should(have.exact_texts('Picture testPicture.png'))
        browser.all("table>tbody>tr:nth-of-type(9)").should(have.exact_texts('Address testAddress'))
        browser.all("table>tbody>tr:nth-of-type(10)").should(have.exact_texts('State and City Rajasthan Jaipur'))












