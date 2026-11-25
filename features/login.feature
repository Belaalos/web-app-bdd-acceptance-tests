Feature: Login on the-internet.herokuapp.com
  As a user I want to sign in so that I can reach the secure area

  Scenario: Successful login
    Given I am on the login page
    When I log in with username "tomsmith" and password "SuperSecretPassword!"
    Then I should see the secure area
    And the message should contain "You logged into a secure area!"

  Scenario Outline: Failed login shows an error
    Given I am on the login page
    When I log in with username "<username>" and password "<password>"
    Then the message should contain "<message>"

    Examples:
      | username | password             | message                  |
      | tomsmith | wrong                | Your password is invalid |
      | nobody   | SuperSecretPassword! | Your username is invalid |

  Scenario: Logout
    Given I am on the login page
    When I log in with username "tomsmith" and password "SuperSecretPassword!"
    And I click logout
    Then I should be back on the login page
