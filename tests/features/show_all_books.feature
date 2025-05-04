# Created by ncasv at 2025-05-04
Feature: Show all books
  On the Katalog page, all books should display

  Scenario Outline: Default books should display
    Given I am at the start page
    Then the book <expected_book_title> with forfattare <expected_forfattare> should show on Katalog page
    Examples:
      | expected_book_title                                        | expected_forfattare |
      | Hur man tappar bort sin TV-fjärr 10 gånger om dagen        | Bertil Flimmer      |
      | Kaffekokaren som visste för mycket                         | Saga Espresson      |
      | Min katt är min chef                                       | Kattis Jamsson      |
      | 100 sätt att undvika måndagar                              | Göran Snooze        |
      | Gräv där du står – och hitta en pizzameny                  | Maja Skruv          |
      | Jag trodde det var tisdag                                  | Kim Vilsen          |
      | Att prata med växter – och vad de egentligen tycker om dig | Flora Tistel        |
