# Created by ncasv at 2025-05-05
Feature: add favorite book
  The user should be able to mark a book as a favorite.

  Scenario: Mark a book as favorite
    Given the book Hur man tappar bort sin TV-fjärr 10 gånger om dagen has status non-favorite
    When I click on the book Hur man tappar bort sin TV-fjärr 10 gånger om dagen
    Then the book Hur man tappar bort sin TV-fjärr 10 gånger om dagen has status favorite

  Scenario: Unmark a favorited book
    Given the book Hur man tappar bort sin TV-fjärr 10 gånger om dagen has status non-favorite
    And I click on the book Hur man tappar bort sin TV-fjärr 10 gånger om dagen
    And the book Hur man tappar bort sin TV-fjärr 10 gånger om dagen has status favorite
    When I click on the book Hur man tappar bort sin TV-fjärr 10 gånger om dagen
    Then the book Hur man tappar bort sin TV-fjärr 10 gånger om dagen has status non-favorite

    # Same steps as Unmark Scenario: favorit:ed book, but with another test name for clarity.
  Scenario: Toggle favorite / unfavorite status on a book
    Given the book Hur man tappar bort sin TV-fjärr 10 gånger om dagen has status non-favorite
    And I click on the book Hur man tappar bort sin TV-fjärr 10 gånger om dagen
    And the book Hur man tappar bort sin TV-fjärr 10 gånger om dagen has status favorite
    When I click on the book Hur man tappar bort sin TV-fjärr 10 gånger om dagen
    Then the book Hur man tappar bort sin TV-fjärr 10 gånger om dagen has status non-favorite
