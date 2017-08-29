# Created by colinwren at 28/08/2017
Feature: Gym List
  As a user of the system
  In order to add a raid visit to a gym so I can track my progress
  I want to see a list of gyms in the city

  Scenario: Gym List - Has No Completed Raids
    Given the user is logged in
    And the user has completed no raids
    When the user visits the gym list page
    Then they see a list of gyms they have yet to visit
    And the list of gyms yet to visit is ordered alphabetically
    And the list and title for completed gyms is hidden

  Scenario: Gym List - Has Completed Raids
    Given the user is logged in
    And the user has completed at least one raid
    When the user visits the gym list page
    Then they see a list of gyms they have yet to visit
    And the list of gyms yet to visit is ordered alphabetically
    And they see a list of gyms they have already visited
    And the list of completed gyms is ordered so the oldest visits are at the top of the list

  Scenario: Gym List - Has Completed all Raids
    Given the user is logged in
    And the user has completed all the raids being tracked
    When the user visits the gym list page
    Then they see a list of gyms they have already visited
    And the list of completed gyms is ordered so the oldest visits are at the top of the list
    And the list and title for yet to visit gyms is hidden

  Scenario: Add Raid to Gym
    Given the user is logged in
    And the user visits the gym list page
    When they click on the Add Raid button on a gym card
    Then the user is taken to the gym item page

  Scenario: Hide Gym in list
    Given the user is logged in
    And the user visits the gym list page
    When they click on the Hide button on a gym card
    Then the gym card is removed from the list
    And the progress bar is updated to reflect the fact the gym is no longer counted

  Scenario: Progress Bar - No raids completed
    Given the user is logged in
    And the user has completed no raids
    When the user visits the gym list page
    Then the progress bar will be empty
    And the completion percentage will be 0%

  Scenario: Progress Bar - At least One Raid completed
    Given the user is logged in
    And the user has completed at least one raid
    When the user visits the gym list page
    Then the progress bar will not be empty
    And the completion percentage will reflect the completion percentage

  Scenario: Progress Bar - All raids completed
    Given the user is logged in
    And the user has completed all the raids being tracked
    When the user visits the gym list page
    Then the progress bar will be full
    And the completion percentage will be 100%
