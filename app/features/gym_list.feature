Feature: Gym List
      As a user of the system
      In order to add a raid visit to a gym so I can track my progress
      I want to see a list of gyms in the city

  Scenario: User can Add Raid to Gym
    # As a user
    # In order to track when I last completed a raid at a specific gym
    # I want to be able to log that I completed a raid on a gym
    Given the user is logged in
    And the user is tracking at least one gym
    And the user visits the gym list page
    When they click on the Add Raid button on a gym card
    Then the user is taken to the add raid page

  Scenario: User is able to search for gyms by name
    # As a user
    # In order to quickly add a raid visit for a gym 
    # I want to be able to search for the gym by name and add the raid visit
    Given the user is logged in
    When the user visits the gym list page
    Then they should see a search bar

  Scenario: Shows raid information if raid active on gym in list
    # As a user
    # In order to see if a raid is active on the gyms in my list
    # I want to see raid information for gyms with raids currently happening
    Given the user is logged in
    And the user is tracking at least one gym
    And a raid is active on a gym
    When the user visits the gym list page
    Then they see a raid active banner on the gym's card
    And the name of the raid pokemon is displayed
    And the level of the raid pokemon is displayed
    And the time remaining of the raid pokemon is displayed

  Scenario: Shows if gym is in a park
    # As a user
    # In order to know if the gym I'm doing a raid on is likely to meet the EX-Raid pass criteria of being in a park
    # I want to see a visual cue indicating this
    Given the user is logged in
    And the user is tracking at least one gym
    And that gym is in a park
    When the user visits the gym list page
    Then they see a tree next to the gym name
