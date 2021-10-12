# imports
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import sys
import os
import requests
import shutil

currentDirectory = os.getcwd()
WebDriver  = webdriver.Chrome(f"{currentDirectory}//wallpaper-scraping//assets//driver//chromedriver.exe")
wait = WebDriverWait(WebDriver, 10)
WebDriver.get("https://wallhaven.cc/")
WebDriver.find_element_by_class_name("random").click()
mainPage = WebDriver.window_handles[0]

try:
    cycles = str(sys.argv[1])
except:
    cycles = 10000
finally:
    rangeOfImages = 8
    refreshes = int(cycles/rangeOfImages)
    print(refreshes)
    for x in range(refreshes):
        for n in range(rangeOfImages):
            # print(n)
            WebDriver.find_element_by_css_selector(f'li:nth-child({n+1}) figure').click()
            wallpaperPage = WebDriver.window_handles[1]
            WebDriver.switch_to.window(wallpaperPage)
            wallpaper = WebDriver.find_element_by_css_selector('#wallpaper').get_attribute("src")
            response = requests.get(wallpaper, stream=True)
            with open(f"{currentDirectory}//wallpaper-scraping//assets//img//{wallpaper[-10:-4]}.png", "wb") as out_file:
                shutil.copyfileobj(response.raw, out_file)
            del response
            WebDriver.close()
            WebDriver.switch_to.window(mainPage)
        
        WebDriver.refresh()
        n = 0