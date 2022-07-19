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

def PostThing(url,username1,password1):
    for i in range(1):
        
        print(f"POST ATTEMPT 1")
        
        PATH = "C:\Program Files (x86)\chromedriver.exe"

        driver = webdriver.Chrome(PATH)
        driver.get(url)
        action = webdriver.ActionChains(driver)
        
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

        import os
        directory = "PhotosToUpload"
        
        # iterate over files in
        # that directory

        directory = r"C:\Users\Henrik\Documents\PROGRAMMING\Instagram bot\memesToUpload"

        for filename in os.scandir(directory):
            if filename.is_file():

                print(filename.path)

                #drv.find_element_by_id("IdOfInputTypeFile").send_keys(os.getcwd()+"/image.png")
                time.sleep(0.5)

                search = driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[3]/div/button")
                search.click()

                time.sleep(0.5)

                clickUpload = driver.find_element_by_xpath("/html/body/div[8]/div[2]/div/div/div/div[2]/div[1]/div/div/div[2]/div/button")
                clickUpload.click()
                time.sleep(1)
                pyautogui.write(filename.path) 
                pyautogui.press('enter')

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

                time.sleep(40)


        #might not need this down here

        time.sleep(100)

        #driver.quit()

if __name__ == '__main__':
    #type username password
    name = "everymemetoday"
    password = "FreeTyler1"
    PostThing("https://www.instagram.com/",name,password)