Scenario Outline: Add new contact
  Given a contacts list
  Given a contact with <firstname>, <lastname>
  When I add the contact to the list
  Then the new contacts list is equal to the old with added contact

  Examples:
  | firstname  | lastname  |
  | firstname1 | lastname1 |
  | firstname2 | lastname2 |



Scenario: Delete a contact
  Given a non empty contacts list
  Given a random contact from the list
  When I delete the contact from the list
  Then the new contacts list is equal to the old list without deleted contact


Scenario Outline: Edit a contact
  Given a non empty contacts list
  Given a new contact data with <firstname>, <lastname>
  When I edit the random contact from the list with new data
  Then the new contacts list is equal to the old list with edited contact

  Examples:
  | firstname   | lastname  |
  | test  | test |