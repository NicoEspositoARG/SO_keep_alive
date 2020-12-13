
import os
import time
import logging

from selenium import webdriver


def login():

    try:
        logger = logging.getLogger('so_fanatic_script')
        logger.debug("Logging into stackoverflow.com ")

        driver = webdriver.Chrome()
        driver.get("https://stackoverflow.com")

        driver.find_element_by_link_text("Log in").click()

        driver.find_element_by_id("email").send_keys(
            os.environ['STACK_OVERFLOW_EMAIL'])
        driver.find_element_by_id("password").send_keys(
            os.environ['STACK_OVERFLOW_PASSWORD'])

        driver.find_element_by_id("submit-button").submit()
        logger.debug("Logged in & waiting!")
        time.sleep(5)
        driver.find_element_by_class_name("my-profile").click()
        logger.debug("Inside profile! & waiting!")

        time.sleep(15)
        # elem = driver.find_element_by_class_name("mini-avatar")
        elem = driver.find_element_by_class_name("my-profile")
        assert os.environ['STACK_OVERFLOW_DISPLAY_NAME'] in elem.text
        logger.debug("Success! Well done!")

    except Exception as e:
        logger.exception("An error occurred while"
                         "trying to access stackoverflow.com!", e)
    finally:
        driver.close()
        # fh.close()


if __name__ == "__main__":
    login()
