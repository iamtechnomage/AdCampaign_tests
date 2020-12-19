import config

from tests_steps.banners_steps import *
from tests_steps.browser_config import *

browser = setup_browser(size='Tablet', polling_time=5)

try:
    browser.get(config.BASE_URL)
    check_banner_visibility_by_css_selector(browser=browser,
                                            css_selector='body > div.container > main > div > div.row.position-relative.d-none.d-lg-flex > div.col-12.d-none.d-lg-flex',
                                            visibility=False)
    small_banners = browser.find_elements_by_css_selector('body > div.container > main > div > div:nth-child(2) > div')
    for banner_number in range(0, len(small_banners)):
        check_banner_visibility_by_banner_object(banner=small_banners[banner_number], visibility=True)
    save_screenshot(browser=browser, test_name='banners_in_mobile_view_test')

finally:
    browser.quit()
