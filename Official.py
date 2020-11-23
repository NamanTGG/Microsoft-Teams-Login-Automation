'''
Hey Fellow Developers , Today We Will Be Automating The Login - Part Of Microsoft Teams Using Python And Selenium

This Is Part 1 Of A Microsoft Teams Automation Series Using Python

Throughout This Series , We Will Automate The Whole Application With Features Such As : Joining Teams , Meetings , Sending Messages etc.

This Series Has Been In The Works For A Long Time

I HATE MY DAD BECAUSE HE IS SUPER MEAN


I Will Also Continue Uploading My Normal Type Of Videos On  My Channel
'''
from selenium import webdriver
from time import sleep
import time
from Credentials import userName,password

driver = webdriver.Chrome()

driver.get('https://www.microsoft.com/en-in/microsoft-365/microsoft-teams/group-chat-software')

time.sleep(7)

driver.find_element_by_xpath('//a[@class="c-button f-secondary ow-slide-in ow-slide-in-2 xs-ow-mr-0 ow-mt-10 ow-txt-trans-upper ow-bvr-signin"]').click()

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