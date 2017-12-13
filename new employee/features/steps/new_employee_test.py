from behave import *
import os
import sys
from step_impl_web_element_handling import *

'''
@given(u'the admin User already has a Seacom User account')
def step_impl(context):
	check_user_for_existence()
	#print('User has an account')


@given(u'the User is logged in to their account')
def step_impl(context):
	user_logging_in()
	#context.browser.get('http://www.google.com')
'''

@given(u'an employee has not been created yet')
def step_impl(context):
	search_for_user_on_employee_list()
	#print('The user is on the login page')

@given(u'the admin user is logged in')
def step_impl(context):
	user_logging_in()
	

@when(u'the User clicks on the New Employee button')
def step_impl(context):
	click_on_new_employee_button()
	#print('Credentials Submitted')

@then(u'the New Employee form should pop up')
def step_impl(context):
	landed_on_new_employee_form()

@given(u'the User is on the Basic Information forms')
def step_impl(context):
	user_lands_on_the_basic_information_form()

@when(u'the user fills in all the basic information required fields on the form')
def step_impl(context):
	fill_in_the_basic_information_form()

@when(u'user clicks on Next to submit basic information form')
def step_impl(context):
	clicks_on_next_submits_basic_info_form()


@then(u'the user should be taken to see the Contact form')
def step_impl(context):
	take_user_to_contactc_info_form()


@given(u'the User is on the Contact Details form')
def step_impl(context):
	user_lands_on_the_contact_info_form()


@when(u'the user fills in all the contact details required fields on the form')
def step_impl(context):
	fill_in_the_contact_details_form()


@when(u'user clicks on Next to submit contact details form')
def step_impl(context):
	clicks_on_next_submits_contact_info_form()


@then(u'the user should be taken to the Profile Information form')
def step_impl(context):
	take_user_to_profile_info()


'''
Path: C:\Users\osola\Downloads\Seacom\Seacom Cucumber\tests\new employee

Run: behave --no-capture --no-capture-stderr

'''