# Авторизоваться на сайте https://fix-online.sbis.ru/
# Перейти в реестр Контакты
# Отправить сообщение самому себе
# Убедиться, что сообщение появилось в реестре
# Удалить это сообщение и убедиться, что удалили
# Для сдачи задания пришлите код и запись с экрана прохождения теста
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, Keys

driver = webdriver.Chrome()
url = "https://fix-online.sbis.ru/"
message_text = 'автотест сообщение'
try:
    driver.get(url)
    sleep(1)

    print('Авторизуемся')
    user_login, user_password = 'en.gladkov1', 'en.gladkov123!A'
    login = driver.find_element(By.CSS_SELECTOR, '[name="Login"]')
    login.send_keys(user_login, Keys.ENTER)
    assert login.get_attribute('value') == user_login
    sleep(1)
    password = driver.find_element(By.CSS_SELECTOR, '[name="Password"]')
    password.send_keys(user_password, Keys.ENTER)
    sleep(5)

    print('Переходим в реестр "Контакты"')
    contact = driver.find_element(By.XPATH, '//span[text()="Контакты"]/..')
    contact.click()
    sleep(3)
    contact_old = driver.find_element(By.CSS_SELECTOR, '.NavigationPanels-SubMenu__headTitle')
    contact_old.click()
    sleep(3)

    print('Отправляем сообщение самому себе')
    print('Открываем список сотрудников')
    message = driver.find_element(By.CSS_SELECTOR, '[data-qa="sabyPage-addButton"]')
    message.click()
    sleep(3)
    print('Выбираем адресата')
    contact = driver.find_element(By.CSS_SELECTOR, '[data-qa="controls-Render__field"] .controls-Field')
    contact.send_keys('Гладков Евгений', Keys.ENTER)
    sleep(3)
    print('Открываем диалог сообшения')
    contact_message = driver.find_element(By.CSS_SELECTOR, '[class="msg-addressee-selector__addressee"]')
    contact_message.click()
    sleep(3)

    print('Отправляем сообщение')
    test_message = driver.find_element(By.CSS_SELECTOR, '[data-qa="textEditor_slate_Field"]')
    test_message.send_keys(message_text, Keys.CONTROL + Keys.ENTER)
    sleep(3)
    print('Проверяем сообщение в списке')
    message_check = driver.find_element(By.CSS_SELECTOR, '.msg-entity-text')
    assert message_check.text == message_text

    print('Удаляем сообщение, проверяем что удалилось')
    message = driver.find_elements(By.CSS_SELECTOR, '.msg-dialogs-detail__layout-content .controls-ListView__item_default')
    action_chains = ActionChains(driver)
    action_chains.move_to_element(message[0])
    action_chains.perform()
    sleep(1)
    delete = driver.find_element(By.CSS_SELECTOR, '[data-qa="controls-itemActions__action deleteToArchive"]')
    delete.click()
    sleep(1)
    check_message = driver.find_elements(By.CSS_SELECTOR, '.msg-dialogs-detail__layout-content '
                                                          '.controls-ListView__item_default .msg-entity-text')
    assert check_message[0].text != message_text, 'Сообщение не удалено'
finally:
    driver.quit()