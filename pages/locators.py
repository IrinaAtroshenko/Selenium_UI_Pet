from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#app > header > div > ul > li:nth-child(1) > a > span')
    DDL = (By.ID, 'pv_id_2')
    DDL_SELECT = (By.ID, "pv_id_2_3")
    PET_FILTER_BY_NAME = (By.XPATH, '//*[@id="petName"]')


class DetailsPageLocators:
    PET_DETAILS = (By.CSS_SELECTOR, '.p-button-label')
    PET_OPEN_PICTURE = (By.CLASS_NAME, 'p-image-preview-indicator')
    PET_PICTURE_ACTION_LEFT = (By.XPATH, '/html/body/div[3]/div[1]/button[2]')
    PET_PICTURE_ACTION_RIGHT = (By.XPATH, '/html/body/div[3]/div[1]/button[1]')
    PET_PICTURE_ZOOM_IN = (By.XPATH, '/html/body/div[3]/div[1]/button[4]')
    PET_PICTURE_ZOOM_OUT = (By.XPATH, '/html/body/div[3]/div[1]/button[3]')
    PET_PICTURE_CLOSE = (By.XPATH, '/html/body/div[3]/div[1]/button[5]')


class LoginPageLocators:
    LOGIN_EMAIL = (By.ID, "login")
    LOGIN_PASS = (By.CSS_SELECTOR, "#password > input")
    LOGIN_BTN = (By.CLASS_NAME, "p-button-label")


class ProfilePageLocators:
    PLUS_BTN = (By.CSS_SELECTOR, '#app > main > div > div > div.p-dataview-header > div > div:nth-child(1) > button')
    NAME_FIELD = (By.XPATH, '//*[@id="name"]')
    AGE_FIELD = (By.XPATH, '//*[@id="age"]/input')
    TYPE_DDL = (By.ID, 'pv_id_2')
    TYPE_DDL_SELECT = (By.ID, "pv_id_2_2")
    GENDER_DDL = (By.ID, 'pv_id_3')
    GENDER_DDL_SELECT = (By.ID, "pv_id_3_0")
    CREATE_PET_BTN = (By.XPATH, '//*[@id="app"]/main/div/div/form/div/div[2]/div[3]/button[1]/span[2]')
    EDIT_PET_BTN = (By.CSS_SELECTOR, '#app > main > div > div > div.p-dataview-content > div > div:nth-child(4) > div > div.product-list-action > button:nth-child(1) > span.p-button-label')
    EDIT_NAME_FIELD = (By.XPATH, '//*[@id="name"]')
    EDIT_AGE_FIELD = (By.XPATH, '//*[@id="age"]/input')
    EDIT_TYPE_DDL = (By.XPATH, '//*[@id="typeSelector"]')
    EDIT_TYPE_DDL_SELECT = (By.ID, "pv_id_2_0")
    SAVE_PET_BTN = (By.XPATH, '//*[@id="app"]/main/div/form/div/div[2]/div[3]/button/span[2]')
    PET_DELETE = (By.XPATH, '//*[@id="app"]/main/div/div/div[2]/div/div[4]/div/div[2]/button[2]/span[2]')
    DELETE_POP_UP = (By.XPATH, '/html/body/div[3]/div[2]/button[2]/span')








