from sys import argv              # Imports required libraries and modules
from configurator import Configurator
from time import sleep
from selenium import webdriver

config = Configurator(argv[1])    # Creates the configuratoe class with input parameter
login = config.get_login()        # Receives login from config
password = config.get_password()  # Receives password from config

browser = webdriver.Chrome('chromedriver.exe')     # Creates object browser
browser.get('https://projectby.trainings.dlabanalytics.com/pzokel963/')  # Input link in the browser
sleep(2)                                               # Time for coffee :)
button = browser.find_element_by_id("details-button")  # Finds element on the page
button.click()                                         # Clicks the element
button = browser.find_element_by_id("proceed-link")    # Finds element on the page
button.click()                                         # Clicks the element
button = browser.find_element_by_id("zocial-epam-idp")  # Finds element on the page
button.click()                                          # Clicks the element
sleep(2)                                                # Time for coffee :)
input_field = browser.find_element_by_id("userNameInput")  # Finds element on the page
input_field.send_keys(login)                               # Inserts the login
input_field = browser.find_element_by_id("passwordInput")  # Finds element on the page
input_field.send_keys(password)                            # Inserts the login
button = browser.find_element_by_id("submitButton")  # Finds element on the page
button.click()                                       # Clicks the element
browser.get('https://projectby.trainings.dlabanalytics.com/pzokel963/notebooks/Test_notebook.ipynb')  # Input link in /
# the browser
sleep(5)                                            # Time for coffee :)
button = browser.find_element_by_link_text('Cell')  # Finds element on the page
button.click()                                      # Clicks the element
button = browser.find_element_by_id('run_all_cells')  # Finds element on the page
button.click()                                        # Clicks the element

sleep(20)                                             # Time for watching results

browser.close()                                       # Closes the browser

if __name__ == '__main__':
    pass
