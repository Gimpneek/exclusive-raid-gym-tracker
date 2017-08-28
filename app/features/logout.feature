# Created by colinwren at 28/08/2017
Feature: Logout
  As a user of the system
  In order to prevent people from accessing my account
  I want to be able to logout of the system when not using it

  Scenario: Logout
    Given the user is logged in
    When they user logs out of the system
    Then they are shown the homepage
    And they cannot access the following pages:
    | Page                     |
    | Gym List                 |
    | Gym Item                 |
    | Reset Gym Data URL       |
    | Hide Gym in Gym List URL |
