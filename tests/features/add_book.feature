# Created by ncasv at 2025-05-03
Feature: Add book
  Implements scenario and requirements for the feature Add book

  Scenario: lagg till ny bok button is initially disabled
    Given I navigate to the lägg till bok page
    Then the lagg till ny bok button is disabled

  Scenario: lagg till ny bok button disabled with only book title
    Given I navigate to the lägg till bok page
    When I type blah in the book titel field
    Then the lagg till ny bok button is disabled

  Scenario: lagg till ny bok button disabled with only book author
    Given I navigate to the lägg till bok page
    When I type blah in the book författare field
    Then the lagg till ny bok button is disabled

  Scenario: Lagg till ny bok button should be enabled when both Titel and Author is filled in
    Given I navigate to the lägg till bok page
    When I type Min bok in the book titel field
    And I type Jan Banan in the book författare field
    Then the lagg till ny bok button is enabled

  Scenario: Create book should clear form
    Given I navigate to the lägg till bok page
    When I create a book with titel blah made by author blooh
    Then titel field should be empty
    And författare field should be empty
    And the lagg till ny bok button is disabled

    Scenario: Created book should show in Katalog page
      Given I navigate to the lägg till bok page
      When I create a book with titel blah made by author blooh
      And I navigate to the katalog page
      Then the book blah should show on Katalog page

