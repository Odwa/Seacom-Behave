from behave import *
import os
import sys
from step_impl_web_element_handling import *


@given(u'a User already has an account on "{admin}"')
def step_impl(context,admin):
	check_user_under_admin(admin)
	#print('User has an account')

@when(u'I launch browser on PC')
def step_impl(context):
	launch_browser()
	#context.browser.get('http://www.google.com')

@when(u'the User is on the login page')
def step_impl(context):
	user_on_login_page()
	#print('The user is on the login page')

@then(u'submit the credentials')
def step_impl(context):
	user_submits_credentials()
	#print('Credentials Submitted')


