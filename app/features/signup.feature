# Created by colinwren at 28/08/2017
@dev
Feature: Sign Up
  As a potential user of the system
  In order to save my progress and personalise my experience
  I want to be able to create an account

  Scenario: Sign up with a non-existent account
    Given the user visits the sign up page
    When the user enters a username not currently in the system
    And the user enters a password
    And the user presses the submit button
    Then an account is created in the system for the user
    And the user is taken to the gym list page

  Scenario: Sign up without a password
    Given the user visits the sign up page
    When the user enters a username not currently in the system
    And the user doesn't enter a password
    And the user presses the submit button
    Then the user is shown an error message asking them to enter a password

  Scenario: Sign up with an existing account
    Given the user visits the sign up page
    When the user enters a username currently in the system
    And the user enters a password
    And the user presses the submit button
    Then the user is shown an error message telling them to use a different username

  Scenario: Redirect logged in users
    Given the user is logged in
    When the user visits the sign up page
    Then the user is taken to the gym list page
