import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()

driver.get("https://7esl.com/english-verbs/")

#test = driver.find_element(By.XPATH, '//*[@id="post-15747"]/div/div[2]/ul[6]')
#//*[@id="post-15747"]/div/div[2]/ul[6]
#//*[@id="post-15747"]/div/div[2]/ul[24]
#print(test.text)
time.sleep(5)
longList = []
for i in range(6,25):
    list = driver.find_element(By.XPATH, f'//*[@id="post-15747"]/div/div[2]/ul[{i}]')
    #print(list.text)
    longList.append(list.text)


#print(longList)
finishedList = []
for i in longList:
    findIndex = i.find(":")
    finishedList.append(i[:findIndex])

for i in finishedList:
    print(i)


for i in longList:
    print(i)









waitforme = input("Press any key to continue!")
