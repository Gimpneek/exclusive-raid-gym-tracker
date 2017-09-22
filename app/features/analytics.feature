# Created by colinwren at 16/09/2017
@dev
Feature: Analytics
  As a person interested in raid activity in Leeds
  In order to learn more about raids in Leeds
  I want to have a page that shows me statistics on raids in Leeds

  Scenario: Analytics shows date range in header
    Given the user visits the analytics page
    Then the analysis date range is shown in the page header

  Scenario: Analytics shows total raids during period
    Given at least one raid has popped up in the date period
    When the user visits the analytics page
    Then the user sees a count of the raids during the period

  Scenario: Analytics shows most active gym during period
    Given at least one raid has popped up in the date period
    When the user visits the analytics page
    Then the user sees the name of the most active gym during the period

  Scenario: Analytics shows most active time of day during period
    Given at least one raid has popped up in the date period
    When the user visits the analytics page
    Then the user sees the most active time of day during the period

  Scenario: Analytics shows total raids during period
    Given at least one raid has popped up in the date period
    When the user visits the analytics page
    Then the user sees a the most active day during the period

  Scenario: Analytics shows table of active gyms
    Given at least one raid has popped up in the date period
    When the user visits the analytics page
    Then the user sees a table of active gyms
    And the user sees a map of the active gyms

  Scenario: Analytics shows table of raid levels
    Given at least one raid has popped up in the date period
    When the user visits the analytics page
    Then the user sees a table of raid levels

  Scenario: Analytics shows table of hours raids happened
    Given at least one raid has popped up in the date period
    When the user visits the analytics page
    Then the user sees a table of hours that raids happened in

  Scenario: Analytics shows table of days raids happened
    Given at least one raid has popped up in the date period
    When the user visits the analytics page
    Then the user sees a table of days that raids happened on