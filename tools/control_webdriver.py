
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep
import random
import string

def write_text_to_element(driver, target_element, text):
    action = ActionChains(driver)
    sleep(random.randrange(100,200)/1000)
    action.move_to_element(target_element).perform()
    sleep(random.randrange(100,200)/1000)
    target_element.click()
    target_element.clear()
    while target_element.get_attribute('value') != text:
        for c in text:
            if random.randrange(100) < 10:
                sleep(random.randrange(100,200)/1000)
                target_element.send_keys(random.choice(string.ascii_lowercase))
                sleep(random.randrange(100,200)/1000)
                target_element.send_keys(Keys.BACK_SPACE)
            sleep(random.randrange(100,200)/1000)
            target_element.send_keys(c)

