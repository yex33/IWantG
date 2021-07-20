import sys
from datetime import date, datetime

import requests
import time
import logging

from IWantG.browser import Browser
from IWantG.constants import *


def renew_session(browser: Browser) -> list:
    print("Renewing booking session")
    browser.delete_all_cookies()
    browser.get(BOOKING_URL)
    # logging.debug("booking website loaded")
    browser.randomized_sleep(LITTLE_SLEEP)
    browser.send_keys_to("#emailAddress", EMAIL_ADDRESS)
    browser.send_keys_to("#confirmEmailAddress", EMAIL_ADDRESS)
    browser.send_keys_to("#licenceNumber", DRIVERS_LICENCE_NUMBER)
    browser.send_keys_to("#licenceExpiryDate", EXPIRY_DATE)
    browser.click_button("#regSubmitBtn")

    browser.click_button(G_BUTTON if TEST_TYPE == "G" else G2_BUTTON, wait_time=LONG_SLEEP)
    # logging.debug("test type selected")
    browser.click_button("button.booking-submit")
    time.sleep(MEDIUM_SLEEP)

    location_ids = []
    session = requests.Session()
    session.headers.update(DEFAULT_HEADERS)
    centers: list = session.get(LOCATION_API).json()['driveTestCentres']
    # logging.debug("drive test centers json fetched")
    preferred_centers = filter(lambda x: x['name'] in PREFERRED_LOCATIONS, centers)
    for center in preferred_centers:
        service_ids = list(filter(lambda x: x['licenceClass'] == TEST_TYPE, center['services']))
        if len(service_ids) > 0:
            location_ids.append((center['name'], service_ids[0]['serviceId']))
    return location_ids


def get_availabilities(browser: Browser, location_ids: list) -> list:
    session = requests.Session()
    session.headers.update(DEFAULT_HEADERS)
    session_cookies = browser.get_cookies()
    for cookie in session_cookies:
        session.cookies.set(cookie['name'], cookie['value'])

    availabilities = []
    for location, service_id in location_ids:
        for month in range(date.today().month, date.today().month + PREFERRED_MONTHS_AHEAD):
            month_info = session.get(
                AVAILABILITY_API.format(service_id, month, PREFERRED_YEAR)
            ).json()['availableBookingDates']
            # logging.debug(f"{location} month {month} json fetched")
            for daily_info in month_info:
                description = daily_info['description']
                if description != "UNAVAILABLE" and description != "FULL":
                    availabilities.append({
                        'month': month,
                        'day': daily_info['day'],
                        'at': location,
                        'description': description
                    })
    return availabilities


def main():
    requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS += 'HIGH:!DH:!aNULL'
    try:
        requests.packages.urllib3.contrib.pyopenssl.DEFAULT_SSL_CIPHER_LIST += 'HIGH:!DH:!aNULL'
    except AttributeError:
        # no pyopenssl support used / needed / available
        pass
    browser = Browser(headless=False if DEBUG else False)
    browser.randomized_sleep(LITTLE_SLEEP)

    wait_time = LONG_SLEEP
    while True:
        try:
            location_ids = renew_session(browser)
            wait_time = max(wait_time / 2, LONG_SLEEP)
            print(f"Successfully renewed logins: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
            for _ in range(SESSION_EXPIRY // AVAILABILITY_REFRESH // 4 * 3):
                availabilities = get_availabilities(browser, location_ids)
                if len(availabilities) > 0:
                    for entry in availabilities:
                        print(
                            f"\n\n{PREFERRED_YEAR}/{entry['month']}/{entry['day']} at {entry['at']}: {entry['description']}\n\n"
                        )
                else:
                    print("No available time slot. ", end="")
                time.sleep(LITTLE_SLEEP)
                print(f"Last fetch: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
                time.sleep(AVAILABILITY_REFRESH * 60)
        except KeyboardInterrupt:
            print("\nCrawler exits")
            break
        except AttributeError:
            wait_time *= 2
            print(f"Timed out. Retry in {MEDIUM_SLEEP} seconds for {wait_time} seconds.")
            time.sleep(MEDIUM_SLEEP)


if __name__ == "__main__":
    if DEBUG:
        root = logging.getLogger()
        root.setLevel(logging.DEBUG)
        handler = logging.StreamHandler(sys.stdout)
        handler.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        root.addHandler(handler)

    main()
