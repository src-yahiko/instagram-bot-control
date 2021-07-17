from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import generate_webdriver
import generate_account_info
import retrieve_from_mailbox
import control_webdriver as cw
from time import sleep
import json
import shutil

user = generate_account_info.generate()

def create(user):
      driver = generate_webdriver.generate(profile=user['username'])

      try:
            with open(f'../selenium_profiles/{user["username"]}/creds.txt') as f:
                  creds = f.readlines()[0]
                  exit("User already exists")
      except:
            creds = open(f'../selenium_profiles/{user["username"]}/creds.txt', 'w')
            creds.write(json.dumps(user))
            creds.close()

      # Open Sign-Up Page
      driver.get('https://www.instagram.com/accounts/emailsignup/')
      sleep(4)

      # Close Cookie Disclaimer
      try: WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div/div/button[1]'))).click()
      except: pass

      # Fill Form and Submit
      sleep(4)
      WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.NAME, 'emailOrPhone'))).click()
      elem_email = driver.find_element_by_name('emailOrPhone')
      elem_fullName = driver.find_element_by_name('fullName')
      elem_username = driver.find_element_by_name('username')
      elem_password = driver.find_element_by_name('password')
      cw.write_text_to_element(driver, elem_email, user['email'])
      cw.write_text_to_element(driver, elem_fullName, user['fullname'])
      cw.write_text_to_element(driver, elem_username, user['username'])
      cw.write_text_to_element(driver, elem_password, user['password'])
      sleep(1)
      WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='react-root']/section/main/div/div/div[1]/div/form/div[7]/div/button"))).click()

      ##### TODO: Make Human-Like (implement control_webdriver for dropdown)
      # Birthday
      sleep(3)

      try: elem_month = driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/div/div[1]/div/div[4]/div/div/span/span[1]/select")
      except: exit("Probably banned")
      elem_day = driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/div/div[1]/div/div[4]/div/div/span/span[2]/select")
      elem_year = driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/div/div[1]/div/div[4]/div/div/span/span[3]/select")

      cw.click_on_element(driver, elem_month)
      sleep(1)
      WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='react-root']/section/main/div/div/div[1]/div/div[4]/div/div/span/span[1]/select/option[4]"))).click()

      cw.click_on_element(driver, elem_day)
      sleep(1)
      WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='react-root']/section/main/div/div/div[1]/div/div[4]/div/div/span/span[2]/select/option[10]"))).click()
      cw.click_on_element(driver, elem_year)
      sleep(1)
      WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='react-root']/section/main/div/div/div[1]/div/div[4]/div/div/span/span[3]/select/option[27]"))).click()

      sleep(1)
      WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='react-root']/section/main/div/div/div[1]/div/div[6]/button"))).click()

      # Submit Verification Code
      instCode = retrieve_from_mailbox.get_instagram_code(user['email'], driver)
      elem_confirm = driver.find_element_by_name('email_confirmation_code')
      cw.write_text_to_element(driver, elem_confirm, instCode)
      driver.find_element_by_name('email_confirmation_code').send_keys(Keys.ENTER)

      sleep(10)

      # Invalid Verification Code Check
      try:
            not_valid = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[4]/div')
            if(not_valid.text == 'That code isn\'t valid. You can request a new one.'):
                  sleep(1)
                  driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div[1]/div[1]/div[2]/div/button').click()
                  sleep(10)
                  instCodeNew = retrieve_from_mailbox.get_instagram_code_double(user['email'], driver, instCode)
                  confInput = driver.find_element_by_name('email_confirmation_code')
                  confInput.send_keys(Keys.CONTROL + "a")
                  confInput.send_keys(Keys.DELETE)
                  cw.write_text_to_element(driver, elem_confirm, instCodeNew)
                  confInput.send_keys(Keys.ENTER)
            if("proxy" in not_valid.text):
                  exit("Proxy detected")
      except:
            pass

      # Check Result
      
      try:
            not_valid = driver.find_element_by_xpath('//html/body/div[1]/section/main/div[2]/div/div/div[1]/div[1]/h2')
            if "Confirm" in not_valid.text:
                  exit("Further verification required")
            else:
                  exit("Success!")
      except:
            exit("Unknown result")

create(user)

input("Press any key to exit...")
exit()