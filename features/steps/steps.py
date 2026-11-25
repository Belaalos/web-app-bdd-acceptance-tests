from behave import given, then, when
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select, WebDriverWait


def wait(context, seconds=10):
    return WebDriverWait(context.driver, seconds)


@given('I am on the login page')
def open_login(context):
    context.driver.get(context.base_url + "/login")


@given('I open "{path}"')
def open_path(context, path):
    context.driver.get(context.base_url + path)


@when('I log in with username "{user}" and password "{password}"')
def do_login(context, user, password):
    d = context.driver
    d.find_element(By.ID, "username").send_keys(user)
    d.find_element(By.ID, "password").send_keys(password)
    d.find_element(By.CSS_SELECTOR, "button[type=submit]").click()


@when('I click logout')
def logout(context):
    wait(context).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a.button.secondary"))).click()


@then('I should see the secure area')
def secure_area(context):
    wait(context).until(EC.url_contains("/secure"))
    assert "Secure Area" in context.driver.find_element(By.TAG_NAME, "h2").text


@then('the message should contain "{text}"')
def flash_message(context, text):
    flash = wait(context).until(EC.visibility_of_element_located((By.ID, "flash")))
    assert text in flash.text, f"flash was: {flash.text!r}"


@then('I should be back on the login page')
def back_on_login(context):
    wait(context).until(EC.url_contains("/login"))
    assert "You logged out" in context.driver.find_element(By.ID, "flash").text


@when('I add {count:d} elements')
def add_elements(context, count):
    button = context.driver.find_element(By.CSS_SELECTOR, "button[onclick='addElement()']")
    for _ in range(count):
        button.click()


@when('I delete {count:d} element')
def delete_elements(context, count):
    for _ in range(count):
        context.driver.find_element(By.CLASS_NAME, "added-manually").click()


@then('I should see {count:d} delete buttons')
def count_delete_buttons(context, count):
    assert len(context.driver.find_elements(By.CLASS_NAME, "added-manually")) == count


@when('I tick the first checkbox')
def tick_first(context):
    box = context.driver.find_elements(By.CSS_SELECTOR, "#checkboxes input")[0]
    if not box.is_selected():
        box.click()


@then('the first checkbox should be checked')
def first_checked(context):
    assert context.driver.find_elements(By.CSS_SELECTOR, "#checkboxes input")[0].is_selected()


@when('I choose "{option}" from the dropdown')
def choose_option(context, option):
    Select(context.driver.find_element(By.ID, "dropdown")).select_by_visible_text(option)


@then('the dropdown should show "{option}"')
def dropdown_shows(context, option):
    selected = Select(context.driver.find_element(By.ID, "dropdown")).first_selected_option
    assert selected.text == option


@when('I click start')
def click_start(context):
    context.driver.find_element(By.CSS_SELECTOR, "#start button").click()


@then('I should see the text "{text}"')
def see_text(context, text):
    wait(context).until(EC.text_to_be_present_in_element((By.ID, "finish"), text))


@when('I click the JS alert button and accept it')
def js_alert(context):
    context.driver.find_element(By.CSS_SELECTOR, "button[onclick='jsAlert()']").click()
    wait(context).until(EC.alert_is_present()).accept()


@then('the result should say "{text}"')
def alert_result(context, text):
    assert text in context.driver.find_element(By.ID, "result").text
