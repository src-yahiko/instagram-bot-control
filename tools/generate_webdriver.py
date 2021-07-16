import undetected_chromedriver.v2 as uc
from selenium.webdriver.common.proxy import Proxy, ProxyType
import argparse

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
		help="Set a browser profile name",
		default="Default")

	parser.add_argument(
		"--url",
		required=False,
		help="Opens a specified url",
		default="https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html")

	return parser.parse_args()

def generate(profile="Default", proxyIP=None, url=None):
	if proxyIP != None:
		print("Proxy not implemented yet")

	options = uc.ChromeOptions()
	options.user_data_dir = f"../selenium_profiles/{profile}"
	options.add_argument('--no-first-run --no-service-autorun --password-store=basic')
	driver = uc.Chrome(options=options)
	if url != None:
		driver.get(url)
	return driver

if __name__ == '__main__':
	args = parse_arguments()
	driver = generate(args.profile, args.proxy)
	driver.get(args.url)
