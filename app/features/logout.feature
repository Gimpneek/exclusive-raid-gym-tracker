Feature: Logout
      As a user of the system
      In order to prevent people from accessing my account
      I want to be able to logout of the system when not using it

  Scenario: Logged in user is logged out
    # As a user
    # I want to people to be unable to access my account when I log out
    # In order to stop people messing up my raid progress
    Given the user is logged in
    When the user presses the log out button
    Then the user session is ended

  Scenario: Once logged out user is redirected to homepage
    # As a user
    # In order to log back into the app if I accidentally log out
    # I want to be redirected to the app's homepage
    Given the user is logged in
    When the user presses the log out button
    Then the user is taken to the landing page
