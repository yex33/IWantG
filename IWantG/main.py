import time

from selenium import webdriver


MICRO_SLEEP = 1


def main():
    browser = webdriver.Firefox()
    time.sleep(MICRO_SLEEP)

