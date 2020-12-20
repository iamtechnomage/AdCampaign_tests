import config
import pathlib

from time import strftime
from selenium import webdriver


def setup_local_browser(size, polling_time: int):
    """

    :param polling_time: items load timeout (in seconds)
    :param size: available 'Mobile S': 320, 'Mobile M': 375, 'Mobile L': 425, 'Tablet': 768, 'Laptop': 1024, 'Laptop L': 1440, 'Full HD': 1980

    :return webdriver.Driver object
    """
    browser = webdriver.Chrome()
    browser.implicitly_wait(polling_time)
    size_list = {'Mobile S': 320, 'Mobile M': 375, 'Mobile L': 425, 'Tablet': 768, 'Laptop': 1024, 'Laptop L': 1440, 'Full HD': 1980}
    if size in size_list:
        browser.set_window_size(size_list[size], 1000)
    else:
        print('This size is not available, check size_list in browser_config.py for available sizes. \n Test aborted')
        browser.quit()
    return browser


def setup_remote_browser(os: str, size: str, polling_time: int):
    """

    :param os: OS in remote host (available OSX_Catalina/Edge use OSX_Catalina and Windows10/Chrome use Windows10)
    :param polling_time: items load timeout (in seconds)
    :param size: available 'Mobile S': 320, 'Mobile M': 375, 'Mobile L': 425, 'Tablet': 768, 'Laptop': 1024, 'Laptop L': 1440, 'Full HD': 1980

    :return webdriver.Driver object
    """
    browser = webdriver.Remote(command_executor=config.BROWSERSTACK_URL,
                               desired_capabilities=config.desired_cap[os])
    browser.implicitly_wait(polling_time)
    size_list = {'Mobile S': 320, 'Mobile M': 375, 'Mobile L': 425, 'Tablet': 768, 'Laptop': 1024, 'Laptop L': 1440, 'Full HD': 1980}
    if size in size_list:
        browser.set_window_size(size_list[size], 1000)
    else:
        print('This size is not available, check size_list in browser_config.py for available sizes. \n Test aborted')
        browser.quit()
    return browser


def save_screenshot(browser, test_name: str):
    browser.save_screenshot(f'{pathlib.Path(__file__).parent.parent.absolute()}/screenshots/{test_name}_{strftime("%Y_%m_%d_%H_%M_%S")}.png')
