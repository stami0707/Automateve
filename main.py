__maintainer__ = "Süli Tamara"
__version__ = "1.1"
__date__ = "2022.01.07."

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager

USER = ""  #Add meg a tevéd nevét!
PWD = ""   #Add meg a tevéd hívójelét!

### OPEN BROWSER ###

driver = Chrome(service=Service(ChromeDriverManager().install()))
driver.get(r"https://teveclub.hu/")

### LOGIN ###

input_user = driver.find_element(By.NAME, 'tevenev')
input_user.send_keys(USER)

input_pwd = driver.find_element(By.NAME, 'pass')
input_pwd.send_keys(PWD)

WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[src='/img_des/login_submit_46.gif'][type='image']"))).click()

### ETETÉS (1 étel és ital) ###

try:
    driver.find_element(By.CSS_SELECTOR, "input[name='etet'][type='submit']").click()
except NoSuchElementException:
    pass

### TANÍTÁS (ha már van elkezdve) ###

try:
    driver.find_element(By.CSS_SELECTOR, '[alt="Tanítom a tevémet!"]').click()
    driver.find_element(By.NAME, "learn").click()
except NoSuchElementException:
    pass
