from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = None
try:
    driver = webdriver.Firefox()
    driver.get('https://www.kh.hu/megtakaritas-befektetes/befektetesi-alap-arfolyam')

    element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH,
            "//td[text()='HU0000715594']/..//td[contains(@class, 'navPerUnit')][1]")))
    print(element.text)
except e:
    print("ERROR: " + e)
finally:
    if driver is not None:
        driver.close()
