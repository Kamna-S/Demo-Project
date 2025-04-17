import pytest
from selenium import webdriver
import os
import pytest
import os
from datetime import datetime

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        driver = item.funcargs['driver']
        screenshot_dir = "screenshots"
        if not os.path.exists(screenshot_dir):
            os.makedirs(screenshot_dir)
        time_stamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        file_name = os.path.join(screenshot_dir, f"{item.name}_{time_stamp}.png")
        driver.save_screenshot(file_name)

        if 'pytest_html' in item.config.pluginmanager.list_plugin_distinfo():
            extra = getattr(rep, 'extra', [])
            extra.append(pytest_html.extras.image(file_name))
            rep.extra = extra

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    # Executes all other hooks to obtain the report object
    outcome = yield
    report = outcome.get_result()

    # Only take screenshot if test failed at the test phase
    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver:
            screenshots_dir = "screenshots"
            if not os.path.exists(screenshots_dir):
                os.makedirs(screenshots_dir)
            file_name = f"{screenshots_dir}/{item.name}.png"
            driver.save_screenshot(file_name)