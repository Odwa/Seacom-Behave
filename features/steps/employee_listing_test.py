from behave import *
import os
import sys
from step_impl_web_element_handling import *


@given(u'a user logged in with valid Seacom credentials')
def step_impl(context):
	check_user_for_existence()
	#print('User has an account')


@when(u'the User is logged in to their account')
def step_impl(context):
	user_logging_in()
	#context.browser.get('http://www.google.com')

@given(u'the User is on the dashboard')
def step_impl(context):
	user_on_the_dashboard()
	#print('The user is on the login page')

@when(u'a list of employees is shown')
def step_impl(context):
	list_of_employees()
	#print('Credentials Submitted')

@then(u'a User should be able to download the list of employees')
def step_impl(context):
	download_list_of_employees()

@then(u'a User should be able to search for an employee')
def step_impl(context):
	search_for_an_employee()

@when(u'a User should be able to filter the employee list')
def step_impl(context):
	using_listing_filters()

@then(u'a User should be able to move to the next employee listing page')
def step_impl(context):
	move_to_next_page()
