Feature: Gym Management
    As a user
    In order to track my progress against my goals on a gym
    I want to be able to track that gym

  Scenario: Link to Gym Management is present on Gym List
    # As a user
    # In order to manage the gyms that I follow
    # I want to get access to the gym management screen while looking at my tracked gyms
    Given the user is logged in
    When the user visits the gym list page
    Then the user sees a link to the gym management page

  Scenario: User can search for a gym in the system
    # As a user
    # In order to track a gym
    # I want to be able to search through all the gyms in the system
    Given the user is logged in
    When the user visits the gym management page
    Then they should see a search bar

  Scenario: User can start tracking a gym
    # As a user
    # In order to track my progress against goals I have against a gym
    # I want to be able to track that gym in the app
    Given the user is logged in
    And the user visits the gym management page
    When the user enters the name of a gym into the search bar
    And the user presses the suggested gym
    Then the user starts tracking that gym

  Scenario: User can stop tracking a gym
    # As a user
    # In order to stop tracking my progress against gyms I no longer care about
    # I want to stop tracking the gym
    Given the user is logged in
    And the user is tracking at least one gym
    When the user visits the gym management page
    And the user presses the Remove Gym button on a gym in the table
    Then the user stops tracking that gym

  Scenario: User automatically follows a gym when they log a raid on it
    # As a user
    # In order to add to my tracked gyms list without having to know all the gyms I want to track
    # I want to have any gyms I log raids on added to my tracked gym list
    Given the user is logged in
    When the user completes a raid on a gym
    Then the user starts tracking that gym
