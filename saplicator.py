from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time


webdriver_path = r'C:\Users\Rumay-Paz\Desktop\Accenture\Trainings\SQLita\session5 - RPA\chromedriver.exe'

urls = ['https://emprego.sapo.pt/offers/rpa-junior-developer?id=953fc519-3448-4020-868e-160a8364af52',
        'https://emprego.sapo.pt/offers/tecnico-p-robotics-process-automation-mf?id=65d0dc9d-7fce-48c5-b912-b698be3f4b98',
        'https://emprego.sapo.pt/offers/rpa-developer-mf-porto?id=ce762e23-8786-47be-9c82-4aed68632a9d',
        'https://emprego.sapo.pt/offers/analista-rpa?id=168ea44f-eea6-45ed-b131-289dd847f98e',
        'https://emprego.sapo.pt/offers/rpa-developer?id=a7aa24c9-803f-42bb-8f7c-253ae3d5db1c',
        'https://emprego.sapo.pt/offers/software-developer-rpa-portugal?id=b7638f86-6881-442e-928d-4cd7c9e38c4a',
        'https://emprego.sapo.pt/offers/rpa-developer?id=af0d7b42-c27f-49f1-a8af-09bdb585290d',
        'https://emprego.sapo.pt/offers/rpaanalyst-developer?id=8ea296cf-94dd-4f0e-b37c-ec80adc8c068',
        'https://emprego.sapo.pt/offers/rpa-business-analyst?id=a731359d-8aad-448b-a8eb-b095117d4504',
        'https://emprego.sapo.pt/offers/rpa-developer?id=44ebe36c-e9bf-4c6b-b220-c1d9f747484b',
        'https://emprego.sapo.pt/offers/rpa-consultant-mf-lisboa?id=6b7fbfa1-06b8-4526-8419-d3b9ff22cfa0',
        'https://emprego.sapo.pt/offers/consultor-rpa?id=b3146d9e-81a0-4b79-b185-03c5945ed5cd']



nombre = "Victor Rumay"
mail = 'rumayv@gmail.com'
tlf = '+5491161347210'
resume = 'C:\\Users\\Rumay-Paz\\Desktop\\Personal\\Victor Rumay - Resume.pdf'



browser = webdriver.Chrome(webdriver_path)
for url in urls:

    newUrl = 'https://emprego.sapo.pt/apply-job/' + url.split('=')[1]

    browser.get(newUrl)
       

    # Give it a second man, it's going to space and coming back to earth
    time.sleep(1)

    try:
        # Input Name
        emailField = browser.find_element_by_id("nome")
        emailField.send_keys(Keys.CONTROL + "a")
        emailField.send_keys(Keys.DELETE)
        emailField.send_keys(nombre)


        # Input Email
        emailField = browser.find_element_by_id("email")
        emailField.send_keys(Keys.CONTROL + "a")
        emailField.send_keys(Keys.DELETE)
        emailField.send_keys(mail)

        # Input Telephone Number
        tlfField = browser.find_element_by_id("telefone")
        tlfField.send_keys(Keys.CONTROL + "a")
        tlfField.send_keys(Keys.DELETE)
        tlfField.send_keys(tlf)

        # Input path to resume file
        uploadFile = browser.find_element_by_xpath('//*[@id="cv"]')
        uploadFile.send_keys(resume)

        # Click data privacy consents            
        clickyOne = browser.find_element_by_xpath('//*[@id="apply-job"]/div/div[2]/div/div/div[2]/form/div/div[7]/div/ul/li[3]/label').click()
        
        
        # Send Application
        clickySend = browser.find_element_by_xpath('//*[@id="apply-job"]/div/div[2]/div/div/div[2]/form/div/div[8]/div/button/span').click()

    except:
        print("That job isn't posted anymore :(")  
        pass