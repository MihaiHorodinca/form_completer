from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


QUIESTION_CARD_CLASS = "geS5n"
QUIESTION_TEXT_CLASS = "M7eMe"
PAGE_CONTROL_CLASS = "NPEfkd"


def controll_page(index = 0):
    page_controll_buttons = driver.find_elements(By.CLASS_NAME, PAGE_CONTROL_CLASS)
    page_controll_buttons[index].click()


# create a function that fills in all question in a page
def complete_question_page(driver):
    questions = driver.find_elements(By.CLASS_NAME, QUIESTION_CARD_CLASS)
    for question in questions:
        # find question text
        question_text = question.find_element(By.CLASS_NAME, QUIESTION_TEXT_CLASS)
        # print(question_text.text)

        # find all answers
        answers = question.find_elements(By.CLASS_NAME, "Zki2Ve")
        answers[0].click()

    # continue to next page
    controll_page(1)
    driver.implicitly_wait(3)


def complete_final_page(driver):
    # find all divs containing questions
    questions = driver.find_elements(By.CLASS_NAME, "Qr7Oae")

    for question in questions[1:]:
        # find question text
        question_text = question.find_element(By.CLASS_NAME, QUIESTION_TEXT_CLASS)
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
    
    controll_page(1)


with open("config.txt", "r") as f:
    FORM_URL = f.read()

driver = webdriver.Firefox()
driver.get(FORM_URL)

## PAGE 1 ##
answer = driver.find_element(By.CLASS_NAME, "ulDsOb")
answer.click()

driver.implicitly_wait(2)

controll_page(0)
if driver.current_url == FORM_URL:
    # retry click
    controll_page(0)

## PAGE 2 ##
complete_question_page(driver)

## PAGE 3 ##
complete_question_page(driver)

## PAGE 4 ##
complete_question_page(driver)

## PAGE 5 ##
complete_final_page(driver)

# # Close the browser
# # driver.close()
