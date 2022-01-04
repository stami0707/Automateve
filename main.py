from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

URL = r"https://teveclub.hu/"
USER = "Segfaulteve"
PWD = ""

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(URL)

driver.execute_script("document.getElementsByName('tevenev').value = \"" + USER + " \";")
driver.execute_script("document.getElementsByName('pass').value = \"" + PWD + " \";")

