Feature: Getting geolocation data using address

  Scenario: Determine coordinates by search queries
    Given I send the address
    When I am try to get coordinates
    Then I should see the correct coordinates
