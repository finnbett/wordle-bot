from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()

initial_word = 'ADIEU'


def start_wordle():
    driver.get('https://www.nytimes.com/games/wordle/index.html')
    time.sleep(3)
    exit_instructions = driver.find_element(by=By.TAG_NAME, value='body')
    exit_instructions.click()
    body = driver.find_element(by=By.TAG_NAME, value='body')
    body.send_keys(initial_word, Keys.ENTER)


start_wordle()


possible_words = open("wordlist", "r")

list_of_words = []
for line in possible_words:
    stripped_line = line.strip()
    # line_list = stripped_line.split()
    list_of_words.append(stripped_line)

possible_words.close()
# print(list_of_words)


list_of_words_split = [list(word) for word in list_of_words]
# print(list_of_words_split)
