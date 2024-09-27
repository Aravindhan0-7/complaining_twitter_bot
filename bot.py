from datetime import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
PROMISED_DOWN=150
PROMISED_UP=10
TWITTER_EMAIL="EMAIL_ID"
TWITTER_PASSWORD="PASSWORD"
TWITTER_USERNAME="USERNAME"
driver_options = webdriver.ChromeOptions()
driver_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=driver_options)


class InternetSpeed:
    def __init__(self,driver_path):
        self.driver_path=driver_path
        self.up=0
        self.down=0
    def get_internet_speed(self):
        self.driver_path.get("https://www.speedtest.net/")
        time.sleep(5)

        accept_button=self.driver_path.find_element(By.ID,value="onetrust-accept-btn-handler")
        accept_button.click()
        time.sleep(2)

        go_button=self.driver_path.find_element(By.XPATH,value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
        go_button.click()
        time.sleep(50)

        download_mbps=self.driver_path.find_element(By.XPATH,value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        download_mbps=float(download_mbps)
        print(f"Download MBPS: {download_mbps}")

        upload_mbps=self.driver_path.find_element(By.XPATH,value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        upload_mbps=float(upload_mbps)
        print(f"Upload_mbps:{upload_mbps}")
        self.up=upload_mbps
        self.down=download_mbps

    def tweet_at_provider(self):
        self.driver_path.get("https://twitter.com/login")
        time.sleep(5)
        # cookies_button=self.driver_path.find_element(By.XPATH,value='//*[@id="layers"]/div/div/div/div/div/button/div/span')
        # cookies_button.click()
        # time.sleep(5)
        email = self.driver_path.find_element(By.XPATH,value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input')
        email.send_keys(TWITTER_EMAIL, Keys.ENTER)

        time.sleep(5)
        twitter_username=self.driver_path.find_element(By.XPATH,value='/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
        twitter_username.send_keys(TWITTER_USERNAME, Keys.ENTER)
        time.sleep(5)

        pass_button=self.driver_path.find_element(By.XPATH,value='/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        pass_button.send_keys(TWITTER_PASSWORD,Keys.ENTER)
        time.sleep(5)


        write_box=self.driver_path.find_element(By.XPATH,value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
        write_box.send_keys(f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?",Keys.ENTER)
        time.sleep(3)

        post_button=self.driver_path.find_element(By.XPATH,value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/button')
        post_button.click()

speed=InternetSpeed(driver)
speed.get_internet_speed()
speed.tweet_at_provider()
