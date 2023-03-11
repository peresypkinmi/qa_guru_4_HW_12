from selene.support.shared import browser
from selene import be, have, command
import os
import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


def test_fill_and_submit_form(open_base_page):
    browser.element('.main-header').should(have.exact_text('Practice Form'))
    browser.element('#firstName').type('testName')
    browser.element('#lastName').type('testName')
    browser.element('#userEmail').type('testName@test.kk')
    browser.element('#gender-radio-1').type(' ')
    browser.element('#userNumber').type('9232455644')
    browser.element('#dateOfBirthInput').click()
    browser.element("[value='2000']").click()
    browser.element("[aria-label='Choose Friday, March 10th, 2000']").click()
    browser.element("#subjectsInput").click()
    browser.element("#subjectsInput").type('Maths').press(Keys.ENTER)
    browser.element("#subjectsInput").type('History').press(Keys.ENTER)
    browser.element("#hobbies-checkbox-2").type(' ')
    browser.element("#uploadPicture").type(os.getcwd()+'/testPicture.png')
    browser.element("#currentAddress").type('testAddress')
    browser.element("#react-select-3-input").type('Rajasthan').press(Keys.ENTER)
    browser.element("#react-select-4-input").type('Jaipur').press(Keys.ENTER)
    browser.element("#submit").press(Keys.ENTER)
    browser.element("[class='modal-title h4']").should(have.exact_text('Thanks for submitting the form'))
