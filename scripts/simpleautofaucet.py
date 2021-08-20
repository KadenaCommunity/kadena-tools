from selenium import webdriver
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import time

browser = webdriver.Chrome(ChromeDriverManager().install())
while True:
    browser.get('https://faucet.testnet.chainweb.com/')

    time.sleep(3)

    button = browser.find_element_by_xpath("//button[text()='Add Funds to Existing Account']")
    button.click()

    time.sleep(1)

    inputElement = browser.find_element_by_xpath("//input[not(@id) and not(@class)]")
    inputElement.send_keys('Your Public Key here')

    time.sleep(1)

    button2 = browser.find_element_by_xpath("//button[text()='Fund Account 10 Coins']")
    button2.click()
    time.sleep(1860)
 #will work while your doing your thing 
