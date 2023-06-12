Feature: Getting geolocation data using coordinates

  Scenario: Determine the address by reverse geocoding
    Given I send coordinates
    When I am try to get address
    Then I should see correct coordinates address