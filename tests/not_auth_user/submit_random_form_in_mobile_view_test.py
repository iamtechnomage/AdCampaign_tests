import time
from random import choice

import config

from tests_steps.banners_steps import *
from tests_steps.browser_config import *

browser = setup_browser(size='Tablet', polling_time=5)

try:
    browser.get(config.BASE_URL)
    banners_row = browser.find_elements_by_css_selector('body > div.container > main > div > div:nth-child(2) > div.position-relative')
    banner = choice(banners_row)
    banner.click()
    time.sleep(0.3)
    banner_form = banner.find_element_by_css_selector('form')
    fill_input_field(form=banner_form,
                     input_selector='div.form-group.mb-4',
                     email_value=f'filling_test{randint(1, 1000)}@local.ad')
    banner_form.find_element_by_css_selector('div.mt-1 > button.btn.btn-primary').click()
    save_screenshot(browser=browser,
                    test_name='filling_and_submit_form_in_mobile_view_test')

finally:
    browser.quit()
