from selenium import webdriver
import selenium
from selenium.webdriver.support.select import Select
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


driver = webdriver.Chrome(executable_path="C:\\Users\\toshi\\AppData\\Local\\Programs\\Python\\Python39\\Lib\\site-packages\\chromedriver_binary\\chromedriver.exe")
driver.get("https://yahoo.co.jp")

#路線情報画面へ遷移
driver.find_element_by_xpath("/html/body/div/div/main/div[1]/nav/div/div/ul/li[25]/div/a/p/span[1]/span").click()
driver.implicitly_wait(5)

#検索条件入力
driver.find_element_by_xpath("/html/body/div/body/div/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/form/dl[1]/dd/input").send_keys("新宿駅")
driver.find_element_by_xpath("/html/body/div/body/div/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/form/dl[2]/dd/input").send_keys("東京駅")

#表示順序設定
dropdown = driver.find_element_by_id("s")
select = Select(dropdown)
select.select_by_value("2")


# driver.find_element_by_xpath("//*[@id=\"air\"]").click()
# driver.find_element_by_xpath("//*[@id=\"sexp\"]").click()

#有料特急を外す
#driver.find_element_by_xpath("//*[@id=\"mdRouteSearch\"]/div[2]/form/div/dl[2]/dd/ul[1]/li[3]").click()

#チェックボックスをすべて外す
block = driver.find_element(By.XPATH,"//dl[@class='optTransport']/dd/ul")
checkboxes = block.find_elements(By.NAME, "type")

print(len(checkboxes))

for checkbox in checkboxes:
    print("Before clicking : ", checkbox.is_selected())
    checkbox.click()
    print("After clicking : ", checkbox.is_selected())

#検索実行
#driver.find_element_by_id("searchModuleSubmit").click()
driver.find_element_by_xpath("//input[@id='searchModuleSubmit']").click()

