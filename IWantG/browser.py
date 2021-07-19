import os
import random
import time

from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from IWantG.constants import MEDIUM_SLEEP


class Browser:
    PROJECT_ROOT: str = os.getcwd()
    GECKODRIVER_PATH: str = os.path.join(PROJECT_ROOT, "bin", "geckodriver")

    def __init__(self, headless: bool = True):
        options = webdriver.FirefoxOptions()
        if headless:
            options.add_argument("--headless")

        self.driver = webdriver.Firefox(
            executable_path=self.GECKODRIVER_PATH,
            firefox_options=options
        )
        self.driver.implicitly_wait(MEDIUM_SLEEP)

    @property
    def current_url(self) -> WebDriver:
        return self.driver.current_url

    def get(self, url: str) -> None:
        self.driver.get(url)

    def get_page_source(self) -> WebDriver:
        return self.driver.page_source

    def implicitly_wait(self, t: int) -> None:
        self.driver.implicitly_wait(t)

    def find(self, css_selector: str, element=None, wait_time: int = 0):
        within = element or self.driver
        try:
            if wait_time > 0:
                WebDriverWait(within, wait_time).until(
                    expected_conditions.presence_of_element_located((By.CSS_SELECTOR, css_selector))
                )
        except TimeoutException:
            return None
        try:
            return within.find_element(By.CSS_SELECTOR, css_selector)
        except NoSuchElementException:
            return None

    @staticmethod
    def randomized_sleep(avg: int = 1):
        time.sleep(random.uniform(avg * 0.5, avg * 1.5))

    def __del__(self):
        try:
            self.driver.quit()
        except Exception:
            # evil
            pass
