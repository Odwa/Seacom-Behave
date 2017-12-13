Feature: Employee Listing

	Background: User already has a Seacom User account
        Given a user logged in with valid Seacom credentials
        When the User is logged in to their account

	Scenario: Employee Listing
        Given the User is on the dashboard
        When a list of employees is shown
        Then a User should be able to download the list of employees
        Then a User should be able to search for an employee
        When a User should be able to filter the employee list
        Then a User should be able to move to the next employee listing page


