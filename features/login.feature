Feature: Seacom Login with valid credentials

    Scenario: Login to the Seacom website
        Given a User already has an account on "http://hr.seacom.io/api/admin/"
        When I launch browser on PC
        And the User is on the login page
        Then submit the credentials

       

        



