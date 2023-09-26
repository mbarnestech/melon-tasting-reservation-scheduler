# ORIGINAL PROMPT

Build a simple service to help users make reservations to go to a fancy melon tasting.

A user should be able to “log in” (by entering their username, password optional), pick a date, choose an optional time range, and then be shown all the available reservations that meet the criteria.

There should also be a page which shows all reservations for a given user.	

Reservation rules:
* each must start and end on the hour or half hour
* each must last exactly 30 minutes long
* a user can only have one reservation on a calendar date
* only one reservation can be made for any given time slot
* time slots are all day, every day - the melon tasting room is always open.

If a user tries to violate the reservation rules, they should receive an error specific message.

The application needs the following pages:
- Simple login screen (no authentication required)
- Page to search for appointments
- Results page to view the results of the appointment search (allowing users to book appointments)
- Page to view all the scheduled appointments for the current user (optional: build in appointment editing/canceling)

# Goal of Current Iteration

* Implement Local Server



