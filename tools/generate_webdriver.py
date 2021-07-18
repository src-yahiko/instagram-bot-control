import random
import undetected_chromedriver.v2 as uc
from selenium.webdriver.common.proxy import Proxy, ProxyType
import re
import requests
import argparse
from time import sleep
import os
import os
from pathlib import Path
ROOT_DIR = os.path.join(Path(__file__).parent.parent)


def parse_arguments():
	"""Parses the program arguments (fails if required argmuents are not given)"""
	parser = argparse.ArgumentParser(description="Selenium Driver Generator")

	parser.add_argument(
		"--proxy",
		required=False,
		help="Proxy IP address to use",
		default=None)

	parser.add_argument(
		"--profile",
		required=False,
		help="Set a browser profile",
		default="Default")

	parser.add_argument(
		"--headless",
		required=False,
		help="Set the browser to headless, default false",
		default=False)

	parser.add_argument(
		"--url",
		required=False,
		help="Opens a specified url",
		default="https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html")
	return parser.parse_args()


def generate(profile="Default", proxyIP=None, url=None, headless=False):
	options = uc.ChromeOptions()
	ua = get_useragent()
	try:
		with open(os.path.join(ROOT_DIR, f'selenium_profiles/{profile}/useragent.txt')) as f:
			ua = f.readlines()[0]
	except:
		try: os.mkdir(os.path.join(ROOT_DIR, f'selenium_profiles/{profile}/'))
		except: pass
		uafile = open(os.path.join(ROOT_DIR, f'selenium_profiles/{profile}/useragent.txt'), 'w')
		uafile.write(ua)
		uafile.close()
	options.add_argument(f'--user-agent="{ua}"')
	if proxyIP != None:
		options.add_argument(f'--proxy-server={proxyIP}')
		#print("Proxy not implemented yet")
	if headless:
		options.add_argument("--disable-extensions")
		options.add_argument("--disable-gpu")
		options.add_argument("--no-sandbox")  # linux only
		options.add_argument("--headless")
	options.user_data_dir = os.path.join(ROOT_DIR, f"selenium_profiles/{profile}")
	options.add_argument(
		'--no-first-run --no-service-autorun --password-store=basic')
	driver = uc.Chrome(options=options)
	if url != None:
		driver.get(url)
	return driver

ua_list = []
userlist=re.sub('\r\n', '\n', str(requests.get('http://pastebin.com/raw/VtUHCwE6').text)).splitlines()

for x in userlist:
	ua_list.append(x)
random.shuffle(ua_list)
def get_useragent():
	return(str(random.choice(ua_list)))

if __name__ == '__main__':
	args = parse_arguments()
	driver = generate(args.profile, args.proxy, headless=args.headless)
	driver.get(args.url)
	if args.headless:
		driver.save_screenshot("_screenshot.png")
	input("Press any key to exit...")