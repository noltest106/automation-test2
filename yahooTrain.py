from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service


driver = webdriver.Chrome(executable_path="\\wsl.localhost\Ubuntu-20.04\home\nol\automation-test2\chromedriver.exe")
driver.get("https://yahoo.co.jp")
