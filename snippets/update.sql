CREATE table IF NOT EXISTS actor_sample (
    actor_id SERIAL,
    first_name VARCHAR(45) NOT NULL,
    last_name VARCHAR(45) NOT NULL,
    last_update TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (actor_id)
);

INSERT INTO actor_sample (first_name, last_name)
SELECT first_name, last_name
FROM actor;

UPDATE  actor_sample
SET first_name = 'LECH'
WHERE actor_id = 1;

UPDATE actor_sample
SET first_name = 'ANTONI' , last_name = 'M'
WHERE actor_id = 2;

UPDATE actor_sample
SET first_name = 'MATEUSZ'
WHERE actor_id IN (1, 3, 7, 10);


SELECT *
FROM film_actor
WHERE film_id = 1;

UPDATE actor_sample
SET first_name = 'ANDRZEJ'
WHERE actor_id IN (
    SELECT actor_id
    FROM film_actor
    WHERE film_id = 1);

SELECT *
FROM actor_sample
ORDER BY actor_id;

DROP table actor_sample;
