from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from settings import *

driver = webdriver.Chrome('../bin/chromedriver')

# go to URL
driver.get('https://www.facebook.com')

# enter username
usernameBox = driver.find_element_by_id('email')
usernameBox.send_keys(usr)

# enter password
passwordBox = driver.find_element_by_id('pass')
passwordBox.send_keys(pwd)

# click login
loginButton = driver.find_element_by_name('login')
loginButton.click()

sleep(2)

# get queries
with open('queries.txt') as queriesFile:
    queries = queriesFile.read().splitlines()

# loop through queries
for query in queries:

    # find friends
    driver.get(f"https://www.facebook.com/search/top/?q={query}&f=Aboa9pExa6Rjo_4i_pXhMj1hLVikL6vXYYIQDYQcp9oF2wum2jMQzMvimjryIwO1fsXiKt4G52fUtFa9TQHcipAqJutd7m5s53YN8sfTPVAf1Ar5YHfxa8F89XzfVHAN7iY")

    sleep(2)

    # add friends
    addButtons = driver.find_elements_by_xpath('//div[@aria-label="Add Friend"]')
    for addButton in addButtons:
        if addButton.is_displayed():
            addButton.click()
            sleep(1)

driver.quit()

print("Finished Successfully!")
