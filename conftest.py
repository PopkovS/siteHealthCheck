# import pytest
# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
#
#
# @pytest.fixture(scope="session")
# def browser():
#     # browser = webdriver.Chrome(ChromeDriverManager().install())
#     browser = webdriver.Chrome("./chromedriver.exe")
#     browser.maximize_window()
#     yield browser
#     print("\nquit browser..")
#     browser.quit()
