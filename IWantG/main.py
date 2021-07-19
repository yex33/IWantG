import requests as requests

from IWantG.browser import Browser
from IWantG.constants import *


def main():
    browser = Browser(headless=False)
    browser.randomized_sleep(LITTLE_SLEEP)

    browser.get(BOOKING_URL)
    browser.randomized_sleep(LITTLE_SLEEP)
    browser.send_keys_to("#emailAddress", EMAIL_ADDRESS)
    browser.send_keys_to("#confirmEmailAddress", EMAIL_ADDRESS)
    browser.send_keys_to("#licenceNumber", DRIVERS_LICENCE_NUMBER)
    browser.send_keys_to("#licenceExpiryDate", EXPIRY_DATE)
    browser.click_button("#regSubmitBtn")

    browser.click_button(TEST_TYPE, wait_time=LONG_SLEEP)
    browser.click_button("button.booking-submit")

    headers = {
        'Host': 'drivetest.ca',
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:90.0) Gecko/20100101 Firefox/90.0',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Referer': 'https://drivetest.ca/book-a-road-test/booking.html',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
    }

    session_cookies = browser.get_cookies()
    session = requests.Session()
    session.headers.update(headers)
    for cookie in session_cookies:
        session.cookies.set(cookie['name'], cookie['value'])
    session.get(LOCATION_API)

    print("get")


if __name__ == "__main__":
    main()
