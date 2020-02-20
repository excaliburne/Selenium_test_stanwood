# Introduction

These set of test will run on the basis of https://mcswiss-web-stage.web.app/. 
The purpose of these tests are to check the Registration, categories and sidebar link functionalities.

## Test cases

- Test valid registration
- Test if element is present on page inside a category
- Test if all sidebar links are working

## Requirements

- Python3
- Selenium WebDriver
`pip3 install selenium`
- Selenium geckodriver </br>
Windows: https://www.softwaretestinghelp.com/geckodriver-selenium-tutorial/ </br>
Mac: `brew install geckodriver` 

## How to use

`python3 ChooseYourTest.py` replace with desired test

## Extra features

*TestRegistrationValid.py* will register an account by default. If you want the form to be filled but not register an account, open the .py and change **register** to False