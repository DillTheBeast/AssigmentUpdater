import os
import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from PIL import Image

def takeScreenshot(driver, folder_path, file_name):
    # Ensure the folder exists
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # Take a screenshot using Selenium
    screenshot_path = os.path.join(folder_path, file_name + ".png")
    driver.save_screenshot(screenshot_path)

    # Open the screenshot using PIL for additional processing if needed
    img = Image.open(screenshot_path)

    # Perform additional processing if needed
    # For example, you can resize or crop the image using PIL

    # Save the processed image
    img.save(screenshot_path)

    return screenshot_path

def getLastFileName(folder_path):
    # List all files in the folder
    files = os.listdir(folder_path)

    # Check if there is exactly one file in the folder
    if len(files) == 1:
        # Extract the name of the only file
        file_name = files[0]
        return file_name
    else:
        # Handle the case where there are no files or more than one file
        return None

email = input("Please enter the email address used for MyKing\n")
password = input("Please enter your password for MyKing\n")

#Getting the path to the folder with the last screenshot and getting the file name in it
folderPath = "/Users/dillonmaltese/Documents/GitHub/AssigmentUpdater/screenshots"
#oldFileName = getLastFileName(folderPath)
#newFileName = oldFileName + "1"
newFileName = "Test"

#Making the Chrome Driver path
chrome_driver_path = "/Users/dillonmaltese/Documents/GitHub/Selenium/chromedriver_mac64"
os.environ["PATH"] += os.pathsep + os.path.dirname(chrome_driver_path)

# Initialize the Chrome WebDriver
driver = webdriver.Chrome()

#Going to MyKing and waiting for a little to let it load
driver.get("https://kingschoolct.myschoolapp.com/app/student#studentmyday/assignment-center")
time.sleep(5)

#Attempting to do next code and if it fails give a detailed error message
try:
    #Finding textbox that is for the username
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "Username")))
    
    #Entering the email address given
    element.send_keys(email)

    time.sleep(5)

    # Find and click the next button
    login_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "nextBtn")))
    login_button.click()

    time.sleep(7)

    #Find and click the sign in with google button
    button = driver.find_element(By.CSS_SELECTOR, 'button[aria-labelledby="googleButtonLabel"]')
    button.click()

    time.sleep(5)

    #Signing in to the google account
    pyautogui.typewrite(email)
    pyautogui.typewrite("\n")
    time.sleep(3)
    pyautogui.typewrite(password)
    pyautogui.typewrite("\n")
    
    time.sleep(5)
    
    driver.maximize_window()
    
    time.sleep(2)
    
    for x in range(3):  # Scroll three times
        takeScreenshot(driver, folderPath, newFileName)
        driver.execute_script("window.scrollBy(0, 500);")
        time.sleep(2)
        newFileName = "Test" + x
    time.sleep(2)

except Exception as e:
    print(f"An error occurred: {e}")