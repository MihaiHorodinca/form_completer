from GPTconnection import AnswerBot
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


QUIESTION_CARD_CLASS = "geS5n"
QUIESTION_TEXT_CLASS = "M7eMe"
PAGE_CONTROL_CLASS = "NPEfkd"

all_questions = []


def controll_page(index = 0):
    page_controll_buttons = driver.find_elements(By.CLASS_NAME, PAGE_CONTROL_CLASS)
    page_controll_buttons[index].click()


# create a function that fills in all question in a page
def complete_question_page(driver, answer_bot: AnswerBot):
    questions = driver.find_elements(By.CLASS_NAME, QUIESTION_CARD_CLASS)
    for question in questions:
        question_text = question.find_element(By.CLASS_NAME, QUIESTION_TEXT_CLASS).text
        all_questions.append(question_text)

        answers = question.find_elements(By.CLASS_NAME, "Zki2Ve")
        # answer_index = answer_bot.answer(question_text)
        answers[1].click()

    # continue to next page
    controll_page(1)


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
    FORM_URL, APY_KEY = f.readlines()

driver = webdriver.Firefox()
driver.get(FORM_URL)

with open("persona_prompt.txt", "r") as f:
    PERSONA_PROMPT = f.readlines()

answer_bot = AnswerBot(APY_KEY, PERSONA_PROMPT)

## PAGE 1 ##
answer = driver.find_element(By.CLASS_NAME, "ulDsOb")
answer.click()

time.sleep(1)
controll_page(0)
controll_page(0)
time.sleep(2)

## PAGE 2 ##
answer_bot.set_limits(1, "never", 5, "very often")
complete_question_page(driver, answer_bot)

## PAGE 3 ##
answer_bot.set_limits(1, "totally agree", 7, "totally disagree")
complete_question_page(driver, answer_bot)

## PAGE 4 ##
answer_bot.set_limits(1, "totally agree", 5, "totally disagree")
complete_question_page(driver, answer_bot)

## PAGE 5 ##
# complete_final_page(driver)

with open("intrebari.txt", "w+") as f:
    f.writelines(all_questions)

# # Close the browser
# # driver.close()
