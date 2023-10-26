# School Library App

This school library app was designed to create a management system by where students can go in and checkout leaving cert books, the site is specifially trageted at leaving cert students with books taken from the 2023/2024 leaving cert cirriculum.

View the live site [here](https://library-management-p3-928b1bbc3b7c.herokuapp.com/).

![screenshot of the live site](https://github.com/DaniCarmo/library-management/blob/main/Screenshots/deployed-screenshot.png?raw=true)


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
   * [Manual Testing](#manual-testing)
   * [Unfixed Bugs](#unfixed-bugs)
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

![flowchart-screenshot1](https://github.com/DaniCarmo/library-management/blob/main/Screenshots/chart1.png?raw=true)
![flowchart-screenshot1](https://github.com/DaniCarmo/library-management/blob/main/Screenshots/chart2.png?raw=true)

## Data Storage (Google Sheets)

The data for the application is stored in a google sheet [here](https://docs.google.com/spreadsheets/d/1hdoiYWrr5WWmtU-qQT488key_tRgNwEsCKvc7pegzsE/edit?usp=sharing).

## Features

### Existing Features

#### The Main Menu

   * When the page is first loaded, the user is presented with a welcome message and a note confirming that book have been loaded and user can begin search.
   * The user has a search menu with three options to search by as well as a fourth option to Quit the programme.
   
   ![screenshot of the main menu](https://github.com/DaniCarmo/library-management/blob/main/Screenshots/main-menu.png?raw=true)

   * Following on from the initial search choice of 1-4, the user is then asked to specify their choice.

   ![screenshot of second page of search](https://github.com/DaniCarmo/library-management/blob/main/Screenshots/second-menu.png?raw=true)

#### The Search Results Display

   * Once the user has input a subject, title or publisher for searching, all matching books are displayed and easily read by the user. Below are screenshots of searchong by the subject "Maths" ad publisher "Folens".

   ![screenshot of search results by subject](https://github.com/DaniCarmo/library-management/blob/main/Screenshots/subject-search.png?raw=true)
   ![screenshot of search results by publisher](https://github.com/DaniCarmo/library-management/blob/main/Screenshots/publisher-search.png?raw=true)

   * If no books are found the user is informed and brought back to the main menu where they can try again or quit.

   ![screenshot when no books found](https://github.com/DaniCarmo/library-management/blob/main/Screenshots/none-found.png?raw=true)

#### Checkout

   * After the user has been presented with a list of relevant books matching their seatch, they are then asked to enter the title of the book they would like to check out or else go back to the main menu.
   * The user will also be presented with a message to confirm the book title that they wish to checkout and they must enter yes or no to confirm, this is an added feature so the user has one more check to confirm and avoid errors before they commit to checking out.

   ![screenshot of checkout option](https://github.com/DaniCarmo/library-management/blob/main/Screenshots/checkout.png?raw=true)

   * If user enters tnhe title incorrectly an error message will show asking the user to try again:

   ![screenshot of checkout error](https://github.com/DaniCarmo/library-management/blob/main/Screenshots/checkout-error.png?raw=true)

#### Checkout Confirmation

   * Once user has chosen the option to check out their book, a confirmation message will appear to advise that the book has been successfully checked out of the library and can be collected from the library reception by 3pm that day.
   * User is also presented with the main search menu again where they can search and checkout another book or quit the programme.

   ![screenshot of checkout confirmation](https://github.com/DaniCarmo/library-management/blob/main/Screenshots/checkout-confirmation.png?raw=true)

#### Feedback For Invalid Inputs

   Every input the user enters is validated to ensure it meets the required standards for the app. If invalid input is entered, the user is notified that it is invalid, informed of the necessary requirements for the input, and requested to input new valid data.

   * The main menu has options 1-4, if the user enters any other number they will be presented with an error message.

    ![screenshot of menu options error](https://github.com/DaniCarmo/library-management/blob/main/Screenshots/menu-error.png?raw=true)

   * If the user enters a subject, publisher or book title that does not exist in the library they will be presented with an error message.

    ![screenshot of choice input error](https://github.com/DaniCarmo/library-management/blob/main/Screenshots/none-found.png?raw=true)

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

## Testing

Various tests were carried out for this project.

NB - HTML, CSS, and JavaScript were provided in the [code institute template](https://github.com/Code-Institute-Org/python-essentials-template) and are not in scope for this project as well as the aspect of responsive design, therefore they were not taken into consideration.

### Python PEP8 Validation

The code has been tested using [Code Institute CI Python Linter (Pep8)](https://pep8ci.herokuapp.com/) and no errors found.

The code was also checked throughout the project where errors showed up on CodeAnywhere regarding lines too long and white space trailing, and these were fixed as they arose.

### Manual Testing

Ran each test mentioned in the table below multiple times and each action executes as intended, providing confirmation of successful user story requirements and actions.
(table)

### Unfixed Bugs

There are no unfixed bugs recorded.

## Deployment and Development

* The project was developed using Codeanywhere to create the code and files required.
* The project files, code, and information are hosted by [Github](https://github.com/).

### Deploying the App

The deployment of the project was done using [Heroku](https://www.heroku.com/) through the following steps.

1. Log in to Heroku or create an account if necessary.
2. Click on the button labeled "New" from the dashboard in the top right corner and select the "Create new app" option in the drop-down menu.
3. Enter a unique name for the application and select the region you are in.
   * For this project, the unique name is "doctor-diary" and the region selected is Europe.
4. Click on "create app".
5. Navigate to the settings tab and locate the "Config Vars" section and click "Reveal config vars".
6. Add a config var (if the project uses creds.json file.)
   * In the "KEY" field:
      * enter "CREDS" in capital letters.
   * In the "VALUE" field:
      * copy and paste the contents of your creds.json file and click "Add".
7. Add another config var.
   * In the "KEY" field:
      * enter PORT in all capital letters.
   * In the "VALUE" field:
      * enter 8000 and click "Add".
8. Scroll to the "Buildpacks" section and click "Add buildpack".
9. Select Python and save changes.
10. Add another buildpack and select Nodejs then save changes again.
11. Ensure that the python buildpack is above the Nodejs buildpack.
12. Navigate to the "Deploy" section by clicking the "Deploy" tab in the top navbar.
13. Select "GitHub" as the deployment method and click "Connect to GitHub".
14. Search for the GitHub repository name in the search bar.
15. Click on "connect" to link the repository to Heroku.
16. Scroll down and click on "Deploy Branch".
17. Once the app is deployed, Heroku will notify you and provide a button to view the app.

NB - If you wish to rebuild the deployed app automatically every time you push to GitHub, you may click on "Enable Automatic Deploys".

### Forking The Repository

This can be done to create a copy of the repository. The copy can be viewed and edited without affecting the original repository.

To fork the repository through GitHub, take the following steps:

1. In the "Project-3-The-Children-s-Book-Picker" repository, click on the "fork" tab in the top right corner.
2. Click on "create fork" to fork the repository.

### Cloning The Repository

To clone the repository through GitHub:

1. In the repository, select the "code" tab located just above the list of files and next to the GitHub button.
2. Ensure HTTPS is selected in the dropdown menu.
3. Copy the URL under HTTPS.
4. Open Git Bash in your IDE of choice.
5. Change the current working directory to the location where you want the cloned directory to be created.
6. Type "git clone" and paste the URL that was copied from the repository.
7. Press the "enter" key to create the clone.

### APIs 
In order for the app to function properly, APIs need to be set up and connected. In particular, the following APIs were used for this project:

* Google Drive API.
   * This helps with getting credentials to access the files within google drive.
* Google Sheets API.
   * This is the API for the google sheets where the data is stored for the program.

I followed the steps in a video from the [Code Institute](https://codeinstitute.net/global/) Love Sandwiches project on how to set up and connect APIs. The link to this video is [here](https://www.youtube.com/watch?v=WTll5p4N7hE).
   
## Credits

* I used [this video](https://www.youtube.com/watch?v=WTll5p4N7hE) from [Code Institute](https://codeinstitute.net/global/) to learn how to create and link APIs.
* Followed tips and troubleshooting throughout the project on Stackoverflow [stackoverflow](https://stackoverflow.blog/) and Python.org [python-org](https://www.python.org/).
* Got the concept for a library system from another code institute alumni with username "Blignaut24" [user-github](https://github.com/Blignaut24/Project-3-The-Children-s-Book-Picker)
* I used ChatGBT [chat-gbt](https://chat.openai.com/) to assist with verifying the main function and helping to split out functions form the main function so there was not too much in one function, as well as assisting in the best way to make user input choices case insensitive to avoid errors when checking out book titles in all lower case.
* I got advice from my mentor Ronan McClelland on splitting out functions as well as the clear terminal function.