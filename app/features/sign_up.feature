Feature: Sign Up
      As a potential user of the system
      In order to save my progress and personalise my experience
      I want to be able to create an account

  Scenario: Redirect logged in users (1)
    Given the user is logged in
    When the user visits the sign up page
    Then the user is taken to the gym list page

  Scenario: Creates account for new user
    Given the user doesn't have an account in the system
    When the user visits the sign up page
    And the user enters a username not currently in the system
    And the user enters the password for the username
    And the user presses the submit button
    Then an account is created in the system for the user
