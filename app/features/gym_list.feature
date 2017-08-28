# Created by colinwren at 28/08/2017
Feature: Gym List
  As a user of the system
  In order to add a raid visit to a gym so I can track my progress
  I want to see a list of gyms in the city

  Scenario: Gym List
    Given the user is logged in
    When they visit the gym list page
    Then they see a list of gyms they have yet to visit
    And the list of gyms is ordered alphabetically
    And they see a list of gyms they have already visited
    And the list of gyms is ordered so the oldest visits are at the top of the list

  Scenario: Add Raid to Gym
    Given the user is logged in
    And they visit the gym list page
    When they click on the Add Raid button on the gym card
    Then they are taken to a data entry page for that gym

  Scenario: Hide Gym in list
    Given the user is logged in
    And they visit the gym list page
    When they click on the Hide button the gym card
    Then the gym card is removed from the list
    And the progress bar is updated to reflect the fact the gym is no longer counted

  Scenario: Progress Bar - No raids completed
    Given the user is logged in
    And they visit the gym list page
    When the user has completed no raids
    Then the progess bar will be empty
    And the completion percentage will be 0%

  Scenario: Progress Bar - At least One Raid completed
    Given the user is logged in
    And they visit the gym list page
    When the user has completed at least one raid
    Then the progress bar will not be empty
    And the completion percentage will reflect the completion percentage

  Scenario: Progress Bar - All raids completed
    Given the user is logged in
    And they visit the gym list page
    When the user has completed all the raids on the visible gyms
    Then the progress bar will be full
    And the completion percentage will be 100%
