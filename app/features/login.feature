# Created by colinwren at 28/08/2017
Feature: Login
  As a user of the system
  In order to access the app
  I want to be able to login

  @form-errors
  Scenario: Login with non-existent account
    Given the user doesn't have an account in the system
    And the user visits the login page
    When the user enters a username not currently in the system
    And the user enters a password
    And the user presses the submit button
    Then the user is shown an error message telling them no account exists for those credentials

  Scenario: Login with existing account
    Given the user has an account in the system
    And the user visits the login page
    When the user enters a username currently in the system
    And the user enters the password for the username
    And the user presses the submit button
    Then the user is logged in
    And the user is taken to the gym list page

  @form-errors
  Scenario: Login with wrong username
    Given the user has an account in the system
    And the user visits the login page
    When the user enters a username currently in the system
    But there is a typo in the username
    And the user enters the password for the username
    And the user presses the submit button
    Then the user is shown an error message telling them no account exists for those credentials

  @form-errors
  Scenario: Login with wrong password
    Given the user has an account in the system
    And the user visits the login page
    When the user enters a username currently in the system
    And the user enters the password for the username
    But there is a typo in the password
    And the user presses the submit button
    Then the user is shown an error message telling them no account exists for those credentials

    Scenario: Redirect logged in users
    Given the user is logged in
    When the user visits the login page
    Then the user is taken to the gym list page
