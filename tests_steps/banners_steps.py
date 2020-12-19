from random import randint


def check_banner_visibility_by_css_selector(browser, css_selector: str, visibility: bool):
    banner = browser.find_element_by_css_selector(css_selector)
    assert banner.is_displayed() is visibility


def check_banner_visibility_by_banner_object(banner, visibility: bool):
    assert banner.is_displayed() is visibility


def fill_input_field(form, input_selector: str, email_value: str = None, password_value: str = None):
    form_input_fields = form.find_elements_by_css_selector(input_selector)
    for element_number in range(0, len(form_input_fields)):
        input_label = form_input_fields[element_number].find_element_by_css_selector('label').text
        input_field = form_input_fields[element_number].find_element_by_css_selector('input')
        if input_label == 'Email':
            input_field.send_keys(email_value)
        elif input_label == 'Телефон':
            input_field.send_keys(f'{randint(1000000000, 9999999999)}')
        elif input_label == 'Пароль':
            input_field.send_keys(password_value)


def check_free_space_banner(browser, small_banners):
    if len(small_banners) <= 4:
        free_space_banner = browser.find_element_by_css_selector(
            f'body > div.container > main > div > div:nth-child(2) > div:nth-child({len(small_banners)})')
        assert free_space_banner.text == 'Это место сейчас свободно, мы готовы с вами сотрудничать, напишите нам\nadmin@test.local', free_space_banner.text
