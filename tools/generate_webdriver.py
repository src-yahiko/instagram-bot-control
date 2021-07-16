import undetected_chromedriver.v2 as uc
from selenium.webdriver.common.proxy import Proxy, ProxyType
import argparse
from time import sleep

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
	if proxyIP != None:
		print("Proxy not implemented yet")
	options = uc.ChromeOptions()
	if headless:
		options.add_argument("--disable-extensions")
		options.add_argument("--disable-gpu")
		options.add_argument("--no-sandbox") # linux only
		options.add_argument("--headless")
	options.user_data_dir = f"../selenium_profiles/{profile}"
	options.add_argument('--no-first-run --no-service-autorun --password-store=basic')
	driver = uc.Chrome(options=options)
	if url != None:
		driver.get(url)
	return driver

if __name__ == '__main__':
	args = parse_arguments()
	driver = generate(args.profile, args.proxy, headless=args.headless)
	driver.get(args.url)
	if args.headless:
		driver.save_screenshot("_screenshot.png")
	sleep(60)
