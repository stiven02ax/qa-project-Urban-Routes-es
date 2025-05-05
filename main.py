import data
import phone_code
from selenium.webdriver import Keys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    button_taxi = (By.XPATH,'//button[contains(text(), "Pedir un taxi")]')
    comfort_tariff = (By.XPATH, '//div[@class="tcard"]//div[contains(@class, "tcard-title") and text()="Comfort"]')
    blanket_label = (By.CSS_SELECTOR,'#root > div > div.workflow > div.workflow-subcontainer > div.tariff-picker.shown > div.form > ''div.reqs.open > div.reqs-body > div:nth-child(1) > div')
    button_phone = (By.CLASS_NAME, 'np-text')
    phone_num = (By.ID, 'phone')
    button_pop_up_window = (By.CSS_SELECTOR,'#root > div > div.number-picker.open > div.modal > div.section.active > form > ''div.buttons > button')
    field_code = (By.CSS_SELECTOR, "input#code")
    confirm_code_number = (By.CSS_SELECTOR,'#root > div > div.number-picker.open > div.modal > div.section.active > form > ''div.buttons > button:nth-child(1)')
    method_payment = (By.CLASS_NAME, "pp-text")
    button_card = (By.CSS_SELECTOR,'#root > div > div.payment-picker.open > div.modal > div.section.active > div.pp-selector > ''div.pp-row.disabled')
    field_card = (By.CLASS_NAME, 'card-input')
    field_code_card = (By.CSS_SELECTOR, "input.card-input[placeholder='12'][name='code']")
    button_agg_card = (By.CSS_SELECTOR,'#root > div > div.payment-picker.open > div.modal.unusual > div.section.active.unusual > ''form > div.pp-buttons > button:nth-child(1)')
    close_popup_window = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[1]/button')
    button_field_message = (By.ID, 'comment')
    selector_blanket = (By.CSS_SELECTOR,'#root > div > div.workflow > div.workflow-subcontainer > div.tariff-picker.shown > div.form ''> div.reqs.open > div.reqs-body > div:nth-child(1) > div > div.r-sw > div > span')
    blanket_value = (By.CSS_SELECTOR,'#root > div > div.workflow > div.workflow-subcontainer > div.tariff-picker.shown > div.form > ''div.reqs.open > div.reqs-body > div:nth-child(1) > div > div.r-sw > div > input')
    ice_cream = (By.CSS_SELECTOR,'#root > div > div.workflow > div.workflow-subcontainer > div.tariff-picker.shown > div.form > ''div.reqs.open > div.reqs-body > div.r.r-type-group > div > div.r-group-items > div:nth-child(''1) > div > div.r-counter > div > div.counter-plus')
    ice2_cream = (By.CSS_SELECTOR,'#root > div > div.workflow > div.workflow-subcontainer > div.tariff-picker.shown > div.form > ''div.reqs.open > div.reqs-body > div.r.r-type-group > div > div.r-group-items > div:nth-child(''1) > div > div.r-counter > div > div.counter-value')
    button_find_taxi = (By.CSS_SELECTOR, '#root > div > div.workflow > div.smart-button-wrapper > button')
    popup_window_for_taxi = (By.XPATH, "//div[contains(@class, 'order-header-title') and text()='Buscar automóvil']")

    def __init__(self, driver):
        self.driver = driver

    def set_from(self, from_address):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.from_field))
        self.driver.find_element(*self.from_field).send_keys(from_address)
    def set_to(self, to_address):
        self.driver.find_element(*self.to_field).send_keys(to_address)
    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')
    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def click_button_taxi(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.button_taxi))
        self.driver.find_element(*self.button_taxi).click()

    def select_comfort(self):
        self.driver.find_element(*self.comfort_tariff).click()

    def click_check_confort_select(self):
        element = self.driver.find_element(*self.blanket_label)
        comfort_is_check = element.is_displayed()
        return comfort_is_check

    def click_phone_number(self):
        self.driver.find_element(*self.button_phone).click()

    def set_phone_number(self, number_phone):
        self.driver.find_element(*self.phone_num).send_keys(number_phone)
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.phone_num))

    def get_phone_number(self):
        return self.driver.find_element(*self.button_phone).get_property('outerText')

    def click_phone_pop_up_window(self):
        self.driver.find_element(*self.button_pop_up_window).click()

    def set_code(self, code):
        self.driver.find_element(*self.field_code).send_keys(code)

    def confirm_code(self):
        self.driver.find_element(*self.confirm_code_number).click()

    def select_method_payment(self):
        self.driver.find_element(*self.method_payment).click()

    def add_card(self):
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located(self.button_card))
        self.driver.find_element(*self.button_card).click()

    def set_card_number(self, number_card):
        self.driver.find_element(*self.field_card).send_keys(number_card)

    def set_code_number(self, code_card):
        self.driver.find_element(*self.field_code_card).send_keys(code_card)
        self.driver.find_element(*self.field_code_card).send_keys(Keys.TAB)

    def get_card_number(self):
        return self.driver.find_element(*self.field_card).get_property('value')

    def get_code_number(self):
        return self.driver.find_element(*self.field_code_card).get_property('value')

    def click_agg_card_and_close(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.button_agg_card))
        self.driver.find_element(*self.button_agg_card).click()
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.close_popup_window))
        self.driver.find_element(*self.close_popup_window).click()

    def set_message_driver(self, message):
        self.driver.find_element(*self.button_field_message).send_keys(message)

    def get_message_for_driver(self):
        return self.driver.find_element(*self.button_field_message).get_property('value')

    def click_selector_blanket(self):
        self.driver.find_element(*self.selector_blanket).click()

    def get_blanket_value(self):
        return self.driver.find_element(*self.blanket_value).get_property('value')

    def click_ice_cream(self):
        self.driver.find_element(*self.ice_cream).click()

    def get_ice_cream_value(self):
        return self.driver.find_element(*self.ice2_cream).get_property('outerText')

    def find_taxi(self):
        self.driver.find_element(*self.button_find_taxi).click()
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(self.popup_window_for_taxi))

    def check_order_taxi (self):
        try:
            element = self.driver.find_element(*self.popup_window_for_taxi)
            return element.is_displayed()
        except:
            return False


class TestUrbanRoutes:
    driver = None

    @classmethod
    def setup_class(cls):

        options = Options()
        options.set_capability("goog:loggingPrefs", {"performance": "ALL"})
        cls.driver = webdriver.Chrome(options=options)

    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_from(address_from)
        routes_page.set_to(address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

    def test_select_confort(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_button_taxi()
        routes_page.select_comfort()
        assert routes_page.click_check_confort_select()

    def test_set_phone(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_phone_number()
        routes_page.set_phone_number(data.phone_number)
        routes_page.click_phone_pop_up_window()
        routes_page.set_code(str(phone_code.retrieve_phone_code(self.driver)))
        routes_page.confirm_code()
        assert routes_page.get_phone_number() == data.phone_number

    def test_add_card(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.select_method_payment()
        routes_page.add_card()
        routes_page.set_card_number(data.card_number)
        routes_page.set_code_number(data.card_code)
        assert routes_page.get_card_number() == data.card_number
        assert routes_page.get_code_number() == data.card_code
        routes_page.click_agg_card_and_close()

    def test_message_for_driver(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_message_driver(data.message_for_driver)
        assert routes_page.get_message_for_driver() == data.message_for_driver

    def test_active_blanket(self):
        routes_page = UrbanRoutesPage(self.driver)
        # Seleccionar la manta y pañuelo
        routes_page.click_selector_blanket()
        assert routes_page.get_blanket_value() == 'on'

    def test_2_ice_creams(self):
        routes_page = UrbanRoutesPage(self.driver)
        for _ in range(2):
            routes_page.click_ice_cream()
        assert routes_page.get_ice_cream_value() == '2'

    def test_taxi_request_modal_display(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.find_taxi()
        assert routes_page.check_order_taxi(), "El modal 'Buscar automóvil' no se mostró correctamente"

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
