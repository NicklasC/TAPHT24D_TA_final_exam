# Created by ncasv at 2025-05-02
Feature: Navigation between pages
  User story: Menu navigation
  It should be possible to navigate to each page from any other page

  Scenario Outline: Navigate from catalog page
    Given I navigate to the "<navigate_to_page>" page
    Then I should be on the "<expected_page>" page
    And the "<disabled_button_name>" navigation button should be disabled
    And the "<enabled_button_name>" navigation button should be enabled

    Examples:
      | navigate_to_page | expected_page | disabled_button_name | enabled_button_name |
      | lägg till bok    | lägg till bok | lägg till bok        | katalog             |
      | mina böcker      | mina böcker   | mina böcker          | katalog             |


  Scenario Outline: Navigate from lägg till bok page
    Given I navigate to the "lägg till bok" page
    Given I navigate to the "<navigate_to_page>" page
    Then I should be on the "<expected_page>" page
    And the "<disabled_button_name>" navigation button should be disabled
    And the "<enabled_button_name>" navigation button should be enabled

    Examples:
      | navigate_to_page | expected_page | disabled_button_name | enabled_button_name |
      | katalog          | katalog       | katalog              | lägg till bok       |
      | mina böcker      | mina böcker   | mina böcker          | lägg till bok       |

  Scenario Outline: Navigate from mina böcker page
    Given I navigate to the "mina böcker" page
    Given I navigate to the "<navigate_to_page>" page
    Then I should be on the "<expected_page>" page
    And the "<disabled_button_name>" navigation button should be disabled
    And the "<enabled_button_name>" navigation button should be enabled

    Examples:
      | navigate_to_page | expected_page | disabled_button_name | enabled_button_name |
      | katalog          | katalog       | katalog              | mina böcker         |
      | lägg till bok    | lägg till bok | lägg till bok        | mina böcker         |

