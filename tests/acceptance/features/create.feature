Feature: Simulate a POST request using Behave

  Scenario: Sending a POST request and verifying the response
    Given I have the following request data:
      | name  | price |
      | "Bob" | 4     |
    When I send a POST request to "http://127.0.0.1:8000/items/"
    Then the response should be JSON:
      """
      {
        "name": "Bob"
      }
      """