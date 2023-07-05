import pytest
import random
from pages.auth_page import AuthPage
from pages.reg_page import RegPage
from settings import valid_email, valid_password, valid_login, valid_phone, valid_ls
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def test_start_page_is_correct(web_browser):
    page = AuthPage(web_browser)
    phone_tab_class = page.phone_tab.get_attribute("class")
    assert phone_tab_class == "rt-tab rt-tab--small rt-tab--active"
    assert page.phone.is_clickable()
    assert page.password.is_clickable()
    assert page.btn_login.is_clickable()
    assert page.registration_link.is_clickable()
    assert page.auth_title.get_text() == "Авторизация"
    assert page.logo_lk.get_text() == "Личный кабинет"

def test_authorization_login(web_browser):
    page = AuthPage(web_browser)
    page.login.send_keys(valid_login)
    page.password.send_keys(valid_password)
    page.btn.click()
    assert page.get_current_url() == 'https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid&state=37cec9d6-3649-4413-88d2-17697d1ea409&theme&auth_type'

def test_authorization_email(web_browser):
    page = AuthPage(web_browser)
    page.email.send_keys(valid_email)
    page.password.send_keys(valid_password)
    page.btn.click()
    assert page.get_current_url() == 'https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid&state=37cec9d6-3649-4413-88d2-17697d1ea409&theme&auth_type'

def test_authorization_phone(web_browser):
    page = AuthPage(web_browser)
    page.phone.send_keys(valid_phone)
    page.password.send_keys(valid_password)
    page.btn.click()
    assert page.get_current_url() == 'https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid&state=37cec9d6-3649-4413-88d2-17697d1ea409&theme&auth_type'

def test_authorization_ls(web_browser):
    page = AuthPage(web_browser)
    page.ls.send_keys(valid_ls)
    page.password.send_keys(valid_password)
    page.btn.click()
    assert page.get_current_url() == 'https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid&state=37cec9d6-3649-4413-88d2-17697d1ea409&theme&auth_type'

def test_registration_page_with_empty_name_field(web_browser):
    auth_page = AuthPage(web_browser)
    auth_page.registration_link.click()
    reg_page = RegPage(web_browser)
    reg_page.name_field.send_keys("")
    reg_page.last_name_field.send_keys("Мусина")
    reg_page.email_or_mobile_phone_field.send_keys("test@mail.ru")
    reg_page.password_field.send_keys("Lmm123")
    reg_page.password_confirmation_field.send_keys("Lmm123")
    reg_page.continue_button.click()
    reg_page.error_message_name.is_visible()
    assert reg_page.error_message_name.get_text() == "Необходимо заполнить поле кириллицей. От 2 до 30 символов."

def test_registration_with_an_incorrect_value_in_the_last_name_field(web_browser):
    auth_page = AuthPage(web_browser)
    auth_page.registration_link.click()
    reg_page = RegPage(web_browser, auth_page.get_current_url())
    reg_page.name_field.send_keys("Елезавета")
    reg_page.last_name_field.send_keys("фывапмтоклтмоалвдолдыьлутдокшипеоироалвтолатусольскудьалукцаблукдаьылтокл")
    reg_page.email_or_mobile_phone_field.send_keys("test123@mail.ru")
    reg_page.password_field.send_keys("Lmm123")
    reg_page.password_confirmation_field.send_keys("Lmm123")
    reg_page.continue_button.click()
    reg_page.error_message_name.is_visible()
    assert reg_page.error_message_last_name.get_text() == "Необходимо заполнить поле кириллицей. От 2 до 30 символов."

def test_pass_recovery_login(web_browser):
    page = AuthPage(web_browser)
    page.recovery.click()
    page.login.send_keys(valid_login)
    symbols = page.captcha.get_text()
    page.symbol.send_keys(symbols)
    page.contin.click()
    page2 = pytest.driver.get('https://e.mail.ru/inbox/')
    element = WebDriverWait(webdriver, 10).until(
        EC.text_to_be_present_in_element(By.TAG_NAME, 'div > span', 'Код подтверждения')
    )
    page2.element.click()
    element2 = webdriver.find_element(By.TAG_NAME, 'div > p')
    for i in element2:
        numb = i.text.split(' ')
        number = numb[2]
        my_code = number.get_text()
    page = AuthPage(web_browser)
    page.rt_code.send_keys(my_code)
    new_pass = random
    page.new_pass.send_keys(new_pass)
    page.confirm.send_keys(new_pass)
    page.save.click()
    assert page.get_current_url() == 'https://start.rt.ru/?tab=main'
