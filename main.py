from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import speech_recognition as sr
import pyttsx3
import time
# import Action chains
from selenium.webdriver.common.action_chains import ActionChains
 
# import KEYS
from selenium.webdriver.common.keys import Keys
 
driver = None

def clickE(xpath):
    global driver
    try:
        element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, xpath)))
        print("Clicking " + xpath)
        element.click()
    except NoSuchElementException as e:
        print(str(e) + "Element does not exist!")

def inputText(xpath, text):
    global driver
    text_field = driver.find_element(By.XPATH, xpath)
    text_field.send_keys(text)
 
def automateYoutube(searchtext):
    global driver
    # giving the path of chromedriver to selenium webdriver
    path = "chromedriver"
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.binary_location = "E:\\Program Files\\Google\\Chrome Beta\\Application\chrome.exe"

    url = "https://www.youtube.com/"
     
    # opening the youtube in chromedriver
    driver = webdriver.Chrome(path,options=options)
    driver.get(url)
    say("Special for you")
    # inputText('//*[@id="search"]', 'rick roll')
    driver.get('https://www.youtube.com/watch?v=BBJa32lCaaY')
    # create action chain object
    action = ActionChains(driver)
     
    # perform the operation
    action.key_down(Keys.CONTROL).send_keys(' ').key_up(Keys.CONTROL).perform()
    action.key_down(Keys.CONTROL).send_keys('f').key_up(Keys.CONTROL).perform()

def say(text) :
    engine.say(text)
    print(text)
    engine.runAndWait()

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('rate', 200)
 
speak = sr.Recognizer()

say("Hello sir")
say("Do you want me to open youtube?")

try:
    with sr.Microphone() as speaky:
       
        # adjust the energy threshold based on
        # the surrounding noise level
        speak.adjust_for_ambient_noise(speaky, duration=0.2)
        print("Waiting for answer")
        
        # listens for the user's input
        searchquery = speak.listen(speaky)
         
        # Using google to recognize audio
        MyText = speak.recognize_google(searchquery)
        MyText = MyText.lower()

        while MyText == "no":
            say("Sure, i'll wait")
            # listens for the user's input
            searchquery = speak.listen(speaky)
             
            # Using google to recognize audio
            MyText = speak.recognize_google(searchquery)
            MyText = MyText.lower()
        say("Okay, i'll play a video for you")
 
except sr.RequestError as e:
    print("Could not request results; {0}".format(e))
 
except sr.UnknownValueError:
    print("unknown error occurred")
 
#Calling the function
automateYoutube("Rick Roll")
