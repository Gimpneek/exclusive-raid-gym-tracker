# Created by colinwren at 28/08/2017
Feature: Add Raid Visit to Gym
  As a user of the system
  In order to update my progress against the goal
  I want to be able to add a raid visit to gyms in the city

  Scenario: Add Raid Date to Gym not previously visited
    Given the user is logged into the system
    And they visit the gym list page
    And they select a gym they haven't previously visited
    And they click on the Add Raid button on the gym card
    And they are taken to a data entry page for that gym
    When they enter a valid date into the last raid visit entry box
    And they press the submit button
    Then they are taken to the Gym List page
    And the gym is present in the list of gyms they have already visited
    And the gym card shows the date they entered as the last visited date

  Scenario: Add Raid Date to Gym previously visited
    Given the user is logged into the system
    And they visit the gym list page
    And they select a gym they have previously visited
    And they click on the Add Raid button on the gym card
    And they are taken to a data entry page for that gym
    When they enter a valid date into the last raid visit entry box
    And they press the submit button
    Then they are taken to the Gym List page
    And the gym is present in the list of gyms they have already visited
    And the gym card shows the date they entered as the last visited date

  Scenario: Remove Raid Date from Gym previously visited
    Given the user is logged into the system
    And they visit the gym list page
    And they select a gym they have previously visited
    And they click on the Add Raid button on the gym card
    And they are taken to a data entry page for that gym
    When they press the Remove Raid Data button
    Then they are taken to the Gym List page
    And the gym is present in the list of gyms they have yet to visit
    And the gym card shows they have yet to visit the gym

  Scenario: Remove Raid Date from Gym not previously visited
    Given the user is logged into the system
    And they visit the gym list page
    And they select a gym they haven't previously visited
    And they click on the Add Raid button on the gym card
    And they are taken to a data entry page for that gym
    When they press the Remove Raid Data button
    Then they are taken to the Gym List page
    And the gym is present in the list of gyms they have yet to visit
    And the gym card shows they have yet to visit the gym

  Scenario: Cancel adding Raid Date to Gym not previously visited
    Given the user is logged into the system
    And they visit the gym list page
    And they select a gym they haven't previously visited
    And they click on the Add Raid button on the gym card
    And they are taken to a data entry page for that gym
    When they press the Cancel button
    Then they are taken to the Gym List page
    And the gym is present in the list of gyms they have yet to visit
    And the gym card shows they have yet to visit the gym

  Scenario: Cancel adding Raid Date to Gym previously visited
    Given the user is logged into the system
    And they visit the gym list page
    And they select a gym they have previously visited
    And they click on the Add Raid button on the gym card
    And they are taken to a data entry page for that gym
    When they press the Cancel button
    Then they are taken to the Gym List page
    And the gym is present in the list of gyms they have already visited
    And the gym card shows the date already in the system as the last visited date

  Scenario: Enter invalid date
    Given the user is logged into the system
    And they visit the gym list page
    And they select a gym
    And they click on the Add Raid button on the gym card
    And they are taken to a data entry page for that gym
    When they enter an invalid date into the last raid visit entry box
    And they press the submit button
    Then They stay on the form
    And they are shown an error message saying the date is invalid
