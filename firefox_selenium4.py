from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import DriverManager
from selenium.webdriver import ActionChains
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FfService
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


ffservice = FfService(GeckoDriverManager().install())


driver = webdriver.Firefox(service=ffservice)
# driver.get("")
