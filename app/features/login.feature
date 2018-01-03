Feature: Login
      As a user of the system
      In order to access the app
      I want to be able to login

  Scenario: Redirect logged in users
    Given the user is logged in
    When the user visits the login page
    Then the user is taken to the gym list page

  Scenario: Redirect logged in users from homepage
    Given the user is logged in
    When the user visits the landing page
    Then the user is taken to the gym list page

  Scenario: Logs user in
    # As a user
    # In order to access my data in the app
    # I want to log in
    Given the user visits the login page
    And the user enters a username currently in the system
    And the user enters the password for the username
    When the user presses the submit button
    Then a user session is created
