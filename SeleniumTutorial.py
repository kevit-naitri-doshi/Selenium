from selenium import webdriver
from selenium.webdriver.common.by import By
import time

website='https://www.gordijnen.nl/wiki'
path='/home/kevit/Downloads/chromedriver-linux64/chromedriver'
cService = webdriver.ChromeService(executable_path=path)
driver = webdriver.Chrome(service = cService)
# driver.get('http://www.google.com')
driver.get(website)

allow_cookies=driver.find_element(By.XPATH,"//button[@id='CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll']")
allow_cookies.click()

close_button=driver.find_element(By.XPATH,"//a[@class='tlwd-absolute tlwd-top-0.5 tlwd-right-1 tlwd-text-xl']")
close_button.click()

data=''
# questions=[]
# items=[]
# answers=[]
# final_questions=[]
# final_answers=[]
# /html/body/main/div[4]/div[1]/div[1]/div/div/div[2]/div[6]/div/div/div[12]/p/a
main_item_index=1
while True:
    try:
        print('INSIDE ITEM LOOP TRY BLOCK')
        print()
        print(main_item_index)
        print()
        item=driver.find_element(By.XPATH,f'/html/body/main/div[4]/div[1]/div[1]/div/div/div[2]/div[{main_item_index}]/h2/button')

        print(f'Items: {item.text}')
        print()
        # items.append(item.text)
        # data.join(f'Items: {item.text}\n\n')
        f=open('WebScraping/Selenium/items.txt','a')
        f.write(f"Item: {item.text}\n\n")
        f.close()
        driver.execute_script("arguments[0].scrollIntoView();", item)
        time.sleep(1)
        item.click()
        questions_index=1
        while True:
            try:
                print("INSIDE QUESTION LOOP TRY BLOCK")
                print()
                print(f"QUESTION NUMBER {questions_index}")
                print()

                question=driver.find_element(By.XPATH,f'/html/body/main/div[4]/div[1]/div[1]/div/div/div[2]/div[{main_item_index}]/div/div/div[{questions_index}]/p/a')

                # time.sleep(1)

                print(f'Question: {question.text}')
                print()
                # data.join(f'Question: {question.text}\n')

                f=open('WebScraping/Selenium/items.txt','a')
                f.write(f'Question: {question.text}\n\n')
                f.close()
                # driver.execute_script('window.scrollBy(0, 1000)')
                driver.execute_script("arguments[0].scrollIntoView();", question)
                # driver.execute_script('arguments[0].scrollIntoView({behavior: "smooth", block: "center", inline: "nearest"}))', question)
                # questions.append(question.text)

                question.click()

                # time.sleep(1)
                
                answer=driver.find_element(By.XPATH,f'/html/body/main/div[4]/div[1]/div[1]/div/div/div[2]/div[{main_item_index}]/div/div/div[{questions_index}]/div')

                # time.sleep(1)
                
                driver.execute_script("arguments[0].scrollIntoView();", answer)

                # time.sleep(1)

                print(f'Answer: {answer.text}')
                print()
                # data.join(f'Answer: {answer.text}\n')
                f=open('WebScraping/Selenium/items.txt','a')
                f.write(f'Answer: {answer.text}\n\n')
                f.close()

                # if (answer.text):
                #     print(f'Answer: {answer.text}')
                #     print()
                # try:
                #     print("INSIDE CHILD ELEMENT CHECK TRY BLOCK")
                #     print()
                #     print(f"QUESTION NO. {questions_index}")
                #     print()

                #     answer_child_elements = answer.find_element(By.TAG_NAME, 'p')

                #     print(f'Answer: {answer_child_elements.text}')
                #     print()
                # except:
                #     # print(f'Answer: {answer.text}')
                #     print("CHILD ELEMENT EXCEPT BLOCK")
                #     print()
                #     print("NO CHILD ELEMENT")
                #     print()
                    
                # if answer_child_elements:
                #     print(f'Answer: {answer_child_elements.text}')
                # else:
                #     print(answer.text)

                # answers.append(answer.text)
                questions_index+=1
            except Exception as e:
                print("INSIDE QUESTION LOOP EXCEPT BLOCK ")
                print()
                print(f"QUESTION NUMBER {questions_index} GOT EXCEPTION")
                print()
                print(f"EXCEPTION: {e}")
                # final_questions.append(questions)
                # final_answers.append(answers)
                main_item_index+=1
                # questions_index=1
                break
                
    except Exception as e:
        print("INSIDE ITEM LOOP EXCEPT BLOCK ")
        print()
        print(f"QUESTION NUMBER {questions_index} IS LAST")
        print()
        print(f"EXCEPTION: {e}")
        break


# f=open('WebScraping/Selenium/items.txt','a')
# f.write(data)
# f.close()