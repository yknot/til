BEGIN;

DROP TABLE IF EXISTS public.posts;

CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    developer_id INTEGER NOT NULL,
    body TEXT NOT NULL,
    created_at timestamp without time zone NOT NULL,
    updated_at timestamp without time zone NOT NULL,
    title character varying NOT NULL,
    slug character varying NOT NULL,
    likes integer DEFAULT 1 NOT NULL,
    tweeted boolean DEFAULT false NOT NULL,
    published_at timestamp with time zone,
    CONSTRAINT likes CHECK ((likes >= 0))
);



INSERT INTO public.posts (
   developer_id, body, created_at, 
    updated_at, title, slug, likes, tweeted, 
    published_at
) 
VALUES 
(
    1, 'test post', now(), now(), 
    'test', 'test', 1, false, now()
),
(  
    1, 'test second post', now(), now(), 
    'again', 'test', 1, false, now()
);

COMMIT;
