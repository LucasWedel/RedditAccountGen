from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import random
import time
import string
import secrets
import os
import PySimpleGUI as sg
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys



def generateAccount():
    # USES CHROMEDRIVERMANAGER TO AUTO UPDATE CHROMEDRIVER
    options = Options()
    options.add_experimental_option("detach", True)
    s = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s, options=options)
  

    # GENERATE PASSWORD
    alphabet = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(alphabet) for _ in range(16))
    # PASSWORD GENERATION FINISHED

    # NAME GENERATION
    driver.get('https://en.wikipedia.org/wiki/Special:Random')
    temp = driver.find_element(By.CLASS_NAME, "firstHeading").text
    wikiFinding = temp
    for char in string.punctuation:
        temp = temp.replace(char, '')  # REMOVES ALL PUNCTUATION
    for char in string.digits:
        temp = temp.replace(char, '')  # REMOVES SPACES
    temp = "".join(filter(lambda char: char in string.printable, temp))  # REMOVES NON ASCII CHARACTERS
    name = ''.join(temp.split())
    name = name[:random.randint(5, 7)]  # KEEPS 5 TO 7 LETTERS OF THE ORIGINAL STRING

    randomNumber = random.randint(10000, 99999)

    dirname = os.path.dirname(__file__)
    text_file_path = os.path.join(dirname, 'namesforreddit.txt')
    text_file = open(text_file_path, "a")
    text_file.write("" + 'Nixue' + name + str(randomNumber) + " PWD: " + password)  # OUTPUTS NAME AND NUMBER
    text_file.write("\n")
    text_file.close()

    finalName = 'Nixue' + name + str(randomNumber)
    time.sleep(1)
    # NAME GENERATION FINISHED

    # REDDIT ACCOUNT CREATION
    driver.get('https://www.reddit.com/register/')
    driver.find_element(By.ID, 'regEmail').send_keys('email@email.com')
    time.sleep(1)
    driver.find_element(By.XPATH, "//button[contains(text(),'Continue')]").click()
    time.sleep(3)
    driver.find_element(By.ID, 'regUsername').send_keys(finalName)
    driver.find_element(By.ID, 'regPassword').send_keys(password)
    print("Account generation complete!")
    print(f"Username: {finalName} | Password: {password}")
    print(f"Origin of username is {wikiFinding}")
    print("> Please manually complete the CAPTCHA! <")
    driver.switch_to.window(driver.current_window_handle)
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])
    driver.get('https://www.1secmail.com/')
    
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[2])
    driver.get('https://chrome.google.com/webstore/detail/browsec-vpn-free-vpn-for/omghfjlpggmjjaagoclmmobgdodcjboh/related')
    


def main():
    sg.theme('DarkBlue2')
    layout = [
        [sg.Text("Just press the button below to generate a brand new Reddit account!")],
        [sg.Text("Nixue Test1")],
        [sg.Text("Eventual errors will appear in the field below")],
        [sg.Text("Nixue Test2 ")],
        [sg.Output(size=(60, 15))],
        [sg.Button("Generate"), sg.Button("Exit"), sg.Button("Instance")]
    ]
    window = sg.Window("Reddit Account Generator", layout)
    while True:
        event, values = window.read()
        if event == "Generate":
            time.sleep(2)
            generateAccount()
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            print("Current Time =", current_time)

        if event == sg.WIN_CLOSED or event == "Exit":
            break

        if event == "Instance":
            options = Options()
            options.add_experimental_option("detach", True)
            s = Service(ChromeDriverManager().install())
            driver = webdriver.Chrome(service=s, options=options)
            driver.get('https://www.reddit.com/login/')
            

    window.close()
    exit()

if __name__ == '__main__':
    main()
