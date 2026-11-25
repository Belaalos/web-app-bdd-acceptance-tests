import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

BASE_URL = "https://the-internet.herokuapp.com"


def before_all(context):
    context.base_url = BASE_URL
    context.headed = os.getenv("HEADED") == "1"


def before_scenario(context, scenario):
    options = Options()
    if not context.headed:
        options.add_argument("--headless=new")
    options.add_argument("--window-size=1300,900")
    context.driver = webdriver.Chrome(options=options)


def after_step(context, step):
    if step.status == "failed":
        os.makedirs("screenshots", exist_ok=True)
        name = step.name.replace(" ", "_")[:40]
        context.driver.save_screenshot(f"screenshots/{name}.png")


def after_scenario(context, scenario):
    context.driver.quit()
