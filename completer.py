from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# extract the form URL from the config file
with open("config.txt", "r") as f:
    FORM_URL = f.read()


# Set up the Firefox driver
driver = webdriver.Firefox()

# Navigate to the web page
driver.get(FORM_URL)

## PAGE 1 ##

# find my button by class
answer = driver.find_element(By.CLASS_NAME, "ulDsOb")
answer.click()

# wait a second
driver.implicitly_wait(2)

inainte = driver.find_element(By.CLASS_NAME, "NPEfkd")
inainte.click()

if driver.current_url == FORM_URL:
    # retry click
    inainte.click()

## PAGE 2 ##
    
PAGE_2_URL = driver.current_url

# find all divs containing questions
questions = driver.find_elements(By.CLASS_NAME, "geS5n")

for question in questions:
    # find question text
    question_text = question.find_element(By.CLASS_NAME, "M7eMe")
    # print(question_text.text)

    # find all answers
    answers = question.find_elements(By.CLASS_NAME, "Zki2Ve")
    answers[2].click()

# continue to next page
inainte = driver.find_elements(By.CLASS_NAME, "NPEfkd")
inainte[1].click()
driver.implicitly_wait(3)


## PAGE 3 ##
    
PAGE_3_URL = driver.current_url

# find all divs containing questions
questions = driver.find_elements(By.CLASS_NAME, "geS5n")

for question in questions:
    # find question text
    question_text = question.find_element(By.CLASS_NAME, "M7eMe")
    # print(question_text.text)

    # find all answers
    answers = question.find_elements(By.CLASS_NAME, "Zki2Ve")
    answers[3].click()

# continue to next page
inainte = driver.find_elements(By.CLASS_NAME, "NPEfkd")
inainte[1].click()
driver.implicitly_wait(3)


## PAGE 4 ##
    
PAGE_4_URL = driver.current_url

# find all divs containing questions
questions = driver.find_elements(By.CLASS_NAME, "geS5n")

for question in questions:
    # find question text
    question_text = question.find_element(By.CLASS_NAME, "M7eMe")
    # print(question_text.text)

    # find all answers
    answers = question.find_elements(By.CLASS_NAME, "Zki2Ve")
    answers[2].click()

# continue to next page
inainte = driver.find_elements(By.CLASS_NAME, "NPEfkd")
inainte[1].click()
driver.implicitly_wait(3)

## PAGE 5 ##
    
PAGE_5_URL = driver.current_url

# find all divs containing questions
questions = driver.find_elements(By.CLASS_NAME, "Qr7Oae")

for question in questions[1:]:
    # find question text
    question_text = question.find_element(By.CLASS_NAME, "M7eMe")
    # print(question_text.text)

    # find all answers
    answers = question.find_elements(By.CLASS_NAME, "docssharedWizToggleLabeledContainer")

    if len(answers) != 0:
        answers[0].click()
    else:
        # try to find input field by class, with possibility of not finding it
        try:
            input_field = question.find_element(By.CLASS_NAME, "whsOnd")
        except:
            input_field = None
        
        # check if input field was found
        if input_field:
            input_field.send_keys("test")
        else:
            # find textarea using CSS selector, by searching for a textarea
            textarea = question.find_element(By.CSS_SELECTOR, "textarea")
            textarea.send_keys("-")


# continue to next page
inainte = driver.find_elements(By.CLASS_NAME, "NPEfkd")
inainte[1].click()
driver.implicitly_wait(3)


# # Close the browser
# # driver.close()
