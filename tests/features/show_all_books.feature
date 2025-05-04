# Created by ncasv at 2025-05-04
Feature: Show all books
  On the Katalog page, all books should display

  Scenario Outline: Default books should display
    Given I am at the start page
    Then the book <expected_book_title> should show on Katalog page
    Examples:
      | expected_book_title                                        |
      | Hur man tappar bort sin TV-fjärr 10 gånger om dagen        |
      | Kaffekokaren som visste för mycket                         |
      | Min katt är min chef                                       |
      | 100 sätt att undvika måndagar                              |
      | Gräv där du står – och hitta en pizzameny                  |
      | Jag trodde det var tisdag                                  |
      | Att prata med växter – och vad de egentligen tycker om dig |