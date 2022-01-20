__maintainer__ = "Süli Tamara"
__version__ = "1.6"
__date__ = "2022.01.20."

import win32.lib.win32con as win32con
import win32gui
import os
import plyer.platforms.win.notification
from plyer import notification
import dotenv
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

the_program_to_hide = win32gui.GetForegroundWindow()
win32gui.ShowWindow(the_program_to_hide, win32con.SW_HIDE)

dotenv.load_dotenv()

### OPEN BROWSER ###

options = ChromeOptions()
options.add_argument('headless')
service = Service(ChromeDriverManager().install())
driver = Chrome(service=service, options=options)
driver.headless = True
driver.get(r"https://teveclub.hu/")

### LOGIN ###

input_user = driver.find_element(By.NAME, 'tevenev')
input_user.send_keys(os.getenv("USER"))

input_pwd = driver.find_element(By.NAME, 'pass')
input_pwd.send_keys(os.getenv("PWD"))

WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[src='/img_des/login_submit_46.gif'][type='image']"))).click()

if driver.current_url == "https://teveclub.hu/error.pet?code=wronglogin":
    notification.notify("Automateve - Hiba", "Hibás felhasználónév vagy jelszó!")
    quit()

### ETETÉS (1 étel és ital) ###

try:
    driver.find_element(By.CSS_SELECTOR, "input[name='etet'][type='submit']").click()
except NoSuchElementException:
    pass

### TANÍTÁS ###

driver.find_element(By.CSS_SELECTOR, '[alt="Tanítom a tevémet!"]').click()

try:
    driver.find_element(By.NAME, "tudomany")
    notification.notify("Automateve - Info", "Ideje ránézni a kis kedvencedre, megint tanult valami újat! :D")
    quit()

except NoSuchElementException:
    try:
        driver.find_element(By.NAME, "learn").click()
    except NoSuchElementException:
        notification.notify("Automateve - Info", "Ajaj, ma már tanult " + os.getenv("USER") + "! :(")
