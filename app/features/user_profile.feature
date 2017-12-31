Feature: User Profile
      As a user of the system
      In order to update data related to myself
      I want to have a page that lets me update my data

  Scenario: Shows user's name in header
    # As a user 
    # In order to share my statistics
    # I want my username to be shown on the page
    Given the user is logged in
    When the user visits the user profile page
    Then the user's name is shown in the page header

  Scenario: Shows list of completed raids
    # As a user
    # In order to see the history of my raiding activity
    # I want to see a the raids I have completed
    Given the user is logged in
    And the user has completed at least one raid
    When the user visits the user profile page
    Then the user sees a list of their completed raids
    And the raid list shows the gym name
    And the raid list shows the visit date
    And the raid list shows a button remove the completed raid

  Scenario: Shows map of raids
    # As a user
    # In order see a visual representation of my raiding journey
    # I want to see a map of my raids over time
    Given the user is logged in
    And the user has completed at least one raid
    When the user visits the user profile page
    Then the user sees a map of their completed raids

  @redirect-to-profile
  Scenario: User can remove Completed Raid from list of completed raids
    # As a user
    # In order to remove any accidental raid visits I logged
    # I want to be able to remove the raid visit from the list of completed raids
    Given the user is logged in
    And the user has completed at least one raid
    When the user visits the user profile page
    And the user sees a list of their completed raids
    And the user presses the Remove Raid Data button
    Then the raid entry is no longer in the list of completed raids

  @future
  Scenario: User can share profile data

  @future
  Scenario: User can interact with map of raids
