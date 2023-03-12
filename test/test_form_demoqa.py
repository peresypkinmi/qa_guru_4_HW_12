from operator import and_

from selene.support.shared import browser
from selene import be, have
import os
from selenium.webdriver.common.keys import Keys


def test_fill_and_submit_form(set_options_in_browser):
    browser.open('automation-practice-form')
    browser.element('.main-header').should(have.exact_text('Practice Form'))
    browser.element('#firstName').should(be.blank).type('testName')
    browser.element('#lastName').should(be.blank).type('testLastName')
    browser.element('#userEmail').should(be.blank).type('testName@test.kk')
    browser.element('[for=gender-radio-1]').should(be.clickable).click()
    browser.element('#userNumber').should(be.blank).type('9232455644')
    browser.element('#dateOfBirthInput').should(be.clickable).click()
    browser.element("[value='2000']").click()
    browser.element("[aria-label='Choose Friday, March 10th, 2000']").should(be.clickable).click()
    browser.element("#subjectsInput").should(be.blank).click()
    browser.element("#subjectsInput").should(be.blank).type('Maths').press(Keys.ENTER)
    browser.element("#subjectsInput").should(be.blank).type('History').press(Keys.ENTER)
    browser.element("[for=hobbies-checkbox-2]").should(be.clickable).click()
    browser.element("#uploadPicture").type(os.getcwd()+'/testPicture.png')
    browser.element("#currentAddress").should(be.blank).type('testAddress')
    browser.element("#react-select-3-input").should(be.blank).type('Rajasthan').press(Keys.ENTER)
    browser.element("#react-select-4-input").should(be.blank).type('Jaipur').press(Keys.ENTER)
    browser.element("#submit").should(be.clickable).press(Keys.ENTER)
    browser.element("[class='modal-title h4']").should(have.exact_text('Thanks for submitting the form'))
    browser.all("table>tbody>tr:nth-of-type(1)").should(have.exact_texts('Student Name testName testLastName'))
    browser.all("table>tbody>tr:nth-of-type(2)").should(have.exact_texts('Student Email testName@test.kk'))
    browser.all("table>tbody>tr:nth-of-type(3)").should(have.exact_texts('Gender Male'))
    browser.all("table>tbody>tr:nth-of-type(4)").should(have.exact_texts('Mobile 9232455644'))
    browser.all("table>tbody>tr:nth-of-type(5)").should(have.exact_texts('Date of Birth 10 March,2000'))
    browser.all("table>tbody>tr:nth-of-type(6)").should(have.exact_texts('Subjects Maths, History'))
    browser.all("table>tbody>tr:nth-of-type(7)").should(have.exact_texts('Hobbies Reading'))
    browser.all("table>tbody>tr:nth-of-type(8)").should(have.exact_texts('Picture testPicture.png'))
    browser.all("table>tbody>tr:nth-of-type(9)").should(have.exact_texts('Address testAddress'))
    browser.all("table>tbody>tr:nth-of-type(10)").should(have.exact_texts('State and City Rajasthan Jaipur'))
    browser.element('#closeLargeModal').should(be.clickable).click()

