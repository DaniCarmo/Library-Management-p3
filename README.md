# School Library App

This school library app was designed to create a management system by where students can go in and checkout leaving cert books, the site is specifially trageted at leaving cert students with books taken from the 2023/2024 leaving cert cirriculum.

View the live site [here]().

![screenshot of the live site]()


## Contents

* [Purpose](#purpose)
* [User Experience](#user-experience)
   * [Project Goals](#project-goals)
   * [User Stories](#user-stories)
   * [Program Flowchart](#program-flowchart)
* [Data Storage](#data-storage-google-sheets)
* [Features](#features)
   * [Existing Features](#existing-features)
      * [The Main Menu](#the-main-menu)
      * [The Search Results Display](#the-search-results-display)
      * [Checkout](#checkout)
      * [Checkout Confirmation](#checkout-confirmation)
      * [Feedback For Invalid Inputs](#feedback-for-invalid-inputs)
   * [Future Features](#future-features)
* [Technologies Used](#technologies-used)
* [Python Packages Used](#python-packages-used)
* [Testing](#testing)
   * [Python PEP8 Validation](#python-pep8-validation)
   * [Testing User Stories](#testing-user-stories)
   * [Development Bugs](#development-bugs)
* [Deployment and Development](#deployment-and-development)
   * [Deploying the App](#deploying-the-app)
   * [Forking The Repository](#forking-the-repository)
   * [Cloning The Repository](#cloning-the-repository)
   * [APIs](#apis)
* [Credits](#credits)

## Purpose

The purpose of this program is to create an online library of school books, where the user can input data that can then be validated and retrieved. It is intended to enable the user to easily search and checkout a book.

This program is developed to demonstrate competency in python programming and is purely for educational purposes.

## User Experience

### Project Goals

As the site owner, I want the program to:
* Provide information on how to use the library.
* Be easy to navigate.
* Provide feedback or a response to the user when they perform a task or action, in the form of options and error messages.
* Allow the user to search for any book within the library by either title, subject or publisher.
* Allow the user to check out a book.

### User Stories

As a user, I want to be able to:
* Easily indentify the menu options and what each consists of.
* Search for books within the library by either title, subject or publisher.
* Check out a book.
* Confirm my choices as I go to avoid errors.
* Be able to go back to the main menu or quit the programme easily.

### Program flowchart

During the planning stages, I created a basic flowchart of how I wanted the program to work and interact.
The flowchart was created using [Lucidchart](https://www.lucidchart.com/pages/).

![flowchart-screenshot]()

## Data Storage (Google Sheets)

The data for the application is stored in a google sheet [here](https://docs.google.com/spreadsheets/d/1hdoiYWrr5WWmtU-qQT488key_tRgNwEsCKvc7pegzsE/edit?usp=sharing).

## Features

### Existing Features

#### The Main Menu

   * When the page is first loaded, the user is presented with a welcome message and a note confirming that book have been loaded and user can begin search.
   * The user has a search menu with three options to search by as well as a fourth option to Quit the programme.
   
   ![screenshot of the main menu]()

   * Following on from the initial search choice of 1-4, the user is then asked to specify their choice.

   ![screenshot of second page of search]()

#### The Search Results Display

   * Once the user has input a subject, title or publisher for searching, all matching books are displayed and easily read by the user.

   ![screenshot of search results by subject]()
   ![screenshot of search results by publisher]()

   * If no books are found the user is informed and brought back to the main menu where they can try again or quit.

   ![screenshot when no books found]()

#### Checkout

   * After the user has been presented with a list of relevant books matching their seatch, they are then asked to enter the title of the book they would like to check out or else go back to the main menu.

   ![screenshot of checkout option]()

   * If user enters tnhe title incorrectly an error message will show asking the user to try again:

   ![screenshot of checkout error]()

   * The user will also be presented with a message to confirm the book title that they wish to checkout and they must enter yes or no to confirm, this is an added feature so the user has one more check to confirm and avoid errors before they commit to checking out.
   
   ![screenshot of checkout message yes/no]()

#### Checkout Confirmation

   * Once user has chosen the option to check out their book, a confirmation message will appear to advise that the book has been successfully checked out of the library and can be collected from the library reception by 3pm that day.
   * User is also presented with the main search menu again where they can search and checkout another book or quit the programme.

   ![screenshot of checkout confirmation]()

#### Feedback For Invalid Inputs

   Every input the user enters is validated to ensure it meets the required standards for the app. If invalid input is entered, the user is notified that it is invalid, informed of the necessary requirements for the input, and requested to input new valid data.

   * The main menu has options 1-4, if the user enters any other number they will be presented with an error message.

    ![screenshot of menu options error]()

   * If the user enters a subject, publisher or book title that does not exist in the library they will be presented with an error message.

    ![screenshot of choice input error]()

### Future Features

Features to be implemented may include:
* A sign in feature for students whereby they must enter their student ID to use the library system and checkout, this will allow the school to keep track of who has what books.
* An admin log in so a staff member can view the library data to see who has checked out books and how many books are available.
* Adding data to the spreadsheet to confirm how many copies of each book are available, so a student can only check out a book if there is one available and will be provided an error message to advise that this book is currently out of stock.
* A feature whereby the student is sent an aoutomated email to remind them to collect the book on the day of checkout as well as an email 1 week later to remind them to return the book.
* A feature to keep track of how long a student has had a book, so if they go over the alloted time they are charged a small fine.

## Technologies used

* [Lucidchart](https://www.lucidchart.com/pages/).
   * Used to create a flowchart during the planning stage.
* [HTML5](https://html.spec.whatwg.org/)
   * Used to add structure and content for the site.
   * (provided in the [code institute template](https://github.com/Code-Institute-Org/python-essentials-template)).
* [CSS](https://www.w3.org/Style/CSS/Overview.en.html)
   * Used to provide styling for the site.
   * (provided in the [code institute template](https://github.com/Code-Institute-Org/python-essentials-template)).
* [Python](https://www.python.org/)
   * Used to provide functionality to the site.
* [Google Sheets](https://www.google.co.uk/sheets/about/)
   * Used to host application data.
* [CodeAnywhere](https://app.codeanywhere.com/)
   * Used to create the code and content for the repository.
* [Github](https://github.com/)
   * Used to host the repository.

## Python Packages Used

* [GSpread](https://pypi.org/project/gspread/)
   * Used to store the data in google sheets.
* [OS](https://docs.python.org/3/library/os.html)
   * Used to clear the terminal.
* [Color](https://pypi.org/project/colour/)
   * Used to add color to certain text.


## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

---

Happy coding!
