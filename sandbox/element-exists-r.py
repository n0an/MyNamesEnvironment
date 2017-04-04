
from selenium import webdriver


driver = webdriver.Chrome("C:/chromedriver.exe")

#save the url to navigate to in a variable
url = 'http://www.w3schools.com/'

#Navigate to the url
driver.get(url)


def element_exists(locator_attribute, locator_text):
    """
    Description: finds and element and returns true of false if element is found or not.
    """

    possible_locators = ["id", "xpath", "link text", "partial link text", "name", "tag name", "class name", "css selector"]

    if locator_attribute not in possible_locators:
        raise BaseException('The locator attribute provided is not in the approved attributes. Or the spelling and format does not match.\
                            The approved attributes are : %s ' % possible_locators)

    try:
        driver.find_element(locator_attribute, locator_text)
        return True
    except:
        return False

def assert_element_exists(locator_attribute, locator_text):
    """

    :param locator_attribute:
    :param locator_text:
    :return:
    """

    if not element_exists(locator_attribute, locator_text):
        raise AssertionError("The requested element with '%s' of '%s' does not exist" % (locator_attribute, locator_text))

    return

def element_visible(element):
    """

    :param element:
    :return:
    """

    if element.is_displayed():
        return True
    else:
        return False

def assert_element_visible(element):
    """

    :param element:
    :return:
    """

    if not element_visible(element):
        raise AssertionError('The element requested is not displayed')

def find_and_assert_element_visible(locator_type, search_term):
    """

    :param locator_type:
    :param search_term:
    :return:
    """

    element = driver.find_element(locator_type, search_term)

    if not element.is_displayed():
        raise AssertionError('The element with locator type "%s" and locator term "%s" and is not displayed' % (locator_type,search_term))
    else:
        print('The element is visible. :)')


assert_element_exists('id', 'menulinktutorials')

find_and_assert_element_visible('id', 'menulinktutorials')