import time

from IWantG.browser import Browser
from IWantG.constants import *


def main():
    browser = Browser(headless=False)
    time.sleep(LITTLE_SLEEP)


if __name__ == "__main__":
    main()
