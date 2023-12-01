Feature: API test for landing page of Lyft

    Scenario: validate the main page html
        Given call the main API
        Then verify the main api status code and schema

    Scenario: validate sending text to user 
        Given call the Post API with user number
        Then verify the post api status code and schema


    