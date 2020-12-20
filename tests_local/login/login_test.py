import config

from tests_steps.banners_steps import *
from tests_steps.browser_config import *


def test_login_as_admin():
    browser = setup_local_browser(size='Full HD', polling_time=5)
    try:
        browser.get(config.AUTH_URL)
        auth_form = browser.find_element_by_css_selector('body > div.container > main > div > div:nth-child(2) > form')
        fill_input_field(form=auth_form,
                         input_selector='div.form-group',
                         email_value=config.AUTH_CREDENTIALS['administrator']['email'],
                         password_value=config.AUTH_CREDENTIALS['administrator']['password'])
        auth_form.find_element_by_css_selector('button.btn.btn-primary').click()
        assert browser.find_element_by_css_selector('body > header > nav > div > div > span').text == 'Привет, Test Admin'
        save_screenshot(browser=browser,
                        test_name='login_as_admin_test')
    finally:
        browser.quit()


def test_login_as_advertiser():
    browser = setup_local_browser(size='Full HD', polling_time=5)
    try:
        browser.get(config.AUTH_URL)
        auth_form = browser.find_element_by_css_selector('body > div.container > main > div > div:nth-child(2) > form')
        fill_input_field(form=auth_form,
                         input_selector='div.form-group',
                         email_value=config.AUTH_CREDENTIALS['advertiser']['email'],
                         password_value=config.AUTH_CREDENTIALS['advertiser']['password'])
        auth_form.find_element_by_css_selector('button.btn.btn-primary').click()
        assert browser.find_element_by_css_selector(
            'body > header > nav > div > div > span').text == 'Привет, Рекламодатель для создания рекламы'
        save_screenshot(browser=browser,
                        test_name='login_as_advertiser_test')
    finally:
        browser.quit()


def test_login_as_banned_advertiser():
    browser = setup_local_browser(size='Full HD', polling_time=5)
    try:
        browser.get(config.AUTH_URL)
        auth_form = browser.find_element_by_css_selector('body > div.container > main > div > div:nth-child(2) > form')
        fill_input_field(form=auth_form,
                         input_selector='div.form-group',
                         email_value=config.AUTH_CREDENTIALS['banned']['email'],
                         password_value=config.AUTH_CREDENTIALS['banned']['password'])
        auth_form.find_element_by_css_selector('button.btn.btn-primary').click()
        assert browser.find_element_by_css_selector(
            'body > div.container > main > div > div:nth-child(3) > div').text == 'Вы заблокированы пользователем MainAdmin'
        save_screenshot(browser=browser, test_name='login_as_banned_advertiser_test')
    finally:
        browser.quit()


def test_login_as_moderator():
    browser = setup_local_browser(size='Full HD', polling_time=5)
    try:
        browser.get(config.AUTH_URL)
        auth_form = browser.find_element_by_css_selector('body > div.container > main > div > div:nth-child(2) > form')
        fill_input_field(form=auth_form,
                         input_selector='div.form-group',
                         email_value=config.AUTH_CREDENTIALS['moderator']['email'],
                         password_value=config.AUTH_CREDENTIALS['moderator']['password'])
        auth_form.find_element_by_css_selector('button.btn.btn-primary').click()
        assert browser.find_element_by_css_selector(
            'body > header > nav > div > div > span').text == 'Привет, Test Moderator'
        save_screenshot(browser=browser,
                        test_name='login_as_moderator_test')
    finally:
        browser.quit()
