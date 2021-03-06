from time import sleep
import requests
import pytest
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# browser = webdriver.Chrome()
# browser.maximize_window()
# @pytest.fixture(scope="session")
# def browser():
#     browser = webdriver.Chrome()
#     browser.maximize_window()
#     yield browser
#     print("\nquit browser..")
#     browser.quit()

# def is_element_present(browser, how, what, timeout=4):
#     try:
#         WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((how, what)))
#     except TimeoutException:
#         return False
#     return True


# def test_display(browser):
# browser.get("http://pub.ast.safib.ru/")
# # browser.get("https://xn--80akicokc0aablc.xn--p1ai/")
# while True:
#     assert is_element_present(browser=browser, how=By.CSS_SELECTOR, what=".introduction"), "Не найден заголовок на " \
#                                                                                             "странице "
#     title_main_page = browser.find_element(By.CSS_SELECTOR, ".introduction").text
#     expected_title_text = "УДОБНЫЙ И БЕЗОПАСНЫЙ ИНСТРУМЕНТ\nдля решения задач удаленного доступа, управления и " \
#                           "администрирования"
#
#     assert title_main_page == expected_title_text, "Полученный текст из заголовка:\n" \
#                                                    f"{title_main_page}\n" \
#                                                    f"Отличается от ожидаемого:\n" \
#                                                    f"{expected_title_text}\n"
#     sleep(2)
#
link_my_ass = "https://xn--80akicokc0aablc.xn--p1ai/"


def check_open(link=link_my_ass):
    try:
        response = requests.get(link)
    except requests.exceptions.ConnectionError:
        return False
    return True


def test_display(link=link_my_ass):
    # while True:
    assert check_open(), f"\nСайт: '{link}' не открывается"
    response = requests.get(link).text
    text_tuple = ("О продукте", "Сертификаты", "Купить", "Акции", "Скачать",
                  "Партнеры и совместимость", "Совместимость", "О нас", "Личный кабинет")
    for i in text_tuple:
        assert i in response, f'\nTeкст "{i}" не найден в коде страницы'

