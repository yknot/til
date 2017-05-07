BEGIN;

DROP TABLE IF EXISTS public.developers;

CREATE TABLE developers (
    developer_id SERIAL PRIMARY KEY,
    first_name character varying NOT NULL,
    last_name character varying NOT NULL

);


INSERT INTO public.developers (
	first_name, last_name
)
VALUES
(
	'Andrew', 'Yale'
);

COMMIT;


