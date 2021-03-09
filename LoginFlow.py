from selenium import webdriver
from time import sleep

usr = input('Enter Email Id/Phone Number:')
pwd = input('Enter Password:')

driver = webdriver.Chrome(executable_path= "C:/Users/Mukesh/PycharmProjects/pythonProject/chromedriver/chromedriver.exe")
driver.get('https://staging-auth.azent.com/login')
driver.maximize_window()
sleep(2)

getTitleLoginPage = driver.title

username_box = driver.find_element_by_id('username')
username_box.send_keys(usr)
sleep(1)

password_box = driver.find_element_by_id('password')
password_box.send_keys(pwd)

login_box = driver.find_element_by_css_selector('button.MuiButtonBase-root:nth-child(4) > span:nth-child(1)')
login_box.click()
sleep(3)

afterLoginTitle = driver.title
if getTitleLoginPage == afterLoginTitle:
    errorMsg = driver.find_element_by_css_selector("#app > div > div.MuiPaper-root.MuiGrid-root.jss3.MuiGrid-container.MuiGrid-item.MuiGrid-grid-xs-true.MuiPaper-elevation1.MuiPaper-rounded > div > main > div > div.MuiBox-root.jss55 > p").text
    print("Authentication Failed: " + errorMsg)
    #driver.quit()
elif driver.find_element_by_id("input-with-icon-grid"):
    print("Login Successfull")
    #driver.quit()
else:
    print("Login Failed: " + driver.title)
    #driver.quit()

