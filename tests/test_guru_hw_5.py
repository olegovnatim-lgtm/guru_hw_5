from selene.support.conditions import have
from selene import browser
from pathlib import Path


def test_guru_hw_5(driver):

    browser.open('https://demoqa.com/automation-practice-form')

    browser.element('#firstName').type('Nastya')

    browser.element('#lastName').type('Timofeeva')

    browser.element('#userEmail').type('test@test.ru')

    browser.element('[for="gender-radio-2"]').click()

    browser.element('#userNumber').type('7999852456')

    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click()
    browser.element('//option[@value="2"]').click()
    browser.element('//option[@value="2007"]').click()
    browser.element('[aria-label="Choose Thursday, March 8th, 2007"]').click()

    browser.element('#subjectsInput').type('Maths').press_enter()

    browser.element('[for="hobbies-checkbox-2"]').click()

    browser.element('#uploadPicture').send_keys(str(Path(__file__).parent.parent) + "\\test_file.pdf")

    browser.element('#currentAddress').type('Moscow')

    browser.element('#state').click()
    browser.element('#react-select-3-option-2').click()

    browser.element('#city').click()
    browser.element('#react-select-4-option-0').click()

    browser.element('#submit').click()

    browser.element('.modal-body table tbody').all('tr').should(
        have.exact_texts(
            'Student Name Nastya Timofeeva',
            'Student Email test@test.ru',
            'Gender Female',
            'Mobile 7999852456',
            'Date of Birth 08 March,2007',
            'Subjects Maths',
            'Hobbies Reading',
            'Picture test_file.pdf',
            'Address Moscow',
            'State and City Haryana Karnal'
        )
    )

    browser.element('#closeLargeModal').click()
