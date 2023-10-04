# Welcome to the Reservation Scheduler. 

The general goal of this project is to build a simple service to help users make reservations to go to a fancy melon tasting. More information can be found in this repo's wiki.

# Database Structure

Two PostgreSQL Tables, Users and Reservations, hold the data regarding users and scheduled reservations.

```mermaid
erDiagram

USERS {
    Integer user_id PK
    String user_name
    String password
}

RESERVATIONS {
    Integer reservation_id PK
    Integer user_id FK
    DateTime appointment
    String status
}

USERS ||--|{ RESERVATIONS: One_to_Many


```