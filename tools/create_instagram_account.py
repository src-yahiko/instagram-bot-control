from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import generate_webdriver
import generate_account_info
import retrieve_from_mailbox
import control_webdriver as cw
from time import sleep

driver = generate_webdriver.generate()
user = generate_account_info.generate()
#code = retrieve_from_mailbox.get_instagram_code(user['email'], driver)

# Open Sign-Up Page
driver.get('https://www.instagram.com/accounts/emailsignup/')

# Close Cookie Disclaimer
try: WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div/div/button[1]'))).click()
except: pass

# Fill Form and Submit
WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.NAME, 'emailOrPhone'))).click()
elem_email = driver.find_element_by_name('emailOrPhone')
elem_fullName = driver.find_element_by_name('fullName')
elem_username = driver.find_element_by_name('username')
elem_password = driver.find_element_by_name('password')
cw.write_text_to_element(driver, elem_email, user['email'])
cw.write_text_to_element(driver, elem_fullName, user['fullname'])
cw.write_text_to_element(driver, elem_username, user['username'])
cw.write_text_to_element(driver, elem_password, user['password'])
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='react-root']/section/main/div/div/div[1]/div/form/div[7]/div/button"))).click()

##### TODO: Make Human-Like (implement control_webdriver for dropdown)
# Birthday
sleep(5)
driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/div/div[1]/div/div[4]/div/div/span/span[1]/select").click()
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='react-root']/section/main/div/div/div[1]/div/div[4]/div/div/span/span[1]/select/option[4]"))).click()

driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/div/div[1]/div/div[4]/div/div/span/span[2]/select").click()
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='react-root']/section/main/div/div/div[1]/div/div[4]/div/div/span/span[2]/select/option[10]"))).click()

driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/div/div[1]/div/div[4]/div/div/span/span[3]/select").click()
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='react-root']/section/main/div/div/div[1]/div/div[4]/div/div/span/span[3]/select/option[27]"))).click()

WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='react-root']/section/main/div/div/div[1]/div/div[6]/button"))).click()

# Submit Verification Code
sleep(3)
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
            exit(not_valid)
except:
      pass

input("Press any key to exit...")