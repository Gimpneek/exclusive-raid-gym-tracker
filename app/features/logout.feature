# Created by colinwren at 28/08/2017
Feature: Logout
  As a user of the system
  In order to prevent people from accessing my account
  I want to be able to logout of the system when not using it

  Scenario: Logout
    Given the user is logged in
    When the user logs out of the system
    Then the user is taken to the landing page
    And they cannot access the following pages
    | Page                     |
    | Gym List                 |
    | Add Raid                 |
    | Reset Gym Data URL       |
    | Hide Gym in Gym List URL |
    But they can access the following pages
    | Page     |
    | Sign Up  |
    | Login    |
    | Homepage |
