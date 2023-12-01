Feature: Landing page functionality

    Scenario: To validate whether the landing page is loading fine
        Given Browser for the testing
        When open the lyft URL
        Then Verify the landing page is working fine

    Scenario: Check whether all modes of transportations are availale for booking
        Given Browser for the testing
        When open the lyft URL
        Then Verify all the modes of transportations are availale for the riders

    Scenario: Validate the Redirection of Renting a cab  
        Given Browser for the testing
        When open the lyft URL
        When Click on the 'wait & save' cabs check the mobile number page
        Then validate the redirected page