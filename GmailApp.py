from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

#ChromeDriver = webdriver.Chrome(ChromeDriverManager().install())
time.sleep(2)
# Launch the chrome web driver
ChromeDriver = webdriver.Chrome()
# Give the url of gamil
ChromeDriver.get('https://mail.google.com/mail/u/0')
time.sleep(5)
# From user ask the username through the terminal..
Username = input("Please give the username:\n")
# From user ask the password
Password = input("Please give the password:\n")
time.sleep(3)
# Give the username in gmail
ChromeDriver.find_element_by_id("identifierId").send_keys(Username)
time.sleep(2)
# Click on Next button
ChromeDriver.find_element_by_class_name("CwaK9").click()
time.sleep(5)
# Give the password in gmail
ChromeDriver.find_element_by_name("password").send_keys(Password)
time.sleep(2)
# Again click on Next button
ChromeDriver.find_element_by_class_name("CwaK9").click()
time.sleep(6)
# From user ask the sender email address through terinal
SenderEmailAddress = input("Please give the sender email address:\n")
# From user ask the subject of email through terminal
SubjectEmail = input("Please mention the subject of email:\n")
time.sleep(7)
# After logging into gmail click on "compose" button
ChromeDriver.find_element_by_xpath("//div[@class='T-I T-I-KE L3']").click()
# Give the sender email address
ChromeDriver.find_element_by_class_name("vO").send_keys(SenderEmailAddress)
# Press Enter
ChromeDriver.find_element_by_class_name("vO").send_keys(Keys.ENTER)
time.sleep(2)
# Give the subject of email address
ChromeDriver.find_element_by_class_name("aoT").send_keys(SubjectEmail)
time.sleep(2)
# Click on send button
ChromeDriver.find_element_by_class_name("dC").click()
time.sleep(6)
print("Email sent")