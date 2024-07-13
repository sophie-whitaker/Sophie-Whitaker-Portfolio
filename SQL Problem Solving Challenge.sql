/* You are given two tables, 'flights' and 'airports'.  
Each row in the table 'flights' contains information about a flight: code of departure pore (start_port) and code of destination port (end_port).
Each row in the table 'airports' contains information about an airport:the city name (city_name) and the port code (port_code).  Each port_code is assigned to at most one airport.
Write an SQL query that finds all cities through which a flight from New York to Tokyo may pass if the passenger wants to make exactly one change of flights.  
*/

SELECT 
    start_port, 
    end_port
FROM 
    flights;

SELECT * FROM flights WHERE start_port='JFK';

SELECT * FROM airports WHERE city_name='New York';
SELECT * FROM airports WHERE city_name='Tokyo';

CREATE TABLE starting_airports(
name    char(3)
);

INSERT INTO starting_airports(name) SELECT port_code FROM airports WHERE city_name='New York';

CREATE TABLE ending_airports(
name    char(3)
);

INSERT INTO ending_airports(name) SELECT port_code FROM airports WHERE city_name='Tokyo';

CREATE TABLE intermediary_airports(
name    char(3)
);

INSERT INTO intermediary_airports(name) SELECT end_port FROM flights WHERE start_port IN starting_airports;

CREATE TABLE airports_destinationtokyo(
name    char(3)
);

INSERT INTO airports_destinationtokyo(name) SELECT start_port FROM flights WHERE end_port IN ending_airports AND start_port IN intermediary_airports;

SELECT city_name FROM airports WHERE port_code IN airports_destinationtokyo;