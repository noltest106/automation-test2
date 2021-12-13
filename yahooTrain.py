from selenium import webdriver
from selenium.webdriver import Chrome
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


driver = webdriver.Chrome(executable_path="C:\\Users\\toshi\\AppData\\Local\\Programs\\Python\\Python39\\Lib\\site-packages\\chromedriver_binary\\chromedriver.exe")
driver.get("https://yahoo.co.jp")
