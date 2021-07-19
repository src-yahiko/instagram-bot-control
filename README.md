# instagram-bot-control
- [ ] **create instagram accounts**
- [ ] run account automation
- [ ] instagram content scraper
- [ ] controlpanel GUI

# Next-Steps To-Dos
- [ ] create database model for accounts, proxies, phonenumbers, signups

# Improvement To-Dos
- [x] Add paths relative to file-location in `tools/generate_webdriver.py` and `tools/create_instagram_account.py` (e.g. use `import pathlib`)
- [x] Add `parse_arguments()` to `tools/create_instagram_account.py` (see `tools/generate_webdriver.py`)
  - proxy
  - headless
  - submission-form (maybe in future: signup through facebook)
  - account-info, `default=generate_account_info.generate()`
- [x] For *"Probably banned"* result add Try-Except around the instructions in `tools/create_instragram_account.py create()` (until Submit Birthday)
- [x] Add *"Browser error"* result (Try-Except around driver generation in `tools/create_instragram_account.py create()`)
- [ ] Think about functions that contribute to more human-like behavior when using selenium (such like hovering around random elements on the page)
- [x] Add Exit Codes to `tools/create_instragram_account.py`

# Tools
- [x] `tools/generate_account_info.py` account-info generation feature "email"
- [x] `tools/retrieve_from_mailbox.py` retrieve code from email
- [ ] account-info generation feature "phonenumber"
- [ ] retrieve code from SMS
- [x] solve reCAPTCHA
- [ ] solve ImageToText
- [ ] proxy-manager
- [ ] phonenumber-manager

# Scripts
- [x] `scripts/setup.sh` setup for linux to install dependencies and `scripts/python_requirements.txt`
- [ ] user creation script pipeline
- [ ] db connectivity (use sqlite)
- [ ] clean-up of `/selenium_profiles` (and database)

# Troubles
* Instagram is suspicious on account creation..
  - Change IP Adress
    - [x] Use proper Proxies
  - Avoid known trashmail-domains
    - [ ] Set up own trashmail-server
  - Verify accounts with *unusual activity*
    - [ ] Use Twilio for phone numbers
    - [x] Somehow solve reCAPTCHAs     
  - Bypass basic Selenium detection
    - [x] [Simple bypass evasions](https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html)

# Intel
- [BlackHatWorld: Instagram-Bulk-Account-Creation](https://www.blackhatworld.com/seo/instagram-bulk-account-creation.1329981/)

# Exit-Codes
#### `tools/create_instagram_account.py`
Code | Meaning | Example
------------ | ------------- | -------------
:godmode: 00 to  09 | Success | [@actinyladybug123](https://www.instagram.com/actinyladybug123/)
:suspect: 10 to  19 | Warning | reCAPTCHA
:feelsgood: 20 to  29 | Failed  | Proxy, IP-Ban, 429,... 
:goberserk:-10 to -19 | Error | Runtime, Internet, Function-Call, ...
