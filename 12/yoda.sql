--
-- PostgreSQL database dump
--

-- Dumped from database version 10.12 (Ubuntu 10.12-0ubuntu0.18.04.1)
-- Dumped by pg_dump version 10.12 (Ubuntu 10.12-0ubuntu0.18.04.1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: actor; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.actor (
    actor_id integer NOT NULL,
    name text NOT NULL,
    surname text NOT NULL
);


ALTER TABLE public.actor OWNER TO postgres;

--
-- Name: actor_actor_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.actor_actor_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.actor_actor_id_seq OWNER TO postgres;

--
-- Name: actor_actor_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.actor_actor_id_seq OWNED BY public.actor.actor_id;


--
-- Name: actor_film; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.actor_film (
    actor_id integer NOT NULL,
    film_id integer NOT NULL
);


ALTER TABLE public.actor_film OWNER TO postgres;

--
-- Name: film; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.film (
    film_id integer NOT NULL,
    title text NOT NULL
);


ALTER TABLE public.film OWNER TO postgres;

--
-- Name: film_film_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.film_film_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.film_film_id_seq OWNER TO postgres;

--
-- Name: film_film_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.film_film_id_seq OWNED BY public.film.film_id;


--
-- Name: producer; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.producer (
    producer_id integer NOT NULL,
    name text NOT NULL,
    surname text NOT NULL
);


ALTER TABLE public.producer OWNER TO postgres;

--
-- Name: producer_film; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.producer_film (
    producer_id integer NOT NULL,
    film_id integer NOT NULL
);


ALTER TABLE public.producer_film OWNER TO postgres;

--
-- Name: producer_producer_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.producer_producer_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.producer_producer_id_seq OWNER TO postgres;

--
-- Name: producer_producer_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.producer_producer_id_seq OWNED BY public.producer.producer_id;


--
-- Name: actor actor_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.actor ALTER COLUMN actor_id SET DEFAULT nextval('public.actor_actor_id_seq'::regclass);


--
-- Name: film film_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.film ALTER COLUMN film_id SET DEFAULT nextval('public.film_film_id_seq'::regclass);


--
-- Name: producer producer_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.producer ALTER COLUMN producer_id SET DEFAULT nextval('public.producer_producer_id_seq'::regclass);


--
-- Data for Name: actor; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.actor (actor_id, name, surname) FROM stdin;
1	Том	Харди
2	Леонардо	Дикаприо
3	Марион	Котийяр
4	Кен	Ватанабе
5	Том	Круз
6	Брэд	Питт
7	Мэтт	Деймон
8	Генри	Кавилл
9	Брюс	Уиллис
10	Милла	Йовович
\.


--
-- Data for Name: actor_film; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.actor_film (actor_id, film_id) FROM stdin;
1	1
1	9
2	1
2	8
2	11
3	1
3	6
4	1
4	3
5	3
5	4
6	4
6	10
7	5
8	2
9	7
10	7
\.


--
-- Data for Name: film; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.film (film_id, title) FROM stdin;
1	Начало
2	Бэтмен против Супермена
3	Последний самурай
4	Интервью с вампиром
5	Марсианин
6	Такси
7	Пятый элемент
8	Совокупность лжи
9	Дюнкерк
10	Легенды осени
11	Кровавый алмаз
\.


--
-- Data for Name: producer; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.producer (producer_id, name, surname) FROM stdin;
1	Кристофер	Нолан
2	Эдвард	Цвик
3	Нил	Джордан
4	Ридли	Скотт
5	Люк	Бессон
\.


--
-- Data for Name: producer_film; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.producer_film (producer_id, film_id) FROM stdin;
1	1
1	2
2	3
3	4
4	5
5	6
5	7
4	8
1	9
2	10
2	11
\.


--
-- Name: actor_actor_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.actor_actor_id_seq', 10, true);


--
-- Name: film_film_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.film_film_id_seq', 11, true);


--
-- Name: producer_producer_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.producer_producer_id_seq', 5, true);


--
-- Name: actor_film actor_film_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.actor_film
    ADD CONSTRAINT actor_film_pkey PRIMARY KEY (actor_id, film_id);


--
-- Name: actor actor_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.actor
    ADD CONSTRAINT actor_pkey PRIMARY KEY (actor_id);


--
-- Name: film film_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.film
    ADD CONSTRAINT film_pkey PRIMARY KEY (film_id);


--
-- Name: producer_film producer_film_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.producer_film
    ADD CONSTRAINT producer_film_pkey PRIMARY KEY (producer_id, film_id);


--
-- Name: producer producer_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.producer
    ADD CONSTRAINT producer_pkey PRIMARY KEY (producer_id);


--
-- Name: actor_film actor_film_actor_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.actor_film
    ADD CONSTRAINT actor_film_actor_id_fkey FOREIGN KEY (actor_id) REFERENCES public.actor(actor_id);


--
-- Name: actor_film actor_film_film_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.actor_film
    ADD CONSTRAINT actor_film_film_id_fkey FOREIGN KEY (film_id) REFERENCES public.film(film_id);


--
-- Name: producer_film producer_film_film_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.producer_film
    ADD CONSTRAINT producer_film_film_id_fkey FOREIGN KEY (film_id) REFERENCES public.film(film_id);


--
-- Name: producer_film producer_film_producer_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.producer_film
    ADD CONSTRAINT producer_film_producer_id_fkey FOREIGN KEY (producer_id) REFERENCES public.producer(producer_id);


--
-- PostgreSQL database dump complete
--

