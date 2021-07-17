
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep
import random
import string

def wait(): return sleep(random.randrange(10,200)/1000)

def write_text_to_element(driver, target_element, text):
    action = ActionChains(driver)
    wait()
    action.move_to_element(target_element).perform()
    wait()
    target_element.click()
    target_element.send_keys(Keys.CONTROL + "a")
    target_element.send_keys(Keys.DELETE)
    while target_element.get_attribute('value') != text:
        for c in text:
            if random.randrange(100) < 10:
                wait()
                target_element.send_keys(random.choice(string.ascii_lowercase))
                wait()
                target_element.send_keys(Keys.BACK_SPACE)
            wait()
            target_element.send_keys(c)

def click_on_element(driver, target_element):
    action = ActionChains(driver)
    wait()
    action.move_to_element(target_element).perform()
    wait()
    target_element.click()
