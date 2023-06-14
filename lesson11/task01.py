# Перейти на https://sbis.ru/
# Перейти в раздел "Контакты"
# Найти баннер Тензор, кликнуть по нему
# Перейти на https://tensor.ru/
# Проверить, что есть блок новости "Сила в людях"
# Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается https://tensor.ru/about
# Для сдачи задания пришлите код и запись с экрана прохождения теста
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
url = "https://sbis.ru/"
try:
    driver.get(url)
    assert driver.current_url

    print('Переходим в раздел "Контакты"')
    contacts_button = driver.find_element(By.CSS_SELECTOR, ".sbisru-Header__menu-item-1")
    contacts_button.click()

    print('Находим баннер Тензор и переходим на его сайт')
    tensor_banner = driver.find_element(By.CSS_SELECTOR, ".sbisru-Contacts__logo-tensor")
    sleep(3)
    tensor_banner.click()
    driver.switch_to.window(driver.window_handles[1])
    assert driver.current_url == "https://tensor.ru/"

    print('Проверяем наличие блока новостей "Сила в людях" и переходим в "Подробнее"')
    news_block = driver.find_element(By.CSS_SELECTOR, '.tensor_ru-Index__block4-content')
    title = news_block.get_attribute('')
    assert news_block.is_displayed()
    news_link = driver.find_element(By.XPATH, ".//a[@href='/about']")
    news_link.click()
    driver.switch_to.window(driver.window_handles[1])
    assert driver.current_url == "https://tensor.ru/about"
    sleep(3)
finally:
    driver.quit()
