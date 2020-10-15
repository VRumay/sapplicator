from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time


webdriver_path = r'C:\Users\Rumay-Paz\Desktop\Accenture\Trainings\SQLita\session5 - RPA\chromedriver.exe'

urls = ['https://emprego.sapo.pt/apply-job/51c24b4c-6609-4636-bd3f-e16bed638cc5',
        'https://emprego.sapo.pt/apply-job/99e3accd-91f3-41bd-98ef-cfd163e14f4a',
        'https://emprego.sapo.pt/apply-job/883bc063-1d8d-4303-b9a0-7908d2fa1b12',
        'https://emprego.sapo.pt/apply-job/92f6c2cf-53a5-4cb6-923a-3b4a1cb0d00e',
        'https://emprego.sapo.pt/apply-job/03ef6dd4-cfbe-40ac-a2cf-8911d1d5ac28',
        'https://emprego.sapo.pt/apply-job/b83c31d2-3cba-4001-84d9-bb0e1a20ad47',
        'https://emprego.sapo.pt/apply-job/8d18f6b9-8e44-4a9a-b7ca-73aa8c05f8ff',
        'https://emprego.sapo.pt/apply-job/d2ce721a-1134-47c9-933f-8a539fd63dd0',
        'https://emprego.sapo.pt/apply-job/03ef6dd4-cfbe-40ac-a2cf-8911d1d5ac28',
        'https://emprego.sapo.pt/apply-job/b83c31d2-3cba-4001-84d9-bb0e1a20ad47',
        'https://emprego.sapo.pt/apply-job/9e7ff056-01ad-4af3-a195-38ca5eade88a',
        'https://emprego.sapo.pt/apply-job/8b06457a-6343-4cb2-b866-0afd3e469eb7',
        'https://emprego.sapo.pt/apply-job/5d80f052-aaa0-40e2-8f58-8c64a4f54274',
        'https://emprego.sapo.pt/apply-job/870701d9-a0b2-4a75-882e-c486da00142e',
        'https://emprego.sapo.pt/apply-job/fa08f627-8b49-49fb-b098-0809f0b490af',
        'https://emprego.sapo.pt/apply-job/a8ded9b9-91f4-4035-8ff2-8945eee3fe46',
        'https://emprego.sapo.pt/apply-job/fce75955-18d0-4339-8f65-275a8ee8e1cd',
        'https://emprego.sapo.pt/apply-job/b71d1500-78c1-4a4a-a6fc-0e2ba42aaec1',
        'https://emprego.sapo.pt/apply-job/d4d9d4f2-fd8b-48c1-8197-0b162160ed66',
        'https://emprego.sapo.pt/apply-job/b71d1500-78c1-4a4a-a6fc-0e2ba42aaec1',
        'https://emprego.sapo.pt/apply-job/32ce935b-e01f-4a91-8202-5340d0ea51c3',
        'https://emprego.sapo.pt/apply-job/7d85b2f2-63f4-40c6-a294-dc263f61bfbd',
        'https://emprego.sapo.pt/apply-job/ea8650a5-49c0-4c58-aa2a-b9ecad9cad8b',
        'https://emprego.sapo.pt/apply-job/4a6748f7-dc23-4edc-9e27-813e2bad546a',
        'https://emprego.sapo.pt/apply-job/c195f445-a247-4432-9881-174c413aeb28',
        'https://emprego.sapo.pt/apply-job/78921aa6-694c-4a8e-b9e1-350cb058f37b',
        'https://emprego.sapo.pt/apply-job/0c9f38ba-b0b3-4ab7-9a89-e158760b775e',
        'https://emprego.sapo.pt/apply-job/2e1a1ce1-2dcc-4a97-8957-a255dc110852']

nombre = "Victor Rumay"
mail = 'rumayv@gmail.com'
tlf = '+5491161347210'
resume = 'C:\\Users\\Rumay-Paz\\Desktop\\Personal\\Victor Rumay - Resume.pdf'



browser = webdriver.Chrome(webdriver_path)
for url in urls:
    browser.get(url)
       

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