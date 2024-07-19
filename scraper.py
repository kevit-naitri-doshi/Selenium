from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from config import *


cService = webdriver.ChromeService(executable_path=path)
driver = webdriver.Chrome(service = cService)
driver.get(website)

allow_cookies=driver.find_element(By.XPATH,"//button[@id='CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll']")
allow_cookies.click()

close_button=driver.find_element(By.XPATH,"//a[@class='tlwd-absolute tlwd-top-0.5 tlwd-right-1 tlwd-text-xl']")
close_button.click()

data=''
main_item_index=1
while True:
    try:
        item=driver.find_element(By.XPATH,f'/html/body/main/div[4]/div[1]/div[1]/div/div/div[2]/div[{main_item_index}]/h2/button')

        print(f'Items: {item.text}')
        print()
        f=open('WebScraping/Selenium/items.txt','a')
        f.write(f"Item: {item.text}\n\n")
        f.close()
        driver.execute_script("arguments[0].scrollIntoView();", item)
        item.click()
        questions_index=1
        while True:
            try:

                question=driver.find_element(By.XPATH,f'/html/body/main/div[4]/div[1]/div[1]/div/div/div[2]/div[{main_item_index}]/div/div/div[{questions_index}]/p/a')

                print(f'Question: {question.text}')
                print()

                f=open('WebScraping/Selenium/items.txt','a')
                f.write(f'Question: {question.text}\n\n')
                f.close()
                driver.execute_script("arguments[0].scrollIntoView();", question)

                question.click()

                answer=driver.find_element(By.XPATH,f'/html/body/main/div[4]/div[1]/div[1]/div/div/div[2]/div[{main_item_index}]/div/div/div[{questions_index}]/div')
                
                driver.execute_script("arguments[0].scrollIntoView();", answer)

                print(f'Answer: {answer.text}')
                print()

                f=open('WebScraping/Selenium/items.txt','a')
                f.write(f'Answer: {answer.text}\n\n')
                f.close()

                questions_index+=1
            except Exception as e:
                print("INSIDE QUESTION LOOP EXCEPT BLOCK ")
                print()
                print(f"QUESTION NUMBER {questions_index} GOT EXCEPTION")
                print()
                print(f"EXCEPTION: {e}")

                main_item_index+=1

                break
                
    except Exception as e:
        break
