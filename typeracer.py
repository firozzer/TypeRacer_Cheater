import msvcrt #helps in capturing input from user without the need of pressing enter
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome() #ensure to put chromedriver.exe in C:\Windows\system32 for this to work
driver.get("https://play.typeracer.com/")
time.sleep(4) #takes some time for the homepage to load
elemBody = driver.find_element_by_tag_name('body') #initializing this variable just so can send keyboard shortcuts on it.
elemBody.send_keys(Keys.CONTROL, Keys.ALT, 'l')
button=driver.find_element(By.XPATH,"""//td[text()="Choose a guest nickname (play without an account)"]""")
button.click()
usernameField = driver.find_element(By.XPATH, """//div[text()="Nickname:"]/parent::*/following-sibling::*/input""") #Finding div containing 'Nickname:', then go to whatever (*) is the parent, then whatever is the next sibling element, and then the tag 'input' therein.
usernameField.clear() # remove the pre-existing Guest therein
usernameField.send_keys("Gorian Dray",Keys.RETURN);time.sleep(1) # enter whatever username you want here.
elemBody.send_keys(Keys.CONTROL, Keys.ALT, 'i')
time.sleep(1)
checkerboi = 'yes'
while checkerboi == 'yes': #simple while loop so that once you pass the captcha test manually, you can just give any input to the program & it will restart.
    elementOfStuffedToBeTyped=driver.find_elements_by_xpath("//span[@unselectable = 'on']") #locates the text to be typed using the unselectable tag
    listOfthingToBeTyped = []
    for i in elementOfStuffedToBeTyped:
        listOfthingToBeTyped.append(i.text) # .text obtains the text from an HTML element grabbed by selenium.
    if len(listOfthingToBeTyped) == 3: #Usually TypeRacer splits it up into 3 or 2 span fields. This gives treatment respectively. 10% chance this step will fail, haven't othered to rectify it yet as anyway i can never overcome their test captcha.
        listOfthingToBeTyped[1] = listOfthingToBeTyped[1]+' '
        stringToBeTyped = ''.join(listOfthingToBeTyped)
    else:
        stringToBeTyped = ' '.join(listOfthingToBeTyped)
    print(stringToBeTyped)
    raceField=driver.find_element_by_xpath("//input[@autocorrect='off' and @autocapitalize='off']")
    print('Should i go ahead?')
    input_char = msvcrt.getch() #once the race starts press any character in the cmd window to start auto-typing.
    length = len(stringToBeTyped)
    stringToBeTyped1 = stringToBeTyped[:int(length/5)] #splitting up into 5 parts otherwise TypeRacer disqualifies instantly as it detects a bot.
    stringToBeTyped2 = stringToBeTyped[int(length/5):int(length*2/5)]
    stringToBeTyped3 = stringToBeTyped[int(length*2/5):int(length*3/5)]
    stringToBeTyped4 = stringToBeTyped[int(length*3/5):int(length*4/5)]
    stringToBeTyped5 = stringToBeTyped[int(length*4/5):]
    raceField.send_keys(stringToBeTyped1);time.sleep(2) #random sleep timings
    raceField.send_keys(stringToBeTyped2);time.sleep(1)
    raceField.send_keys(stringToBeTyped3);time.sleep(2)
    raceField.send_keys(stringToBeTyped4);time.sleep(1)
    raceField.send_keys(stringToBeTyped5);time.sleep(1)
    print('Race Done?') # pass the captcha test manually in your browser. Then once you go onto a new test, come into cmd press any key & while loop will restart.
    input_char = msvcrt.getch()
