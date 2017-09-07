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

  #Scenario: Hide Gym in list
  #  Given the user is logged in
  #  And the user visits the gym list page
  #  When they click on the Hide button on a gym card
  #  Then the gym card is removed from the list
  #  And the progress bar is updated to reflect the fact the gym is no longer counted

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

  Scenario: Search Bar
    Given the user is logged in
    And the user visits the gym list page
    Then they should see a search bar

  Scenario: Search Bar - Autocomplete Suggestions
    Given the user is logged in
    And the user visits the gym list page
    When they enter a partial gym name into the search input
    Then they should see a list of gyms that match that substring

  Scenario: Search Bar - Autocomplete no suggestions
    Given the user is logged in
    And the user visits the gym list page
    When they enter a substring not found in any gym name into the search input
    Then they should see no gyms

  Scenario: Search Bar - Jump to Gym by clicking
    Given the user is logged in
    And the user visits the gym list page
    When they enter a partial gym name into the search input
    And they press the suggested gym
    Then the user is taken to the gym item page

#  Scenario: Search Bar - Jump to Gym by pressing return key
#    Given the user is logged in
#    And the user visits the gym list page
#    When they enter a partial gym name into the search input
#    And they press the return key
#    Then the user is taken to the gym item page

  Scenario: Active Raid on Gym
    Given the user is logged in
    And a raid is active on a gym
    When the user visits the gym list page
    Then the name of the raid pokemon is displayed
    And the level of the raid pokemon is displayed
    And the time remaining of the raid pokemon is displayed

    @dev
  Scenario: Gyms with raids are at top of yet to complete list
    Given the user is logged in
    And a raid is active on a gym
    When the user visits the gym list page
    Then the gym is at the top of the yet to complete gym list