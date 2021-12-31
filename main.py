from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Type your Internet Service Provider (ISP)'s guaranteed internet speeds. This should be in your contract somewhere.
PROMISED_DOWN = 100
PROMISED_UP = 10

# Your Twitter Login Information
TWITTER_USERNAME = "YOUR TWITTER USERNAME/E-MAIL"
TWITTER_PASSWORD = "YOUR TWITTER PASSWORD"

# ChromeDriver Tool Path
CHROME_DRIVER_PATH = "YOUR CHROME DRIVER PATH"


class InternetSpeedTwitterBot:

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
        self.up = PROMISED_UP
        self.down = PROMISED_DOWN

    def get_internet_speed(self):
        self.driver.get("https://speedtest.net")

        time.sleep(3)

        # For first time the website might wants a give permission for using cookies.
        consent_button = self.driver.find_element(By.XPATH, '//*[@id="_evidon-banner-acceptbutton"]')
        consent_button.click()

        start_test = self.driver.find_element(By.XPATH,
                                              '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
        start_test.click()

        time.sleep(60)
        self.up = self.driver.find_element(By.XPATH,
                                           '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text
        self.down = self.driver.find_element(By.XPATH,
                                             '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text


    def tweet_at_provider(self):
        self.driver.get("http://www.twitter.com/login")
        time.sleep(2)

        username_input = self.driver.find_element(By.NAME, "text")
        username_input.send_keys(TWITTER_USERNAME)

        next_button = self.driver.find_element(By.XPATH,
                                               '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[6]/div')
        next_button.click()
        time.sleep(3)
        password_input = self.driver.find_element(By.NAME, "password")
        password_input.send_keys(TWITTER_PASSWORD)
        time.sleep(2)
        password_input.send_keys(Keys.ENTER)

        time.sleep(5)
        tweet_compose = self.driver.find_element(By.XPATH,
                                                 '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')
        tweet = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up" \
                f" when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
        tweet_compose.send_keys(tweet)
        time.sleep(3)
        tweet_button = self.driver.find_element(By.XPATH,
                                                '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span')
        tweet_button.click()
        time.sleep(2)


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()
