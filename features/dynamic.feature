Feature: Dynamic page elements

  Scenario: Add and remove elements
    Given I open "/add_remove_elements/"
    When I add 3 elements
    And I delete 1 element
    Then I should see 2 delete buttons

  Scenario: Checkboxes can be toggled
    Given I open "/checkboxes"
    When I tick the first checkbox
    Then the first checkbox should be checked

  Scenario: Select a dropdown option
    Given I open "/dropdown"
    When I choose "Option 2" from the dropdown
    Then the dropdown should show "Option 2"

  Scenario: Hidden element appears after loading
    Given I open "/dynamic_loading/1"
    When I click start
    Then I should see the text "Hello World!"

  Scenario: JavaScript alert can be accepted
    Given I open "/javascript_alerts"
    When I click the JS alert button and accept it
    Then the result should say "You successfully clicked an alert"
