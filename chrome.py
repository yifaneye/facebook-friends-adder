from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from settings import *

driver = webdriver.Chrome('../bin/chromedriver')


def login():
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


def add_friends():
    # add friends
    addButtons = driver.find_elements_by_xpath('//div[@aria-label="Add Friend"]')
    for addButton in addButtons:
        if addButton.is_displayed():
            addButton.click()
            sleep(1)


def add_friends_from_groups():
    # get queries
    with open('groups.txt') as queriesFile:
        queries = queriesFile.read().splitlines()

    # loop through queries
    for query in queries:
        # find friends
        driver.get(f"https://www.facebook.com/groups/{query}/members/things_in_common")

        sleep(2)

        add_friends()

        driver.get(f"https://www.facebook.com/groups/{query}/members/near_you")

        sleep(2)

        add_friends()


def add_friends_from_queries():
    # get queries
    with open('queries.txt') as queriesFile:
        queries = queriesFile.read().splitlines()

    # loop through queries
    for query in queries:
        # find friends
        driver.get(
            f"https://www.facebook.com/search/top/?q={query}&f=Aboa9pExa6Rjo_4i_pXhMj1hLVikL6vXYYIQDYQcp9oF2wum2jMQzMvimjryIwO1fsXiKt4G52fUtFa9TQHcipAqJutd7m5s53YN8sfTPVAf1Ar5YHfxa8F89XzfVHAN7iY")

        sleep(2)

        add_friends()


login()
add_friends_from_queries()
add_friends_from_groups()

driver.quit()

print("Finished Successfully!")
