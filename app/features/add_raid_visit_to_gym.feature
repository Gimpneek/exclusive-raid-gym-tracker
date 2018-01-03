Feature: Add Raid Visit to Gym
      As a user of the system
      In order to update my progress against the goal
      I want to be able to add a raid visit to gyms in the city

  Background:
    Given the user is logged in
    And the user is tracking at least one gym

  @redirect-to-list
  Scenario: After submitting raid visit user is taken back to previous gym / raid list
    # As a user
    # In order to add another raid visit
    # I want to be taken back to taken back to the gym / raid list I was on before adding a raid
    Given the user visits the gym list page
    And the user presses the Add Raid button on a gym
    And the user is taken to the add raid page
    And they enter a valid date into the last raid visit entry box
    When the user presses the Submit Raid button
    Then the user is taken to the gym list page
    And the gym card shows the date they entered as the last visited date

  Scenario: Raid visit not logged on pressing cancel
    # As a user
    # In order to not add raid visits by accident
    # I want to be able to cancel the form and return to the previous raid / gym list
    Given the user visits the gym list page
    And the user presses the Add Raid button on a gym
    And the user is taken to the add raid page
    When the user presses the Cancel button
    Then the user is taken to the gym list page
    And the gym card shows they have yet to visit the gym

  Scenario: Shows list of last 5 raids on the gym
    Given the user visits the gym list page
    And at least one raid has popped up in the date period
    When the user presses the Add Raid button on a gym
    Then the user is taken to the add raid page
    And the user sees a list of the last 5 raids on the gym

  @Future
  Scenario: User can add CP of pokemon

  @Future
  Scenario: User can number of balls won

  @Future
  Scenario: User can add if pokemon caught or not
