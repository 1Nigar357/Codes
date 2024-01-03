-- Keep a log of any SQL queries you execute as you solve the mystery.
.schema
/*
sqlite> .schema
CREATE TABLE crime_scene_reports (
    id INTEGER,
    year INTEGER,
    month INTEGER,
    day INTEGER,
    street TEXT,
    description TEXT,
    PRIMARY KEY(id)
);
CREATE TABLE interviews (
    id INTEGER,
    name TEXT,
    year INTEGER,
    month INTEGER,
    day INTEGER,
    transcript TEXT,
    PRIMARY KEY(id)
);
CREATE TABLE atm_transactions (
    id INTEGER,
    account_number INTEGER,
    year INTEGER,
    month INTEGER,
    day INTEGER,
    atm_location TEXT,
    transaction_type TEXT,
    amount INTEGER,
    PRIMARY KEY(id)
);
CREATE TABLE bank_accounts (
    account_number INTEGER,
    person_id INTEGER,
    creation_year INTEGER,
    FOREIGN KEY(person_id) REFERENCES people(id)
);
CREATE TABLE airports (
    id INTEGER,
    abbreviation TEXT,
    full_name TEXT,
    city TEXT,
    PRIMARY KEY(id)
);
CREATE TABLE flights (
    id INTEGER,
    origin_airport_id INTEGER,
    destination_airport_id INTEGER,
    year INTEGER,
    month INTEGER,
    day INTEGER,
    hour INTEGER,
    minute INTEGER,
    PRIMARY KEY(id),
    FOREIGN KEY(origin_airport_id) REFERENCES airports(id),
    FOREIGN KEY(destination_airport_id) REFERENCES airports(id)
);
CREATE TABLE passengers (
    flight_id INTEGER,
    passport_number INTEGER,
    seat TEXT,
    FOREIGN KEY(flight_id) REFERENCES flights(id)
);
CREATE TABLE phone_calls (
    id INTEGER,
    caller TEXT,
    receiver TEXT,
    year INTEGER,
    month INTEGER,
    day INTEGER,
    duration INTEGER,
    PRIMARY KEY(id)
);
CREATE TABLE people (
    id INTEGER,
    name TEXT,
    phone_number TEXT,
    passport_number INTEGER,
    license_plate TEXT,
    PRIMARY KEY(id)
);
CREATE TABLE bakery_security_logs (
    id INTEGER,
    year INTEGER,
    month INTEGER,
    day INTEGER,
    hour INTEGER,
    minute INTEGER,
    activity TEXT,
    license_plate TEXT,
    PRIMARY KEY(id)
);

*/
.schema crime_scene_reports

SELECT description FROM crime_scene_reports
WHERE street = 'Humphrey Street' AND year = 2021 AND month = 7 AND day = 28;
/*RESULT*/
/* Theft of the CS50 duck took place at 10:15am at the Humphrey Street bakery.
Interviews were conducted today with three witnesses who were present at the time –
each of their interview transcripts mentions the bakery. */


SELECT * FROM interviews WHERE transcript like "%thief%bakery%";
/*
| id  |  name   | year | month | day |
transcript

| 161 | Ruth    | 2021 | 7     | 28  |
Sometime within ten minutes of the theft,
I saw the thief get into a car in the bakery parking lot and drive away.
If you have security footage from the bakery parking lot,
you might want to look for cars that left the parking lot in that time frame.                                                          |

| 162 | Eugene  | 2021 | 7     | 28  |
I don't know the thief's name, but it was someone I recognized.
Earlier this morning, before I arrived at Emma's bakery, I was walking by the ATM on Leggett Street
and saw the thief there withdrawing some money.                                                                                                 |

| 163 | Raymond | 2021 | 7     | 28  |
As the thief was leaving the bakery,
they called someone who talked to them for less than a minute.
In the call, I heard the thief say that they were planning to take the earliest flight out of Fiftyville tomorrow.
The thief then asked the person on the other end of the phone to purchase the flight ticket. |
*/


.schema bakery_security_logs
/* CREATE TABLE bakery_security_logs (
    id INTEGER,
    year INTEGER,
    month INTEGER,
    day INTEGER,
    hour INTEGER,
    minute INTEGER,
    activity TEXT,
    license_plate TEXT,
    PRIMARY KEY(id)
);
*/

SELECT * FROM bakery_security_logs
WHERE year = 2021 AND month = 7 AND day = 28 AND hour = 10 AND minute > 15 AND minute < 26;
/*
    +-----+------+-------+-----+------+--------+----------+---------------+
    | id  | year | month | day | hour | minute | activity | license_plate |
    +-----+------+-------+-----+------+--------+----------+---------------+
    | 260 | 2021 | 7     | 28  | 10   | 16     | exit     | 5P2BI95       |
    | 261 | 2021 | 7     | 28  | 10   | 18     | exit     | 94KL13X       |
    | 262 | 2021 | 7     | 28  | 10   | 18     | exit     | 6P58WS2       |
    | 263 | 2021 | 7     | 28  | 10   | 19     | exit     | 4328GD8       |
    | 264 | 2021 | 7     | 28  | 10   | 20     | exit     | G412CB7       |
    | 265 | 2021 | 7     | 28  | 10   | 21     | exit     | L93JTIZ       |
    | 266 | 2021 | 7     | 28  | 10   | 23     | exit     | 322W7JE       |
    | 267 | 2021 | 7     | 28  | 10   | 23     | exit     | 0NTHK55       |
    +-----+------+-------+-----+------+--------+----------+---------------+
*/



.schema people
/*CREATE TABLE people (
    id INTEGER,
    name TEXT,
    phone_number TEXT,
    passport_number INTEGER,
    license_plate TEXT,
    PRIMARY KEY(id)
);
*/

SELECT minute, people.license_plate, people.id, people.name, phone_number, passport_number FROM bakery_security_logs
JOIN people ON people.license_plate = bakery_security_logs.license_plate
WHERE year = 2021 AND month = 7 AND day = 28 AND hour = 10 AND minute > 15 AND minute < 26;
/*
    +--------+---------------+--------+---------+----------------+-----------------+
    | minute | license_plate |   id   |  name   |  phone_number  | passport_number |
    +--------+---------------+--------+---------+----------------+-----------------+
    | 16     | 5P2BI95       | 221103 | Vanessa | (725) 555-4692 | 2963008352      |
    | 18     | 94KL13X       | 686048 | Bruce   | (367) 555-5533 | 5773159633      |
    | 18     | 6P58WS2       | 243696 | Barry   | (301) 555-4174 | 7526138472      |
    | 19     | 4328GD8       | 467400 | Luca    | (389) 555-5198 | 8496433585      |
    | 20     | G412CB7       | 398010 | Sofia   | (130) 555-0289 | 1695452385      |
    | 21     | L93JTIZ       | 396669 | Iman    | (829) 555-5269 | 7049073643      |
    | 23     | 322W7JE       | 514354 | Diana   | (770) 555-1861 | 3592750733      |
    | 23     | 0NTHK55       | 560886 | Kelsey  | (499) 555-9472 | 8294398571      |
    +--------+---------------+--------+---------+----------------+-----------------+
*/

/*
LIST OF SUSPECTS:
    Vanessa
    Bruce
    Barry
    Luca
    Sofia
    Iman
    Diana
    Kelsey
*/

.schema bank_accounts
/*
    CREATE TABLE bank_accounts (
        account_number INTEGER,
        person_id INTEGER,
        creation_year INTEGER,
        FOREIGN KEY(person_id) REFERENCES people(id)
    );
*/

SELECT bank_accounts.person_id, account_number, people.name FROM bank_accounts
JOIN people ON people.id = bank_accounts.person_id
WHERE person_id IN (221103, 686048, 243696, 467400, 398010, 396669, 514354, 560886);
/*
    +-----------+----------------+-------+
    | person_id | account_number | name  |
    +-----------+----------------+-------+
    | 686048    | 49610011       | Bruce |
    | 514354    | 26013199       | Diana |
    | 396669    | 25506511       | Iman  |
    | 467400    | 28500762       | Luca  |
    | 243696    | 56171033       | Barry |
    +-----------+----------------+-------+
*/

/*
LIST OF SUSPECTS:
    Bruce
    Barry
    Luca
    Iman
    Diana
*/

.schema atm_transactions
/*
CREATE TABLE atm_transactions (
    id INTEGER,
    account_number INTEGER,
    year INTEGER,
    month INTEGER,
    day INTEGER,
    atm_location TEXT,
    transaction_type TEXT,
    amount INTEGER,
    PRIMARY KEY(id)
);
*/

-- BRUCE
SELECT atm_location, transaction_type FROM atm_transactions
WHERE account_number = 49610011
AND year = 2021 AND month = 7 AND day = 28;
/*
    +----------------+------------------+
    |  atm_location  | transaction_type |
    +----------------+------------------+
    | Leggett Street | withdraw         |
    +----------------+------------------+
*/



-- DIANA
SELECT atm_location, transaction_type FROM atm_transactions
WHERE account_number = 26013199
AND year = 2021 AND month = 7 AND day = 28;
/*
    +----------------+------------------+
    |  atm_location  | transaction_type |
    +----------------+------------------+
    | Leggett Street | withdraw         |
    +----------------+------------------+
*/

-- IMAN
SELECT atm_location, transaction_type FROM atm_transactions
WHERE account_number = 25506511
AND year = 2021 AND month = 7 AND day = 28;
/*
    +----------------+------------------+
    |  atm_location  | transaction_type |
    +----------------+------------------+
    | Leggett Street | withdraw         |
    +----------------+------------------+
*/

-- LUCA
SELECT atm_location, transaction_type FROM atm_transactions
WHERE account_number = 28500762
AND year = 2021 AND month = 7 AND day = 28;
/*
    +----------------+------------------+
    |  atm_location  | transaction_type |
    +----------------+------------------+
    | Leggett Street | withdraw         |
    +----------------+------------------+
*/

-- BARRY
SELECT atm_location, transaction_type FROM atm_transactions
WHERE account_number = 56171033
AND year = 2021 AND month = 7 AND day = 28;
/*
    +----------------------+------------------+
    |     atm_location     | transaction_type |
    +----------------------+------------------+
    | Daboin Sanchez Drive | deposit          |
    +----------------------+------------------+
*/


/*
LIST OF SUSPECTS:
    Bruce
    Luca
    Iman
    Diana
*/

.schema phone_calls
/*
CREATE TABLE phone_calls (
    id INTEGER,
    caller TEXT,
    receiver TEXT,
    year INTEGER,
    month INTEGER,
    day INTEGER,
    duration INTEGER,
    PRIMARY KEY(id)
);
*/
SELECT people.name, phone_number FROM bakery_security_logs
JOIN people ON people.license_plate = bakery_security_logs.license_plate
WHERE year = 2021 AND month = 7 AND day = 28 AND hour = 10 AND minute > 15 AND minute < 26;
/*
+---------+----------------+
|  name   |  phone_number  |
+---------+----------------+
| Bruce   | (367) 555-5533 |

| Luca    | (389) 555-5198 |

| Iman    | (829) 555-5269 |

| Diana   | (770) 555-1861 |

*/

SELECT caller, receiver FROM phone_calls
WHERE year = 2021 AND month = 7 AND day = 28 AND duration < 60;
/*
RESULT:
    +----------------+----------------+
    |     caller     |    receiver    |
    +----------------+----------------+
    | (130) 555-0289 | (996) 555-8899 |
    | (499) 555-9472 | (892) 555-8872 |
    | (367) 555-5533 | (375) 555-8161 |
    | (499) 555-9472 | (717) 555-1342 |
    | (286) 555-6063 | (676) 555-6554 |
    | (770) 555-1861 | (725) 555-3243 |
    | (031) 555-6622 | (910) 555-3251 |
    | (826) 555-1652 | (066) 555-9701 |
    | (338) 555-6650 | (704) 555-2131 |
    +----------------+----------------+
*/


/*
    +----------------+----------------+
    |     caller     |    receiver    |
    +----------------+----------------+
    | (367) 555-5533 | (375) 555-8161 |
    | (770) 555-1861 | (725) 555-3243 |
    +----------------+----------------+

    LIST OF SUSPECTS:
        Bruce
        Diana
*/


SELECT * FROM people
WHERE phone_number = '(375) 555-8161';
/*
    +--------+-------+----------------+-----------------+---------------+
    |   id   | name  |  phone_number  | passport_number | license_plate |
    +--------+-------+----------------+-----------------+---------------+
    | 864400 | Robin | (375) 555-8161 |                 | 4V16VO0       |
    +--------+-------+----------------+-----------------+---------------+
*/


SELECT * FROM people
WHERE phone_number = '(725) 555-3243';
/*
    +--------+--------+----------------+-----------------+---------------+
    |   id   |  name  |  phone_number  | passport_number | license_plate |
    +--------+--------+----------------+-----------------+---------------+
    | 847116 | Philip | (725) 555-3243 | 3391710505      | GW362R6       |
    +--------+--------+----------------+-----------------+---------------+
*/



/*
LIST OF SUSPECTS:
    Bruce, ACCOMPLICE: Robin
    Diana, ACCOMPLICE: Philip
*/

.schema passengers
/*
CREATE TABLE passengers (
    flight_id INTEGER,
    passport_number INTEGER,
    seat TEXT,
    FOREIGN KEY(flight_id) REFERENCES flights(id)
);
*/

.schema flights
/*
CREATE TABLE flights (
    id INTEGER,
    origin_airport_id INTEGER,
    destination_airport_id INTEGER,
    year INTEGER,
    month INTEGER,
    day INTEGER,
    hour INTEGER,
    minute INTEGER,
    PRIMARY KEY(id),
    FOREIGN KEY(origin_airport_id) REFERENCES airports(id),
    FOREIGN KEY(destination_airport_id) REFERENCES airports(id)
);
*/

.schema airports
/*
CREATE TABLE airports (
    id INTEGER,
    abbreviation TEXT,
    full_name TEXT,
    city TEXT,
    PRIMARY KEY(id)
);
*/

--   | 18     | 94KL13X       | 686048 | Bruce   | (367) 555-5533 | 5773159633      |
--   | 23     | 322W7JE       | 514354 | Diana   | (770) 555-1861 | 3592750733      |



SELECT origin_airport_id ,destination_airport_id, year, month, day, hour, minute FROM flights
JOIN passengers ON passengers.flight_id = flights.id
WHERE passport_number = 5773159633;
/*
    +-------------------+------------------------+------+-------+-----+------+--------+
    | origin_airport_id | destination_airport_id | year | month | day | hour | minute |
    +-------------------+------------------------+------+-------+-----+------+--------+
    | 8                 | 4                      | 2021 | 7     | 29  | 8    | 20     |
    +-------------------+------------------------+------+-------+-----+------+--------+
*/

SELECT origin_airport_id ,destination_airport_id, year, month, day, hour, minute FROM flights
JOIN passengers ON passengers.flight_id = flights.id
WHERE passport_number = 3592750733;
/*
    +-------------------+------------------------+------+-------+-----+------+--------+
    | origin_airport_id | destination_airport_id | year | month | day | hour | minute |
    +-------------------+------------------------+------+-------+-----+------+--------+
    | 8                 | 6                      | 2021 | 7     | 29  | 16   | 0      |
    | 7                 | 8                      | 2021 | 7     | 30  | 16   | 27     |
    | 8                 | 5                      | 2021 | 7     | 30  | 10   | 19     |
    +-------------------+------------------------+------+-------+-----+------+--------+
*/

SELECT * FROM airports WHERE id IN (4, 8);
/*
    +----+--------------+-----------------------------+---------------+
    | id | abbreviation |          full_name          |     city      |
    +----+--------------+-----------------------------+---------------+
    | 4  | LGA          | LaGuardia Airport           | New York City |
    | 8  | CSF          | Fiftyville Regional Airport | Fiftyville    |
    +----+--------------+-----------------------------+---------------+
*/

-- ANSWERS
/*
    THIEF: Bruce
    ACCOMPLICE: Robin
    THE CITY THE THIEF ESCAPED TO: New York City
*/