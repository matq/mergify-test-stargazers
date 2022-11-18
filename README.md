# Testing the API

In order to sign in, please input the following credentials:
- username: mathieu
- password: quilliec

That's not very secure but at least you can test it :)

# Structure

Even though the project is relatively small, the organization is split into multiple folders
to make it easier to work through.

- Core
  - main.py with the app and its basic functionality
  - /schemas for pydantic models
  - /utils for code that can have multiple uses
  - /tests for unit tests, fixtures and sample data

# Endpoint

The endpoint is to retrieve a list of neighbours repositories from a user where stargazers are in common
with the repository passed in parameter.

Since it's not possible to query a repository only by its name without its owner, there is a double for loop
when listing repositories.

# Improvements

- Add more detailed unit tests
- Connect to a database to avoid having to do a lot of API calls
- Refactor the list_repos function to optimize performance
- Handling errors to make sure the code doesn't crash
- Add a better authentication process