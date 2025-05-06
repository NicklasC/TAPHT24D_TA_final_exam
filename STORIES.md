# Epic: Läslistan - a site where you can add new books and save your book favorites

Description: A web application for managing book collections and favorites 

## Feature: Show all books (Katalog)
Priority: High
Status: Done
### User story: Show all books on Katalog page
    As a user
    I want to see all previously added books
    So I can get ideas of what book to read

#### Acceptance criteria: 
    [A1] All books should be listed with title and author.

### User story: Show added book on Katalog page
    As a user
    I want to see my newly added book to the book list
    So I know friends can get it as a recommendation

    [A2] Newly added book should be visible on the Katalog page
    [A3] All previously added book should still be visible


## Feature: Add and remove favorite flag on a book
Priority: Medium

### User story: add favorite flag on book
    As a user
    I want to add a favorite flag on a book
    So I can mark it as a favorite book

    [A1] A click on a book with no favorite marking should mark the book as favorite
    [A2] A book with favorite marking should show with a heart icon to the left of it
    [A3] A book with favorite marking should be listed on the mina favoriter page

### User story: remove favorite flag on book
    As a user
    I want to remove a favorite flag on a book
    So I can remove the favorite flag on a book

    [A4] A click on a book with favorite marking should be unflagged as favorite
    [A5] A book without favorite marking should show without any heart icon to the left of it
    [A6] A book that is not marked as favorite should not be visible on the mina favoriter page

## Feature: Show favorite books

### User story
    As a user
    I want to be able to see a list of all my favorites
    So I can be reminded of what books to recommend to my friends

    [A1] If no books are marked as favorite, the user be informed that they will be listed
    [A2] if one or many books are marked as favorite, they will be listed on the favorite page.




## Feature: Add book
Priority: High
Status: Done

### User story: Add a book
    As a user
    I want to add a book
    To add to the collection for me and other users

### User story: Book Data Validation
    As a user
    I want to have proper validation when adding a book
    So that the book information is consistent and reliable

### User story: Book title and author should support åäö
    As a user
    I want to be able to have characters åäö as a part of the book name and author
    So that swedish book names and authors can be entered correctly.


#### Acceptance criteria:
    - [A1] It should be possible to create a book
    - [A2] Creation form should be cleared after book is created
    - [A3] "Lägg till ny bok" button should be disabled when page is loaded
    - [A4] "Lägg till ny bok" button should be disabled when only Titel is filled in.
    - [A5] "Lägg till ny bok" button should be disabled when only Author is filled in.
    - [A6] "Lägg till ny bok" button should be enabled when both Titel and Author is filled in.
    - [A7] It should be possible to create a book with åäö characters in title and Author field.
    - [A8] A created book should be visible on the Katalog page

## Feature: Navigate site
Priority: High
Status: Done

### User story: Menu navigation
    As a user
    I want to click the navigation buttons 
    So that I can move between the different sections of the site

#### Acceptance criteria:
    - [A1] Three navigation buttons available: Katalog, Lägg till bok, Mina böcker
    - [A2] Clicking a button leads to correct page
    - [A3] The current page navigation button should be disabled
    - [A4] Navigation buttons should be visible on all pages

