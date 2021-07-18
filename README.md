# instagram-bot-control
- [ ] create instagram accounts
- [ ] run account automation
- [ ] instagram content scraper
- [ ] controlpanel GUI

# Improvement To-Do:
- [ ] Add paths relative to file-location in tools/generate_webdriver.py and tools/create_instagram_account.py (using import pathlib etc.)
- [ ] Add parse_arguments() to tools/create_instagram_account.py (see tools/generate_webdriver.py)
  - proxyIP
  - headless
  - user, default=generate_account_info.generate()
- [ ] For "Probably banned" result add Try-Except around the whole process (until Submit Birthday)
- [ ] Add "Browser error" result (Try-Except around driver generation)
- [ ] Create random-hovering above random html-tags function in tools/control_webdriver.py to simulate mouse-hovering around the page

# Tools
- [x] account-info generation feature "email"
- [x] retrieve code from email
- [ ] account-info generation feature "phonenumber"
- [ ] retrieve code from SMS
- [ ] solve reCAPTCHA
- [ ] solve ImageToText

# Scripts
- [x] setup for linux to install dependencies

# Troubles
* Instagram is suspicious on account creation..
  - Change IP Adress
    - [ ] Use proper Proxies
  - Avoid known trashmail-domains
    - [ ] Set up own trashmail-server
  - Bypass basic Selenium detection
    - [x] [Simple bypass evasions](https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html)
