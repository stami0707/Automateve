__maintainer__ = "Süli Tamara"
__version__ = "1.3"
__date__ = "2022.01.07."

import os
import tkinter
import tkinter.messagebox

import dotenv
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

dotenv.load_dotenv()


def messagebox(title, text):
    root = tkinter.Tk()
    root.withdraw()
    tkinter.messagebox.showerror(title, text)
    root.destroy()


### OPEN BROWSER ###

driver = Chrome(service=Service(ChromeDriverManager().install()))
driver.get(r"https://teveclub.hu/")

### LOGIN ###

input_user = driver.find_element(By.NAME, 'tevenev')
input_user.send_keys(os.getenv("USER"))

input_pwd = driver.find_element(By.NAME, 'pass')
input_pwd.send_keys(os.getenv("PWD"))

WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[src='/img_des/login_submit_46.gif'][type='image']"))).click()

if driver.current_url == "https://teveclub.hu/error.pet?code=wronglogin":
    messagebox("Automateve - Hiba", "Hibás felhasználónév vagy jelszó!")
    quit()

### ETETÉS (1 étel és ital) ###

try:
    driver.find_element(By.CSS_SELECTOR, "input[name='etet'][type='submit']").click()
except NoSuchElementException:
    pass

### TANÍTÁS ###

driver.find_element(By.CSS_SELECTOR, '[alt="Tanítom a tevémet!"]').click()

try:
    driver.find_element(By.NAME, "learn").click()
except NoSuchElementException:
    messagebox("Automateve - Hiba", "Ma már tanult " + os.getenv("USER") + "! :( (vagy ki kell választanod, mit tanuljon mától)")
