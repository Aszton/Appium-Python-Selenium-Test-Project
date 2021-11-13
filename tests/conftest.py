import pytest
import time
from base.driverClass import startApp


@pytest.yield_fixture(scope='class')
def beforeClass(request):
    print('Before Class')
    driver1 = startApp()
    driver = driver1.openApp()
    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    time.sleep(5)
    driver.quit()
    print('After Class')

@pytest.yield_fixture()
def beforeMethod():
    print('Before Method')
    yield
    print('After Method')