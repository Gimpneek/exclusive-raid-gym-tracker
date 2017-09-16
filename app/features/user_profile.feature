# Created by colinwren at 16/09/2017
Feature: User Profile
  As a user of the system
  In order to update data related to myself
  I want to have a page that lets me update my data

  Scenario: User Profile Shows name in header
    Given the user is logged in
    When the user visits the user profile page
    Then the user's name is shown in the page header

  Scenario: User Profile Shows list of completed raids
    Given the user is logged in
    And the user has completed at least one raid
    When the user visits the user profile page
    Then the user sees a list of their completed raids
    And the raid list shows the gym name
    And the raid list shows the visit date
    And the raid list shows a button remove the completed raid

  @dev
  Scenario: User Profile shows map of raids
    Given the user is logged in
    And the user has completed at least one raid
    When the user visits the user profile page
    Then the user sees a map of their completed raids

  @redirect-to-profile
  Scenario: Remove Completed Raid from list of completed raids
    Given the user is logged in
    And the user has completed at least one raid
    When the user visits the user profile page
    And the user sees a list of their completed raids
    And the user presses the Remove Raid Data button
    Then the raid entry is no longer in the list of completed raids

  Scenario: Removing raids puts gym in Yet To Visit List
    Given the user is logged in
    And the user has completed at least one raid
    When the user visits the user profile page
    And the user sees a list of their completed raids
    And the user presses the Remove Raid Data button
    And the user visits the gym list page
    Then the gym is present in the list of gyms they have yet to visit
     And the gym card shows they have yet to visit the gym