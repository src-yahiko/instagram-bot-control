
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep
import random
import string
from pathlib import Path
import os
import generate_webdriver as gw
ROOT_DIR = os.path.join(Path(__file__).parent.parent)

#############################
# system libraries
import os
import urllib

# recaptcha libraries
import pydub
import speech_recognition as sr
# selenium libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def solve_recaptcha(driver):
    PROFILE = list(filter(lambda x: "user-data-dir" in x, driver.__dict__['options'].__dict__['_arguments']))[0].split("/")[-1]
    # main program
    # switch to recaptcha frame
    wait(5000)
    driver.switch_to.frame(driver.find_element_by_xpath("//iframe[@title='reCAPTCHA']"))
    wait(3000)

    # click on checkbox to activate recaptcha
    driver.find_element_by_class_name("recaptcha-checkbox-border").click()
    # switch to recaptcha audio control frame
    driver.switch_to.default_content()
    driver.switch_to.frame(driver.find_element_by_xpath("//iframe[@title='reCAPTCHA']"))
    wait(3000)

    # click on audio challenge
    driver.switch_to.default_content()
    driver.switch_to.frame(driver.find_element_by_xpath("//iframe[@title='recaptcha challenge']"))
    d=True
    while d or "multiple" in driver.page_srouce:
        d=False
        driver.find_element_by_id("recaptcha-audio-button").click()

        # switch to recaptcha audio challenge frame

        wait(3000)

        # get the mp3 audio file
        if "network" in driver.page_source:
            driver = gw.restart_with_new_useragent(driver)
            return solve_recaptcha(driver)
        src = driver.find_element_by_id("audio-source").get_attribute("src")

        # download the mp3 audio file from the source
        SAMPLE_MP3 = os.path.join(ROOT_DIR, "selenium_profiles", PROFILE, "sample.mp3")
        SAMPLE_WAV = os.path.join(ROOT_DIR, "selenium_profiles", PROFILE, "sample.wav")
        try: urllib.request.urlretrieve(src, SAMPLE_MP3)
        except: pass
        wait(3000)


        try:
            sound = pydub.AudioSegment.from_mp3(SAMPLE_MP3)
            sound.export(SAMPLE_WAV, format="wav")
            sample_audio = sr.AudioFile(SAMPLE_WAV)
        except Exception:
            exit("[ERR] Please run program as administrator or download ffmpeg manually, "
                "http://blog.gregzaal.com/how-to-install-ffmpeg-on-windows/")

        # translate audio to text with google voice recognition
        r = sr.Recognizer()
        with sample_audio as source:
            audio = r.record(source)
        key = r.recognize_google(audio)

        # key in results and submit
        driver.find_element_by_id("audio-response").send_keys(key.lower())
        driver.find_element_by_id("audio-response").send_keys(Keys.ENTER)
    driver.switch_to.default_content()
    wait(3000)
    driver.find_element_by_id("recaptcha-demo-submit").click()
    wait(3000)

    return key

def wait(t=300): sleep(random.randrange(10,t)/1000)

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
    wait(1000)
    action = ActionChains(driver)
    action.move_to_element(target_element).perform()
    wait(500)
    action.click(on_element=target_element)
