"""Set up all the configuration variables needed for run.py"""
BASE_URL = "https://adcampaigndemo.robonet.me/"
AUTH_URL = "https://adcampaigndemo.robonet.me/Auth"

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
