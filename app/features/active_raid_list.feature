Feature: Active Raid List
    As a user
    In order to go do raids and start logging them
    I want to see a list of active raids on the gyms that I track

  Scenario: Shows active raids on tracked gyms
    # As a user
    # In order to know which gyms to visit
    # I want to see a list of active raids
    Given the user is logged in
    And the user is tracking at least one gym
    And a raid is active on a gym
    When the user visits the active raid list page
    Then the user sees a list of raids that are currently happening
