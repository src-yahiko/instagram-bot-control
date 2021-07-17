import time

def get_instagram_code(email, driver):
    INST_CODE = 'https://email-fake.com/' + email
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])
    driver.get(INST_CODE)
    t = driver.title

    while True:
        if t[:4]=="Fake":
            driver.refresh()
            t = driver.title
            time.sleep(1)
        else:
            break

    code = t[:6]
    driver.switch_to.window(driver.window_handles[0])
    return code

def get_instagram_code_double(email, driver, oldCode):
    INST_CODE = 'https://email-fake.com/' + email
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])
    driver.get(INST_CODE)
    time.sleep(4)
    code = driver.find_element_by_xpath("/html/body/div[3]/div/div/div[1]/div[2]/a[1]/div[2]").text
    while oldCode == code:
        driver.refresh()
        # print('Whait for new code!')
        time.sleep(1)
        code = driver.find_element_by_xpath("//*[@id='email-table']/div[2]/div[1]/div/h1").text
    
    codeNew = code[:6]
    driver.switch_to.window(driver.window_handles[0])
    return codeNew
