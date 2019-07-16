import pytest
import requests

google_url = 'https://www.google.com'
response_good = 200

def test_function():
    assert requests.get(google_url).status_code == 200, ('Website ' + google_url + 
    ' did not respond with code ' + str(response_good))
