from pages.base import WebPage
from pages.elements import WebElement

class AuthPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = 'https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid&state=37cec9d6-3649-4413-88d2-17697d1ea409&theme&auth_type'

        super().__init__(web_driver, url)

    phone = WebElement(id='username')
    password = WebElement(id='password')
    login = WebElement(id='username')
    email = WebElement(id='username')
    ls = WebElement(id='username')
    code = WebElement(id='back_to_otp_btn')
    auth_code = WebElement(id='address')
    get_code = WebElement(id='otp_get_code')
    rt_code = WebElement(id='rt-code-0')
    btn = WebElement(id='kc-login')
    recovery = WebElement(id='forgot_password')
    captcha = WebElement(alt='Captcha')
    symbol = WebElement(id='captcha')
    contin = WebElement(id='reset')
    new_pass = WebElement(id='password-new')
    auth_title = WebElement(xpath='//*[@id="page-right"]/div/div/h1')
    registration_link = WebElement(id='kc-register')
    phone_tab = WebElement(id='t-btn-tab-phone')
    logo_lk = WebElement(xpath='//*[@id="page-left"]/div/div[2]/h2')
    auth_form = WebElement(xpath='//*[@id="page-left"]/div/div')
    lk_form = WebElement(xpath='//*[@id="page-right"]/div/div[2]')
    message_invalid_username_or_password = WebElement(xpath='//*[@id="page-right"]/div/div/p')
    the_element_forgot_the_password = WebElement(xpath='//*[@id="forgot_password"]')