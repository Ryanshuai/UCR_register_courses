import requests
import sys
import io
import time
from selenium import webdriver

from pynput.keyboard import Key, Controller


def register(usr, pwd, course):
    keyboard = Controller()

    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

    driver = webdriver.Chrome('C:\Program Files\Google\Chrome\Application\chromedriver.exe')

    url = r'https://auth.ucr.edu/cas/login'
    driver.get(url)

    username_input = driver.find_element_by_name('username')
    username_input.send_keys(usr)
    password_input = driver.find_element_by_name('password')
    password_input.send_keys(pwd)
    login_button = driver.find_element_by_xpath('//*[@id="fm1"]/div[2]/button')
    login_button.click()

    url = r'https://registrationssb.ucr.edu/StudentRegistrationSsb/ssb/registration/registration'
    driver.get(url)

    link = driver.find_element_by_xpath('//*[@id="registerLink"]')
    link.click()

    term_button = driver.find_element_by_xpath('//*[@id="s2id_txt_term"]')
    term_button.click()
    driver.implicitly_wait(2)

    time.sleep(2)
    keyboard.type("\n")

    time.sleep(2)
    keyboard.type("\n")

    time.sleep(4)
    subject_course_number = driver.find_element_by_xpath('//*[@id="s2id_txt_subjectcoursecombo"]')
    subject_course_number.click()
    time.sleep(0.5)
    keyboard.type(course)
    time.sleep(2)
    keyboard.type("\n")
    time.sleep(0.5)
    keyboard.type("\n")

    while True:
        add_button = driver.find_element_by_xpath('//*[@id="addSection20214013111"]')
        add_button.click()
        time.sleep(1)
        submit_button = driver.find_element_by_xpath('//*[@id="saveButton"]')
        submit_button.click()
        time.sleep(8)


if __name__ == '__main__':
    register(usr="", pwd="", course="CS218")
