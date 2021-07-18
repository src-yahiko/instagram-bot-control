from logging import info
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import generate_webdriver
import generate_account_info
import retrieve_from_mailbox
import control_webdriver as cw
from time import sleep
from time import time
import json
from sys import exit
import os
import argparse
from pathlib import Path
ROOT_DIR = os.path.join(Path(__file__).parent.parent)

def parse_arguments():
	"""Parses the program arguments (fails if required argmuents are not given)"""
	parser = argparse.ArgumentParser(description="Automated Instagram Account Creation")

	parser.add_argument(
		"--proxy",
		required=False,
		help="Proxy IP address to use",
		default=None)

	parser.add_argument(
		"--account-info",
		required=False,
		help="Account-info to use",
		default=generate_account_info.generate())

	parser.add_argument(
		"--headless",
		required=False,
		help="Set the browser to headless, default false",
		default=False)

	parser.add_argument(
		"--submission-form",
		required=False,
		help="Submission profile",
		default="instagram")
	return parser.parse_args()

def instagram(user):
      start = time()
      driver = generate_webdriver.generate(profile=user['username'], headless=args.headless, proxy=args.proxy)

      try:
            with open(os.path.join(ROOT_DIR, f'selenium_profiles/{user["username"]}/creds.txt')) as f:
                  creds = f.readlines()[0]
                  exit("User already exists")
      except:
            creds = open(os.path.join(ROOT_DIR, f'selenium_profiles/{user["username"]}/creds.txt'), 'w')
            creds.write(json.dumps(user))
            creds.close()

      # Open Sign-Up Page
      print("Request page...")
      driver.get('https://www.instagram.com/accounts/emailsignup/')
      sleep(4)
      if "Login" not in driver.title:
            exit("Try again later")

      # Close Cookie Disclaimer
      print("Closing cookie disclaimer...")
      try: WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div/div/button[1]'))).click()
      except: pass

      # Fill Form and Submit
      sleep(4)
      WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.NAME, 'emailOrPhone'))).click()
      elem_email = driver.find_element_by_name('emailOrPhone')
      elem_fullName = driver.find_element_by_name('fullName')
      elem_username = driver.find_element_by_name('username')
      elem_password = driver.find_element_by_name('password')
      print("Fill Form and Submit 1/4")
      cw.write_text_to_element(driver, elem_email, user['email'])
      print("Fill Form and Submit 2/4")
      cw.write_text_to_element(driver, elem_fullName, user['fullname'])
      print("Fill Form and Submit 3/4")
      cw.write_text_to_element(driver, elem_username, user['username'])
      print("Fill Form and Submit 4/4")
      cw.write_text_to_element(driver, elem_password, user['password'])
      print("Submit Form, Sleep for 4s...")
      sleep(4)
      WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='react-root']/section/main/div/div/div[1]/div/form/div[7]/div/button"))).click()

      ##### TODO: Make Human-Like (implement control_webdriver for dropdown)
      # Birthday
      print("Birthday, Sleep for 4s...")
      sleep(3)

      try: elem_month = driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/div/div[1]/div/div[4]/div/div/span/span[1]/select")
      except: exit("Probably banned")
      elem_day = driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/div/div[1]/div/div[4]/div/div/span/span[2]/select")
      elem_year = driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/div/div[1]/div/div[4]/div/div/span/span[3]/select")

      print("Birthday 1/3")
      cw.click_on_element(driver, elem_month)
      sleep(1)
      WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='react-root']/section/main/div/div/div[1]/div/div[4]/div/div/span/span[1]/select/option[4]"))).click()
      print("Birthday 2/3")
      cw.click_on_element(driver, elem_day)
      sleep(1)
      WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='react-root']/section/main/div/div/div[1]/div/div[4]/div/div/span/span[2]/select/option[10]"))).click()
      print("Birthday 3/3")
      cw.click_on_element(driver, elem_year)
      sleep(1)
      WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='react-root']/section/main/div/div/div[1]/div/div[4]/div/div/span/span[3]/select/option[27]"))).click()
      print("Submit Birthday, sleep for 1s...")

      sleep(1)
      WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='react-root']/section/main/div/div/div[1]/div/div[6]/button"))).click()

      # Submit Verification Code
      print("Retrieve verification code...")
      instCode = retrieve_from_mailbox.get_instagram_code(user['email'], driver)
      print("Entering verification code...")
      elem_confirm = driver.find_element_by_name('email_confirmation_code')
      cw.write_text_to_element(driver, elem_confirm, instCode)
      driver.find_element_by_name('email_confirmation_code').send_keys(Keys.ENTER)
      sleep(10)

      # Invalid Verification Code Check
      try:
            not_valid = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[4]/div')
            if(not_valid.text == 'That code isn\'t valid. You can request a new one.'):
                  print("New verification code required...")
                  sleep(1)
                  driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div[1]/div[1]/div[2]/div/button').click()
                  sleep(10)
                  instCodeNew = retrieve_from_mailbox.get_instagram_code_double(user['email'], driver, instCode)
                  confInput = driver.find_element_by_name('email_confirmation_code')
                  confInput.send_keys(Keys.CONTROL + "a")
                  confInput.send_keys(Keys.DELETE)
                  cw.write_text_to_element(driver, elem_confirm, instCodeNew)
                  confInput.send_keys(Keys.ENTER)
      except:
            pass

      # Check Result
      print(f"Script took {start - time()} seconds")
      print("Check results, save screenshot")
      driver.save_screenshot(os.path.join(ROOT_DIR, f"selenium_profiles/{user['username']}/screenshot.png"))

      if "unusual activity" in driver.page_source: exit("Further verification required")
      if "open proxy" in driver.page_source: exit("Proxy detected")
      if "Search" in driver.page_source: exit("Success")
      exit("Unknown result")

if __name__ == '__main__':
      args = parse_arguments()
      print(json.dumps(args.__dict__, indent=4))
      if args.submission_form == "instagram":
            instagram(args.account_info)
      exit("No such submission-form", args.submission_form)