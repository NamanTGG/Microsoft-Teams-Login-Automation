'''
Hey Fellow Developers , Today We Will Be Automating The Login - Part Of Microsoft Teams Using Python And Selenium

'''
from selenium import webdriver
from time import sleep
import time
from LoginCredentials import userName,password

driver = webdriver.Chrome()

driver.get('https://www.microsoft.com/en-in/microsoft-365/microsoft-teams/group-chat-software')

time.sleep(7)

driver.find_element_by_xpath('/html/body/section/div[1]/div/div/div/section/div/div[2]/div[2]/a').click()

driver.switch_to.window(driver.window_handles[1])#switching to tab 1
time.sleep(5)

driver.switch_to_active_element().send_keys(userName)
time.sleep(2)
driver.find_element_by_xpath('//input[@class="button ext-button primary ext-primary"]').click()
print('Username Entered')
time.sleep(5)

driver.switch_to_active_element().send_keys(password)
time.sleep(2)
driver.find_element_by_xpath('//input[@id="idSIButton9"]').click()
print('Password Entered')
time.sleep(6)

time.sleep(4)
driver.find_element_by_xpath('//input[@class="button ext-button primary ext-primary"]').click()#yes button always remember
print('Yes Button Has Been Clicked')
time.sleep(10)

driver.find_element_by_xpath('/html/body/promote-desktop/div/div/div/div[1]/div[2]/div/a').click()
time.sleep(10)
print('Using Web App')
