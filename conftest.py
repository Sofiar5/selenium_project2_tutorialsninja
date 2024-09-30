import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

@pytest.fixture(scope='module')
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920*1080")
    chrome_options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

@pytest.fixture(scope='function')
def login(driver):
    driver.get("https://tutorialsninja.com/demo/index.php?route=account/login")

    driver.find_element(By.ID,'input-email').send_keys("sofiavetisyan22@gmail.com")
    driver.find_element(By.ID,'input-password').send_keys("agbu123!@#")
    driver.find_element(By.XPATH,'//*[@id="content"]/div/div[2]/div/form/input').click()
