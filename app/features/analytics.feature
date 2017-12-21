Feature: Analytics
      As a person interested in raid activity in Leeds
      In order to learn more about raids in Leeds
      I want to have a page that shows me statistics on raids in Leeds

  Scenario: Date range for analytics is shown
    # As a user
    # In order to understand the period for the statistics I'm being shown
    # I want to see the dates covered
    Given the user visits the analytics page
    Then the analysis date range is shown in the page header

  Scenario: Shows list of gyms with most raids
    # As a user
    # In order to get a better idea of which gyms have the most raids
    # I want to see a list of gyms that have had the most raids at them during the reporting period
    Given at least ten raid has popped up in the date period
    When the user visits the analytics page
    Then the user sees a table of active gyms
    But only the ten most active gyms are shown in the table

  Scenario: Shows list of most common raid levels
    # As a user
    # In order to gauge how rare certain raids are
    # I want to see a list of the raid levels ordered by total number that happened during the reporting period
    Given at least one raid has popped up in the date period
    When the user visits the analytics page
    Then the user sees a table of raid levels

  Scenario: Show list of busiest days for raids
    # As a user
    # In order to gauge when is the best day(s) to go raiding in Leeds
    # I want to see a list of the days of the week ordered by the number of raids that happened during that period
    Given at least one raid has popped up in the date period
    When the user visits the analytics page
    Then the user sees a table of days that raids happened on

  @Future
  Scenario: Can define custom date range

  @Future
  Scenario: Can filter out non-tracked gyms
