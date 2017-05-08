DROP TABLE IF EXISTS public.developer;

CREATE TABLE developer (
    developer_id SERIAL PRIMARY KEY,
    first_name character varying NOT NULL,
    last_name character varying NOT NULL

);


INSERT INTO public.developer (
	first_name, last_name
)
VALUES
(
	'Andrew', 'Yale'
);

