from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import ElementClickInterceptedException

class InstaFollower:
    def __init__(self):
        self.chrome_option = webdriver.ChromeOptions()
        self.chrome_option.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.chrome_option)
    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(2)
        reject_cookie = self.driver.find_element(By.XPATH, '/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[2]')
        reject_cookie.click()
        time.sleep(2)
        username = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
        username.send_keys('tanvir.python.test@gmail.com')
        time.sleep(3)
        password = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
        password.send_keys('v%Fyr8Ea$o4y6X8(Y')
        time.sleep(2)
        login = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')
        login.click()
        time.sleep(4)
        login_info_save = self.driver.find_element(by=By.XPATH, value="//div[contains(text(), 'Not now')]")
        login_info_save.click()
        time.sleep(2)
        notification = self.driver.find_element(by=By.XPATH, value= "//button[contains(text(), 'Not Now')]")
        notification.click()

    def find_followers(self):
        self.driver.get("https://www.instagram.com/thedogist/")
        time.sleep(4)
        click_followers = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/div/div[2]/section/main/div/header/section[3]/ul/li[2]/div/a/span')
        click_followers.click()
        time.sleep(3)
        element_inside_pop_Up = self.driver.find_element(By.XPATH, '/html/body/div[6]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div/div/div/div[3]/div/button')
        element_inside_pop_Up.send_keys(Keys.END)
    def follow(self):
        all_buttons = self.driver.find_elements(By.CSS_SELECTOR, value='._aano button')
        for button in all_buttons:
            try:
                button.click()
                time.sleep(1.1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(by=By.XPATH, value="//button[contains(text(), 'Cancel')]")
                cancel_button.click()


