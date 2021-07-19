EMAIL_ADDRESS: str = "simple-happiness@outlook.com"
DRIVERS_LICENCE_NUMBER: str = "Y20017890011221"
EXPIRY_DATE: str = "20230719"
LOCATION: str = "St Catharines"
YEAR: int = 2021

BOOKING_URL: str = "https://drivetest.ca/book-a-road-test/booking.html"
LOCATION_API: str = "https://drivetest.ca/booking/v1/location"
AVAILABILITY_API: str = "https://drivetest.ca/booking/v1/booking/{}?month={}&year={}"
G2: str = "#G2btn"
G: str = "#Gbtn"
TEST_TYPE: str = G

# sleeping constants for more realistic human input
LITTLE_SLEEP = 1
MEDIUM_SLEEP = 5
LONG_SLEEP = 10
TYPING_CPS = 8  # Character Per Second (CPS)
TYPING_FACTOR = 1 / TYPING_CPS
