from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--headless")
# chrome_options.add_argument("--disable-gpu")
#
# browser = webdriver.Chrome(options=chrome_options)

url = 'https://www.baidu.com'

def share_browser():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")

    browser = webdriver.Chrome(options=chrome_options)
    return browser

my_b = share_browser()

my_b.get(url)

my_b.save_screenshot('screenshot.png')