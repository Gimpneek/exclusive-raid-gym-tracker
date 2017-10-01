# Created by colinwren at 30/09/2017
Feature: Add Raid Visit to Gym - Recent Raid Table
  As a user of the system
  In order to ensure I don't enter the wrong time when adding a raid after a heavy session
  I want to see a list of recent raids

  Scenario: Recent Raid Table
    Given the user is logged in
    And a raid has happened on a gym
    And the user visits the gym list page
    When they click on the Add Raid button on a gym card
    Then the user is taken to the add raid page
    And they see a table of recent raids on the gym

  Scenario: Recent Raid Table - Includes Current
    Given the user is logged in
    And a raid is active on a gym
    And the user visits the gym list page
    When they click on the Add Raid button on a gym card
    Then the user is taken to the add raid page
    And they see a table of recent raids on the gym

  Scenario: Recent Raid Table - No Raids
    Given the user is logged in
    And there has been no raids on a gym
    And the user visits the gym list page
    When they click on the Add Raid button on a gym card
    Then the user is taken to the add raid page
    And they don't see a table of recent raids on the gym