#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
import os
from selenium import webdriver  # pip install selenium==3.5.0
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

#chromeDriverExe = 'features/utilities/chromedriver.exe'
delay_quick = 3  # sec
delay_medium = 5  # sec
delay_large = 9  # sec
driver = webdriver.Firefox()

def wait_for_following_page_title(driver, expected_title):
    try:
        WebDriverWait(driver, delay_quick).until(expected_conditions.title_contains(expected_title))
        return True
    except TimeoutException:
        raise Exception('************* Page with required title not found : ' + expected_title + ' actual title is: ' + driver.title)


def intiate_browser_items():
    driver.maximize_window()
    driver.delete_all_cookies()


def get_driver_and_navigate_to_url_with_title(url,expected_title):
    #driver_temp = webdriver.Chrome(executable_path=chromeDriverExe)
    #driver = webdriver.Firefox()
    intiate_browser_items()
    driver.get(url)
    wait_for_following_page_title(driver,expected_title)
    return driver


def webdriver_shutdown(driver):
    driver.close()
    driver.quit()


def launch_browser():
    driver.get('http://hr.seacom.io/')
    print('Launched Browser')


def check_user_for_existence():
    print('Checking user existence...')


def user_logging_in():
    launch_browser()
    intiate_browser_items()
    driver.find_element_by_xpath("//input[@type='text']").send_keys('testuser')
    driver.find_element_by_xpath("//input[@type='password']").send_keys('testpassword')
    driver.find_element_by_xpath("//button[@type='submit']").click()


def search_for_user_on_employee_list():
    print('Searching for user...')


def click_on_new_employee_button():
    intiate_browser_items()
    driver.get('http://hr.seacom.io/login/')
    driver.find_element_by_xpath("//input[@type='text']").send_keys('testuser')
    driver.find_element_by_xpath("//input[@type='password']").send_keys('testpassword')
    driver.find_element_by_xpath("//button[@type='submit']").click()

    #driver.find_element_by_link_text("Dashboard").click()
    driver.find_element_by_link_text("+ New Employee").click()

def landed_on_new_employee_form():
    print('User is on the new employee form')

def download_list_of_employees():
    print('Downloading employees...')


def user_lands_on_the_basic_information_form():
    print('Landed on Basic information form...')


def clicks_on_next_submits_basic_info_form():
    print('Basic info next button clicked')  


def fill_in_the_basic_information_form():
    intiate_browser_items()
    driver.get('http://hr.seacom.io/login/')
    driver.find_element_by_xpath("//input[@type='text']").send_keys('testuser')
    driver.find_element_by_xpath("//input[@type='password']").send_keys('testpassword')
    driver.find_element_by_xpath("//button[@type='submit']").click()

    #driver.find_element_by_link_text("Dashboard").click()
    driver.find_element_by_link_text("+ New Employee").click()

    driver.find_element_by_xpath("//input[@type='text']").clear()
    driver.find_element_by_xpath("//input[@type='text']").send_keys("Test")
    driver.find_element_by_xpath("(//input[@type='text'])[2]").clear()
    driver.find_element_by_xpath("(//input[@type='text'])[2]").send_keys("User")
    driver.find_element_by_xpath("(//input[@type='text'])[3]").clear()
    driver.find_element_by_xpath("(//input[@type='text'])[3]").send_keys("Unomena")
    driver.find_element_by_xpath("(//input[@type='text'])[4]").clear()
    driver.find_element_by_xpath("(//input[@type='text'])[4]").send_keys("983798475936")
    driver.find_element_by_xpath("(//input[@type='text'])[5]").clear()
    driver.find_element_by_xpath("(//input[@type='text'])[5]").send_keys("308459348")
    driver.find_element_by_xpath("(//input[@type='text'])[6]").click()
    driver.find_element_by_xpath("//bs-datepicker-navigation-view/button[3]").click()
    driver.find_element_by_xpath("//td[3]/span").click()
    driver.find_element_by_xpath("//tr[2]/td[2]/span").click()
    driver.find_element_by_xpath("//td[3]/span").click()
    driver.find_element_by_xpath("//div[@id='newEmployeeModal']/div/div/div/form/tabset/div/tab/div/div[2]/div/div/select").click()
    Select(driver.find_element_by_xpath("//div[@id='newEmployeeModal']/div/div/div/form/tabset/div/tab/div/div[2]/div/div/select")).select_by_visible_text("Male")
    driver.find_element_by_xpath("//option[@value='M']").click()
    driver.find_element_by_xpath("//div[@id='newEmployeeModal']/div/div/div/form/tabset/div/tab/div/div[2]/div[2]/div/select").click()
    Select(driver.find_element_by_xpath("//div[@id='newEmployeeModal']/div/div/div/form/tabset/div/tab/div/div[2]/div[2]/div/select")).select_by_visible_text("African")
    driver.find_element_by_xpath("//div[@id='newEmployeeModal']/div/div/div/form/tabset/div/tab/div/div[2]/div[2]/div/select/option[2]").click()
    driver.find_element_by_xpath("//div[@id='newEmployeeModal']/div/div/div/form/tabset/div/tab/div/div[2]/div[3]/div/select").click()
    Select(driver.find_element_by_xpath("//div[@id='newEmployeeModal']/div/div/div/form/tabset/div/tab/div/div[2]/div[3]/div/select")).select_by_visible_text("South African")
    driver.find_element_by_xpath("//div[@id='newEmployeeModal']/div/div/div/form/tabset/div/tab/div/div[2]/div[3]/div/select/option[8]").click()
    driver.find_element_by_xpath("(//input[@type='text'])[7]").click()
    driver.find_element_by_xpath("//bs-datepicker-navigation-view/button[3]").click()
    driver.find_element_by_xpath("//bs-datepicker-navigation-view/button").click()
    driver.find_element_by_xpath("//bs-datepicker-navigation-view/button").click()
    driver.find_element_by_xpath("//td[3]/span").click()
    driver.find_element_by_xpath("//tr[2]/td[2]/span").click()
    driver.find_element_by_xpath("//td[5]/span").click()
    driver.find_element_by_xpath("//div[@id='newEmployeeModal']/div/div/div/form/tabset/div/tab/div/div[2]/div[5]/div/select").click()
    Select(driver.find_element_by_xpath("//div[@id='newEmployeeModal']/div/div/div/form/tabset/div/tab/div/div[2]/div[5]/div/select")).select_by_visible_text("Widowed")
    driver.find_element_by_xpath("//div[@id='newEmployeeModal']/div/div/div/form/tabset/div/tab/div/div[2]/div[5]/div/select/option[3]").click()
    driver.find_element_by_xpath("(//button[@name='button'])[2]").click()


def take_user_to_contactc_info_form():
    fill_in_the_basic_information_form()
    #print('User is taken to the profile info form')
    

def user_lands_on_the_contact_info_form():
    print('User is taken to the Contact form')

def fill_in_the_contact_details_form():
    print('Contact form filled')
    pass

def clicks_on_next_submits_contact_info_form():
    print('Basic info next button clicked')


def take_user_to_profile_info():
    print('User is taken to the profile info form')


    

'''    

def check_user_under_admin(url):
    intiate_browser_items()
    driver = get_driver_and_navigate_to_url_with_title(url,'Log in | Django site admin')
    print ('Landed on the admin site')
    driver.find_element_by_id('id_username').send_keys('testuser')
    driver.find_element_by_id('id_password').send_keys('testpassword')
    driver.find_element_by_xpath("//form[@id='login-form']/div[3]/input").click()
    print ('Admin form submitted')

def launch_browser():
    driver.get('http://hr.seacom.io/')
    print('Launched Browser')


def user_on_login_page():
    intiate_browser_items()
    #driver.get('http://hr.seacom.io/login')
    if driver.title == "HR Portal":
        print ('Landed on the login page')
    else:
        print('User is not on the Login Page')

def user_submits_credentials():
    intiate_browser_items()
    driver.get('http://hr.seacom.io/')
    print('User is about to submit the login details')
    driver.find_element_by_xpath("//input[@type='text']").send_keys('testuser')
    driver.find_element_by_xpath("//input[@type='password']").send_keys('testpassword')
    driver.find_element_by_xpath("//button[@type='submit']").click()
    print ('login form submitted')



def check_user_for_existence():
    intiate_browser_items()
    driver.get('http://hr.seacom.io/api/admin/')
    driver.find_element_by_id('id_username').send_keys('testuser')
    driver.find_element_by_id('id_password').send_keys('testpassword')
    driver.find_element_by_xpath("//form[@id='login-form']/div[3]/input").click()
    driver.find_element_by_xpath("//div[@id='content-main']/div[2]/table/tbody/tr[2]/th/a").click()
    driver.find_element_by_id('searchbar').click()
    driver.find_element_by_id('searchbar').send_keys("testuser")
    driver.find_element_by_xpath("//input[@value='Search']").click()
    driver.find_element_by_xpath("//table[@id='result_list']/tbody/tr/th/a").click()


def user_logging_in():
    intiate_browser_items()
    driver.get('http://hr.seacom.io/login/')
    driver.find_element_by_xpath("//input[@type='text']").send_keys('testuser')
    driver.find_element_by_xpath("//input[@type='password']").send_keys('testpassword')
    driver.find_element_by_xpath("//button[@type='submit']").click()

def user_on_the_dashboard():
    if driver.title == "HR Portal":
        print ('Landed on the Dashboard')
    else:
        print('User is not on the Employee Listing page')


def list_of_employees():
    print('Employee Listing is showing')

def download_list_of_employees():
    print('Downloaded the Employee List')


def search_for_an_employee():
    print('Searched for an Employee')


def using_listing_filters():
    print('Filters are working')


def move_to_next_page():
    print('On to the next page')


    


def web_element_pop_up_example1(url):
    driver1 = get_chrome_driver_and_navigate_to_url_with_title(url,'Bootstrap Alerts')
    print ('  Clicking to invoke auto vanishing pop up')
    driver1.find_element_by_id("autoclosable-btn-success").click()
    time.sleep(6)
    print ('  Clicking to invoke sticky pop up')
    driver1.find_element_by_id("normal-btn-success").click()
    time.sleep(2)
    print ('  Click to close sticky pop up')
    driver1.find_element_by_class_name("close").click()
    time.sleep(2)
    webdriver_shutdown(driver1)


def web_element_pop_up_example2_javascript(url):
    driver2 = get_chrome_driver_and_navigate_to_url_with_title(url,'Bootstrap Modal Demo')
    print ('  Clicking to invoke javascript pop up type 1')
    driver2.find_element_by_css_selector("a[href='#myModal0']").click()
    time.sleep(6)
    print ('  Clicking to close java script pop up type 1')
    driver2.find_element_by_css_selector("a[data-dismiss='modal']").click()
    time.sleep(5)
    print ('  Clicking to invoke javascript pop up type 2')
    driver2.find_element_by_css_selector("a[href='#myModal']").click()
    time.sleep(3)
    print ('  Clicking to invoke additional on top of existing java script pop up type 2')
    driver2.find_element_by_css_selector("a[href='#myModal2']").click()
    time.sleep(5)
    print ('  Clicking to close additional java script on top of existing java script pop up type 2')
    driver2.find_elements_by_css_selector("a[data-dismiss='modal']")[2].click()
    time.sleep(3)
    print ('  Clicking to close java script pop up type 2')
    driver2.find_elements_by_css_selector("a[data-dismiss='modal']")[1].click()
    time.sleep(3)
    webdriver_shutdown(driver2)


def web_element_tabular_elements(url):
    driver3 = get_chrome_driver_and_navigate_to_url_with_title(url,'Just another WordPress site')
    driver3.find_element_by_css_selector("div[role='tabpanel']").location_once_scrolled_into_view
    print ('  Clicking to tab 1')
    driver3.find_element_by_id("ui-id-1").click()
    time.sleep(1)
    print ('  Clicking to tab 1')
    driver3.find_element_by_id("ui-id-2").click()
    time.sleep(1)
    print ('  Clicking to tab 3')
    driver3.find_element_by_id("ui-id-3").click()
    time.sleep(1)
    webdriver_shutdown(driver3)


def web_element_form_elements_part1(url):
    driver4 = get_chrome_driver_and_navigate_to_url_with_title(url,'Registration')
    print ('  Sending text to text box')
    driver4.find_element_by_id("name_3_firstname").send_keys("this is text box")
    print ('  Clicking on radio button')
    driver4.find_element_by_css_selector("input[value='single']").click()
    print ('  Clicking to tick box')
    driver4.find_element_by_css_selector("input[value='dance']").click()
    driver4.find_element_by_css_selector("input[value='reading']").click()
    time.sleep(1)
    print ('  Selecting from drop box')
    country_select = Select(driver4.find_element_by_id("dropdown_7"))
    # for single_option in country_select.options :
    #     print (single_option.text)
    country_select.select_by_visible_text('Luxembourg')
    time.sleep(3)
    webdriver_shutdown(driver4)


def web_element_form_elements_part2(url):
    driver5 = get_chrome_driver_and_navigate_to_url_with_title(url,'Registration')
    driver5.find_element_by_name("pie_submit").location_once_scrolled_into_view
    print ('  Selecting from drop box')
    driver5.find_element_by_id("profile_pic_10").send_keys(str(os.getcwd()) + "\utilities\image_to_upload.png")
    time.sleep(2)
    print ('  Verification of element color or css value')
    driver5.find_element_by_id("password_2").send_keys("1g1EF6;~?7F5p")
    time.sleep(2)
    driver5.find_element_by_id("confirm_password_password_2").send_keys("1g1EF6;~?7F5p")
    time.sleep(2)
    colour_letter_array = str(driver5.find_element_by_id("piereg_passwordStrength").value_of_css_property('background-color'))
    actual_color = ''
    for colour_letter in colour_letter_array:
        actual_color+= colour_letter_array
    if 'rgba(195, 255, 136, 1)' in actual_color :
        print ('  This is a strong password')
    print ('  Clicking on a button')
    driver5.find_element_by_name("pie_submit").click()
    time.sleep(2)
    webdriver_shutdown(driver5)


def web_element_drag_and_drop(url):
    driver6 = get_chrome_driver_and_navigate_to_url_with_title(url,'Droppable')
    print ('  Performing drag and drop')
    time.sleep(2)
    source_element = driver6.find_element_by_id("draggableview");
    dest_element = driver6.find_element_by_id("droppableview");
    ActionChains(driver6).drag_and_drop(source_element, dest_element).perform()
    time.sleep(2)
    webdriver_shutdown(driver6)


def web_element_resize(url):
    driver7 = get_chrome_driver_and_navigate_to_url_with_title(url,'Resizable')
    print ('  Performing resize')
    horizontal_border = driver7.find_element_by_class_name("ui-resizable-e")
    ActionChains(driver7).click_and_hold(horizontal_border).move_by_offset(90,0).perform()
    time.sleep(5)
    vertical_border = driver7.find_element_by_class_name("ui-resizable-s")
    ActionChains(driver7).click_and_hold(vertical_border).move_by_offset(0,90).perform()
    time.sleep(5)
    webdriver_shutdown(driver7)


def web_element_date_pick(url):
    driver8 = get_chrome_driver_and_navigate_to_url_with_title(url,'Datepicker')
    print ('  Performing date pick')
    driver8.find_element_by_id("datepicker1").click()
    time.sleep(1)
    driver8.find_element_by_xpath("// *[ @ id = \"ui-datepicker-div\"] / table / tbody / tr[3] / td[4] / a").click()
    time.sleep(2)
    webdriver_shutdown(driver8)


def web_element_slider(url):
    driver9 = get_chrome_driver_and_navigate_to_url_with_title(url,'Slider')
    print ('  Performing slider')
    slider_element = driver9.find_element_by_class_name("ui-slider-handle").click()
    ActionChains(driver9).click_and_hold(slider_element).move_by_offset(80, 0).perform()
    time.sleep(3)
    webdriver_shutdown(driver9)


def web_element_frame_handling(url):
    driver10 = get_chrome_driver_and_navigate_to_url_with_title(url,'HTML Frames')
    print ('  Performing frame handling')
    top_frame = driver10.find_element_by_name("topFrame").click()
    print ('  Switching to iframe')
    driver10.switch_to_frame(top_frame)
    print ('  Switching to default content')
    driver10.switch_to_default_content()
    time.sleep(1)
    webdriver_shutdown(driver10)


def web_element_window_handling(url):
    driver11 = get_chrome_driver_and_navigate_to_url_with_title(url,'Frames and windows')
    print ('  Performing window handling')
    current_w_handle = driver11.current_window_handle
    driver11.find_element_by_css_selector("a[target='_blank']").click()
    time.sleep(2)
    if 0 is not len(driver11.window_handles):
        # print (' Multiple windows found ' + len(driver11.window_handles))
        driver11.switch_to.window(driver11.window_handles[1])
        print ( ' New windows title is  ' + driver11.title)
        driver11.switch_to.window(current_w_handle)
    else:
        raise Exception('************* Multiple windows are not found ')
    time.sleep(2)
    webdriver_shutdown(driver11)
'''