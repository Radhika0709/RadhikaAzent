from selenium import webdriver
from time import sleep


driver = webdriver.Chrome(executable_path= "C:/Users/Mukesh/PycharmProjects/pythonProject/chromedriver/chromedriver.exe")
driver.get('https://staging-auth.azent.com/login')
driver.maximize_window()
sleep(2)

getTitleLoginPage = driver.title

createAccount = driver.find_element_by_link_text("New Account? Sign Up!")
createAccount.click()
sleep(2)

fName = input('Enter First Name:')
lName = input('Enter Last Name:')
emailAdd = input('Enter Email Address: ')
phoneNumber = input('Enter Phone Number:')
pwd = input('Enter Password: ')
reenterpwd = input('Enter Re-Enter Password: ')

first_Name = driver.find_element_by_id('firstName')
first_Name.send_keys(fName)

last_Name = driver.find_element_by_id('lastName')
last_Name.send_keys(lName)

email_Add = driver.find_element_by_id('email')
email_Add.send_keys(emailAdd)

phone_number = driver.find_element_by_id('mobile')
phone_number.send_keys(phoneNumber)

password = driver.find_element_by_id('password-1')
password.send_keys(pwd)

reEnterPwd = driver.find_element_by_id('password-2')
reEnterPwd.send_keys(reenterpwd)

if password != reEnterPwd:
    print("Reenter correct password")

sign_up = driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/main/div/form/button[1]/span[1]')
sign_up.click()
sleep(2)

if getTitleLoginPage == driver.title:
    print("Account not created,please review")
    #driver.quit()
elif getTitleLoginPage != driver.title:
    print("Account Created Sucessfully")
else:
    print("Account Not Created:" + driver.title)
