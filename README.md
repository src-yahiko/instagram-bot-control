# instagram-bot-control
- [ ] **create instagram accounts**
- [ ] run account automation
- [ ] instagram content scraper
- [ ] controlpanel GUI

# Next-Steps To-Dos
- [ ] create database model for accounts, proxies, phonenumbers, signups

# Improvement To-Dos
- [ ] **Revisit!** Add Exit Codes to `tools/create_instragram_account.py` **trouble verifiying your confirmation code, change success exit**

# Tools
- [x] `tools/generate_account_info.py` account-info generation feature "email"
- [x] `tools/retrieve_from_mailbox.py` retrieve code from email
- [ ] account-info generation feature "phonenumber"
- [ ] retrieve code from SMS
- [x] solve reCAPTCHA
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
