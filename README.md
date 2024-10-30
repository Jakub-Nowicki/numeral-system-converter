# numeral-system-converter

## Overview
**Number Converter** is a Python-based web application built using **Flask**. This app provides a user-friendly web interface to convert numbers between decimal and any base from 2 to 16. It supports conversions to and from bases including binary, octal, decimal, and hexadecimal.

## Features
- **Interactive Web Interface**: Uses Flask to manage web requests and serve pages, allowing users to input numbers and select bases for conversion.
- **Support for Multiple Bases**: Converts numbers between decimal and bases ranging from binary (base 2) to hexadecimal (base 16).
- **Dynamic Form Update**: The web page dynamically updates to show conversion results without reloading.

## Technologies Used
- **Flask**: A lightweight WSGI (Web Server Gateway Interface) web application framework.
- **HTML/CSS**: For creating and styling the user interface.

## Installation

To run this application locally, you'll need Python and Flask. Follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Jakub-Nowicki/numeral-system-converter.git
   cd number-converter
   
2. **Install Flask**:
   ```bash
   pip install Flask

3. **Running the Application**:
   ```bash
   python app.py

This will start the Flask server on `localhost:5000`. Open your web browser and navigate to [http://localhost:5000](http://localhost:5000) to use the application.

## Usage

- **Convert Decimal to Base**: Enter a decimal number and select the target base to see the equivalent value in the chosen base.
- **Convert Base to Decimal**: Enter a number in the specified base and select the correct base to convert it back to decimal.
- **Interactivity**: The form updates the results immediately after the conversion button is clicked without needing to reload the page.

## Contributing

This project is open for contributions. Here are some ways you can contribute:

- **Report Bugs**: Provide details about the bugs in the Issues section.
- **Suggest Enhancements**: Suggest your ideas for new features or enhancements.
- **Improve Documentation**: Help new users understand the project better by improving the documentation.

To contribute, fork the repository, make your changes, and submit a pull request.

