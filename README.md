# Welcome to the Reservation Scheduler. 

The general goal of this project is to build a simple service to help users make reservations to go to a fancy melon tasting. More information can be found in this repo's wiki.

# Database Structure

Two PostgreSQL Tables, Users and Reservations hold the data regarding users and scheduled reservations.

```mermaid
erDiagram

USERS {
    int user_ID PK
    string user_name
    string password
}

RESERVATIONS {
    int reservation_ID PK
    int user_ID FK
    int year
    int month
    int day
    int hour
    int minute
    string status
}

USERS ||--|{ RESERVATIONS: One_to_Many


```