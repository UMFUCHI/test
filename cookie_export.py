from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import selenium
import pickle
import time
import data
from seleniumwire import webdriver
from colorama import Fore

options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")


def export():
    for i in range(len(data.login)):
        print(f"{i+1}. {data.login[i]}")
        driver = webdriver.Chrome(service=Service('\\Google\\chromedriver.exe'), options=options)
        driver.minimize_window()
        try:
            driver.get(url="https://twitter.com/i/flow/login/")
            time.sleep(1)

            selenium.webdriver.support.wait.WebDriverWait(driver, 120).until(lambda x: x.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div'))#чекає поки прогрузить вікно для логіну
            driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label').send_keys(data.login[i])
            driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]').click()#Нажимає далее після вводу логіну

            selenium.webdriver.support.wait.WebDriverWait(driver, 120).until(lambda x: x.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label'))
            driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label').send_keys(data.password[i])
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@data-testid="LoginForm_Login_Button"]').click()#Війти

            time.sleep(3)
            if driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input') == None:
                print('email none')
                pass
            else:
                time.sleep(1)
                driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input').send_keys(data.twitemails[i])
                time.sleep(0.5)
                driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div').click()

            time.sleep(5)
            pickle.dump(driver.get_cookies(), open(f'cookie/{data.login[i]}_cookies', 'wb'))
        except Exception as ex:
            print(ex)
        finally:
            driver.close()
            driver.quit()
