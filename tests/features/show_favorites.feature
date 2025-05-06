# Created by ncasv at 2025-05-06
Feature: Show favorite books page
  # Enter feature description here

  Scenario: Show favorites books page, no favorites selected
    When I navigate to the mina böcker page
    Then the no favorites selected text should show
    And the dina favoriter text should not show


  Scenario: Show favorites books page lists favorites
    Given I navigate to the lägg till bok page
    And I create a book with titel Kalle kula made by author Kapten Haddock
    And I navigate to the katalog page
    And I click on the book Kalle kula
    When I navigate to the mina böcker page
    Then the dina favoriter text should show
    Then the no favorites selected text should not show
    And the book Kalle kula should be listed

Scenario: Show favorites books page should not list a non favorite book
    Given I navigate to the lägg till bok page
    And I create a book with titel Kalle kula made by author Kapten Haddock
    When I navigate to the mina böcker page
    Then the no favorites selected text should show
    And the dina favoriter text should not show
    And the book Kalle kula should not be listed

