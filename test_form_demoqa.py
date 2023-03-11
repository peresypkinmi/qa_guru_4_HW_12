from selene.support.shared import browser
from selene import be, have, command
import pytest


def test_fill_and_submit_form(open_base_page):
    browser.element('.main-header').should(have.exact_text('Practice Form'))
    browser.element('#firstName').type('testName')
    browser.element('#lastName').type('testName')
    browser.element('#gender-radio-1').type(' ')
    browser.element('#userNumber').type('9232455644')
    browser.element('#dateOfBirthInput').click()
    browser.element("[value='2000']").click()
    browser.element("[aria-label='Choose Friday, March 10th, 2000']").click()
    pass