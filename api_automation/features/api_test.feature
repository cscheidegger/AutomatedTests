Feature: API Automation Test
  As a QA engineer
  I want to test the API flow
  So that I can validate the functionality of user and book operations

  Scenario: Create a user and reserve books
    Given I have valid user credentials
    When I create the user
    And I generate a token
    And I list all available books
    And I reserve two books
    Then I should see the reserved books in the user details