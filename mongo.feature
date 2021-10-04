Feature: editProfile

  Edits site running on port 3000

  Scenario: changing the data
    Given the mail is yossigoldberg2@gmail.com
    When I change mail to yossiyossi@gmail
    Then mongoDB mail also is updated