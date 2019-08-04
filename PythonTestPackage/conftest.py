import pytest

@pytest.yield_fixture()
def setUp(osType):
    print("Running method level setUp")
    if osType =='windows':
        print('running tests on windows')
    else:
        print('running test on Linux')
    yield
    print("Running method level tearDown")


@pytest.yield_fixture(scope="module")
def oneTimeSetUp(request,browser, osType):
    print("Running one time setUp")
    if browser == 'firefox':
        value = 10
        print("Running tests on FF")
    else:
        value = 20
        print("Running tests on chrome")

    # if request.cls is not None:
    #     request.cls.value = value

    yield

    # yield value
    # print("Running one time tearDown")
    # yield
    # print("Running one time tearDown")

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating system")
    # pytest_addoption("--browser")
    # pytest_addoption("--osType", help="Type of operating system")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")