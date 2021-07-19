import control_webdriver as cw
import generate_webdriver as gw
import time
from sys import exit
# solve_recaptcha() test file

driver = gw.generate()
driver.get("https://recaptcha-demo.appspot.com/recaptcha-v2-checkbox.php")
cw.solve_recaptcha(driver)