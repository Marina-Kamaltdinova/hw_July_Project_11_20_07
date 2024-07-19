from selene import browser, command, have
from demoqa_tests import resources
from test_data.user import User
import allure


class RegistrationPage:
    def open(self):
        with allure.step("Открыть браузер"):
            browser.open('/automation-practice-form')
            return self

    def type_first_name(self, name):
        with allure.step("Ввод имени"):
            browser.element('#firstName').type(name)
            return self

    def type_last_name(self, lastname):
        with allure.step("Ввод фамилии"):
            browser.element('#lastName').type(lastname)
            return self

    def type_email(self, email):
        with allure.step("Ввод почты"):
            browser.element('#userEmail').type(email)
            return self

    def click_gender(self):
        with allure.step("Выбор пола"):
            browser.element('[for="gender-radio-2"]').click()
            return self

    def type_number(self, number):
        with allure.step("Ввести номер телефона"):
            browser.element("#userNumber").type(number)
            return self

    def type_subject(self, subject):
        with allure.step("Выбор тематики"):
            browser.element('#subjectsInput').type(subject).press_enter()
            return self

    def type_birthday(self, month, year, day):
        with allure.step("Выбор даты рождения"):
            browser.element('#dateOfBirthInput').perform(command.js.scroll_into_view).click()
            browser.element('.react-datepicker__month-select').type(month)
            browser.element('.react-datepicker__year-select').click()
            browser.element('.react-datepicker__year-select').element(f'[value="{year}"]').click()
            browser.element(f'.react-datepicker__day--0{day}').click()
            return self

    def type_hobbies(self):
        with allure.step("ОВыбор хобби"):
            browser.element('[for="hobbies-checkbox-1"]').click()
            return self

    def upload_photo(self, photo):
        with allure.step("Загрузить фото"):
            browser.element('#uploadPicture').set_value(resources.resources_path(photo))
            return self

    def type_address(self, address):
        with allure.step("Ввод адреса"):
            browser.element('#currentAddress').type(address).press_enter()
            return self

    def type_state(self, state):
        with allure.step("Выбор штата"):
            browser.element("#react-select-3-input").type(state).press_enter()
            return self

    def type_city(self, city):
        with allure.step("Выбор города"):
            browser.element("#react-select-4-input").type(city).press_enter()
            return self

    def click_submit(self):
        with allure.step("Отправка формы"):
            browser.element('#submit').press_enter()
            return self

    def register(self, marina: User):
        self.type_first_name(marina.name)
        self.type_last_name(marina.lastname)
        self.type_email(marina.email)
        self.click_gender()
        self.type_number(marina.number)
        self.type_subject(marina.subject)
        self.type_birthday(marina.birthday_month, marina.birthday_year, marina.birthday_day)
        self.type_hobbies()
        self.upload_photo(marina.photo)
        self.type_address(marina.address)
        self.type_state(marina.state)
        self.type_city(marina.city)
        self.click_submit()

    def should_have_registered(self, marina: User):
        with allure.step("Проверка заполненных данных"):
            browser.element('.table').all('td').even.should(have.exact_texts(f'{marina.name} {marina.lastname}',
                                                                             f'{marina.email}',
                                                                             f'{marina.gender}',
                                                                             f'{marina.number}',
                                                                             f'{marina.birthday_day} {marina.birthday_month},{marina.birthday_year}',
                                                                             f'{marina.subject}',
                                                                             f'{marina.hobbies}',
                                                                             f'{marina.photo}',
                                                                             f'{marina.address}',
                                                                             f'{marina.state} {marina.city}'))


registration = RegistrationPage()
