# School Library App

This school library app was designed to create a management system by where students can go in and checkout leaving cert books, the site is specifially trageted at leaving cert students with all books taken from the 2023/2024 leaving cert cirriculum.

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
      * [The Search Menu](#the-search-menu)
      * [The Search Results Display](#the-search-results-display)
      * [The Display For Today's Appointments](#the-display-for-todays-appointments)
      * [The Date Input Prompt](#the-date-input-prompt)
      * [The Time Input Prompt](#the-time-input-prompt)
      * [The Name Input Prompt](#the-name-input-prompt)
      * [The Booking Confirmation](#the-booking-confirmation)
      * [The Already Booked Display](#the-already-booked-display)
      * [The Cancelation Prompt](#the-cancelation-prompt)
      * [The confirmed Cancelation Display](#the-confirmed-cancelation-display)
      * [The Application Instructions Display](#the-application-instructions-display)
      * [The Emergency Exit Option](#the-emergency-exit-option)
      * [Feedback For Invalid Inputs](#feedback-for-invalid-inputs)
      * [Background Features](#background-features)
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
