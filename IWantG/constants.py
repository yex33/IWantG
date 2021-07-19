EMAIL_ADDRESS: str = "simple-happiness@outlook.com"
DRIVERS_LICENCE_NUMBER: str = "Y20017890011221"
EXPIRY_DATE: str = "20230719"
TEST_TYPE: str = "G"
PREFERRED_LOCATIONS: set = {"Hamilton", "St Catharines"}
PREFERRED_MONTHS_AHEAD: int = 3
PREFERRED_YEAR: int = 2021

BOOKING_URL: str = "https://drivetest.ca/book-a-road-test/booking.html"
LOCATION_API: str = "https://drivetest.ca/booking/v1/location"
AVAILABILITY_API: str = "https://drivetest.ca/booking/v1/booking/{}?month={}&year={}"
DEFAULT_HEADERS: dict = {
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
G2_BUTTON: str = "#G2btn"
G_BUTTON: str = "#Gbtn"

# sleeping constants for more realistic human input
LITTLE_SLEEP = 1
MEDIUM_SLEEP = 5
LONG_SLEEP = 10
TYPING_CPS = 8  # Character Per Second (CPS)
TYPING_FACTOR = 1 / TYPING_CPS
