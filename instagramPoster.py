import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import csv
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui
import zipfile
import os

#Hearthstone9


def PostThing(url,username1,password1,subreddit):
    for i in range(1):
        
        print(f"POST ATTEMPT 1")
        
        PATH = "C:\Program Files (x86)\chromedriver.exe"

        driver = webdriver.Chrome(PATH)
        action = webdriver.ActionChains(driver)

        #---DOWNLOADING 

        driver.get("https://redditdownloader.github.io/")

        time.sleep(2)
    
        #send subreddit
        search = driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/div[1]/input")
        search.send_keys(subreddit)

        time.sleep(1)

        #turn off imgur and gyfcat
        search = driver.find_element_by_xpath("/html/body/div/div[2]/div[3]/div[2]/div[3]/div/div/div/label")
        search.click()

        #turn off vidoes
        search = driver.find_element_by_xpath("/html/body/div/div[2]/div[3]/div[2]/div[1]/div[2]/div/div/div/label")
        search.click()

        time.sleep(1)
        
        #click download
        search = driver.find_element_by_xpath("/html/body/div/div[2]/button")
        search.click()

        time.sleep(7)

        zipName = f"{subreddit}_hot.zip"

        directory = (fr"C:\Users\Henrik\Downloads\{zipName}")

        time.sleep(2)

        driver.quit

        #---GOING TO INSTAGRAM

        driver.get(url)
        
        time.sleep(3)

        search = driver.find_element_by_xpath("/html/body/div[4]/div/div/button[1]")
        search.click()

        search = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input")
        search.send_keys(username1)

        search = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input")
        search.send_keys(password1)

        time.sleep(1)

        search = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]/button/div")
        search.click()
        #logged in

        time.sleep(3)

        
        # iterate over files in
        # that directory

        
    files = zipfile.ZipFile(directory, "r")
    for name in files.namelist():
        print(files.namelist())

        pathName = os.path.abspath(fr"C:\Users\Henrik\Downloads\{zipName}\{name}")
        coolPath = os.path.join(directory, name)
        print(pathName)
        print(coolPath)

        time.sleep(5)

        search = driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[3]/div/button")
        search.click()

        time.sleep(2)

        clickUpload = driver.find_element_by_xpath("/html/body/div[8]/div[2]/div/div/div/div[2]/div[1]/div/div/div[2]/div/button")
        clickUpload.click()
        time.sleep(1)
        pyautogui.write(pathName) 
        pyautogui.press('enter')

        time.sleep(1)
        #crop

        buttonNext = driver.find_element_by_xpath("/html/body/div[6]/div[2]/div/div/div/div[2]/div[1]/div/div/div/div[1]/div/div[2]/div/button")
        buttonNext.click()
        time.sleep(1)

        buttonNext = driver.find_element_by_xpath("/html/body/div[6]/div[2]/div/div/div/div[2]/div[1]/div/div/div/div[1]/div/div[1]/div/button[1]")
        buttonNext.click()

        #done cropping
        time.sleep(1)

        buttonNext = driver.find_element_by_xpath("/html/body/div[6]/div[2]/div/div/div/div[1]/div/div/div[3]/div/button")
        buttonNext.click()

        time.sleep(1)

        buttonNext = driver.find_element_by_xpath("/html/body/div[6]/div[2]/div/div/div/div[1]/div/div/div[3]/div/button")
        buttonNext.click()
                
        time.sleep(0.5)
        #write caption
                
        captionWriteArea = driver.find_element_by_xpath("/html/body/div[6]/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/textarea")
        captionWriteArea.send_keys("#meme #funny #memedayeveryday #everymemetoday")

        time.sleep(0.5)

        buttonShare = driver.find_element_by_xpath("/html/body/div[6]/div[2]/div/div/div/div[1]/div/div/div[3]/div/button")
        buttonShare.click()

        time.sleep(6)

        buttonX = driver.find_element_by_xpath("/html/body/div[6]/div[1]/button")
        buttonX.click()

        time.sleep(30)

        #might not need this down here

        #driver.quit()
    os.remove(directory)

if __name__ == '__main__':
    #type username password
    name = "everymemetoday"
    password = "FreeTyler1"
    subRedditToDownload = "okbuddyretard"
    PostThing("https://www.instagram.com/",name,password,subRedditToDownload)