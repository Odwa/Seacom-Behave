Feature: New Employee
    
   
    Scenario: Create a new Employee
        Given an employee has not been created yet
        And the admin user is logged in
        When the User clicks on the New Employee button
        Then the New Employee form should pop up
        
    Scenario: Fill in Basic Information
        Given the User is on the Basic Information forms
        When the user fills in all the basic information required fields on the form
        And user clicks on Next to submit basic information form
        Then the user should be taken to see the Contact form


    Scenario: Fill in Contact Details form
        Given the User is on the Contact Details form
        When the user fills in all the contact details required fields on the form
        And user clicks on Next to submit contact details form
        Then the user should be taken to the Profile Information form