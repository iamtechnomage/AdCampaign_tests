import time
import config

from tests_steps.browser_config import *


def test_go_to_login_page_in_full_hd():
    browser = setup_local_browser(size='Full HD', polling_time=5)
    try:
        browser.get(config.BASE_URL)
        browser.find_element_by_css_selector('body > header > nav > div > div > ul > li > a').click()
        time.sleep(0.3)
        assert browser.current_url == 'https://adcampaigndemo.robonet.me/Auth'
        save_screenshot(browser=browser,
                        test_name='go_to_login_page_in_full_hd')
    finally:
        browser.quit()


def test_go_to_login_page_in_mobile_view():
    browser = setup_local_browser(size='Tablet', polling_time=5)
    try:
        browser.get(config.BASE_URL)
        browser.find_element_by_css_selector('body > header > nav > div > button').click()
        browser.find_element_by_css_selector('body > header > nav > div > div > ul > li > a').click()
        time.sleep(0.3)
        assert browser.current_url == 'https://adcampaigndemo.robonet.me/Auth'
        save_screenshot(browser=browser,
                        test_name='go_to_login_page_in_mobile_view')
    finally:
        browser.quit()
