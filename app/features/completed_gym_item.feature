# Created by colinwren at 28/08/2017
Feature: Add Raid Visit to Gym - Completed raid
  As a user of the system
  In order to update my progress against the goal
  I want to be able to add a raid visit to gyms in the city

  Background:
    Given the user is logged in
    And the user has completed at least one raid
    And the user visits the gym list page
    And they click on the Add Raid button on a gym card
    And the user is taken to the gym item page

  @redirect-to-list
  Scenario: Add Raid Date to Gym
    When they enter a valid date into the last raid visit entry box
    And the user presses the Submit Raid button
    Then the user is taken to the gym list page
    And the gym is present in the list of gyms they have already visited
    And the gym card shows the date they entered as the last visited date

  @redirect-to-list
  Scenario: Remove Raid Date from Gym
    When the user presses the Remove Raid Data button
    Then the user is taken to the gym list page
    And the gym is present in the list of gyms they have yet to visit
    And the gym card shows they have yet to visit the gym

  Scenario: Cancel adding Raid Date to Gym
    When the user presses the Cancel button
    Then the user is taken to the gym list page
    And the gym is present in the list of gyms they have already visited
    And the gym card shows the unchanged visit date

  @form-errors @safari
  Scenario: Enter invalid date
    When they enter an invalid date into the last raid visit entry box
    And the user presses the submit button
    Then They stay on the form
    And the user is shown an error message saying the date is invalid
