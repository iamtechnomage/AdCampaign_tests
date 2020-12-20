"""Set up all the configuration variables"""
BASE_URL = "https://adcampaigndemo.robonet.me/"
AUTH_URL = "https://adcampaigndemo.robonet.me/Auth"
BROWSERSTACK_URL = 'https://bsuser7502156758:g272SmXwnCsHJjHDsAqS@hub-cloud.browserstack.com/wd/hub'

AUTH_CREDENTIALS = {
    'administrator': {'email': 'test_admin@local.ad',
                      'password': 'testpassword'},
    'moderator': {'email': 'test_moderator@local.ad',
                  'password': 'testpassword'},
    'advertiser': {'email': 'test_advertiser@local.ad',
                   'password': 'testpassword'},
    'banned': {'email': 'test_banned@local.ad',
               'password': 'testpassword'},
}

desired_cap = {
    'Windows10': {
        'bstack:options': {
            "os": "Windows",
            "osVersion": "10",
            "resolution": "1920x1080",
            "local": "false",
            "seleniumVersion": "3.14.0",
        },
        "browserName": "Chrome",
        "browserVersion": "latest",
    },
    'OSX_Catalina': {
        'bstack:options': {
            "os": "OS X",
            "osVersion": "Catalina",
            "resolution": "1920x1080",
            "local": "false",
            "seleniumVersion": "3.141.0",
        },
        "browserName": "Edge",
        "browserVersion": "latest",
        }
}
