from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

funds_url = 'https://www.kh.hu/megtakaritas-befektetes/befektetesi-alap-arfolyam'
driver = None

isin = 'HU0000715594'
navigate_to_unit_cell = "//td[text()='%s']/..//td[contains(@class, 'navPerUnit')][1]"

try:
    driver = webdriver.Firefox()
    driver.get(funds_url)

    element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH,
                                          navigate_to_unit_cell % isin)))
    print(element.text)
except Exception as e:
    print("ERROR: " + str(e))
finally:
    if driver is not None:
        driver.close()
