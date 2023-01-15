import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# from selenium.webdriver.common.keys import Keys


def buy():
    """grabs list of purchasable items from store and buys the the most expensive
    """
    store = driver.find_elements(By.CSS_SELECTOR, "#rightPanel #store div")
    store = [i for i in store if i.get_attribute("class") == ""]
    #you need this for loop just incase there are no items in store
    for item in store[::-1]:
        item.click()
        break


chrome_driver_path = "/Users/momo/Development/chromedriver"
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
check_time = time.time() + 1
timeout = time.time() + 60 * 5  #total time to play game
driver = webdriver.Chrome(options=options,
                          service=Service(executable_path=chrome_driver_path))
driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.CSS_SELECTOR, "#cookie")

click_on = True
while click_on:
    cookie.click()
    if time.time() >= check_time:
        buy()
        check_time = time.time() + 1
    if time.time() >= timeout:
        score = ((driver.find_element(By.CSS_SELECTOR,
                                      "#cps")).text).split(" ")[2]
        print(f"score: {score}")
        break