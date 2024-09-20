# Automation Challenge using Python, Pytest, Playwright and the Screenplay design pattern

## Structure
   
### UI tests

The UI automation test is a suite with the following test cases:

   * User registration 
   * Login
   * Logout
   * Complete a purchase
   

## Technologies and dependencies

* Python 
* Pytest
* Playwright 
* Pylint
* Faker
* Python-dotenv
* Pytest-reporter-html1
* Black
* autopep8

## How to run the tests locally

### Installation

1. Clone the repo and create the .env file using the .env.example as example (the users in the env.example are already created, you can use them)

2. Install all dependencies using
 ```
 pip install
   ```
All dependencies are listed on the requirements.txt file, so the command should be the following

 ```
 pip install -r requirements.txt
   ```

Install playwright with all the browsers with 

 ```
 Playwright install
   ```

3. Run the tests using pytest. Type on the terminal:

   ```
   pytest
   ```
This runs all the tests on headless mode 

4. To run the tests on headed mode type on the terminal:

   ```
   pytest --headed
   ```
   
4. To generate the reports type on the terminal:

   ```
   --template=html1/index.html --report=report.html
   ```
   
## Naming conventions

* Use `snake_case` for _variables_, _properties_, files and _function_ names.
* Use `PascalCase` for _class names_.
* Use `UPPERCASE with underscores` for _constants_.

## Contributing

When creating a commit please use an accurate description of the purpose, e.g. `Upgrade pytest version`.

Remember to run the linter and the formatter before pushing any changes, this can be done by running on the terminal `pylint` and `black` and specifying the path and name of your file.

Every time a push is done, the workflow is going to be triggered building and running all the tests.
