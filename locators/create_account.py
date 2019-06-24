from selenium.webdriver.common.by import By

RADIO_GENDER_MR = (By.XPATH, '//input[@name="id_gender" and @value="1"]')
RADIO_GENDER_MRS = (By.XPATH, '//input[@name="id_gender" and @value="2"]')
INPUT_FIRST_NAME = (By.XPATH, '//input[@name="firstname"]')
INPUT_LAST_NAME = (By.XPATH, '//input[@name="lastname"]')
INPUT_EMAIL = (By.XPATH, '//input[@name="email"]')
INPUT_PASSWORD = (By.XPATH, '//input[@name="password"]')
INPUT_BIRTHDATE = (By.XPATH, '//input[@name="birthday"]')
BTN_SAVE = (By.XPATH, '//button[@data-link-action="save-customer"]')
