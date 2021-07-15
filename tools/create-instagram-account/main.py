from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent
import accountInfoGenerator as account
import verifCode as verifCode
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import argparse

# Fake-Account
user = account.generate()
print(user)

# UserAgent
options = Options()
options.add_argument(f'user-agent={UserAgent().random}')
driver = webdriver.Chrome(options=options, executable_path='/snap/chromium/1646/usr/lib/chromium-browser/chromedriver')

# Submit Sign-Up
driver.get('https://www.instagram.com/accounts/emailsignup/')
time.sleep(3)
## Close Cookie Disclaimer
try:
	cookie = driver.find_element_by_xpath('/html/body/div[3]/div/div/button[1]').click()
except:
	pass
## Fill Email
driver.find_element_by_name('emailOrPhone').send_keys(user['trashmail'])
## Fill Fullname
driver.find_element_by_name('fullName').send_keys(user['fullname'])
## Fill Username
driver.find_element_by_name('username').send_keys(user['username'])
## Fill Password
driver.find_element_by_name('password').send_keys(user['password'])
## Submit Form
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='react-root']/section/main/div/div/div[1]/div/form/div[7]/div/button"))).click()
## Submit Birthday
time.sleep(3)
driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/div/div[1]/div/div[4]/div/div/span/span[1]/select").click()
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='react-root']/section/main/div/div/div[1]/div/div[4]/div/div/span/span[1]/select/option[4]"))).click()

driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/div/div[1]/div/div[4]/div/div/span/span[2]/select").click()
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='react-root']/section/main/div/div/div[1]/div/div[4]/div/div/span/span[2]/select/option[10]"))).click()

driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/div/div[1]/div/div[4]/div/div/span/span[3]/select").click()
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='react-root']/section/main/div/div/div[1]/div/div[4]/div/div/span/span[3]/select/option[27]"))).click()

WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='react-root']/section/main/div/div/div[1]/div/div[6]/button"))).click()
## Submit Verification Code
time.sleep(3)
instCode=verifCode.getInstVeriCode(user['trashmail'], driver)
driver.find_element_by_name('email_confirmation_code').send_keys(instCode, Keys.ENTER)
time.sleep(10)
### Invalid Verification Code Check
try:
    not_valid = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[4]/div')
    if(not_valid.text == 'That code isn\'t valid. You can request a new one.'):
      time.sleep(1)
      driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div[1]/div[1]/div[2]/div/button').click()
      time.sleep(10)
      instCodeNew = verifiCode.getInstVeriCodeDouble(mailName, domain, driver, instCode)
      confInput = driver.find_element_by_name('email_confirmation_code')
      confInput.send_keys(Keys.CONTROL + "a")
      confInput.send_keys(Keys.DELETE)
      confInput.send_keys(instCodeNew, Keys.ENTER)
except:
      pass

driver.quit()
