# Epic: Läslistan - a site where you can add new books and save your book favorites

Description: A web application for managing book collections and favorites 

## Feature: Show all books (Katalog)
Priority: High

## Feature: Add favorites
Priority: Medium

## Feature: Add book
Priority: High

### User story: Add a book
    As a user
    I want to add a book
    To add to the collection for me and other users

#### Acceptance criteria:
    - [A1] It should be possible to create a book
    - [A2] Creation form should be cleared after book is created
    - [A3] "Lägg till ny bok" button should be disabled when page is loaded
    - [A4] "Lägg till ny bok" button should be disabled when only Titel is filled in.
    - [A5] "Lägg till ny bok" button should be disabled when only Author is filled in.
    - [A6] "Lägg till ny bok" button should be enabled when both Titel and Author is filled in.
    - [A7] It should be possible to create a book with åäö characters in title and Author field.
    - [A8] A created book should be visible on the show my favorites page
    - [A9] A created book should be visible on the show all books page

## Feature: Show my favorites
Priority: Low

## Feature: Navigate site
Priority: High

### User story: Menu navigation

    As a user
    I want to click the navigation buttons 
    So that I can move between the different sections of the site

#### Acceptance criteria:

    - [A1] Three navigation buttons available: Katalog, Lägg till bok, Mina böcker
    - [A2] Clicking a button leads to correct page
    - [A3] The current page navigation button should be disabled
    - [A4] Navigation buttons should be visible on all pages

